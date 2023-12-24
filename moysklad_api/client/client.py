import typing
import base64
import datetime
import json

import aiohttp
import asyncio
import aiohttp.client_exceptions

from ..errors import MoySkladError
from .. import types
from ..types import Unset

from ..api.entities import (
    product as product_api,
    product_folder as product_folder_api,
    custom_entity as custom_entity_api,
    store as store_api,
    organization as organization_api,
    webhook as webhook_api,
)
from ..api.reports import (
    stocks as stocks_api,
)
from ..api.documents import (
    supply as supply_api,
    enter as enter_api,
    internal_order as internal_order_api,
    move as move_api,
    demand as demand_api,
    purchase_order as purchase_order_api,
    invoice_in as invoice_in_api,
)


class MoySkladClient:
    def __init__(
        self,
        login: typing.Union[Unset, str] = Unset,
        password: typing.Union[Unset, str] = Unset,
        api_token: typing.Union[Unset, str] = Unset,
        debug: bool = False,
        auto_retry_count: int = 5,
        auto_retry_delay: float = 1.0,
    ):
        """
        Create a MoySkladClient instance. Converts login and password to api_token, if needed.
        Either login and password or api_token must be provided.
        (Создает экземпляр MoySkladClient. Конвертирует логин и пароль в api_token, если нужно.
        Либо логин и пароль, либо api_token должны быть указаны.)

        :param login: Optional login (Логин)
        :param password:  Optional password (Пароль)
        :param api_token:  Optional api_token (Токен)
        :param debug:  If True, prints all requests and responses (Если True, печатает все запросы и ответы)
        :param auto_retry_count:  Number of times to retry a request if it fails (ClientConnectError, errorcode > 500, etc) (Количество попыток повторить запрос, если он не удался (ClientConnectError, errorcode> 500 и т. Д.))
        :param auto_retry_delay:  Delay between retries (Задержка между повторами)
        """
        if not (login and password) and not api_token:
            raise ValueError("Either login and password or api_token must be provided")
        if not api_token:
            api_token = base64.b64encode(f"{login}:{password}".encode()).decode()
        else:
            # check if api_token is valid base64 and has `:` in it
            # (проверяем, что api_token - это валидный base64 и содержит `:`)
            try:
                decoded = base64.b64decode(api_token).decode()
            except Exception:
                raise ValueError("api_token is not valid base64")
            if ":" not in decoded:
                raise ValueError("api_token is not valid, no : in it")

        self._api_token = api_token
        self._debug = debug
        self._auto_retry_count = auto_retry_count if auto_retry_count > 0 else 0
        if auto_retry_delay < 0:
            raise ValueError("auto_retry_delay must be >= 0")
        self._auto_retry_delay = auto_retry_delay

    async def request(
        self,
        method: typing.Literal["GET", "POST", "PUT", "DELETE"],
        url: str,
        allow_non_json=False,
        **kwargs,
    ) -> dict:
        """
        Make a request to the MoySklad API, automatically adding the Authorization header.
        (Делает запрос к API MoySklad, автоматически добавляя заголовок Authorization.)

        :raises MoySkladError: if the request failed (Сообщает об ошибке, если запрос не удался)

        :param method: HTTP method GET, POST, PUT, DELETE
        :param url:  URL to request (URL для запроса)
        :param allow_non_json:  If True, error is not raised if the response is not JSON (Если True, ошибка не вызывается, если ответ не JSON)
        :param kwargs:  Additional arguments for aiohttp.ClientSession.request
         (Дополнительные аргументы для aiohttp.ClientSession.request)

        :return: JSON Response from the MoySklad API (JSON Ответ от MoySklad API)
        """
        async with aiohttp.ClientSession() as session:
            kwargs.setdefault("headers", {})
            kwargs["headers"]["Authorization"] = f"Basic {self._api_token}"
            is_json = kwargs.get("json") is not None
            json_text = "{}"
            if is_json:
                if self._debug:
                    # convert json to a body with a pretty printed json, set content-type to application/json.
                    # This is needed for better error reading.
                    # (конвертируем json в тело с красиво отформатированным json,
                    # устанавливаем content-type в application/json)
                    # (это нужно для лучшего чтения ошибок)
                    kwargs["data"] = json.dumps(
                        kwargs.pop("json", {}), indent=4, ensure_ascii=False
                    )
                else:
                    kwargs["data"] = json.dumps(
                        kwargs.pop("json", {}),
                        separators=(",", ":"),
                        ensure_ascii=False,
                    )
                json_text = kwargs["data"]
                kwargs["headers"]["Content-Type"] = "application/json"

            # allow gzipped responses
            # (разрешаем сжатые ответы)
            kwargs["headers"]["Accept-Encoding"] = "gzip"

            last_exception = None
            for retry_num in range(1, self._auto_retry_count + 1):
                is_last_retry = retry_num == self._auto_retry_count
                try:
                    async with session.request(method, url, **kwargs) as resp:
                        if self._debug:
                            print(
                                f"Request: {method} {url} {kwargs.get('json', '')} {kwargs.get('data', '')}\n"
                                f"Response: {resp.status} {await resp.text()}"
                            )
                        if resp.status >= 500:
                            try:
                                json_resp = await resp.json()
                            except (aiohttp.ContentTypeError, json.JSONDecodeError):
                                json_resp = {}
                            last_exception = MoySkladError(
                                json_resp.get(
                                    "errors",
                                    {"error": f"Server returned {resp.status}"},
                                ),
                                json_text,
                            )
                            if is_last_retry:
                                raise last_exception
                            await asyncio.sleep(self._auto_retry_delay)
                            continue
                        if resp.content_type != "application/json":
                            if allow_non_json:
                                return {}
                            raise ValueError(
                                f"Response is not JSON: `{resp.content_type}` : {await resp.text()}"
                            )
                        json_resp = await resp.json()
                        if resp.status >= 400:
                            raise MoySkladError(json_resp["errors"][0], json_text)
                        return json_resp
                except (
                    aiohttp.client_exceptions.ClientConnectorError,
                    asyncio.TimeoutError,
                ) as e:
                    if is_last_retry:
                        raise e
                    await asyncio.sleep(self._auto_retry_delay)
                    last_exception = e
        if last_exception is not None:
            raise last_exception
        raise ValueError("This should never happen")

    async def raw_request(
        self,
        *args,
        **kwargs,
    ) -> (int, bytes, dict):
        """
        Make a request to the MoySklad API, automatically adding the Authorization header.
        (Делает запрос к API MoySklad, автоматически добавляя заголовок Authorization.)

        :returns (status, body, headers): status code, body and headers of the response
        """
        async with aiohttp.ClientSession() as session:
            kwargs.setdefault("headers", {})
            kwargs["headers"]["Authorization"] = f"Basic {self._api_token}"
            kwargs["headers"]["Accept-Encoding"] = "gzip"

            async with session.request(*args, **kwargs) as resp:
                return resp.status, await resp.read(), resp.headers

    # function that allows us to use MoySkladClient as a caller
    # (функция, которая позволяет нам использовать MoySkladClient как вызывающий)
    async def __call__(self, request):
        if not isinstance(request, types.ApiRequest):
            raise TypeError("request must be an ApiRequest")
        result = await self.request(**request.to_request().to_kwargs())
        return request.from_response(result)

    # internal orders (внутренние заказы)

    async def get_internal_orders(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[internal_order_api.InternalOrder]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennie-zakazy

        Get a list of internal orders. (Получает список внутренних заказов.)
        :param limit: Limit the number of results (Ограничить количество результатов)
        :param offset:  Offset the results (Сместить результаты)
        :param search:  Search query (Поисковый запрос)
        :return: List of InternalOrder objects (Список объектов InternalOrder)
        """
        return await self(
            internal_order_api.GetInternalOrdersRequest(
                limit=limit, offset=offset, search=search
            )
        )

    async def create_internal_order(
        self,
        organization: types.Meta,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        name: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, typing.Union[str, datetime.datetime]] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        sum_: typing.Union[Unset, int] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset,
            typing.List[internal_order_api.CreateInternalOrderRequest.CreatePosition],
        ] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        files: typing.Union[Unset, list] = Unset,
        moves: typing.Union[Unset, list] = Unset,
        purchase_orders: typing.Union[Unset, list] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> internal_order_api.InternalOrder:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-sozdat-vnutrennij-zakaz

        Create an internal order. (Создает внутренний заказ.)

        :param organization: Organization (Организация)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий)
        :param group: Group (Группа)
        :param name: Name (Название)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param moment: Date (Дата)
        :param applicable: Applicable (Применимый)
        :param rate: Rate (Ставка)
        :param sum_: Sum (Сумма)
        :param store: Store (Склад)
        :param project: Project (Проект)
        :param state: State (Состояние)
        :param positions: Positions (Позиции)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param files: Files (Файлы)
        :param moves: Moves (Движения)
        :param purchase_orders: Purchase orders (Заказы на закупку)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(
            internal_order_api.CreateInternalOrderRequest(
                organization=organization,
                owner=owner,
                shared=shared,
                group=group,
                name=name,
                description=description,
                external_code=external_code,
                moment=moment,
                applicable=applicable,
                rate=rate,
                sum_=sum_,
                store=store,
                project=project,
                state=state,
                positions=positions,
                attributes=attributes,
                code=code,
                delivery_planned_moment=delivery_planned_moment,
                files=files,
                moves=moves,
                purchase_orders=purchase_orders,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def get_internal_order(self, id_: str) -> internal_order_api.InternalOrder:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennij-zakaz

        Get an internal order. (Получает внутренний заказ.)
        :param id_: Internal order ID (ID внутреннего заказа)
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(internal_order_api.GetInternalOrderRequest(id_=id_))

    async def update_internal_order(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        name: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, typing.Union[str, datetime.datetime]] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        sum_: typing.Union[Unset, int] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset,
            typing.List[internal_order_api.UpdateInternalOrderRequest.UpdatePosition],
        ] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        files: typing.Union[Unset, list] = Unset,
        moves: typing.Union[Unset, list] = Unset,
        purchase_orders: typing.Union[Unset, list] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> internal_order_api.InternalOrder:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-izmenit-vnutrennij-zakaz

        Update an internal order. (Обновляет внутренний заказ.)
        :param id_: Internal order ID (ID внутреннего заказа)
        :param organization: Organization (Организация)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий)
        :param group: Group (Группа)
        :param name: Name (Название)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param moment: Date (Дата)
        :param applicable: Applicable (Применимый)
        :param rate: Rate (Ставка)
        :param sum_: Sum (Сумма)
        :param store: Store (Склад)
        :param project: Project (Проект)
        :param state: State (Состояние)
        :param positions: Positions (Позиции)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param files: Files (Файлы)
        :param moves: Moves (Движения)
        :param purchase_orders: Purchase orders (Заказы на закупку)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(
            internal_order_api.UpdateInternalOrderRequest(
                id_=id_,
                organization=organization,
                owner=owner,
                shared=shared,
                group=group,
                name=name,
                description=description,
                external_code=external_code,
                moment=moment,
                applicable=applicable,
                rate=rate,
                sum_=sum_,
                store=store,
                project=project,
                state=state,
                positions=positions,
                attributes=attributes,
                code=code,
                delivery_planned_moment=delivery_planned_moment,
                files=files,
                moves=moves,
                purchase_orders=purchase_orders,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def get_order_positions(
        self,
        id_: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[internal_order_api.Position]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-pozicii-vnutrennego-zakaza

        Get an internal order positions. (Получает позиции внутреннего заказа.)
        :param id_: Internal order ID (ID внутреннего заказа)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :param search: Search (Поиск)
        :return: list(InternalOrder) object (Список объектов InternalOrder)
        """
        return await self(
            internal_order_api.GetOrderPositionsRequest(
                id_=id_, limit=limit, offset=offset, search=search
            )
        )

    async def add_order_positions(
        self,
        id_: str,
        positions: typing.List[internal_order_api.AddOrderPositionsRequest.AddPosition],
    ) -> typing.List[internal_order_api.Position]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-pozicii-vnutrennego-zakaza

        Add positions to an internal order. (Добавляет позиции внутреннего заказа.)

        :param id_: Internal order ID (ID внутреннего заказа)
        :param positions: Positions (Позиции, которые нужно добавить)
        :return: list(InternalOrder) object (Список объектов InternalOrder)
        """
        return await self(
            internal_order_api.AddOrderPositionsRequest(id_=id_, positions=positions)
        )

    async def delete_order_position(
        self,
        order_id: str,
        position_id: str,
    ) -> None:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-udalit-poziciu-vnutrennego-zakaza

        Delete an internal order position. (Удаляет позицию внутреннего заказа.)

        :param order_id: Internal order ID (ID внутреннего заказа)
        :param position_id: Position ID (ID позиции)
        :return: None
        """
        return await self(
            internal_order_api.DeleteOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    async def get_order_position(
        self,
        order_id: str,
        position_id: str,
    ) -> internal_order_api.Position:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-poziciu

        Get position by its id from order by order and positions id
        Получить позицию по ее id из заказа по id заказа и позиции
        :param order_id: order id (id заказа)
        :param position_id: position id (id позиции)
        :return: Position object (Объект Position)
        """
        return await self(
            internal_order_api.GetOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    # products_api
    async def get_product_list(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[product_api.Product]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-spisok-towarow

        Get a list of product. (Получает список товаров.)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: list(Product) object (Список объектов Product)
        """
        return await self(product_api.GetProductListRequest(limit=limit, offset=offset))

    async def create_product(
        self,
        name: str,
        code: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        effective_vat: typing.Union[Unset, int] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        uom: typing.Union[Unset, types.Meta] = Unset,
        supplier: typing.Union[Unset, types.Meta] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        buy_price: typing.Union[Unset, dict] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        article: typing.Union[Unset, str] = Unset,
        weight: typing.Union[Unset, int] = Unset,
        volume: typing.Union[Unset, int] = Unset,
        packs: typing.Union[Unset, typing.List[dict]] = Unset,
        is_serial_trackable: typing.Union[Unset, bool] = Unset,
        tracking_type: typing.Union[
            Unset,
            typing.Literal[
                "ELECTRONICS",
                "LP_CLOTHES",
                "LP_LINENS",
                "MILK",
                "NCP",
                "NOT_TRACKED",
                "OTP",
                "PERFUMERY",
                "SHOES",
                "TIRES",
                "TOBACCO",
                "WATER",
            ],
        ] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        images: typing.Union[Unset, typing.List[dict]] = Unset,
        alcoholic: typing.Union[Unset, dict] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        country: typing.Union[Unset, types.Meta] = Unset,
        files: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        minimum_balance: typing.Union[Unset, int] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        partial_disposal: typing.Union[Unset, bool] = Unset,
        payment_item_type: typing.Union[
            Unset,
            typing.Literal[
                "GOODS",
                "EXCISABLE_GOOD",
                "COMPOUND_PAYMENT_ITEM",
                "ANOTHER_PAYMENT_ITEM",
            ],
        ] = Unset,
        ppe_type: typing.Union[Unset, str] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        tax_system: typing.Union[
            Unset,
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ],
        ] = Unset,
        things: typing.Union[Unset, typing.List[str]] = Unset,
        tnved: typing.Union[Unset, str] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
    ) -> product_api.Product:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-sozdat-towar

        :param name: Name (Название)
        :param code: Code (Код Комплекта)
        :param external_code: External code (Внешний код комплекта)
        :param description: Description (Описание)
        :param vat: VAT (НДС)
        :param effective_vat: Real VAT (Реальный НДС)
        :param discount_prohibited: Prohibition of discounts (Запрет на скидки)
        :param uom: Unit (Единица измерения)
        :param supplier: Supplier (Поставщик)
        :param min_price: Minimum price (Минимальная цена) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-modifikaciq-modifikacii-atributy-wlozhennyh-suschnostej-minimal-naq-cena
        :param buy_price: Purchase price (Закупочная цена) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-zakupochnaq-cena
        :param sale_prices: Sale prices (Цены продажи)
        :param barcodes: Barcodes (Штрихкоды) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-modifikaciq-modifikacii-atributy-wlozhennyh-suschnostej-shtrih-kody
        :param article: Article (Артикул)
        :param weight: Weight (Вес)
        :param volume: Volume (Объем)
        :param packs: Packs (Упаковки модификации) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-modifikaciq-modifikacii-atributy-wlozhennyh-suschnostej-upakowki-modifikacii
        :param is_serial_trackable: Serial tracking (Серийный учет)
        :param tracking_type: Tracking type (Тип отслеживания) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-suschnosti-tip-markiruemoj-produkcii
        :param attributes: Attributes (Атрибуты)
        :param images: Images (Изображения) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-izobrazhenie
        :param alcoholic: Alcoholic (Объект, содержащий поля алкогольной продукции) https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-ob-ekt-soderzhaschij-polq-alkogol-noj-produkcii
        :param archived: Archived (Архивный)
        :param country: Country (Страна)
        :param files: Files (Метаданные массива Файлов (Максимальное количество файлов - 100))
        :param group: Group (Метаданные отдела сотрудника)
        :param minimum_balance: Minimum balance (Минимальный остаток)
        :param owner: Owner (Метаданные владельца (Сотрудника))
        :param partial_disposal: Partial disposal (Управление состоянием частичного выбытия маркированного товара. «true» - возможность включена.)
        :param payment_item_type: Payment item type (Признак предмета расчета. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-komplekt-komplekty-atributy-suschnosti-priznak-predmeta-rascheta)
        :param ppe_type: PPE type (Код вида номенклатурной классификации медицинских средств индивидуальной защиты (EAN-13)) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-suschnosti-kod-wida-nomenklaturnoj-klassifikacii-medicinskih-sredstw-indiwidual-noj-zaschity
        :param product_folder: Product folder (Метаданные группы товара)
        :param shared: Shared (Общий)
        :param tax_system: Tax system (Система налогообложения) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-suschnosti-kod-sistemy-nalogooblozheniq
        :param things: Serial numbers (Серийные номера)
        :param tnved: TNVED (Код ТН ВЭД)
        :param use_parent_vat: Use parent VAT (Использовать родительский НДС)
        :return: Product object (Объект Product)
        """
        return await self(
            product_api.CreateProductRequest(
                name=name,
                code=code,
                external_code=external_code,
                description=description,
                vat=vat,
                effective_vat=effective_vat,
                discount_prohibited=discount_prohibited,
                uom=uom,
                supplier=supplier,
                min_price=min_price,
                buy_price=buy_price,
                sale_prices=sale_prices,
                barcodes=barcodes,
                article=article,
                weight=weight,
                volume=volume,
                packs=packs,
                is_serial_trackable=is_serial_trackable,
                tracking_type=tracking_type,
                attributes=attributes,
                images=images,
                alcoholic=alcoholic,
                archived=archived,
                country=country,
                files=files,
                group=group,
                minimum_balance=minimum_balance,
                owner=owner,
                partial_disposal=partial_disposal,
                payment_item_type=payment_item_type,
                ppe_type=ppe_type,
                product_folder=product_folder,
                shared=shared,
                tax_system=tax_system,
                things=things,
                tnved=tnved,
                use_parent_vat=use_parent_vat,
            )
        )

    async def delete_product(self, id_: str) -> None:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-udalit-towar

        :param id_: Product ID (ID Товара)
        :return: None
        """
        await self(product_api.DeleteProductRequest(id_=id_))

    async def get_product(self, id_: str) -> product_api.Product:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-towar

        :param id_: Product ID (ID Товара)
        :return: Product object (Объект Product)
        """
        return await self(product_api.GetProductRequest(id_=id_))

    async def update_product(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        effective_vat: typing.Union[Unset, int] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        uom: typing.Union[Unset, types.Meta] = Unset,
        supplier: typing.Union[Unset, types.Meta] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        buy_price: typing.Union[Unset, dict] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        article: typing.Union[Unset, str] = Unset,
        weight: typing.Union[Unset, int] = Unset,
        volume: typing.Union[Unset, int] = Unset,
        packs: typing.Union[Unset, typing.List[dict]] = Unset,
        is_serial_trackable: typing.Union[Unset, bool] = Unset,
        tracking_type: typing.Union[
            Unset,
            typing.Literal[
                "ELECTRONICS",
                "LP_CLOTHES",
                "LP_LINENS",
                "MILK",
                "NCP",
                "NOT_TRACKED",
                "OTP",
                "PERFUMERY",
                "SHOES",
                "TIRES",
                "TOBACCO",
                "WATER",
            ],
        ] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        images: typing.Union[Unset, typing.List[dict]] = Unset,
        alcoholic: typing.Union[Unset, dict] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        country: typing.Union[Unset, types.Meta] = Unset,
        files: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        minimum_balance: typing.Union[Unset, int] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        partial_disposal: typing.Union[Unset, bool] = Unset,
        payment_item_type: typing.Union[
            Unset,
            typing.Literal[
                "GOODS",
                "EXCISABLE_GOOD",
                "COMPOUND_PAYMENT_ITEM",
                "ANOTHER_PAYMENT_ITEM",
            ],
        ] = Unset,
        ppe_type: typing.Union[Unset, str] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        tax_system: typing.Union[
            Unset,
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ],
        ] = Unset,
        things: typing.Union[Unset, typing.List[str]] = Unset,
        tnved: typing.Union[Unset, str] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
    ) -> product_api.Product:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-izmenit-towar

        :param id_: Product ID (ID Товара)
        :param name: Name (Название)
        :param code: Code (Код Комплекта)
        :param external_code: External code (Внешний код комплекта)
        :param description: Description (Описание)
        :param vat: VAT (НДС)
        :param effective_vat: Real VAT (Реальный НДС)
        :param discount_prohibited: Prohibition of discounts (Запрет на скидки)
        :param uom: Unit (Единица измерения)
        :param supplier: Supplier (Поставщик)
        :param min_price: Minimum price (Минимальная цена) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-modifikaciq-modifikacii-atributy-wlozhennyh-suschnostej-minimal-naq-cena
        :param buy_price: Purchase price (Закупочная цена) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-zakupochnaq-cena
        :param sale_prices: Sale prices (Цены продажи)
        :param barcodes: Barcodes (Штрихкоды) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-modifikaciq-modifikacii-atributy-wlozhennyh-suschnostej-shtrih-kody
        :param article: Article (Артикул)
        :param weight: Weight (Вес)
        :param volume: Volume (Объем)
        :param packs: Packs (Упаковки модификации) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-modifikaciq-modifikacii-atributy-wlozhennyh-suschnostej-upakowki-modifikacii
        :param is_serial_trackable: Serial tracking (Серийный учет)
        :param tracking_type: Tracking type (Тип отслеживания) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-suschnosti-tip-markiruemoj-produkcii
        :param attributes: Attributes (Атрибуты)
        :param images: Images (Изображения) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-izobrazhenie
        :param alcoholic: Alcoholic (Объект, содержащий поля алкогольной продукции) https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-ob-ekt-soderzhaschij-polq-alkogol-noj-produkcii
        :param archived: Archived (Архивный)
        :param country: Country (Страна)
        :param files: Files (Метаданные массива Файлов (Максимальное количество файлов - 100))
        :param group: Group (Метаданные отдела сотрудника)
        :param minimum_balance: Minimum balance (Минимальный остаток)
        :param owner: Owner (Метаданные владельца (Сотрудника))
        :param partial_disposal: Partial disposal (Управление состоянием частичного выбытия маркированного товара. «true» - возможность включена.)
        :param payment_item_type: Payment item type (Признак предмета расчета. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-komplekt-komplekty-atributy-suschnosti-priznak-predmeta-rascheta)
        :param ppe_type: PPE type (Код вида номенклатурной классификации медицинских средств индивидуальной защиты (EAN-13)) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-suschnosti-kod-wida-nomenklaturnoj-klassifikacii-medicinskih-sredstw-indiwidual-noj-zaschity
        :param product_folder: Product folder (Метаданные группы товара)
        :param shared: Shared (Общий)
        :param tax_system: Tax system (Система налогообложения) - https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-suschnosti-kod-sistemy-nalogooblozheniq
        :param things: Serial numbers (Серийные номера)
        :param tnved: TNVED (Код ТН ВЭД)
        :param use_parent_vat: Use parent VAT (Использовать родительский НДС)
        :return: Product object (Объект Product)
        """

        return await self(
            product_api.UpdateProductRequest(
                id_=id_,
                name=name,
                code=code,
                external_code=external_code,
                description=description,
                vat=vat,
                effective_vat=effective_vat,
                discount_prohibited=discount_prohibited,
                uom=uom,
                supplier=supplier,
                min_price=min_price,
                buy_price=buy_price,
                sale_prices=sale_prices,
                barcodes=barcodes,
                article=article,
                weight=weight,
                volume=volume,
                packs=packs,
                is_serial_trackable=is_serial_trackable,
                tracking_type=tracking_type,
                attributes=attributes,
                images=images,
                alcoholic=alcoholic,
                archived=archived,
                country=country,
                files=files,
                group=group,
                minimum_balance=minimum_balance,
                owner=owner,
                partial_disposal=partial_disposal,
                payment_item_type=payment_item_type,
                ppe_type=ppe_type,
                product_folder=product_folder,
                shared=shared,
                tax_system=tax_system,
                things=things,
                tnved=tnved,
                use_parent_vat=use_parent_vat,
            )
        )

    async def get_moves(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[move_api.Move]:
        """

        :param limit: Limit of move to get (Лимит передвижений для получения)
        :param offset: Offset of move to get (Отступ передвижений для получения)
        :param search: Search string (Строка поиска)
        """

        return await self(
            move_api.GetMovesRequest(
                limit=limit,
                offset=offset,
                search=search,
            )
        )

    async def create_move(
        self,
        organization: types.Meta,
        source_store: types.Meta,
        target_store: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
        customer_order: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset, typing.List[move_api.CreateMoveRequest.CreatePosition]
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ) -> move_api.Move:
        """

        :param organization: Organization (Организация)
        :param source_store: Source store (Склад-источник)
        :param target_store: Target store (Склад-получатель)

        :param applicable: Applicable (Отметка о проведении)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param internal_order: Internal order (Внутренний заказ)
        :param customer_order: Customer order (Заказ покупателя)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param overhead: Overhead (Накладные расходы)
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        """

        return await self(
            move_api.CreateMoveRequest(
                organization=organization,
                source_store=source_store,
                target_store=target_store,
                applicable=applicable,
                attributes=attributes,
                code=code,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                internal_order=internal_order,
                customer_order=customer_order,
                meta=meta,
                moment=moment,
                name=name,
                overhead=overhead,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                sync_id=sync_id,
            )
        )

    async def delete_move(self, move_id: str) -> None:
        """

        :param move_id: Move id (ID перемещения)
        """
        return await self(move_api.DeleteMoveRequest(move_id=move_id))

    async def get_move(self, move_id: str) -> move_api.Move:
        """

        :param move_id: Move id (ID перемещения)
        """
        return await self(move_api.GetMoveRequest(move_id=move_id))

    async def update_move(
        self,
        move_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        source_store: typing.Union[Unset, types.Meta] = Unset,
        target_store: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
        customer_order: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, types.MetaArray] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ) -> move_api.Move:
        """

        :param move_id: Move id (ID перемещения)

        :param organization: Organization (Организация)
        :param source_store: Source store (Склад-источник)
        :param target_store: Target store (Склад-получатель)
        :param applicable: Applicable (Отметка о проведении)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param internal_order: Internal order (Внутренний заказ)
        :param customer_order: Customer order (Заказ покупателя)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param overhead: Overhead (Накладные расходы)
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        """
        return await self(
            move_api.UpdateMoveRequest(
                move_id=move_id,
                organization=organization,
                source_store=source_store,
                target_store=target_store,
                applicable=applicable,
                attributes=attributes,
                code=code,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                internal_order=internal_order,
                customer_order=customer_order,
                meta=meta,
                moment=moment,
                name=name,
                overhead=overhead,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                sync_id=sync_id,
            )
        )

    async def get_move_positions(
        self,
        move_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[move_api.MovePosition]:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param limit: Limit (Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.)
        :param offset: Offset (Отступ в выдаваемом списке сущностей.)
        :param search: Search (Фильтр документов по указанной поисковой строке.)
        """

        return await self(
            move_api.GetMovePositionsRequest(
                move_id=move_id, limit=limit, offset=offset, search=search
            )
        )

    async def create_move_position(
        self,
        move_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, int] = Unset,
        overhead: typing.Union[Unset, int] = Unset,
    ) -> move_api.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """
        return await self(
            move_api.CreateMovePositionRequest(
                move_id=move_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                overhead=overhead,
            )
        )

    async def get_move_position(
        self, move_id: str, position_id: str
    ) -> move_api.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции перемещения)
        """
        return await self(
            move_api.GetMovePositionRequest(move_id=move_id, position_id=position_id)
        )

    async def update_move_position(
        self,
        move_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, int] = Unset,
        price: typing.Union[Unset, int] = Unset,
        overhead: typing.Union[Unset, int] = Unset,
    ) -> move_api.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """

        return await self(
            move_api.UpdateMovePositionRequest(
                move_id=move_id,
                position_id=position_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                overhead=overhead,
            )
        )

    async def delete_move_position(self, move_id: str, position_id: str) -> None:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции)
        """
        return await self(
            move_api.DeleteMovePositionRequest(move_id=move_id, position_id=position_id)
        )

    # purchase_order
    async def get_purchase_orders(
        self, limit: int = 1000, offset: int = 0, search: str = None
    ) -> typing.List[purchase_order_api.PurchaseOrder]:
        """
        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке.)
        """
        return await self(
            purchase_order_api.GetPurchaseOrderListRequest(
                limit=limit, offset=offset, search=search
            )
        )

    async def create_purchase_order(
        self,
        organization: types.Meta,
        agent: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset,
            typing.List[purchase_order_api.CreatePurchaseOrderRequest.CreatePosition],
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
        wait_sum: typing.Union[Unset, float] = Unset,
        customer_orders: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        invoices_in: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        payments: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        supplies: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
    ) -> purchase_order_api.PurchaseOrder:
        """

        :param organization: Organization meta (Метаданные юрлица)
        :param agent: Agent meta (Метаданные контрагента)
        :param agent_account: Agent account meta (Метаданные счета контрагента)
        :param applicable: Applicable (Действует)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract meta (Метаданные договора)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group meta (Метаданные группы)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param organization_account: Organization account meta (Метаданные счета организации)
        :param owner: Owner meta (Метаданные владельца)
        :param positions: Positions (Позиции)
        :param project: Project meta (Метаданные проекта)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State meta (Метаданные статуса заказа)
        :param store: Store meta (Метаданные склада)
        :param sync_id: Sync ID (ID синхронизации. После заполнения недоступен для изменения)
        :param vat_enabled: Vat enabled (Учитывается ли НДС)
        :param vat_included: Vat included (Включен ли НДС в цену)
        :param wait_sum: Wait sum (Сумма товаров в пути)
        :param customer_orders: Customer orders (Заказы покупателей)
        :param invoices_in: Invoices in (Входящие счета)
        :param payments: Payments (Платежи)
        :param supplies: Supplies (Поставки)
        :param internal_order: Internal order meta (Метаданные внутреннего заказа)
        """

        return await self(
            purchase_order_api.CreatePurchaseOrderRequest(
                organization=organization,
                agent=agent,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                delivery_planned_moment=delivery_planned_moment,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                meta=meta,
                moment=moment,
                name=name,
                organization_account=organization_account,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                store=store,
                sync_id=sync_id,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
                wait_sum=wait_sum,
                customer_orders=customer_orders,
                invoices_in=invoices_in,
                payments=payments,
                supplies=supplies,
                internal_order=internal_order,
            )
        )

    async def delete_purchase_order(self, order_id: str) -> None:
        """

        :param order_id: Order id to delete (ID Заказа поставщику для удаления)
        """
        return await self(
            purchase_order_api.DeletePurchaseOrderRequest(order_id=order_id)
        )

    async def get_purchase_order(
        self, order_id: str
    ) -> purchase_order_api.PurchaseOrder:
        """

        :param order_id: Order id to get (ID Заказа поставщику для получения)
        """
        return await self(purchase_order_api.GetPurchaseOrderRequest(order_id=order_id))

    async def update_purchase_order(
        self,
        order_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset,
            typing.List[purchase_order_api.UpdatePurchaseOrderRequest.UpdatePosition],
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
        wait_sum: typing.Union[Unset, float] = Unset,
        customer_orders: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        invoices_in: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        payments: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        supplies: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
    ) -> purchase_order_api.PurchaseOrder:
        """

        :param order_id: ID Заказа поставщику
        :param organization: Organization meta (Метаданные юрлица)
        :param agent: Agent meta (Метаданные контрагента)
        :param agent_account: Agent account meta (Метаданные счета контрагента)
        :param applicable: Applicable (Действует)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract meta (Метаданные договора)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group meta (Метаданные группы)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param organization_account: Organization account meta (Метаданные счета организации)
        :param owner: Owner meta (Метаданные владельца)
        :param positions: Positions (Позиции)
        :param project: Project meta (Метаданные проекта)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State meta (Метаданные статуса заказа)
        :param store: Store meta (Метаданные склада)
        :param sync_id: Sync ID (ID синхронизации. После заполнения недоступен для изменения)
        :param vat_enabled: Vat enabled (Учитывается ли НДС)
        :param vat_included: Vat included (Включен ли НДС в цену)
        :param wait_sum: Wait sum (Сумма товаров в пути)
        :param customer_orders: Customer orders (Заказы покупателей)
        :param invoices_in: Invoices in (Входящие счета)
        :param payments: Payments (Платежи)
        :param supplies: Supplies (Поставки)
        :param internal_order: Internal order meta (Метаданные внутреннего заказа)
        """
        return await self(
            purchase_order_api.UpdatePurchaseOrderRequest(
                order_id=order_id,
                organization=organization,
                agent=agent,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                delivery_planned_moment=delivery_planned_moment,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                meta=meta,
                moment=moment,
                name=name,
                organization_account=organization_account,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                store=store,
                sync_id=sync_id,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
                wait_sum=wait_sum,
                customer_orders=customer_orders,
                invoices_in=invoices_in,
                payments=payments,
                supplies=supplies,
                internal_order=internal_order,
            )
        )

    async def get_purchase_order_positions(
        self, order_id: str, limit: int = 1000, offset: int = 0
    ) -> typing.List[purchase_order_api.PurchaseOrderPosition]:
        return await self(
            purchase_order_api.GetPurchaseOrderPositionsRequest(
                order_id=order_id, limit=limit, offset=offset
            )
        )

    async def get_purchase_order_position(
        self, order_id: str, position_id: str
    ) -> purchase_order_api.PurchaseOrderPosition:
        return await self(
            purchase_order_api.GetPurchaseOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    async def update_purchase_order_position(
        self,
        order_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        price: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
        in_transit: typing.Union[Unset, int] = Unset,
        discount: typing.Union[Unset, float] = Unset,
    ) -> purchase_order_api.PurchaseOrderPosition:
        return await self(
            purchase_order_api.UpdatePurchaseOrderPositionRequest(
                order_id=order_id,
                position_id=position_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                vat=vat,
                in_transit=in_transit,
                discount=discount,
            )
        )

    async def delete_purchase_order_position(
        self, order_id: str, position_id: str
    ) -> None:
        return await self(
            purchase_order_api.DeletePurchaseOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    # product folders

    async def get_product_folders(
        self, limit: int = 1000, offset: int = 0
    ) -> typing.List[product_folder_api.ProductFolder]:
        """
        Get product folders (Получить папки товаров)
        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        :return: List of product folders (Список папок товаров)
        """
        return await self(
            product_folder_api.GetProductFoldersRequest(limit=limit, offset=offset)
        )

    async def create_product_folder(
        self,
        name: str,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        tax_system: typing.Union[
            Unset,
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ],
        ] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
    ) -> product_folder_api.ProductFolder:
        """
        Create product folder (Создать папку товаров)

        :param name: Name of the product folder (Имя группы товаров)
        :param code: Code of the product folder (Код группы товаров)
        :param description: Description of the product folder (Описание группы товаров)
        :param external_code: External code of the product folder (Внешний код группы товаров)
        :param group: Group of the product folder (Группа группы товаров)
        :param meta: Meta of the product folder (Метаданные группы товаров)
        :param owner: Owner of the product folder (Владелец группы товаров)
        :param product_folder: Product folder of the product folder (Группа товаров группы товаров)
        :param shared: Shared of the product folder (Общий доступ группы товаров)
        :param tax_system: Tax system of the product folder (Код системы налогообложения группы товаров)
        :param use_parent_vat: Use parent vat of the product folder (Используется ли ставка НДС родительской группы)
        :param vat: Vat of the product folder (НДС % группы товаров)
        :param vat_enabled: Vat enabled of the product folder (Включен ли НДС для группы товаров)
        :return: Created product folder (Созданная группа товаров)
        """

        return await self(
            product_folder_api.CreateProductFolderRequest(
                name=name,
                code=code,
                description=description,
                external_code=external_code,
                group=group,
                meta=meta,
                owner=owner,
                product_folder=product_folder,
                shared=shared,
                tax_system=tax_system,
                use_parent_vat=use_parent_vat,
                vat=vat,
                vat_enabled=vat_enabled,
            )
        )

    async def delete_product_folder(
        self,
        folder_id: str,
    ):
        """
        Delete product folder (Удалить папку товаров)
        :param folder_id: Product folder id (ID папки товаров)
        :return: None
        """
        return await self(
            product_folder_api.DeleteProductFolderRequest(folder_id=folder_id)
        )

    async def get_product_folder(
        self,
        folder_id: str,
    ) -> product_folder_api.ProductFolder:
        """
        Get product folder by id (Получить папку товаров по ID)
        :param folder_id: Product folder id (ID папки товаров)
        :return: Product folder (Папка товаров)
        """
        return await self(
            product_folder_api.GetProductFolderRequest(folder_id=folder_id)
        )

    async def update_product_folder(
        self,
        folder_id: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        tax_system: typing.Union[
            Unset,
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ],
        ] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
    ) -> product_folder_api.ProductFolder:
        """
        Update product folder (Обновить папку товаров)
        :param folder_id: Product folder id (ID папки товаров)
        :param name: Name of the product folder (Имя группы товаров)
        :param code: Code of the product folder (Код группы товаров)
        :param description: Description of the product folder (Описание группы товаров)
        :param external_code: External code of the product folder (Внешний код группы товаров)
        :param group: Group of the product folder (Группа группы товаров)
        :param meta: Meta of the product folder (Метаданные группы товаров)
        :param owner: Owner of the product folder (Владелец группы товаров)
        :param product_folder: Product folder of the product folder (Группа товаров группы товаров)
        :param shared: Shared of the product folder (Общий доступ группы товаров)
        :param tax_system: Tax system of the product folder (Код системы налогообложения группы товаров)
        :param use_parent_vat: Use parent vat of the product folder (Используется ли ставка НДС родительской группы)
        :param vat: Vat of the product folder (НДС % группы товаров)
        :param vat_enabled: Vat enabled of the product folder (Включен ли НДС для группы товаров)
        :return: Updated product folder (Обновленная группа товаров)
        """
        return await self(
            product_folder_api.UpdateProductFolderRequest(
                folder_id=folder_id,
                name=name,
                code=code,
                description=description,
                external_code=external_code,
                group=group,
                meta=meta,
                owner=owner,
                product_folder=product_folder,
                shared=shared,
                tax_system=tax_system,
                use_parent_vat=use_parent_vat,
                vat=vat,
                vat_enabled=vat_enabled,
            )
        )

    # enters_api
    async def get_enters(
        self,
        limit: typing.Union[Unset, int] = 1000,
        offset: typing.Union[Unset, int] = 0,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[enter_api.Enter]:
        """

        :param limit: Limit of entities to extract. (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке)
        :return: List of enter (Список приходов)
        """

        return await self(
            enter_api.GetEntersRequest(limit=limit, offset=offset, search=search)
        )

    async def create_enter(
        self,
        organization: types.Meta,
        store: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, list] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        positions: typing.Union[
            Unset, typing.List[enter_api.CreateEnterRequest.CreateEnterPosition]
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ) -> enter_api.Enter:
        """

        :param organization: Organization meta (Метаданные организации)
        :param store: Store meta (Метаданные склада)
        :param applicable: Mark of the document (Отметка о проведении)
        :param attributes: Attributes (Доп. поля)
        :param code: Code (Код)
        :param description: Description (Комментарий)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Отдел сотрудника)
        :param moment: Moment (Дата документа)
        :param name: Name (Номер)
        :param overhead: Overhead (Накладные расходы)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Валюта)
        :param shared: Shared (Общий доступ)
        :return: Created enter (Созданный приход)
        """
        return await self(
            enter_api.CreateEnterRequest(
                organization=organization,
                store=store,
                applicable=applicable,
                attributes=attributes,
                code=code,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                moment=moment,
                name=name,
                overhead=overhead,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
            )
        )

    async def delete_enter(self, enter_id: str) -> None:
        """

        :param enter_id: ID of enter (ID оприходования)
        """
        return await self(enter_api.DeleteEnterRequest(enter_id=enter_id))

    async def get_enter(self, enter_id: str) -> enter_api.Enter:
        """

        :param enter_id: ID of enter (ID оприходования)
        :return: Enter (Оприходование)
        """
        return await self(enter_api.GetEnterRequest(enter_id=enter_id))

    async def update_enter(
        self,
        enter_id: str,
        organization: typing.Union[Unset, str] = Unset,
        store: typing.Union[Unset, str] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, dict] = Unset,
        group: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        positions: typing.Union[
            Unset, typing.List[enter_api.UpdateEnterRequest.UpdateEnterPosition]
        ] = Unset,
        project: typing.Union[Unset, str] = Unset,
        rate: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ) -> enter_api.Enter:
        """

        :param enter_id: ID of enter (ID оприходования)
        :param organization: Organization (Организация)
        :param store: Store (Склад)
        :param applicable: Applicable (Проведен)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param moment: Moment (Момент)
        :param name: Name (Название)
        :param overhead: Overhead (Налоги)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Валюта)
        :param shared: Shared (Общий доступ)
        :return: Updated enter (Обновленное оприходование)
        """
        return await self(
            enter_api.UpdateEnterRequest(
                enter_id=enter_id,
                organization=organization,
                store=store,
                applicable=applicable,
                attributes=attributes,
                code=code,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                moment=moment,
                name=name,
                overhead=overhead,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
            )
        )

    async def get_enter_positions(
        self,
        enter_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[enter_api.EnterPosition]:
        """

        :param enter_id: ID of enter (ID оприходования)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: Enter positions (Позиции оприходования)
        """
        return await self(
            enter_api.GetEnterPositionsRequest(
                enter_id=enter_id,
                limit=limit,
                offset=offset,
            )
        )

    async def create_enter_position(
        self,
        enter_id: str,
        positions: typing.List[
            enter_api.CreateEnterPositionRequest.CreateEnterPosition
        ],
    ) -> typing.List[enter_api.EnterPosition]:
        """

        :param enter_id: Enter id (id Оприходования)
        :param positions: Positions (Позиции)
        :return: Created enter positions (Созданные позиции оприходования)
        """
        return await self(
            enter_api.CreateEnterPositionRequest(
                enter_id=enter_id,
                positions=positions,
            )
        )

    async def get_enter_position(
        self,
        enter_id: str,
        position_id: str,
    ) -> enter_api.EnterPosition:
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id Позиции)
        :return: Enter position (Позиция оприходования)
        """
        return await self(
            enter_api.GetEnterPositionRequest(
                enter_id=enter_id,
                position_id=position_id,
            )
        )

    async def update_enter_position(
        self,
        enter_id: str,
        position_id: str,
        assortment: types.Meta,
        price: float,
        quantity: float,
        country: typing.Union[Unset, types.Meta] = Unset,
        gtd: typing.Union[Unset, typing.Dict] = Unset,
        pack: typing.Union[Unset, typing.Dict] = Unset,
        reason: typing.Union[Unset, str] = Unset,
        slot: typing.Union[Unset, types.Meta] = Unset,
        things: typing.Union[Unset, typing.Dict] = Unset,
        overhead: typing.Union[Unset, int] = Unset,
    ) -> enter_api.EnterPosition:
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id позиции)
        :param assortment: Assortment of position (Метаданные товара/услуги/серии/модификации, которую представляет собой позиция)
        :param price: Price of position (Цена товара/услуги в копейках)
        :param quantity: Quantity of position (Количество товаров/услуг данного вида в позиции)
        :param country: Country of position (Метаданные страны)
        :param gtd: GTD of position (ГТД)
        :param pack: Pack of position (Упаковка Товара)
        :param reason: Reason of position (Причина оприходования данной позиции)
        :param slot: Slot of position (Ячейка на складе)
        :param things: Things of position (Серийные номера)
        :param overhead: Overhead of position (Накладные расходы)
        :return: Updated enter position (Обновленная позиция оприходования)
        """

        return await self(
            enter_api.UpdateEnterPositionRequest(
                enter_id=enter_id,
                position_id=position_id,
                assortment=assortment,
                price=price,
                quantity=quantity,
                country=country,
                gtd=gtd,
                pack=pack,
                reason=reason,
                slot=slot,
                things=things,
                overhead=overhead,
            )
        )

    async def delete_enter_position(
        self,
        enter_id: str,
        position_id: str,
    ) -> None:
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id позиции)
        :return: None
        """
        return await self(
            enter_api.DeleteEnterPositionRequest(
                enter_id=enter_id,
                position_id=position_id,
            )
        )

    # stocks
    async def get_full_stock_report(
        self,
        limit: typing.Union[Unset, int] = 1000,
        offset: typing.Union[Unset, int] = 0,
        group_by: typing.Union[
            Unset, typing.Literal["product", "variant", "consignment"]
        ] = Unset,
        include_related: typing.Union[Unset, bool] = Unset,
    ) -> typing.List[stocks_api.FullStockReport]:
        """

        :param limit: Limit the number of entities to retrieve. (Ограничить количество сущностей для извлечения.)
        :param offset: Offset in the returned list of entities. (Отступ в выдаваемом списке сущностей.)
        :param group_by: Type to group by. (Тип, по которому нужно сгруппировать выдачу.)
        :param include_related: Include consignments for product and variants. (Вывод остатков по модификациям и сериям товаров.)
        :return: List of full stock reports (Список отчетов по остаткам)
        """
        return await self(
            stocks_api.GetFullStockReportRequest(
                limit=limit,
                offset=offset,
                group_by=group_by,
                include_related=include_related,
            )
        )

    async def get_small_stock_current_report(
        self,
        include: typing.Union[Unset, str] = Unset,
        changed_since: typing.Union[Unset, datetime.datetime] = Unset,
        stock_type: typing.Union[
            Unset, typing.Literal["stock", "freeStock", "quantity"]
        ] = Unset,
        filter_assortment_id: typing.Union[Unset, typing.List[str]] = Unset,
        filter_store_id: typing.Union[Unset, typing.List[str]] = Unset,
    ) -> typing.List[stocks_api.SmallStockReport]:
        """

        :param include: Include related entities (Включить связанные сущности)
        :param changed_since: Changed since (Изменено с)
        :param stock_type: Stock type (Тип остатка)
        :param filter_assortment_id: Filter by assortment id (Фильтр по id товара)
        :param filter_store_id: Filter by store id (Фильтр по id склада)
        :return: List of small stock reports (Список отчетов по остаткам)
        """

        return await self(
            stocks_api.GetSmallStockReportCurrentRequest(
                include=include,
                changed_since=changed_since,
                stock_type=stock_type,
                filter_assortment_id=filter_assortment_id,
                filter_store_id=filter_store_id,
            )
        )

    # custom entities
    async def create_custom_entity(
        self,
        name: str,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ) -> custom_entity_api.CustomEntity:
        """
        Create custom entity (Создание пользовательского справочника)

        :param name: Name of custom entity (Наименование Пользовательского справочника)
        :param meta: Meta of custom entity (Метаданные Пользовательского справочника)
        :return: Created custom entity (Созданный пользовательский справочник)
        """

        return await self(
            custom_entity_api.CreateCustomEntityRequest(
                name=name,
                meta=meta,
            )
        )

    async def update_custom_entity(
        self,
        metadata_id: str,
        name: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ) -> custom_entity_api.CustomEntity:
        """
        Update custom entity (Обновление пользовательского справочника)

        :param metadata_id: ID of custom entity (ID Пользовательского справочника)
        :param name: Name of custom entity (Наименование Пользовательского справочника)
        :param meta: Meta of custom entity (Метаданные Пользовательского справочника)
        :return: Updated custom entity (Обновленный пользовательский справочник)
        """
        return await self(
            custom_entity_api.UpdateCustomEntityRequest(
                metadata_id=metadata_id,
                name=name,
                meta=meta,
            )
        )

    async def delete_custom_entity(self, metadata_id: str) -> None:
        """
        Delete custom entity (Удаление пользовательского справочника)

        :param metadata_id: ID of custom entity (ID Пользовательского справочника)
        :return: None
        """
        return await self(
            custom_entity_api.DeleteCustomEntityRequest(
                metadata_id=metadata_id,
            )
        )

    async def create_custom_entity_element(
        self,
        metadata_id: str,
        name: str,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ) -> custom_entity_api.CustomEntityElement:
        """
        Create custom entity element (Создание элемента пользовательского справочника)

        :param metadata_id: ID of the custom entity (ID справочника)
        :param name: Name of the custom entity element (Наименование элемента справочника)
        :param code: Code of the custom entity element (Код элемента справочника)
        :param description: Description of the custom entity element (Описание элемента справочника)
        :param external_code: External code of the custom entity element (Внешний код элемента справочника)
        :param meta: Metadata of the custom entity element (Метаданные элемента справочника)
        :param group: Group of the custom entity element (Отдел элемента справочника)
        :param owner: Owner of the custom entity element (Владелец элемента справочника)
        :param shared: Shared access of the custom entity element (Общий доступ элемента справочника)
        :return: Created custom entity element (Созданный элемент пользовательского справочника)
        """
        return await self(
            custom_entity_api.CreateCustomEntityElementRequest(
                metadata_id=metadata_id,
                name=name,
                code=code,
                description=description,
                external_code=external_code,
                meta=meta,
                group=group,
                owner=owner,
                shared=shared,
            )
        )

    async def update_custom_entity_element(
        self,
        metadata_id: str,
        element_id: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ) -> custom_entity_api.CustomEntityElement:
        """
        Update custom entity element (Обновление элемента пользовательского справочника)

        :param metadata_id: ID of the custom entity (ID справочника)
        :param element_id: ID of the custom entity element (ID элемента справочника)
        :param name: Name of the custom entity element (Наименование элемента справочника)
        :param code: Code of the custom entity element (Код элемента справочника)
        :param description: Description of the custom entity element (Описание элемента справочника)
        :param external_code: External code of the custom entity element (Внешний код элемента справочника)
        :param meta: Metadata of the custom entity element (Метаданные элемента справочника)
        :param group: Group of the custom entity element (Отдел элемента справочника)
        :param owner: Owner of the custom entity element (Владелец элемента справочника)
        :param shared: Shared access of the custom entity element (Общий доступ элемента справочника)
        :return: Updated custom entity element (Обновленный элемент пользовательского справочника)
        """
        return await self(
            custom_entity_api.UpdateCustomEntityElementRequest(
                metadata_id=metadata_id,
                element_id=element_id,
                name=name,
                code=code,
                description=description,
                external_code=external_code,
                meta=meta,
                group=group,
                owner=owner,
                shared=shared,
            )
        )

    async def delete_custom_entity_element(
        self,
        metadata_id: str,
        element_id: str,
    ) -> None:
        """
        Delete custom entity element (Удаление элемента пользовательского справочника)

        :param metadata_id: ID of the custom entity (ID справочника)
        :param element_id: ID of the custom entity element (ID элемента справочника)
        """
        return await self(
            custom_entity_api.DeleteCustomEntityElementRequest(
                metadata_id=metadata_id,
                element_id=element_id,
            )
        )

    async def get_custom_entity_element(
        self,
        metadata_id: str,
        element_id: str,
    ) -> custom_entity_api.CustomEntityElement:
        """
        Get custom entity element (Получение элемента пользовательского справочника)

        :param metadata_id: ID of the custom entity (ID справочника)
        :param element_id: ID of the custom entity element (ID элемента справочника)
        :return: Custom entity element (Элемент пользовательского справочника)
        """
        return await self(
            custom_entity_api.GetCustomEntityElementRequest(
                metadata_id=metadata_id,
                element_id=element_id,
            )
        )

    async def list_custom_entity_elements(
        self,
        metadata_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[custom_entity_api.CustomEntityElement]:
        """
        List custom entity elements (Получение списка элементов пользовательского справочника)

        :param metadata_id: ID of the custom entity (ID справочника)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: List of custom entity elements (Список элементов пользовательского справочника)
        """
        return await self(
            custom_entity_api.GetCustomEntityElementsRequest(
                metadata_id=metadata_id,
                limit=limit,
                offset=offset,
            )
        )

    # store
    async def get_stores(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[store_api.Store]:
        """
        Get store (Получение списка складов)

        :param limit: Limit of entities to extract. (Лимит сущностей для извлечения.)
        :param offset: Offset in the list of entities. (Отступ в выдаваемом списке сущностей.)
        :return: List of store (Список складов)
        """
        return await self(store_api.GetStoresRequest(limit=limit, offset=offset))

    async def create_store(
        self,
        name: str,
        address: typing.Union[Unset, str] = Unset,
        address_full: typing.Union[
            Unset, store_api.CreateStoreRequest.AddressFull
        ] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent: typing.Union[Unset, types.Meta] = Unset,
        path_name: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ) -> store_api.Store:
        """
        Create store (Создание склада)

        :param name: Name of the store. (Название склада.)
        :param address: Address of the store. (Адрес склада.)
        :param address_full: Full address of the store. (Полный адрес склада.)
        :param archived: Archived status of the store. (Статус архивности склада.)
        :param attributes: Attributes of the store. (Атрибуты склада.)
        :param code: Code of the store. (Код склада.)
        :param description: Description of the store. (Описание склада.)
        :param external_code: External code of the store. (Внешний код склада.)
        :param group: Group of the store. (Группа склада.)
        :param meta: Meta of the store. (Метаданные склада.)
        :param owner: Owner of the store. (Владелец склада.)
        :param parent: Parent of the store. (Родительский склад.)
        :param path_name: Path name of the store. (Путь склада.)
        :param shared: Shared status of the store. (Статус общего доступа склада.)
        :return: Store (Склад)
        """

        return await self(
            store_api.CreateStoreRequest(
                name=name,
                address=address,
                address_full=address_full,
                archived=archived,
                attributes=attributes,
                code=code,
                description=description,
                external_code=external_code,
                group=group,
                meta=meta,
                owner=owner,
                parent=parent,
                path_name=path_name,
                shared=shared,
            )
        )

    async def update_store(
        self,
        store_id: str,
        name: typing.Union[Unset, str] = Unset,
        address: typing.Union[Unset, str] = Unset,
        address_full: typing.Union[
            Unset, store_api.UpdateStoreRequest.AddressFull
        ] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent: typing.Union[Unset, types.Meta] = Unset,
        path_name: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ) -> store_api.Store:
        """
        Update store (Обновление склада)

        :param store_id: ID of the store. (ID склада.)
        :param name: Name of the store. (Название склада.)
        :param address: Address of the store. (Адрес склада.)
        :param address_full: Full address of the store. (Полный адрес склада.)
        :param archived: Archived status of the store. (Статус архивности склада.)
        :param attributes: Attributes of the store. (Атрибуты склада.)
        :param code: Code of the store. (Код склада.)
        :param description: Description of the store. (Описание склада.)
        :param external_code: External code of the store. (Внешний код склада.)
        :param group: Group of the store. (Группа склада.)
        :param meta: Meta of the store. (Метаданные склада.)
        :param owner: Owner of the store. (Владелец склада.)
        :param parent: Parent of the store. (Родительский склад.)
        :param path_name: Path name of the store. (Путь склада.)
        :param shared: Shared status of the store. (Статус общего доступа склада.)
        :return: Store (Склад)
        """

        return await self(
            store_api.UpdateStoreRequest(
                store_id=store_id,
                name=name,
                address=address,
                address_full=address_full,
                archived=archived,
                attributes=attributes,
                code=code,
                description=description,
                external_code=external_code,
                group=group,
                meta=meta,
                owner=owner,
                parent=parent,
                path_name=path_name,
                shared=shared,
            )
        )

    async def delete_store(
        self,
        store_id: str,
    ):
        """
        Delete store (Удаление склада)

        :param store_id: ID of the store. (ID склада.)
        """

        return await self(
            store_api.DeleteStoreRequest(
                store_id=store_id,
            )
        )

    async def get_store(
        self,
        store_id: str,
    ) -> store_api.Store:
        """
        Get store (Получение склада)

        :param store_id: ID of the store. (ID склада.)
        :return: Store (Склад)
        """

        return await self(
            store_api.GetStoreRequest(
                store_id=store_id,
            )
        )

    async def get_store_zones(
        self,
        store_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[store_api.StoreZone]:
        """
        Get store zones (Получение зон склада)

        :param store_id: ID of the store. (ID склада.)
        :param limit: Limit of the response. (Лимит ответа.)
        :param offset: Offset of the response. (Смещение ответа.)
        :return: GetStoreZonesResponse (Ответ на запрос получения зон склада)
        """

        return await self(
            store_api.GetStoreZonesRequest(
                store_id=store_id,
                limit=limit,
                offset=offset,
            )
        )

    async def create_store_zone(
        self,
        store_id: str,
        name: str,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ) -> store_api.StoreZone:
        """
        Create store zone (Создание зоны склада)

        :param store_id: ID of the store. (ID склада.)
        :param name: Name of the store zone. (Название зоны склада.)
        :param external_code: External code of the store zone. (Внешний код зоны склада.)
        :param meta: Meta of the store zone. (Метаданные зоны склада.)
        :return: StoreZone (Зона склада)
        """

        return await self(
            store_api.CreateStoreZoneRequest(
                store_id=store_id,
                name=name,
                external_code=external_code,
                meta=meta,
            )
        )

    async def update_store_zone(
        self,
        store_id: str,
        zone_id: str,
        name: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ) -> store_api.StoreZone:
        """
        Update store zone (Обновление зоны склада)

        :param store_id: ID of the store. (ID склада.)
        :param zone_id: ID of the store zone. (ID зоны склада.)
        :param name: Name of the store zone. (Название зоны склада.)
        :param external_code: External code of the store zone. (Внешний код зоны склада.)
        :param meta: Meta of the store zone. (Метаданные зоны склада.)
        :return: StoreZone (Зона склада)
        """

        return await self(
            store_api.UpdateStoreZoneRequest(
                store_id=store_id,
                zone_id=zone_id,
                name=name,
                external_code=external_code,
                meta=meta,
            )
        )

    async def delete_store_zone(
        self,
        store_id: str,
        zone_id: str,
    ):
        """
        Delete store zone (Удаление зоны склада)

        :param store_id: ID of the store. (ID склада.)
        :param zone_id: ID of the store zone. (ID зоны склада.)
        """

        return await self(
            store_api.DeleteStoreZoneRequest(
                store_id=store_id,
                zone_id=zone_id,
            )
        )

    async def get_store_zone(
        self,
        store_id: str,
        zone_id: str,
    ) -> store_api.StoreZone:
        """
        Get store zone (Получение зоны склада)

        :param store_id: ID of the store. (ID склада.)
        :param zone_id: ID of the store zone. (ID зоны склада.)
        :return: StoreZone (Зона склада)
        """

        return await self(
            store_api.GetStoreZoneRequest(
                store_id=store_id,
                zone_id=zone_id,
            )
        )

    async def get_store_slots(
        self,
        store_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[store_api.StoreSlot]:
        """
        Get store slots (Получение ячеек склада)

        :param store_id: ID of the store. (ID склада.)
        :param limit: Limit of the response. (Лимит ответа.)
        :param offset: Offset of the response. (Смещение ответа.)
        :return: GetStoreSlotsResponse (Ответ на запрос получения ячеек склада)
        """

        return await self(
            store_api.GetStoreSlotsRequest(
                store_id=store_id,
                limit=limit,
                offset=offset,
            )
        )

    async def create_store_slot(
        self,
        store_id: str,
        name: str,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        zone: typing.Union[Unset, types.Meta] = Unset,
    ) -> store_api.StoreSlot:
        """
        Create store slot (Создание ячейки склада)

        :param store_id: ID of the store. (ID склада.)
        :param name: Name of the store slot. (Название ячейки склада.)
        :param external_code: External code of the store slot. (Внешний код ячейки склада.)
        :param meta: Meta of the store slot. (Метаданные ячейки склада.)
        :param zone: Zone of the store slot. (Зона ячейки склада.)
        :return: StoreSlot (Ячейка склада)
        """

        return await self(
            store_api.CreateStoreSlotRequest(
                store_id=store_id,
                name=name,
                external_code=external_code,
                meta=meta,
                zone=zone,
            )
        )

    async def update_store_slot(
        self,
        store_id: str,
        slot_id: str,
        name: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        zone: typing.Union[Unset, types.Meta] = Unset,
    ) -> store_api.StoreSlot:
        """
        Update store slot (Обновление ячейки склада)

        :param store_id: ID of the store. (ID склада.)
        :param slot_id: ID of the store slot. (ID ячейки склада.)
        :param name: Name of the store slot. (Название ячейки склада.)
        :param external_code: External code of the store slot. (Внешний код ячейки склада.)
        :param meta: Meta of the store slot. (Метаданные ячейки склада.)
        :param zone: Zone of the store slot. (Зона ячейки склада.)
        :return: StoreSlot (Ячейка склада)
        """

        return await self(
            store_api.UpdateStoreSlotRequest(
                store_id=store_id,
                slot_id=slot_id,
                name=name,
                external_code=external_code,
                meta=meta,
                zone=zone,
            )
        )

    async def delete_store_slot(
        self,
        store_id: str,
        slot_id: str,
    ):
        """
        Delete store slot (Удаление ячейки склада)

        :param store_id: ID of the store. (ID склада.)
        :param slot_id: ID of the store slot. (ID ячейки склада.)
        """

        return await self(
            store_api.DeleteStoreSlotRequest(
                store_id=store_id,
                slot_id=slot_id,
            )
        )

    async def get_store_slot(
        self,
        store_id: str,
        slot_id: str,
    ) -> store_api.StoreSlot:
        """
        Get store slot (Получение ячейки склада)

        :param store_id: ID of the store. (ID склада.)
        :param slot_id: ID of the store slot. (ID ячейки склада.)
        :return: StoreSlot (Ячейка склада)
        """

        return await self(
            store_api.GetStoreSlotRequest(
                store_id=store_id,
                slot_id=slot_id,
            )
        )

    # supply
    async def get_supplies(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[supply_api.Supply]:
        """
        Get supply ;ost (Получение списка приёмок)

        :param limit: Limit of entities to extract (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities (Отступ в выдаваемом списке сущностей)
        :param search: Filter documents by the specified search string (Фильтр документов по указанной поисковой строке)
        :return: List of supply (Список приёмок)
        """

        return await self(
            supply_api.GetSuppliesRequest(
                limit=limit,
                offset=offset,
                search=search,
            )
        )

    async def create_supply(
        self,
        organization: types.Meta,
        agent: types.Meta,
        store: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        incoming_date: typing.Union[Unset, datetime.datetime] = Unset,
        incoming_number: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset, typing.List[supply_api.CreateSupplyRequest.CreatePosition]
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> supply_api.Supply:
        """
        Create supply (Создание приёмки)

        :param organization: Organization (Организация)
        :param agent: Agent (Контрагент)
        :param store: Store (Склад)
        :param agent_account: Metadata of the agent account (Метаданные счета контрагента)
        :param applicable: Mark as applicable (Пометить как проведенный)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract (Договор)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param incoming_date: Incoming date (Дата поступления)
        :param incoming_number: Incoming number (Номер поступления)
        :param moment: Moment (Время документа)
        :param name: Name (Название)
        :param organization_account: Metadata of the organization account (Метаданные счета организации)
        :param overhead: Overhead (Налоги) https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-priemka-priemki-nakladnye-rashody
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        :param vat_enabled: VAT enabled (НДС включен)
        :param vat_included: VAT included (НДС считается)
        :return: Supply (Приёмка)
        """

        return await self(
            supply_api.CreateSupplyRequest(
                organization=organization,
                agent=agent,
                store=store,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                incoming_date=incoming_date,
                incoming_number=incoming_number,
                moment=moment,
                name=name,
                organization_account=organization_account,
                overhead=overhead,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                sync_id=sync_id,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def delete_supply(self, supply_id: str):
        """
        Delete supply (Удалить приемку)

        :param supply_id: ID of the supply (ID приемки)
        """
        return await self(
            supply_api.DeleteSupplyRequest(
                supply_id=supply_id,
            )
        )

    async def get_supply(self, supply_id: str) -> supply_api.Supply:
        """
        Get supply (Получить приемку)

        :param supply_id: ID of the supply (ID приемки)
        :return: Supply (Приёмка)
        """
        return await self(
            supply_api.GetSupplyRequest(
                supply_id=supply_id,
            )
        )

    async def update_supply(
        self,
        supply_id: str,
        organization: typing.Union[Unset, types.Meta],
        agent: typing.Union[Unset, types.Meta],
        store: typing.Union[Unset, types.Meta],
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        incoming_date: typing.Union[Unset, datetime.datetime] = Unset,
        incoming_number: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset, typing.List[supply_api.UpdateSupplyRequest.UpdatePosition]
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> supply_api.Supply:
        """
        Update supply (Редактировать приемку)

        :param supply_id: ID of the supply (ID приемки)
        :param organization: Organization (Организация)
        :param agent: Agent (Контрагент)
        :param store: Store (Склад)
        :param agent_account: Metadata of the agent account (Метаданные счета контрагента)
        :param applicable: Mark as applicable (Пометить как проведенный)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract (Договор)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param incoming_date: Incoming date (Дата поступления)
        :param incoming_number: Incoming number (Номер поступления)
        :param moment: Moment (Время документа)
        :param name: Name (Название)
        :param organization_account: Metadata of the organization account (Метаданные счета организации)
        :param overhead: Overhead (Налоги) https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-priemka-priemki-nakladnye-rashody
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        :param vat_enabled: VAT enabled (НДС включен)
        :param vat_included: VAT included (НДС считается)
        :return: Supply (Приёмка)
        """
        return await self(
            supply_api.UpdateSupplyRequest(
                supply_id=supply_id,
                organization=organization,
                agent=agent,
                store=store,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                incoming_date=incoming_date,
                incoming_number=incoming_number,
                moment=moment,
                name=name,
                organization_account=organization_account,
                overhead=overhead,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                sync_id=sync_id,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def get_supply_positions(
        self,
        supply_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[supply_api.Position]:
        """
        Get supply positions
        Получить позиции приемки

        :param supply_id: ID of supply (ID приемки)
        :param limit: Limit of positions (Максимальное количество позиций)
        :param offset: Offset of positions (Отступ в выдаваемом списке позиций)
        :return: List of positions (Список позиций)
        """
        return await self(
            supply_api.GetSupplyPositionsRequest(
                supply_id=supply_id,
                limit=limit,
                offset=offset,
            )
        )

    async def create_supply_position(
        self,
        supply_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, int] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        tracking_codes: typing.Union[Unset, typing.List[dict]] = Unset,
        overhead: typing.Union[Unset, float] = Unset,
    ) -> supply_api.Position:
        """
        Create supply position
        Создать позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param assortment: Assortment (Информация о товаре)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param discount: Discount (Скидка)
        :param vat: VAT (НДС)
        :param tracking_codes: Tracking codes (Коды отслеживания)
        :param overhead: Overhead (Накладные расходы)
        :return: Position (Позиция)
        """
        return await self(
            supply_api.CreateSupplyPositionRequest(
                supply_id=supply_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                discount=discount,
                vat=vat,
                tracking_codes=tracking_codes,
                overhead=overhead,
            )
        )

    async def get_supply_position(
        self,
        supply_id: str,
        position_id: str,
    ) -> supply_api.Position:
        """
        Get supply position
        Получить позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param position_id: ID of position (ID позиции приемки)
        :return: Position (Позиция)
        """
        return await self(
            supply_api.GetSupplyPositionRequest(
                supply_id=supply_id,
                position_id=position_id,
            )
        )

    async def update_supply_position(
        self,
        supply_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, int] = Unset,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, int] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        tracking_codes: typing.Union[Unset, typing.List[dict]] = Unset,
        overhead: typing.Union[Unset, float] = Unset,
    ) -> supply_api.Position:
        """
        Update supply position
        Изменить позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param position_id: ID of position (ID позиции приемки)
        :param assortment: Assortment (Информация о товаре)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param discount: Discount (Скидка)
        :param vat: VAT (НДС)
        :param tracking_codes: Tracking codes (Коды отслеживания)
        :param overhead: Overhead (Накладные расходы)
        :return: Position (Позиция)
        """
        return await self(
            supply_api.UpdateSupplyPositionRequest(
                supply_id=supply_id,
                position_id=position_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                discount=discount,
                vat=vat,
                tracking_codes=tracking_codes,
                overhead=overhead,
            )
        )

    async def delete_supply_position(
        self,
        supply_id: str,
        position_id: str,
    ) -> None:
        """
        Delete supply position
        Удалить позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param position_id: ID of position (ID позиции приемки)
        """
        return await self(
            supply_api.DeleteSupplyPositionRequest(
                supply_id=supply_id,
                position_id=position_id,
            )
        )

    # demand
    async def create_demand(
        self,
        organization: types.Meta,
        agent: types.Meta,
        store: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, list] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, bool] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset, demand_api.CreateDemandRequest.CreateDemandPosition
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, bool] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        shipment_address: typing.Union[Unset, str] = Unset,
        shipment_address_full: typing.Union[Unset, dict] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> demand_api.Demand:
        """
        Creates a demand
        Создаёт отгрузку

        :param organization: Organization (организация)
        :param agent: Agent (контрагент)
        :param store: Store (склад)
        :param agent_account: Agent account (Аккаунт контрагента)
        :param applicable: Is applicable (Проведено(
        :param attributes: Attributes (массив дополнительных полей)
        :param code: Code (код)
        :param contract: Contract (договор)
        :param description: Description (описание)
        :param external_code: External code (внешний код)
        :param files: Files (файлы)
        :param group: Group (группа)
        :param moment: Creation date (Время создания)
        :param name: Name (название)
        :param organization_account: Organization account (аккаунт организации)
        :param overhead: Overhead (накладные расходы)
        :param owner: Owner (владелец)
        :param positions: Positions (позиции)
        :param project: Project (проект)
        :param rate: Rate (валюта)
        :param sales_channel: Sales channel (канал продаж)
        :param shared: Shared (общий доступ)
        :param shipment_address: Shipment address (адрес доставки)
        :param shipment_address_full: Shipment address full (полный адрес доставки)
        :param state: State (статус)
        :param sync_id: Sync id (id синхронизации)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)

        :return: Demand (Отгрузка)
        """
        return await self(
            demand_api.CreateDemandRequest(
                organization=organization,
                agent=agent,
                store=store,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                moment=moment,
                name=name,
                organization_account=organization_account,
                overhead=overhead,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                sales_channel=sales_channel,
                shared=shared,
                shipment_address=shipment_address,
                shipment_address_full=shipment_address_full,
                state=state,
                sync_id=sync_id,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def get_demand(self, demand_id: str) -> demand_api.Demand:
        """
        Get demand
        Получить отгрузку

        :param demand_id: ID of demand (ID отгрузки)
        :return: Demand (Отгрузка)
        """
        return await self(demand_api.GetDemandRequest(demand_id=demand_id))

    async def get_demands(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[demand_api.Demand]:
        """
        Get demand
        Получить отгрузки

        :param limit: Limit (ограничение)
        :param offset: Offset (смещение)
        :param search: Search (поиск)
        :return: List of demand (список отгрузок)
        """
        return await self(
            demand_api.GetDemandsRequest(
                limit=limit,
                offset=offset,
                search=search,
            )
        )

    async def update_demand(
        self,
        demand_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, list] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, bool] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[
            Unset, demand_api.UpdateDemandRequest.UpdateDemandPosition
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, bool] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        shipment_address: typing.Union[Unset, str] = Unset,
        shipment_address_full: typing.Union[Unset, dict] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> demand_api.Demand:
        """

        :param demand_id: ID (идентификатор)
        :param organization: Organization (организация)
        :param agent: Agent (контрагент)
        :param store: Store (склад)
        :param agent_account: Agent account (Аккаунт контрагента)
        :param applicable: Is applicable (Проведено(
        :param attributes: Attributes (массив дополнительных полей)
        :param code: Code (код)
        :param contract: Contract (договор)
        :param description: Description (описание)
        :param external_code: External code (внешний код)
        :param files: Files (файлы)
        :param group: Group (группа)
        :param moment: Creation date (Время создания)
        :param name: Name (название)
        :param organization_account: Organization account (аккаунт организации)
        :param overhead: Overhead (накладные расходы)
        :param owner: Owner (владелец)
        :param positions: Positions (позиции)
        :param project: Project (проект)
        :param rate: Rate (валюта)
        :param sales_channel: Sales channel (канал продаж)
        :param shared: Shared (общий доступ)
        :param shipment_address: Shipment address (адрес доставки)
        :param shipment_address_full: Shipment address full (полный адрес доставки)
        :param state: State (статус)
        :param sync_id: Sync id (id синхронизации)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)

        :return: Demand (Отгрузка)
        """
        return await self(
            demand_api.UpdateDemandRequest(
                demand_id=demand_id,
                organization=organization,
                agent=agent,
                store=store,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                moment=moment,
                name=name,
                organization_account=organization_account,
                overhead=overhead,
                owner=owner,
                positions=positions,
                project=project,
                rate=rate,
                sales_channel=sales_channel,
                shared=shared,
                shipment_address=shipment_address,
                shipment_address_full=shipment_address_full,
                state=state,
                sync_id=sync_id,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def delete_demand(self, demand_id: str) -> None:
        """
        Delete demand
        Удалить отгрузку

        :param demand_id: ID (идентификатор)
        :return:
        """
        await self(demand_api.DeleteDemandRequest(demand_id=demand_id))

    async def create_demand_positions(
        self,
        demand_id: str,
        positions: typing.List[
            demand_api.CreateDemandPositionsRequest.CreateDemandPositionPosition
        ],
    ) -> typing.List[demand_api.DemandPosition]:
        """
        Create demand positions
        Создать позиции отгрузки

        :param demand_id: ID (идентификатор)
        :param positions: Positions (позиции)
        :return: List of demand positions (список позиций отгрузки)
        """

        return await self(
            demand_api.CreateDemandPositionsRequest(
                demand_id=demand_id, positions=positions
            )
        )

    async def get_demand_positions(
        self, demand_id: str, limit: int = 1000, offset: int = 0
    ) -> typing.List[demand_api.DemandPosition]:
        """
        Get demand positions
        Получить позиции отгрузки

        :param demand_id: ID (идентификатор)
        :param limit: Limit (лимит)
        :param offset: Offset (смещение)
        :return: List of demand positions (список позиций отгрузки)
        """

        return await self(
            demand_api.GetDemandPositionsRequest(
                demand_id=demand_id, limit=limit, offset=offset
            )
        )

    async def get_demand_position(
        self, demand_id: str, position_id: str
    ) -> demand_api.DemandPosition:
        """
        Get demand position
        Получить позицию отгрузки

        :param demand_id: ID of demand (ID отгрузки)
        :param position_id: ID of position (ID позиции)
        :return: Demand position (позиция отгрузки)
        """
        return await self(
            demand_api.GetDemandPositionRequest(
                demand_id=demand_id, position_id=position_id
            )
        )

    async def update_demand_position(
        self,
        demand_id: str,
        position_id: str,
        position: demand_api.UpdateDemandPositionRequest.UpdateDemandPositionPosition,
    ) -> demand_api.DemandPosition:
        """
        Update demand position
        Изменить позицию отгрузки

        :param demand_id: ID of demand (ID отгрузки)
        :param position_id: ID of position (ID позиции)
        :param position: Position (позиция)
        :return: Demand position (позиция отгрузки)
        """
        return await self(
            demand_api.UpdateDemandPositionRequest(
                demand_id=demand_id, position_id=position_id, position=position
            )
        )

    async def delete_demand_position(self, demand_id: str, position_id: str) -> None:
        """
        Delete demand position
        Удалить позицию отгрузки

        :param demand_id: ID of demand (ID отгрузки)
        :param position_id: ID of position (ID позиции)
        :return:
        """
        await self(
            demand_api.DeleteDemandPositionRequest(
                demand_id=demand_id, position_id=position_id
            )
        )

    # organization
    async def get_organizations(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[organization_api.Organization]:
        """

        :param limit:  Limit (макс. )
        :param offset: Offset (Смещение)
        :return: List of organization (список организаций)
        """
        return await self(
            organization_api.GetOrganizationsRequest(limit=limit, offset=offset)
        )

    async def get_organization(
        self, organization_id: str
    ) -> organization_api.Organization:
        """

        :param organization_id: ID (идентификатор)
        :return: Organization (организация)
        """
        return await self(
            organization_api.GetOrganizationRequest(organization_id=organization_id)
        )

    async def create_organization(
        self,
        name: str,
        actual_address: typing.Union[Unset, str] = Unset,
        actual_address_full: typing.Union[Unset, dict] = Unset,
        archived: bool = None,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        bonus_program: typing.Union[Unset, types.Meta] = Unset,
        code: typing.Union[Unset, str] = Unset,
        company_type: typing.Literal["legal", "entrepreneur", "individual"] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: str = None,
        group: types.Meta = None,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: bool = None,
        sync_id: typing.Union[Unset, str] = Unset,
        tracking_contract_date: typing.Union[Unset, datetime.datetime] = Unset,
        tracking_contract_number: typing.Union[Unset, str] = Unset,
    ) -> organization_api.Organization:
        """

        :param name: Name of organization (Название организации)
        :param actual_address: Actual address (Фактический адрес)
        :param actual_address_full: Actual address full (Полный фактический адрес)
        :param archived: Is archived (Архивирован)
        :param attributes: Attributes (Атрибуты)
        :param bonus_program: Bonus program (Бонусная программа)
        :param code: Code (Код)
        :param company_type: Company type (Тип компании)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param group: Group (Группа)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий доступ)
        :param sync_id: Sync id (Синхронизационный id)
        :param tracking_contract_date: Tracking contract date (Дата договора отслеживания)
        :param tracking_contract_number: Tracking contract number (Номер договора отслеживания)
        :return: Organization (организация)
        """
        return await self(
            organization_api.CreateOrganizationRequest(
                name=name,
                actual_address=actual_address,
                actual_address_full=actual_address_full,
                archived=archived,
                attributes=attributes,
                bonus_program=bonus_program,
                code=code,
                company_type=company_type,
                description=description,
                external_code=external_code,
                group=group,
                owner=owner,
                shared=shared,
                sync_id=sync_id,
                tracking_contract_date=tracking_contract_date,
                tracking_contract_number=tracking_contract_number,
            )
        )

    async def update_organization(
        self,
        organization_id: str,
        name: typing.Union[Unset, str] = Unset,
        actual_address: typing.Union[Unset, str] = Unset,
        actual_address_full: typing.Union[Unset, dict] = Unset,
        archived: bool = None,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        bonus_program: typing.Union[Unset, types.Meta] = Unset,
        code: typing.Union[Unset, str] = Unset,
        company_type: typing.Literal["legal", "entrepreneur", "individual"] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: str = None,
        group: types.Meta = None,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: bool = None,
        sync_id: typing.Union[Unset, str] = Unset,
        tracking_contract_date: typing.Union[Unset, datetime.datetime] = Unset,
        tracking_contract_number: typing.Union[Unset, str] = Unset,
    ) -> organization_api.Organization:
        """

        :param organization_id: Organization id (Идентификатор организации)
        :param name: Name of organization (Название организации)
        :param actual_address: Actual address (Фактический адрес)
        :param actual_address_full: Actual address full (Полный фактический адрес)
        :param archived: Is archived (Архивирован)
        :param attributes: Attributes (Атрибуты)
        :param bonus_program: Bonus program (Бонусная программа)
        :param code: Code (Код)
        :param company_type: Company type (Тип компании)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param group: Group (Группа)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий доступ)
        :param sync_id: Sync id (Синхронизационный id)
        :param tracking_contract_date: Tracking contract date (Дата договора отслеживания)
        :param tracking_contract_number: Tracking contract number (Номер договора отслеживания)
        :return: Organization (организация)
        """
        return await self(
            organization_api.UpdateOrganizationRequest(
                organization_id=organization_id,
                name=name,
                actual_address=actual_address,
                actual_address_full=actual_address_full,
                archived=archived,
                attributes=attributes,
                bonus_program=bonus_program,
                code=code,
                company_type=company_type,
                description=description,
                external_code=external_code,
                group=group,
                owner=owner,
                shared=shared,
                sync_id=sync_id,
                tracking_contract_date=tracking_contract_date,
                tracking_contract_number=tracking_contract_number,
            )
        )

    async def delete_organization(self, organization_id: str) -> None:
        """

        :param organization_id: Organization id (Идентификатор организации)
        :return:
        """
        await self(
            organization_api.DeleteOrganizationRequest(organization_id=organization_id)
        )

    async def create_webhook(
        self,
        url: str,
        entity_type: str,
        action: str,
        diff_type: typing.Union[Unset, str] = Unset,
    ) -> webhook_api.Webhook:
        """
        Create a webhook

        :param url: URL of webhook (URL вебхука)
        :param entity_type: type of entity (Тип сущности)
        :param action: type of action (Тип действия)
        :param diff_type: diff type for update action (Тип изменения для действия обновления)
        """
        return await self(
            webhook_api.CreateWebhookRequest(
                url=url,
                entity_type=entity_type,
                action=action,
                diff_type=diff_type,
            )
        )

    async def get_webhook(self, webhook_id: str) -> webhook_api.Webhook:
        """
        Get a webhook

        :param webhook_id: ID of webhook (ID вебхука)
        """
        return await self(webhook_api.GetWebhookRequest(webhook_id=webhook_id))

    async def get_webhooks(self) -> typing.List[webhook_api.Webhook]:
        """
        Get webhook
        """
        return await self(webhook_api.GetWebhooksRequest())

    async def delete_webhook(self, webhook_id: str) -> None:
        """
        Delete a webhook

        :param webhook_id: ID of webhook (ID вебхука)
        """
        await self(webhook_api.DeleteWebhookRequest(webhook_id=webhook_id))

    async def update_webhook(
        self,
        webhook_id: str,
        url: typing.Union[Unset, str] = Unset,
        entity_type: typing.Union[Unset, str] = Unset,
        action: typing.Union[Unset, str] = Unset,
        diff_type: typing.Union[Unset, str] = Unset,
    ) -> webhook_api.Webhook:
        """
        Update a webhook

        :param webhook_id: ID of webhook (ID вебхука)
        :param url: URL of webhook (URL вебхука)
        :param entity_type: type of entity (Тип сущности)
        :param action: type of action (Тип действия)
        :param diff_type: diff type for update action (Тип изменения для действия обновления)
        """
        return await self(
            webhook_api.UpdateWebhookRequest(
                webhook_id=webhook_id,
                url=url,
                entity_type=entity_type,
                action=action,
                diff_type=diff_type,
            )
        )

    # invoice in
    async def get_invoices_in(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ) -> typing.List[invoice_in_api.InvoiceIn]:
        """
        Get invoices in
        Получить счета-фактуры поставщиков

        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :param search: Search (Поиск)
        :return: List of invoices in (Список счетов-фактур поставщиков)
        """
        return await self(
            invoice_in_api.GetInvoicesInRequest(
                limit=limit,
                offset=offset,
                search=search,
            )
        )

    async def create_invoice_in(
        self,
        name: str,
        organization: types.Meta,
        agent: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        incoming_date: typing.Union[Unset, datetime.datetime] = Unset,
        incoming_number: typing.Union[Unset, float] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payed_sum: typing.Union[Unset, float] = Unset,
        payment_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        positions: typing.Union[
            Unset,
            typing.List[invoice_in_api.CreateInvoiceInRequest.CreateInvoiceInPosition],
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> typing.List[invoice_in_api.InvoiceIn]:
        """
        Создание счета поставщика

        :param name: Invoice number (Номер счета)
        :param organization: Link to your organization in Metadata format (Ссылка на ваше юрлицо в формате Метаданных
        :param agent: Link to the counterparty (supplier) in Metadata format (Ссылка на контрагента (поставщика) в формате Метаданных)
        :param agent_account: Link to the counterparty's account in Metadata format (Ссылка на счет контрагента в формате Метаданных)
        :param applicable: Marking for the document (Отметка о проведении)
        :param attributes: Additional fields operators (Операторы доп. полей)
        :param code: Invoice code (Код счета)
        :param contract: Link to the contract in Metadata format (Ссылка на договор в формате Метаданных)
        :param description: Invoice comment (Комментарий счета)
        :param external_code: Invoice external code (Внешний код счета)
        :param files: File array metadata (Метаданные массива Файлов)
        :param group: Department of the employee (Отдел сотрудника)
        :param incoming_date: Incoming date (Входящая дата)
        :param incoming_number: Incoming number (Входящий номер)
        :param moment: Document date (Дата документа)
        :param organization_account: Link to the organization's account in Metadata format (Ссылка на счет юрлица в формате Метаданных)
        :param owner: Owner (Employee) (Владелец (Сотрудник))
        :param payed_sum: Amount of incoming payments on the invoice (Сумма входящих платежей по счету)
        :param payment_planned_moment: Planned payment date (Планируемая дата оплаты)
        :param positions: Invoice positions (Позиции счета)
        :param project: Link to the project in Metadata format (Ссылка на проект в формате Метаданных)
        :param rate: Currency (Валюта)
        :param shared: Common Access (Общий доступ)
        :param state: Link to the status of the account in Metadata format (Ссылка на статус счета в формате Метаданных)
        :param store: Link to the warehouse in Metadata format (Ссылка на склад в формате Метаданных)
        :param vat_enabled: Is VAT taken into account (Учитывается ли НДС)
        :param vat_included: Is VAT included in the price (Включен ли НДС в цену)
        :return: Invoice (Счет)
        """
        return await self(
            invoice_in_api.CreateInvoiceInRequest(
                name=name,
                organization=organization,
                agent=agent,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                incoming_date=incoming_date,
                incoming_number=incoming_number,
                moment=moment,
                organization_account=organization_account,
                owner=owner,
                payed_sum=payed_sum,
                payment_planned_moment=payment_planned_moment,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                store=store,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def delete_invoice_in(self, invoice_id: str) -> None:
        """
        Delete invoice in
        Удалить счет поставщика

        :param invoice_id: ID of invoice (ID счета)
        """
        await self(invoice_in_api.DeleteInvoiceInRequest(invoice_id=invoice_id))

    async def get_invoice_in(self, invoice_id: str) -> invoice_in_api.InvoiceIn:
        """
        Get invoice in
        Получить счет поставщика

        :param invoice_id: ID of invoice (ID счета)
        :return: Invoice (Счет)
        """
        return await self(invoice_in_api.GetInvoiceInRequest(invoice_id=invoice_id))

    async def update_invoice_in(
        self,
        invoice_in_id: str,
        name: typing.Union[Unset, str],
        organization: typing.Union[Unset, types.Meta],
        agent: typing.Union[Unset, types.Meta],
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        incoming_date: typing.Union[Unset, datetime.datetime] = Unset,
        incoming_number: typing.Union[Unset, float] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payed_sum: typing.Union[Unset, float] = Unset,
        payment_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        positions: typing.Union[
            Unset,
            typing.List[invoice_in_api.UpdateInvoiceInRequest.UpdateInvoiceInPosition],
        ] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ) -> invoice_in_api.InvoiceIn:
        """
        Изменение счета поставщика

        :param invoice_in_id: ID of invoice (ID счета)
        :param name: Invoice number (Номер счета)
        :param organization: Link to your organization in Metadata format (Ссылка на ваше юрлицо в формате Метаданных
        :param agent: Link to the counterparty (supplier) in Metadata format (Ссылка на контрагента (поставщика) в формате Метаданных)
        :param agent_account: Link to the counterparty's account in Metadata format (Ссылка на счет контрагента в формате Метаданных)
        :param applicable: Marking for the document (Отметка о проведении)
        :param attributes: Additional fields operators (Операторы доп. полей)
        :param code: Invoice code (Код счета)
        :param contract: Link to the contract in Metadata format (Ссылка на договор в формате Метаданных)
        :param description: Invoice comment (Комментарий счета)
        :param external_code: Invoice external code (Внешний код счета)
        :param files: File array metadata (Метаданные массива Файлов)
        :param group: Department of the employee (Отдел сотрудника)
        :param incoming_date: Incoming date (Входящая дата)
        :param incoming_number: Incoming number (Входящий номер)
        :param moment: Document date (Дата документа)
        :param organization_account: Link to the organization's account in Metadata format (Ссылка на счет юрлица в формате Метаданных)
        :param owner: Owner (Employee) (Владелец (Сотрудник))
        :param payed_sum: Amount of incoming payments on the invoice (Сумма входящих платежей по счету)
        :param payment_planned_moment: Planned payment date (Планируемая дата оплаты)
        :param positions: Invoice positions (Позиции счета)
        :param project: Link to the project in Metadata format (Ссылка на проект в формате Метаданных)
        :param rate: Currency (Валюта)
        :param shared: Common Access (Общий доступ)
        :param state: Link to the status of the account in Metadata format (Ссылка на статус счета в формате Метаданных)
        :param store: Link to the warehouse in Metadata format (Ссылка на склад в формате Метаданных)
        :param vat_enabled: Is VAT taken into account (Учитывается ли НДС)
        :param vat_included: Is VAT included in the price (Включен ли НДС в цену)
        :return: Invoice (Счет)
        """
        return await self(
            invoice_in_api.UpdateInvoiceInRequest(
                invoice_in_id=invoice_in_id,
                name=name,
                organization=organization,
                agent=agent,
                agent_account=agent_account,
                applicable=applicable,
                attributes=attributes,
                code=code,
                contract=contract,
                description=description,
                external_code=external_code,
                files=files,
                group=group,
                incoming_date=incoming_date,
                incoming_number=incoming_number,
                moment=moment,
                organization_account=organization_account,
                owner=owner,
                payed_sum=payed_sum,
                payment_planned_moment=payment_planned_moment,
                positions=positions,
                project=project,
                rate=rate,
                shared=shared,
                state=state,
                store=store,
                vat_enabled=vat_enabled,
                vat_included=vat_included,
            )
        )

    async def get_invoice_in_positions(
        self,
        invoice_in_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ) -> typing.List[invoice_in_api.InvoiceInPosition]:
        """
        Get invoice in positions
        Получить позиции счета поставщика

        :param invoice_in_id: ID of invoice (ID счета)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: List of invoice in positions (Список позиций счета поставщика)
        """
        return await self(
            invoice_in_api.GetInvoiceInPositionsRequest(
                invoice_in_id=invoice_in_id,
                limit=limit,
                offset=offset,
            )
        )

    async def get_invoice_in_position(
        self,
        invoice_in_id: str,
        position_id: str,
    ) -> invoice_in_api.InvoiceInPosition:
        """
        Get invoice in position
        Получить позицию счета поставщика

        :param invoice_in_id: ID of invoice (ID счета)
        :param position_id: ID of position (ID позиции)
        :return: Invoice position (Позиция счета)
        """
        return await self(
            invoice_in_api.GetInvoiceInPositionRequest(
                invoice_in_id=invoice_in_id,
                position_id=position_id,
            )
        )

    async def create_invoice_in_position(
        self,
        invoice_in_id: str,
        quantity: float,
        assortment: types.Meta,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
    ) -> invoice_in_api.InvoiceInPosition:
        """
        Добавить позицию счета поставщика

        :param invoice_in_id: ID счета поставщика
        :param quantity: Количество товара
        :param assortment: Товар
        :param price: Цена товара
        :param discount: Скидка
        :param vat: НДС
        :return: Invoice position (Позиция счета)
        """
        return await self(
            invoice_in_api.CreateInvoiceInPositionRequest(
                invoice_in_id=invoice_in_id,
                quantity=quantity,
                assortment=assortment,
                price=price,
                discount=discount,
                vat=vat,
            )
        )

    async def delete_invoice_in_position(
        self,
        invoice_in_id: str,
        position_id: str,
    ) -> None:
        """
        Delete invoice in position
        Удалить позицию счета поставщика

        :param invoice_in_id: ID of invoice (ID счета)
        :param position_id: ID of position (ID позиции)
        """
        await self(
            invoice_in_api.DeleteInvoiceInPositionRequest(
                invoice_in_id=invoice_in_id,
                position_id=position_id,
            )
        )

    async def update_invoice_in_position(
        self,
        invoice_in_id: str,
        position_id: str,
        quantity: typing.Union[Unset, float] = Unset,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
    ) -> invoice_in_api.InvoiceInPosition:
        """
        Изменить позицию счета поставщика

        :param invoice_in_id: ID счета поставщика
        :param position_id: ID позиции
        :param quantity: Количество товара
        :param assortment: Товар
        :param price: Цена товара
        :param discount: Скидка
        :param vat: НДС
        :return: Invoice position (Позиция счета)
        """
        return await self(
            invoice_in_api.UpdateInvoiceInPositionRequest(
                invoice_in_id=invoice_in_id,
                position_id=position_id,
                quantity=quantity,
                assortment=assortment,
                price=price,
                discount=discount,
                vat=vat,
            )
        )

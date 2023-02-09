import typing
import base64
import aiohttp
import datetime
from ..errors import MoySkladError
from .. import types

from ..api.entities import (
    internalorders as internalorders_api,
    products as products_api,
    moves as moves_api,
    purchaseorders as purchaseorders_api,
    productfolders as productfolders_api,
    enters as enters_api,
)
from ..api.reports import stocks
import json


class MoySkladClient:
    def __init__(
        self,
        login: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        api_token: typing.Optional[str] = None,
        debug: bool = False,
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

            async with session.request(method, url, **kwargs) as resp:
                if self._debug:
                    print(
                        f"Request: {method} {url} {kwargs.get('json', '')} {kwargs.get('data', '')}\n"
                        f"Response: {resp.status} {await resp.text()}"
                    )
                if resp.content_type != "application/json":
                    if allow_non_json:
                        return {}
                    raise ValueError(
                        f"Response is not JSON: `{resp.content_type}` : {await resp.text()}"
                    )
                json_resp = await resp.json()
                if resp.status >= 400:
                    if self._debug:
                        print(f"Raising error!")
                    raise MoySkladError(json_resp["errors"][0], json_text)
                return json_resp

    # function that allows us to use MoySkladClient as a caller
    # (функция, которая позволяет нам использовать MoySkladClient как вызывающий)
    async def __call__(self, request):
        if not isinstance(request, types.ApiRequest):
            raise TypeError("request must be an ApiRequest")
        result = await self.request(**request.to_request())
        return request.from_response(result)

    # internal orders (внутренние заказы)

    async def get_internal_orders(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ) -> typing.List[internalorders_api.InternalOrder]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennie-zakazy

        Get a list of internal orders. (Получает список внутренних заказов.)
        :param limit: Limit the number of results (Ограничить количество результатов)
        :param offset:  Offset the results (Сместить результаты)
        :param search:  Search query (Поисковый запрос)
        :return: List of InternalOrder objects (Список объектов InternalOrder)
        """
        return await self(
            internalorders_api.GetInternalOrdersRequest(
                limit=limit, offset=offset, search=search
            )
        )

    async def create_internal_order(
        self,
        organization: types.Meta,
        owner: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        group: typing.Optional[types.Meta] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        moment: typing.Optional[typing.Union[str, datetime.datetime]] = None,
        applicable: typing.Optional[bool] = None,
        rate: typing.Optional[types.Rate] = None,
        sum_: typing.Optional[int] = None,
        store: typing.Optional[types.Meta] = None,
        project: typing.Optional[types.Meta] = None,
        state: typing.Optional[types.Meta] = None,
        positions: typing.Optional[
            typing.List[internalorders_api.CreateInternalOrderRequest.CreatePosition]
        ] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        delivery_planned_moment: typing.Optional[datetime.datetime] = None,
        files: typing.Optional[list] = None,
        moves: typing.Optional[list] = None,
        purchase_orders: typing.Optional[list] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
    ) -> internalorders_api.InternalOrder:
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
            internalorders_api.CreateInternalOrderRequest(
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

    async def get_internal_order(self, id_: str) -> internalorders_api.InternalOrder:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennij-zakaz

        Get an internal order. (Получает внутренний заказ.)
        :param id_: Internal order ID (ID внутреннего заказа)
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(internalorders_api.GetInternalOrderRequest(id_=id_))

    async def update_internal_order(
        self,
        id_: str,
        organization: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        group: typing.Optional[types.Meta] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        moment: typing.Optional[typing.Union[str, datetime.datetime]] = None,
        applicable: typing.Optional[bool] = None,
        rate: typing.Optional[types.Rate] = None,
        sum_: typing.Optional[int] = None,
        store: typing.Optional[types.Meta] = None,
        project: typing.Optional[types.Meta] = None,
        state: typing.Optional[types.Meta] = None,
        positions: typing.Optional[
            typing.List[internalorders_api.UpdateInternalOrderRequest.UpdatePosition]
        ] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        delivery_planned_moment: typing.Optional[datetime.datetime] = None,
        files: typing.Optional[list] = None,
        moves: typing.Optional[list] = None,
        purchase_orders: typing.Optional[list] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
    ) -> internalorders_api.InternalOrder:
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
            internalorders_api.UpdateInternalOrderRequest(
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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ) -> typing.List[internalorders_api.Position]:
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
            internalorders_api.GetOrderPositionsRequest(
                id_=id_, limit=limit, offset=offset, search=search
            )
        )

    async def add_order_positions(
        self,
        id_: str,
        positions: typing.List[internalorders_api.AddOrderPositionsRequest.AddPosition],
    ) -> typing.List[internalorders_api.Position]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-pozicii-vnutrennego-zakaza

        Add positions to an internal order. (Добавляет позиции внутреннего заказа.)

        :param id_: Internal order ID (ID внутреннего заказа)
        :param positions: Positions (Позиции, которые нужно добавить)
        :return: list(InternalOrder) object (Список объектов InternalOrder)
        """
        return await self(
            internalorders_api.AddOrderPositionsRequest(id_=id_, positions=positions)
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
            internalorders_api.DeleteOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    async def get_order_position(
        self,
        order_id: str,
        position_id: str,
    ) -> internalorders_api.Position:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-poziciu

        Get position by its id from order by order and positions id
        Получить позицию по ее id из заказа по id заказа и позиции
        :param order_id: order id (id заказа)
        :param position_id: position id (id позиции)
        :return: Position object (Объект Position)
        """
        return await self(
            internalorders_api.GetOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    # products_api
    async def get_product_list(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.List[products_api.Product]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-spisok-towarow

        Get a list of products. (Получает список товаров.)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: list(Product) object (Список объектов Product)
        """
        return await self(
            products_api.GetProductListRequest(limit=limit, offset=offset)
        )

    async def create_product(
        self,
        name: str,
        code: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        vat: typing.Optional[int] = None,
        effective_vat: typing.Optional[int] = None,
        discount_prohibited: typing.Optional[bool] = None,
        uom: typing.Optional[types.Meta] = None,
        supplier: typing.Optional[types.Meta] = None,
        min_price: typing.Optional[dict] = None,
        buy_price: typing.Optional[dict] = None,
        sale_prices: typing.Optional[typing.List[dict]] = None,
        barcodes: typing.Optional[typing.List[dict]] = None,
        article: typing.Optional[str] = None,
        weight: typing.Optional[int] = None,
        volume: typing.Optional[int] = None,
        packs: typing.Optional[typing.List[dict]] = None,
        is_serial_trackable: typing.Optional[bool] = None,
        tracking_type: typing.Optional[
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
            ]
        ] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        images: typing.Optional[typing.List[dict]] = None,
        alcoholic: typing.Optional[dict] = None,
        archived: typing.Optional[bool] = None,
        country: typing.Optional[types.Meta] = None,
        files: typing.Optional[typing.List[dict]] = None,
        group: typing.Optional[types.Meta] = None,
        minimum_balance: typing.Optional[int] = None,
        owner: typing.Optional[types.Meta] = None,
        partial_disposal: typing.Optional[bool] = None,
        payment_item_type: typing.Optional[
            typing.Literal[
                "GOODS",
                "EXCISABLE_GOOD",
                "COMPOUND_PAYMENT_ITEM",
                "ANOTHER_PAYMENT_ITEM",
            ]
        ] = None,
        ppe_type: typing.Optional[str] = None,
        product_folder: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        tax_system: typing.Optional[
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ]
        ] = None,
        things: typing.Optional[typing.List[str]] = None,
        tnved: typing.Optional[str] = None,
        use_parent_vat: typing.Optional[bool] = None,
    ) -> products_api.Product:
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
            products_api.CreateProductRequest(
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
        await self(products_api.DeleteProductRequest(id_=id_))

    async def get_product(self, id_: str) -> products_api.Product:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-towar

        :param id_: Product ID (ID Товара)
        :return: Product object (Объект Product)
        """
        return await self(products_api.GetProductRequest(id_=id_))

    async def update_product(
        self,
        id_: str,
        name: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        vat: typing.Optional[int] = None,
        effective_vat: typing.Optional[int] = None,
        discount_prohibited: typing.Optional[bool] = None,
        uom: typing.Optional[types.Meta] = None,
        supplier: typing.Optional[types.Meta] = None,
        min_price: typing.Optional[dict] = None,
        buy_price: typing.Optional[dict] = None,
        sale_prices: typing.Optional[typing.List[dict]] = None,
        barcodes: typing.Optional[typing.List[dict]] = None,
        article: typing.Optional[str] = None,
        weight: typing.Optional[int] = None,
        volume: typing.Optional[int] = None,
        packs: typing.Optional[typing.List[dict]] = None,
        is_serial_trackable: typing.Optional[bool] = None,
        tracking_type: typing.Optional[
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
            ]
        ] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        images: typing.Optional[typing.List[dict]] = None,
        alcoholic: typing.Optional[dict] = None,
        archived: typing.Optional[bool] = None,
        country: typing.Optional[types.Meta] = None,
        files: typing.Optional[typing.List[dict]] = None,
        group: typing.Optional[types.Meta] = None,
        minimum_balance: typing.Optional[int] = None,
        owner: typing.Optional[types.Meta] = None,
        partial_disposal: typing.Optional[bool] = None,
        payment_item_type: typing.Optional[
            typing.Literal[
                "GOODS",
                "EXCISABLE_GOOD",
                "COMPOUND_PAYMENT_ITEM",
                "ANOTHER_PAYMENT_ITEM",
            ]
        ] = None,
        ppe_type: typing.Optional[str] = None,
        product_folder: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        tax_system: typing.Optional[
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ]
        ] = None,
        things: typing.Optional[typing.List[str]] = None,
        tnved: typing.Optional[str] = None,
        use_parent_vat: typing.Optional[bool] = None,
    ) -> products_api.Product:
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
            products_api.UpdateProductRequest(
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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ) -> typing.List[moves_api.Move]:
        """

        :param limit: Limit of moves to get (Лимит передвижений для получения)
        :param offset: Offset of moves to get (Отступ передвижений для получения)
        :param search: Search string (Строка поиска)
        """

        return await self(
            moves_api.GetMovesRequest(
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
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[dict] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        internal_order: typing.Optional[types.Meta] = None,
        customer_order: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        overhead: typing.Optional[dict] = None,
        owner: typing.Optional[types.Meta] = None,
        positions: typing.Optional[types.MetaArray] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[types.Rate] = None,
        shared: typing.Optional[bool] = None,
        state: typing.Optional[types.Meta] = None,
        sync_id: typing.Optional[str] = None,
    ) -> moves_api.Move:
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
            moves_api.CreateMoveRequest(
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
        return await self(moves_api.DeleteMoveRequest(move_id=move_id))

    async def get_move(self, move_id: str) -> moves_api.Move:
        """

        :param move_id: Move id (ID перемещения)
        """
        return await self(moves_api.GetMoveRequest(move_id=move_id))

    async def update_move(
        self,
        move_id: str,
        organization: typing.Optional[types.Meta] = None,
        source_store: typing.Optional[types.Meta] = None,
        target_store: typing.Optional[types.Meta] = None,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[dict] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        internal_order: typing.Optional[types.Meta] = None,
        customer_order: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        overhead: typing.Optional[dict] = None,
        owner: typing.Optional[types.Meta] = None,
        positions: typing.Optional[types.MetaArray] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[types.Rate] = None,
        shared: typing.Optional[bool] = None,
        state: typing.Optional[types.Meta] = None,
        sync_id: typing.Optional[str] = None,
    ) -> moves_api.Move:
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
            moves_api.UpdateMoveRequest(
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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ) -> typing.List[moves_api.MovePosition]:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param limit: Limit (Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.)
        :param offset: Offset (Отступ в выдаваемом списке сущностей.)
        :param search: Search (Фильтр документов по указанной поисковой строке.)
        """

        return await self(
            moves_api.GetMovePositionsRequest(
                move_id=move_id, limit=limit, offset=offset, search=search
            )
        )

    async def create_move_position(
        self,
        move_id: str,
        assortment: types.Meta,
        quantity: int,
        price: typing.Optional[int] = None,
        overhead: typing.Optional[int] = None,
    ) -> moves_api.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """
        return await self(
            moves_api.CreateMovePositionRequest(
                move_id=move_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                overhead=overhead,
            )
        )

    async def get_move_position(
        self, move_id: str, position_id: str
    ) -> moves_api.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции перемещения)
        """
        return await self(
            moves_api.GetMovePositionRequest(move_id=move_id, position_id=position_id)
        )

    async def update_move_position(
        self,
        move_id: str,
        position_id: str,
        assortment: typing.Optional[types.Meta] = None,
        quantity: typing.Optional[int] = None,
        price: typing.Optional[int] = None,
        overhead: typing.Optional[int] = None,
    ) -> moves_api.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """

        return await self(
            moves_api.UpdateMovePositionRequest(
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
            moves_api.DeleteMovePositionRequest(
                move_id=move_id, position_id=position_id
            )
        )

    # purchaseorder
    async def get_purchase_orders(
        self, limit: int = 1000, offset: int = 0, search: str = None
    ) -> typing.List[purchaseorders_api.PurchaseOrder]:
        """
        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке.)
        """
        return await self(
            purchaseorders_api.GetPurchaseOrderListRequest(
                limit=limit, offset=offset, search=search
            )
        )

    async def create_purchase_order(
        self,
        organization: types.Meta,
        agent: types.Meta,
        agent_account: typing.Optional[types.Meta] = None,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        contract: typing.Optional[types.Meta] = None,
        delivery_planned_moment: typing.Optional[datetime.datetime] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        organization_account: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        positions: typing.Optional[
            typing.List[purchaseorders_api.CreatePurchaseOrderRequest.CreatePosition]
        ] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[types.Rate] = None,
        shared: typing.Optional[bool] = None,
        state: typing.Optional[types.Meta] = None,
        store: typing.Optional[types.Meta] = None,
        sync_id: typing.Optional[str] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
        wait_sum: typing.Optional[float] = None,
        customer_orders: typing.Optional[typing.List[types.Meta]] = None,
        invoices_in: typing.Optional[typing.List[types.Meta]] = None,
        payments: typing.Optional[typing.List[types.Meta]] = None,
        supplies: typing.Optional[typing.List[types.Meta]] = None,
        internal_order: typing.Optional[types.Meta] = None,
    ) -> purchaseorders_api.PurchaseOrder:
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
            purchaseorders_api.CreatePurchaseOrderRequest(
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
            purchaseorders_api.DeletePurchaseOrderRequest(order_id=order_id)
        )

    async def get_purchase_order(
        self, order_id: str
    ) -> purchaseorders_api.PurchaseOrder:
        """

        :param order_id: Order id to get (ID Заказа поставщику для получения)
        """
        return await self(purchaseorders_api.GetPurchaseOrderRequest(order_id=order_id))

    async def update_purchase_order(
        self,
        order_id: str,
        organization: typing.Optional[types.Meta] = None,
        agent: typing.Optional[types.Meta] = None,
        agent_account: typing.Optional[types.Meta] = None,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        contract: typing.Optional[types.Meta] = None,
        delivery_planned_moment: typing.Optional[datetime.datetime] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        organization_account: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        positions: typing.Optional[
            typing.List[purchaseorders_api.UpdatePurchaseOrderRequest.UpdatePosition]
        ] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[types.Rate] = None,
        shared: typing.Optional[bool] = None,
        state: typing.Optional[types.Meta] = None,
        store: typing.Optional[types.Meta] = None,
        sync_id: typing.Optional[str] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
        wait_sum: typing.Optional[float] = None,
        customer_orders: typing.Optional[typing.List[types.Meta]] = None,
        invoices_in: typing.Optional[typing.List[types.Meta]] = None,
        payments: typing.Optional[typing.List[types.Meta]] = None,
        supplies: typing.Optional[typing.List[types.Meta]] = None,
        internal_order: typing.Optional[types.Meta] = None,
    ) -> purchaseorders_api.PurchaseOrder:
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
            purchaseorders_api.UpdatePurchaseOrderRequest(
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
    ) -> typing.List[purchaseorders_api.PurchaseOrderPosition]:
        return await self(
            purchaseorders_api.GetPurchaseOrderPositionsRequest(
                order_id=order_id, limit=limit, offset=offset
            )
        )

    async def get_purchase_order_position(
        self, order_id: str, position_id: str
    ) -> purchaseorders_api.PurchaseOrderPosition:
        return await self(
            purchaseorders_api.GetPurchaseOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    async def update_purchase_order_position(
        self,
        order_id: str,
        position_id: str,
        assortment: typing.Optional[types.Meta] = None,
        quantity: typing.Optional[float] = None,
        price: typing.Optional[float] = None,
        vat: typing.Optional[float] = None,
        in_transit: typing.Optional[int] = None,
        discount: typing.Optional[float] = None,
    ) -> purchaseorders_api.PurchaseOrderPosition:
        return await self(
            purchaseorders_api.UpdatePurchaseOrderPositionRequest(
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
            purchaseorders_api.DeletePurchaseOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    # product folders

    async def get_product_folders(
        self, limit: int = 1000, offset: int = 0
    ) -> typing.List[productfolders_api.ProductFolder]:
        """
        Get product folders (Получить папки товаров)
        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        :return: List of product folders (Список папок товаров)
        """
        return await self(
            productfolders_api.GetProductFoldersRequest(limit=limit, offset=offset)
        )

    async def create_product_folder(
        self,
        name: str,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        group: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        product_folder: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        tax_system: typing.Optional[
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ]
        ] = None,
        use_parent_vat: typing.Optional[bool] = None,
        vat: typing.Optional[int] = None,
        vat_enabled: typing.Optional[bool] = None,
    ) -> productfolders_api.ProductFolder:
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
            productfolders_api.CreateProductFolderRequest(
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
            productfolders_api.DeleteProductFolderRequest(folder_id=folder_id)
        )

    async def get_product_folder(
        self,
        folder_id: str,
    ) -> productfolders_api.ProductFolder:
        """
        Get product folder by id (Получить папку товаров по ID)
        :param folder_id: Product folder id (ID папки товаров)
        :return: Product folder (Папка товаров)
        """
        return await self(
            productfolders_api.GetProductFolderRequest(folder_id=folder_id)
        )

    async def update_product_folder(
        self,
        folder_id: str,
        name: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        group: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        product_folder: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        tax_system: typing.Optional[
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ]
        ] = None,
        use_parent_vat: typing.Optional[bool] = None,
        vat: typing.Optional[int] = None,
        vat_enabled: typing.Optional[bool] = None,
    ) -> productfolders_api.ProductFolder:
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
            productfolders_api.UpdateProductFolderRequest(
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
        limit: typing.Optional[int] = 1000,
        offset: typing.Optional[int] = 0,
        search: typing.Optional[str] = None,
    ) -> typing.List[enters_api.Enter]:
        """

        :param limit: Limit of entities to extract. (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке)
        :return: List of enters (Список приходов)
        """

        return await self(
            enters_api.GetEntersRequest(limit=limit, offset=offset, search=search)
        )

    async def create_enter(
        self,
        organization: types.Meta,
        store: types.Meta,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[list] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        overhead: typing.Optional[dict] = None,
        positions: typing.Optional[
            typing.List[enters_api.CreateEnterRequest.CreateEnterPosition]
        ] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[dict] = None,
        shared: typing.Optional[bool] = None,
    ) -> enters_api.Enter:

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
            enters_api.CreateEnterRequest(
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
        return await self(enters_api.DeleteEnterRequest(enter_id=enter_id))

    async def get_enter(self, enter_id: str) -> enters_api.Enter:
        """

        :param enter_id: ID of enter (ID оприходования)
        :return: Enter (Оприходование)
        """
        return await self(enters_api.GetEnterRequest(enter_id=enter_id))

    async def update_enter(
        self,
        enter_id: str,
        organization: typing.Optional[str] = None,
        store: typing.Optional[str] = None,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[dict] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[dict] = None,
        group: typing.Optional[str] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        overhead: typing.Optional[dict] = None,
        positions: typing.Optional[
            typing.List[enters_api.UpdateEnterRequest.UpdateEnterPosition]
        ] = None,
        project: typing.Optional[str] = None,
        rate: typing.Optional[str] = None,
        shared: typing.Optional[bool] = None,
    ) -> enters_api.Enter:
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
            enters_api.UpdateEnterRequest(
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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.List[enters_api.EnterPosition]:
        """

        :param enter_id: ID of enter (ID оприходования)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: Enter positions (Позиции оприходования)
        """
        return await self(
            enters_api.GetEnterPositionsRequest(
                enter_id=enter_id,
                limit=limit,
                offset=offset,
            )
        )

    async def create_enter_position(
        self,
        enter_id: str,
        positions: typing.List[
            enters_api.CreateEnterPositionRequest.CreateEnterPosition
        ],
    ) -> typing.List[enters_api.EnterPosition]:
        """

        :param enter_id: Enter id (id Оприходования)
        :param positions: Positions (Позиции)
        :return: Created enter positions (Созданные позиции оприходования)
        """
        return await self(
            enters_api.CreateEnterPositionRequest(
                enter_id=enter_id,
                positions=positions,
            )
        )

    async def get_enter_position(
        self,
        enter_id: str,
        position_id: str,
    ) -> enters_api.EnterPosition:
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id Позиции)
        :return: Enter position (Позиция оприходования)
        """
        return await self(
            enters_api.GetEnterPositionRequest(
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
        quantity: int,
        country: typing.Optional[types.Meta] = None,
        gtd: typing.Optional[typing.Dict] = None,
        pack: typing.Optional[typing.Dict] = None,
        reason: typing.Optional[str] = None,
        slot: typing.Optional[types.Meta] = None,
        things: typing.Optional[typing.Dict] = None,
        overhead: typing.Optional[int] = None,
    ) -> enters_api.EnterPosition:
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
            enters_api.UpdateEnterPositionRequest(
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
            enters_api.DeleteEnterPositionRequest(
                enter_id=enter_id,
                position_id=position_id,
            )
        )

    # stocks
    async def get_full_stock_report(
        self,
        limit: typing.Optional[int] = 1000,
        offset: typing.Optional[int] = 0,
        group_by: typing.Optional[
            typing.Literal["product", "variant", "consignment"]
        ] = None,
        include_related: typing.Optional[bool] = None,
    ) -> typing.List[stocks.FullStockReport]:
        """

        :param limit: Limit the number of entities to retrieve. (Ограничить количество сущностей для извлечения.)
        :param offset: Offset in the returned list of entities. (Отступ в выдаваемом списке сущностей.)
        :param group_by: Type to group by. (Тип, по которому нужно сгруппировать выдачу.)
        :param include_related: Include consignments for products and variants. (Вывод остатков по модификациям и сериям товаров.)
        :return: List of full stock reports (Список отчетов по остаткам)
        """
        return await self(
            stocks.GetFullStockReportRequest(
                limit=limit,
                offset=offset,
                group_by=group_by,
                include_related=include_related,
            )
        )

    async def get_small_stock_current_report(
        self,
        include: typing.Optional[str] = None,
        changed_since: typing.Optional[datetime.datetime] = None,
        stock_type: typing.Optional[
            typing.Literal["stock", "freeStock", "quantity"]
        ] = None,
        filter_assortment_id: typing.Optional[typing.List[str]] = None,
        filter_store_id: typing.Optional[typing.List[str]] = None,
    ) -> typing.List[stocks.SmallStockReport]:
        """

        :param include: Include related entities (Включить связанные сущности)
        :param changed_since: Changed since (Изменено с)
        :param stock_type: Stock type (Тип остатка)
        :param filter_assortment_id: Filter by assortment id (Фильтр по id товара)
        :param filter_store_id: Filter by store id (Фильтр по id склада)
        :return: List of small stock reports (Список отчетов по остаткам)
        """

        return await self(
            stocks.GetSmallStockReportCurrentRequest(
                include=include,
                changed_since=changed_since,
                stock_type=stock_type,
                filter_assortment_id=filter_assortment_id,
                filter_store_id=filter_store_id,
            )
        )

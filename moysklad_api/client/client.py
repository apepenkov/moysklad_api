import typing
import base64
import aiohttp
import datetime
from ..errors import MoySkladError
from .. import types

from ..api.entities import internalorders, products, moves, purchaseorders
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
                    kwargs["data"] = json.dumps(kwargs.pop("json", {}), indent=4)
                else:
                    kwargs["data"] = json.dumps(
                        kwargs.pop("json", {}), separators=(",", ":")
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
    ) -> typing.List[internalorders.InternalOrder]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennie-zakazy

        Get a list of internal orders. (Получает список внутренних заказов.)
        :param limit: Limit the number of results (Ограничить количество результатов)
        :param offset:  Offset the results (Сместить результаты)
        :param search:  Search query (Поисковый запрос)
        :return: List of InternalOrder objects (Список объектов InternalOrder)
        """
        return await self(
            internalorders.GetInternalOrdersRequest(
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
            typing.List[internalorders.CreateInternalOrderRequest.CreatePosition]
        ] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
    ) -> internalorders.InternalOrder:
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
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(
            internalorders.CreateInternalOrderRequest(
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
            )
        )

    async def get_internal_order(self, id_: str) -> internalorders.InternalOrder:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennij-zakaz

        Get an internal order. (Получает внутренний заказ.)
        :param id_: Internal order ID (ID внутреннего заказа)
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(internalorders.GetInternalOrderRequest(id_=id_))

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
            typing.List[internalorders.UpdateInternalOrderRequest.UpdatePosition]
        ] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
    ) -> internalorders.InternalOrder:
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
        :return: InternalOrder object (Объект InternalOrder)
        """
        return await self(
            internalorders.UpdateInternalOrderRequest(
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
            )
        )

    async def get_order_positions(
        self,
        id_: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ) -> typing.List[internalorders.Position]:
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
            internalorders.GetOrderPositionsRequest(
                id_=id_, limit=limit, offset=offset, search=search
            )
        )

    async def add_order_positions(
        self,
        id_: str,
        positions: typing.List[internalorders.AddOrderPositionsRequest.AddPosition],
    ) -> typing.List[internalorders.Position]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-pozicii-vnutrennego-zakaza

        Add positions to an internal order. (Добавляет позиции внутреннего заказа.)

        :param id_: Internal order ID (ID внутреннего заказа)
        :param positions: Positions (Позиции, которые нужно добавить)
        :return: list(InternalOrder) object (Список объектов InternalOrder)
        """
        return await self(
            internalorders.AddOrderPositionsRequest(id_=id_, positions=positions)
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
            internalorders.DeleteOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    async def get_order_position(
        self,
        order_id: str,
        position_id: str,
    ) -> internalorders.Position:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-poziciu

        Get position by its id from order by order and positions id
        Получить позицию по ее id из заказа по id заказа и позиции
        :param order_id: order id (id заказа)
        :param position_id: position id (id позиции)
        :return: Position object (Объект Position)
        """
        return await self(
            internalorders.GetOrderPositionRequest(
                order_id=order_id, position_id=position_id
            )
        )

    # products
    async def get_product_list(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> typing.List[products.Product]:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-spisok-towarow

        Get a list of products. (Получает список товаров.)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :return: list(Product) object (Список объектов Product)
        """
        return await self(products.GetProductListRequest(limit=limit, offset=offset))

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
    ) -> products.Product:
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
        :return: Product object (Объект Product)
        """
        return await self(
            products.CreateProductRequest(
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
            )
        )

    async def delete_product(self, id_: str) -> None:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-udalit-towar

        :param id_: Product ID (ID Товара)
        :return: None
        """
        await self(products.DeleteProductRequest(id_=id_))

    async def get_product(self, id_: str) -> products.Product:
        """
        https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-towar

        :param id_: Product ID (ID Товара)
        :return: Product object (Объект Product)
        """
        return await self(products.GetProductRequest(id_=id_))

    async def update_product(
        self,
        id_: str,
        name: typing.Optional[str],
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
    ) -> products.Product:
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
        :return: Product object (Объект Product)
        """

        return await self(
            products.UpdateProductRequest(
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
            )
        )

    async def get_moves(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ) -> typing.List[moves.Move]:
        """

        :param limit: Limit of moves to get (Лимит передвижений для получения)
        :param offset: Offset of moves to get (Отступ передвижений для получения)
        :param search: Search string (Строка поиска)
        """

        return await self(
            moves.GetMovesRequest(
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
    ) -> moves.Move:
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
            moves.CreateMoveRequest(
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
        return await self(moves.DeleteMoveRequest(move_id=move_id))

    async def get_move(self, move_id: str) -> moves.Move:
        """

        :param move_id: Move id (ID перемещения)
        """
        return await self(moves.GetMoveRequest(move_id=move_id))

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
    ) -> moves.Move:
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
            moves.UpdateMoveRequest(
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
    ) -> typing.List[moves.MovePosition]:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param limit: Limit (Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.)
        :param offset: Offset (Отступ в выдаваемом списке сущностей.)
        :param search: Search (Фильтр документов по указанной поисковой строке.)
        """

        return await self(
            moves.GetMovePositionsRequest(
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
    ) -> moves.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """
        return await self(
            moves.CreateMovePositionRequest(
                move_id=move_id,
                assortment=assortment,
                quantity=quantity,
                price=price,
                overhead=overhead,
            )
        )

    async def get_move_position(
        self, move_id: str, position_id: str
    ) -> moves.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции перемещения)
        """
        return await self(
            moves.GetMovePositionRequest(move_id=move_id, position_id=position_id)
        )

    async def update_move_position(
        self,
        move_id: str,
        position_id: str,
        assortment: typing.Optional[types.Meta] = None,
        quantity: typing.Optional[int] = None,
        price: typing.Optional[int] = None,
        overhead: typing.Optional[int] = None,
    ) -> moves.MovePosition:
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """

        return await self(
            moves.UpdateMovePositionRequest(
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
            moves.DeleteMovePositionRequest(move_id=move_id, position_id=position_id)
        )

    # purchaseorder
    async def get_purchase_orders(
        self, limit: int = 1000, offset: int = 0, search: str = None
    ) -> typing.List[purchaseorders.PurchaseOrder]:
        """
        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке.)
        """
        return await self(
            purchaseorders.GetPurchaseOrderListRequest(
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
            typing.List[purchaseorders.CreatePurchaseOrderRequest.CreatePosition]
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
    ) -> purchaseorders.PurchaseOrder:
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
            purchaseorders.CreatePurchaseOrderRequest(
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
        return await self(purchaseorders.DeletePurchaseOrderRequest(order_id=order_id))

    async def get_purchase_order(self, order_id: str) -> purchaseorders.PurchaseOrder:
        """

        :param order_id: Order id to get (ID Заказа поставщику для получения)
        """
        return await self(purchaseorders.GetPurchaseOrderRequest(order_id=order_id))

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
            typing.List[purchaseorders.UpdatePurchaseOrderRequest.UpdatePosition]
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
    ) -> purchaseorders.PurchaseOrder:
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
            purchaseorders.UpdatePurchaseOrderRequest(
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
    ) -> typing.List[purchaseorders.PurchaseOrderPosition]:
        return await self(
            purchaseorders.GetPurchaseOrderPositionsRequest(
                order_id=order_id, limit=limit, offset=offset
            )
        )


async def get_purchase_order_position(
    self, order_id: str, position_id: str
) -> purchaseorders.PurchaseOrderPosition:
    return await self(
        purchaseorders.GetPurchaseOrderPositionRequest(
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
) -> purchaseorders.PurchaseOrderPosition:
    return await self(
        purchaseorders.UpdatePurchaseOrderPositionRequest(
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


async def delete_purchase_order_position(self, order_id: str, position_id: str) -> None:
    return await self(
        purchaseorders.DeletePurchaseOrderPositionRequest(
            order_id=order_id, position_id=position_id
        )
    )

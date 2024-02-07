import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


# https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary


class Product(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary

    accountId 	            UUID 		        ID учетной записи    Обязательное при ответе Только для чтения
    alcoholic            	Object 		        Объект, содержащий поля алкогольной продукции. Подробнее тут
    archived            	Boolean 	        Добавлен ли Товар в архив     Обязательное при ответе
    article 	            String(255) 	    Артикул
    attributes          	Array(Object) 	    Операторы доп. полей 	Коллекция доп. полей
    barcodes            	Array(Object) 	    Штрихкоды Комплекта. Подробнее тут
    buyPrice            	Object 		        Закупочная цена. Подробнее тут
    code 	                String(255) 	    Код Товара
    country             	Meta 		        Метаданные Страны
    description 	        String(4096)    	Описание Товара
    discountProhibited  	Boolean 	    	Признак запрета скидок     Обязательное при ответе
    effectiveVat 	        Int 	        	Реальный НДС %     Только для чтения
    effectiveVatEnabled 	Boolean 	    	Дополнительный признак для определения разграничения реального НДС = 0 или "без НДС". (effectiveVat = 0, effectiveVatEnabled = false) -> "без НДС", (effectiveVat = 0, effectiveVatEnabled = true) -> 0%.     Только для чтения
    externalCode 	        String(255) 		Внешний код Товара     Обязательное при ответе
    files 	                MetaArray   		Метаданные массива Файлов (Максимальное количество файлов - 100)
    group 	                Meta            	Метаданные отдела сотрудника  Обязательное при ответе Expand
    id 	                    UUID            	ID Товара Обязательное при ответе Только для чтения
    images 	                MetaArray   		Массив метаданных Изображений (Максимальное количество изображений - 10)     Expand
    isSerialTrackable 	    Boolean         	Учет по серийным номерам. Данная отметка не сочетается с признаками weighed, alcoholic, ppeType, trackingType, onTap.
    meta 	                Meta 	        	Метаданные Товара     Обязательное при ответе
    minPrice 	            Object 	        	Минимальная цена. Подробнее тут
    minimumBalance      	Int 	            Неснижаемый остаток
    name 	                String(255)     	Наименование Товара Обязательное при ответе Необходимо при создании
    owner 	                Meta 	            Метаданные владельца (Сотрудника)
    packs               	Array(Object) 		Упаковки Товара. Подробнее тут
    partialDisposal 	    Boolean 		    Управление состоянием частичного выбытия маркированного товара. «true» - возможность включена.
    pathName 	            String 	            Наименование группы, в которую входит Товар     Обязательное при ответе Только для чтения
    paymentItemType 	    Enum 		        Признак предмета расчета. Подробнее тут
    ppeType 	            Enum 		        Код вида номенклатурной классификации медицинских средств индивидуальной защиты (EAN-13). Подробнее тут
    productFolder 	        Meta 		        Метаданные группы Товара
    salePrices 	            Array(Object) 		Цены продажи. Подробнее тут     shared 	Boolean 	Общий доступ     Обязательное при ответе
    supplier            	Meta 	            Метаданные контрагента-поставщика
    syncId              	UUID 	            ID синхронизации     Только для чтения Заполнение при создании
    taxSystem 	            Enum 		        Код системы налогообложения. Подробнее тут
    things 	                Array(String) 		Серийные номера
    tnved 	                String(255) 		Код ТН ВЭД
    trackingType 	        Enum 		        Тип маркируемой продукции. Подробнее тут
    uom 	                Meta 	        	Единицы измерения
    updated 	            DateTime        	Момент последнего обновления сущности     Обязательное при ответе Только для чтения
    useParentVat 	        Boolean 	    	Используется ли ставка НДС родительской группы. Если true для единицы ассортимента будет применена ставка, установленная для родительской группы.     Обязательное при ответе
    variantsCount 	        Int 		        Количество модификаций у данного товара     Обязательное при ответе Только для чтения
    vat 	                Int 		        НДС %
    vatEnabled          	Boolean 		    Включен ли НДС для товара. С помощью этого флага для товара можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%.
    volume 	                Int 	            Объем
    weight 	                Int 	            Вес
    """

    account_id: str
    alcoholic: dict
    archived: bool
    article: str
    attributes: list
    barcodes: list
    buy_price: dict
    code: str
    country: types.Meta
    description: str
    discount_prohibited: bool
    effective_vat: int
    effective_vat_enabled: bool
    external_code: str
    files: types.MetaArray
    group: types.Meta
    id: str
    images: types.MetaArray
    is_serial_trackable: bool
    meta: types.Meta
    min_price: dict
    minimum_balance: int
    name: str
    owner: types.Meta
    packs: list
    partial_disposal: bool
    path_name: str
    payment_item_type: str
    ppe_type: str
    product_folder: types.Meta
    sale_prices: list
    supplier: types.Meta
    sync_id: str
    tax_system: str
    things: typing.List[str]
    tnved: str
    tracking_type: str
    uom: types.Meta
    updated: datetime.datetime
    use_parent_vat: bool
    variants_count: int
    vat: int
    vat_enabled: bool
    volume: int
    weight: int

    @classmethod
    def from_json(cls, dict_data: dict) -> "Product":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.alcoholic = dict_data.get("alcoholic")
        instance.archived = dict_data.get("archived")
        instance.article = dict_data.get("article")
        instance.attributes = dict_data.get("attributes")
        instance.barcodes = dict_data.get("barcodes")
        instance.buy_price = dict_data.get("buyPrice")
        instance.code = dict_data.get("code")
        instance.country = helpers.get_meta(dict_data.get("country"))
        instance.description = dict_data.get("description")
        instance.discount_prohibited = dict_data.get("discountProhibited")
        instance.effective_vat = dict_data.get("effectiveVat")
        instance.effective_vat_enabled = dict_data.get("effectiveVatEnabled")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.images = dict_data.get("images")
        instance.is_serial_trackable = dict_data.get("isSerialTrackable")
        instance.meta = dict_data.get("meta")
        instance.min_price = dict_data.get("minPrice")
        instance.minimum_balance = dict_data.get("minimumBalance")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.packs = dict_data.get("packs")
        instance.partial_disposal = dict_data.get("partialDisposal")
        instance.path_name = dict_data.get("pathName")
        instance.payment_item_type = dict_data.get("paymentItemType")
        instance.ppe_type = dict_data.get("ppeType")
        instance.product_folder = helpers.get_meta(dict_data.get("productFolder"))
        instance.sale_prices = dict_data.get("salePrices")
        instance.supplier = helpers.get_meta(dict_data.get("supplier"))
        instance.sync_id = dict_data.get("syncId")
        instance.tax_system = dict_data.get("taxSystem")
        instance.things = dict_data.get("things")
        instance.tnved = dict_data.get("tnved")
        instance.tracking_type = dict_data.get("trackingType")
        instance.uom = helpers.get_meta(dict_data.get("uom"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.use_parent_vat = dict_data.get("useParentVat")
        instance.variants_count = dict_data.get("variantsCount")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.volume = dict_data.get("volume")
        instance.weight = dict_data.get("weight")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return ("product",)


class GetProductListRequest(types.ApiRequest):
    """https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-spisok-towarow
    Request to get all products of account
    Запрос на получение всех Товаров для данной учетной записи.
    """

    def __init__(self, limit=0, offset=1000):
        """

        :param limit: int, default 0 - start from first element (номер первого элемента в выдаче)
        :param offset: int, default 1000 - count of elements in response (количество элементов в выдаче)
        """
        self.limit = limit
        self.offset = offset

    def to_request(
        self,
    ) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset

        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/product",
            params=params,
        )

    def from_response(self, response: dict) -> typing.List[Product]:
        return [Product.from_json(product) for product in response["rows"]]


class CreateProductRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-sozdat-towar

    Request to create product (Создание товара)
    """

    def __init__(
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
    ):
        """

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
        """
        self.name = name
        self.code = code
        self.external_code = external_code
        self.description = description
        self.vat = vat
        self.effective_vat = effective_vat
        self.discount_prohibited = discount_prohibited
        self.uom = uom
        self.supplier = supplier
        self.min_price = min_price
        self.buy_price = buy_price
        self.sale_prices = sale_prices
        self.barcodes = barcodes
        self.article = article
        self.weight = weight
        self.volume = volume
        self.packs = packs
        self.is_serial_trackable = is_serial_trackable
        self.tracking_type = tracking_type
        self.attributes = attributes
        self.images = images
        self.alcoholic = alcoholic
        self.archived = archived
        self.country = country
        self.files = files
        self.group = group
        self.minimum_balance = minimum_balance
        self.owner = owner
        self.partial_disposal = partial_disposal
        self.payment_item_type = payment_item_type
        self.ppe_type = ppe_type
        self.product_folder = product_folder
        self.shared = shared
        self.tax_system = tax_system
        self.things = things
        self.tnved = tnved
        self.use_parent_vat = use_parent_vat

    def to_request(self) -> RequestData:
        if not self.name:
            raise ValueError("Name is required")
        json_data = {"name": self.name}
        if self.code != Unset:
            json_data["code"] = self.code
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.effective_vat != Unset:
            json_data["effectiveVat"] = self.effective_vat
        if self.discount_prohibited != Unset:
            json_data["discountProhibited"] = self.discount_prohibited
        if self.uom != Unset:
            json_data["uom"] = {"meta": self.uom} if self.uom is not None else None
        if self.supplier != Unset:
            json_data["supplier"] = (
                {"meta": self.supplier} if self.supplier is not None else None
            )
        if self.min_price != Unset:
            json_data["minPrice"] = self.min_price
        if self.buy_price != Unset:
            json_data["buyPrice"] = self.buy_price
        if self.sale_prices != Unset:
            json_data["salePrices"] = self.sale_prices
        if self.barcodes != Unset:
            json_data["barcodes"] = self.barcodes
        if self.article != Unset:
            json_data["article"] = self.article
        if self.weight != Unset:
            json_data["weight"] = self.weight
        if self.volume != Unset:
            json_data["volume"] = self.volume
        if self.packs != Unset:
            json_data["packs"] = self.packs
        if self.is_serial_trackable != Unset:
            json_data["isSerialTrackable"] = self.is_serial_trackable
        if self.tracking_type != Unset:
            if self.tracking_type not in [
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
            ]:
                raise ValueError("Tracking type is not valid")
            json_data["trackingType"] = self.tracking_type
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.images != Unset:
            json_data["images"] = self.images
        if self.alcoholic != Unset:
            json_data["alcoholic"] = self.alcoholic
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.country != Unset:
            json_data["country"] = (
                {"meta": self.country} if self.country is not None else None
            )
        if self.files != Unset:
            json_data["files"] = self.files
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group} if self.group is not None else None
            )
        if self.minimum_balance != Unset:
            json_data["minimumBalance"] = self.minimum_balance
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.partial_disposal != Unset:
            json_data["partialDisposal"] = self.partial_disposal
        if self.payment_item_type != Unset:
            json_data["paymentItemType"] = self.payment_item_type
        if self.ppe_type != Unset:
            json_data["ppeType"] = self.ppe_type
        if self.product_folder != Unset:
            json_data["productFolder"] = (
                {"meta": self.product_folder}
                if self.product_folder is not None
                else None
            )
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.tax_system != Unset:
            json_data["taxSystem"] = self.tax_system
        if self.things != Unset:
            json_data["things"] = self.things
        if self.tnved != Unset:
            json_data["tnved"] = self.tnved
        if self.use_parent_vat != Unset:
            json_data["useParentVat"] = self.use_parent_vat

        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/product",
            json=json_data,
        )

    def from_response(self, response: dict) -> Product:
        return Product.from_json(response)


class DeleteProductRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-udalit-towar

    Request to delete product (Удаление товара)
    """

    def __init__(self, id_: str):
        """

        :param id_: Product ID (ID Товара)
        """
        self.id = id_

    def to_request(self) -> RequestData:
        if not self.id:
            raise ValueError("Product ID is required")
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/product/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, response: dict) -> None:
        return None


class GetProductRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-poluchit-towar

    Request to get product (Получение товара)
    """

    def __init__(self, id_: str):
        """

        :param id_: Product ID (ID Товара)
        """
        self.id = id_

    def to_request(self) -> RequestData:
        if not self.id:
            raise ValueError("Product ID is required")
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/product/{self.id}",
        )

    def from_response(self, response: dict) -> Product:
        return Product.from_json(response)


class UpdateProductRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-obnovit-towar

    Request to update product (Обновление товара)
    """

    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        effective_vat: typing.Union[Unset, int] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        uom: typing.Union[Unset, dict] = Unset,
        supplier: typing.Union[Unset, dict] = Unset,
        min_price: typing.Union[Unset, int] = Unset,
        buy_price: typing.Union[Unset, int] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[str]] = Unset,
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
    ):
        """

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
        """
        self.id = id_
        self.name = name
        self.code = code
        self.external_code = external_code
        self.description = description
        self.vat = vat
        self.effective_vat = effective_vat
        self.discount_prohibited = discount_prohibited
        self.uom = uom
        self.supplier = supplier
        self.min_price = min_price
        self.buy_price = buy_price
        self.sale_prices = sale_prices
        self.barcodes = barcodes
        self.article = article
        self.weight = weight
        self.volume = volume
        self.packs = packs
        self.is_serial_trackable = is_serial_trackable
        self.tracking_type = tracking_type
        self.attributes = attributes
        self.images = images
        self.alcoholic = alcoholic
        self.archived = archived
        self.country = country
        self.files = files
        self.group = group
        self.minimum_balance = minimum_balance
        self.owner = owner
        self.partial_disposal = partial_disposal
        self.payment_item_type = payment_item_type
        self.ppe_type = ppe_type
        self.product_folder = product_folder
        self.shared = shared
        self.tax_system = tax_system
        self.things = things
        self.tnved = tnved
        self.use_parent_vat = use_parent_vat

    def to_request(self) -> RequestData:
        if not self.id:
            raise ValueError("Product ID is required")

        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.code != Unset:
            json_data["code"] = self.code
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.effective_vat != Unset:
            json_data["effectiveVat"] = self.effective_vat
        if self.discount_prohibited != Unset:
            json_data["discountProhibited"] = self.discount_prohibited
        if self.uom != Unset:
            json_data["uom"] = self.uom
        if self.supplier != Unset:
            json_data["supplier"] = self.supplier
        if self.min_price != Unset:
            json_data["minPrice"] = self.min_price
        if self.buy_price != Unset:
            json_data["buyPrice"] = self.buy_price
        if self.sale_prices != Unset:
            json_data["salePrices"] = self.sale_prices
        if self.barcodes != Unset:
            json_data["barcodes"] = self.barcodes
        if self.article != Unset:
            json_data["article"] = self.article
        if self.weight != Unset:
            json_data["weight"] = self.weight
        if self.volume != Unset:
            json_data["volume"] = self.volume
        if self.packs != Unset:
            json_data["packs"] = self.packs
        if self.is_serial_trackable != Unset:
            json_data["isSerialTrackable"] = self.is_serial_trackable
        if self.tracking_type != Unset:
            if self.tracking_type not in [
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
            ]:
                raise ValueError("Tracking type is not valid")
            json_data["trackingType"] = self.tracking_type
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.images != Unset:
            json_data["images"] = self.images
        if self.alcoholic != Unset:
            json_data["alcoholic"] = self.alcoholic
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.country != Unset:
            json_data["country"] = (
                {"meta": self.country} if self.country is not None else None
            )
        if self.files != Unset:
            json_data["files"] = self.files
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group} if self.group is not None else None
            )
        if self.minimum_balance != Unset:
            json_data["minimumBalance"] = self.minimum_balance
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.partial_disposal != Unset:
            json_data["partialDisposal"] = self.partial_disposal
        if self.payment_item_type != Unset:
            json_data["paymentItemType"] = self.payment_item_type
        if self.ppe_type != Unset:
            json_data["ppeType"] = self.ppe_type
        if self.product_folder != Unset:
            json_data["productFolder"] = (
                {"meta": self.product_folder}
                if self.product_folder is not None
                else None
            )
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.tax_system != Unset:
            json_data["taxSystem"] = self.tax_system
        if self.things != Unset:
            json_data["things"] = self.things
        if self.tnved != Unset:
            json_data["tnved"] = self.tnved
        if self.use_parent_vat != Unset:
            json_data["useParentVat"] = self.use_parent_vat
        # actually it would be good to place a check for len(json_data) > 1, to avoid extra requests,
        # but I don't think that should be done on library level
        # Здесь было бы хорошо проверить, что длина json_data > 1, чтобы избежать лишних запросов,
        # но я не думаю, что это должно делаться на уровне библиотеки
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/product/{self.id}",
            json=json_data,
        )

    def from_response(self, response: dict) -> Product:
        return Product.from_json(response)

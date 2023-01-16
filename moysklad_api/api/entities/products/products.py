import datetime
import typing

from .... import types


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

    def __init__(self):
        # TODO: set optional where required
        self.account_id: str = None
        self.alcoholic: dict = None
        self.archived: bool = None
        self.article: str = None
        self.attributes: list = None
        self.barcodes: list = None
        self.buy_price: int = None
        self.code: str = None
        self.country: types.Meta = None
        self.description: str = None
        self.discount_prohibited: bool = None
        self.effective_vat: int = None
        self.effective_vat_enabled: bool = None
        self.external_code: str = None
        self.files: types.MetaArray = None
        self.group: types.Meta = None
        self.id: str = None
        self.images: types.MetaArray = None
        self.is_serial_trackable: bool = None
        self.meta: types.Meta = None
        self.min_price: dict = None
        self.minimum_balance: int = None
        self.name: str = None
        self.owner: types.Meta = None
        self.packs: list = None
        self.partial_disposal: bool = None
        self.path_name: str = None
        self.payment_item_type: str = None
        self.ppe_type: str = None
        self.product_folder: types.Meta = None
        self.sale_prices: list = None
        self.supplier: types.Meta = None
        self.sync_id: str = None
        self.tax_system: str = None
        self.things: typing.List[str] = None
        self.tnved: str = None
        self.tracking_type: str = None
        self.uom: types.Meta = None
        self.updated: datetime.datetime = None
        self.use_parent_vat: bool = None
        self.variants_count: int = None
        self.vat: int = None
        self.vat_enabled: bool = None
        self.volume: int = None
        self.weight: int = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Product":
        result = cls()
        result.account_id = dict_data.get("accountId")
        result.alcoholic = dict_data.get("alcoholic")
        result.archived = dict_data.get("archived")
        result.article = dict_data.get("article")
        result.attributes = dict_data.get("attributes")
        result.barcodes = dict_data.get("barcodes")
        result.buy_price = dict_data.get("buyPrice")
        result.code = dict_data.get("code")
        result.country = dict_data.get("country")
        result.description = dict_data.get("description")
        result.discount_prohibited = dict_data.get("discountProhibited")
        result.effective_vat = dict_data.get("effectiveVat")
        result.effective_vat_enabled = dict_data.get("effectiveVatEnabled")
        result.external_code = dict_data.get("externalCode")
        result.files = dict_data.get("files")
        result.group = dict_data.get("group")
        result.id = dict_data.get("id")
        result.images = dict_data.get("images")
        result.is_serial_trackable = dict_data.get("isSerialTrackable")
        result.meta = dict_data.get("meta")
        result.min_price = dict_data.get("minPrice")
        result.minimum_balance = dict_data.get("minimumBalance")
        result.name = dict_data.get("name")
        result.owner = dict_data.get("owner")
        result.packs = dict_data.get("packs")
        result.partial_disposal = dict_data.get("partialDisposal")
        result.path_name = dict_data.get("pathName")
        result.payment_item_type = dict_data.get("paymentItemType")
        result.ppe_type = dict_data.get("ppeType")
        result.product_folder = dict_data.get("productFolder")
        result.sale_prices = dict_data.get("salePrices")
        result.supplier = dict_data.get("supplier")
        result.sync_id = dict_data.get("syncId")
        result.tax_system = dict_data.get("taxSystem")
        result.things = dict_data.get("things")
        result.tnved = dict_data.get("tnved")
        result.tracking_type = dict_data.get("trackingType")
        result.uom = dict_data.get("uom")
        updated = dict_data.get("updated")
        if updated:
            result.updated = datetime.datetime.fromisoformat(updated)
        result.use_parent_vat = dict_data.get("useParentVat")
        result.variants_count = dict_data.get("variantsCount")
        result.vat = dict_data.get("vat")
        result.vat_enabled = dict_data.get("vatEnabled")
        result.volume = dict_data.get("volume")
        result.weight = dict_data.get("weight")
        return result


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
    ) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset

        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/product",
            "params": params,
        }

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

    def to_request(self) -> dict:
        if not self.name:
            raise ValueError("Name is required")
        json_data = {"name": self.name}
        if self.code is not None:
            json_data["code"] = self.code
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.description is not None:
            json_data["description"] = self.description
        if self.vat is not None:
            json_data["vat"] = self.vat
        if self.effective_vat is not None:
            json_data["effectiveVat"] = self.effective_vat
        if self.discount_prohibited is not None:
            json_data["discountProhibited"] = self.discount_prohibited
        if self.uom is not None:
            json_data["uom"] = {"meta": self.uom}
        if self.supplier is not None:
            json_data["supplier"] = {"meta": self.supplier}
        if self.min_price is not None:
            json_data["minPrice"] = self.min_price
        if self.buy_price is not None:
            json_data["buyPrice"] = self.buy_price
        if self.sale_prices is not None:
            json_data["salePrices"] = self.sale_prices
        if self.barcodes is not None:
            json_data["barcodes"] = self.barcodes
        if self.article is not None:
            json_data["article"] = self.article
        if self.weight is not None:
            json_data["weight"] = self.weight
        if self.volume is not None:
            json_data["volume"] = self.volume
        if self.packs is not None:
            json_data["packs"] = self.packs
        if self.is_serial_trackable is not None:
            json_data["isSerialTrackable"] = self.is_serial_trackable
        if self.tracking_type is not None:
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
        if self.attributes is not None:
            json_data["attributes"] = self.attributes
        if self.images is not None:
            json_data["images"] = self.images

        return {
            "method": "POST",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/product",
            "json": json_data,
        }

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

    def to_request(self) -> dict:
        if not self.id:
            raise ValueError("Product ID is required")
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/product/{self.id}",
            "allow_non_json": True,
        }

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

    def to_request(self) -> dict:
        if not self.id:
            raise ValueError("Product ID is required")
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/product/{self.id}",
        }

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
        name: typing.Optional[str],
        code: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        vat: typing.Optional[int] = None,
        effective_vat: typing.Optional[int] = None,
        discount_prohibited: typing.Optional[bool] = None,
        uom: typing.Optional[dict] = None,
        supplier: typing.Optional[dict] = None,
        min_price: typing.Optional[int] = None,
        buy_price: typing.Optional[int] = None,
        sale_prices: typing.Optional[typing.List[dict]] = None,
        barcodes: typing.Optional[typing.List[str]] = None,
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

    def to_request(self) -> dict:
        if not self.id:
            raise ValueError("Product ID is required")

        json_data = {}
        if self.name is not None:
            json_data["name"] = self.name
        if self.code is not None:
            json_data["code"] = self.code
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.description is not None:
            json_data["description"] = self.description
        if self.vat is not None:
            json_data["vat"] = self.vat
        if self.effective_vat is not None:
            json_data["effectiveVat"] = self.effective_vat
        if self.discount_prohibited is not None:
            json_data["discountProhibited"] = self.discount_prohibited
        if self.uom is not None:
            json_data["uom"] = self.uom
        if self.supplier is not None:
            json_data["supplier"] = self.supplier
        if self.min_price is not None:
            json_data["minPrice"] = self.min_price
        if self.buy_price is not None:
            json_data["buyPrice"] = self.buy_price
        if self.sale_prices is not None:
            json_data["salePrices"] = self.sale_prices
        if self.barcodes is not None:
            json_data["barcodes"] = self.barcodes
        if self.article is not None:
            json_data["article"] = self.article
        if self.weight is not None:
            json_data["weight"] = self.weight
        if self.volume is not None:
            json_data["volume"] = self.volume
        if self.packs is not None:
            json_data["packs"] = self.packs
        if self.is_serial_trackable is not None:
            json_data["isSerialTrackable"] = self.is_serial_trackable
        if self.tracking_type is not None:
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
        if self.attributes is not None:
            json_data["attributes"] = self.attributes
        if self.images is not None:
            json_data["images"] = self.images
        # actually it would be good to place a check for len(json_data) > 1, to avoid extra requests,
        # but I don't think that should be done on library level
        # Здесь было бы хорошо проверить, что длина json_data > 1, чтобы избежать лишних запросов,
        # но я не думаю, что это должно делаться на уровне библиотеки
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/product/{self.id}",
            "json": json_data,
        }

    def from_response(self, response: dict) -> Product:
        return Product.from_json(response)

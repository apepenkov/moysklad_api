import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

BundlePaymentItemType = typing.Literal[
    "GOOD", "EXCISABLE_GOOD", "COMPOUND_PAYMENT_ITEM", "ANOTHER_PAYMENT_ITEM"
]

BundleTaxSystem = typing.Literal[
    "GENERAL_TAX_SYSTEM",
    "PATENT_BASED",
    "PRESUMPTIVE_TAX_SYSTEM",
    "SIMPLIFIED_TAX_SYSTEM_INCOME",
    "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
    "TAX_SYSTEM_SAME_AS_GROUP",
    "UNIFIED_AGRICULTURAL_TAX",
]


class Bundle(types.MoySkladBaseClass):
    """
    accountId           | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived            | Boolean     | Добавлен ли Комплект в архив. Обязательное при ответе
    article             | String(255) | Артикул
    attributes          | Array(Object)| Коллекция доп. полей
    barcodes            | Array(Object)| Штрихкоды Комплекта
    code                 | String(255) | Код Комплекта
    components           | MetaArray   | Массив компонентов Комплекта. Expand
    country               | Meta        | Метаданные Страны. Expand
    description           | String(4096)| Описание Комплекта
    discountProhibited    | Boolean     | Признак запрета скидок. Обязательное при ответе
    effectiveVat           | Int         | Реальный НДС %. Только для чтения
    effectiveVatEnabled     | Boolean     | Только для чтения
    externalCode            | String(255) | Внешний код Комплекта. Обязательное при ответе
    files                    | MetaArray   | Файлы. Expand
    group                     | Meta        | Метаданные отдела. Обязательное при ответе, Expand
    id                         | UUID        | ID Комплекта. Обязательное при ответе, Только для чтения
    images                     | MetaArray   | Изображения. Expand
    meta                        | Meta        | Метаданные Комплекта. Обязательное при ответе
    minPrice                    | Object      | Минимальная цена
    name                         | String(255) | Наименование Комплекта. Обязательное при ответе, Необходимо при создании
    overhead                     | Object      | Дополнительные расходы
    owner                         | Meta        | Метаданные владельца. Expand
    partialDisposal               | Boolean     | Частичное выбытие маркированного товара
    pathName                       | String      | Наименование группы. Обязательное при ответе, Только для чтения
    paymentItemType                 | Enum        | Признак предмета расчета
    productFolder                    | Meta        | Метаданные группы Комплекта. Expand
    salePrices                        | Array(Object)| Цены продажи
    shared                             | Boolean     | Общий доступ. Обязательное при ответе
    syncId                              | UUID        | ID синхронизации. Только для чтения, Заполнение при создании
    taxSystem                           | Enum        | Код системы налогообложения
    tnved                                | String(255) | Код ТН ВЭД
    trackingType                         | Enum        | Тип маркируемой продукции
    uom                                   | Meta        | Единица измерения. Expand
    updated                               | DateTime    | Момент последнего обновления. Обязательное при ответе, Только для чтения
    useParentVat                          | Boolean     | Используется ли ставка НДС родительской группы. Обязательное при ответе
    vat                                    | Int         | НДС %
    vatEnabled                             | Boolean     | Включен ли НДС
    volume                                 | Float       | Объем
    weight                                  | Float       | Вес
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    article: typing.Optional[str]
    attributes: typing.Optional[typing.List[dict]]
    barcodes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    components: typing.Optional[dict]
    country: typing.Optional[types.Meta]
    description: typing.Optional[str]
    discount_prohibited: typing.Optional[bool]
    effective_vat: typing.Optional[int]
    effective_vat_enabled: typing.Optional[bool]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    images: typing.Optional[dict]
    meta: typing.Optional[types.Meta]
    min_price: typing.Optional[dict]
    name: typing.Optional[str]
    overhead: typing.Optional[dict]
    owner: typing.Optional[types.Meta]
    partial_disposal: typing.Optional[bool]
    path_name: typing.Optional[str]
    payment_item_type: typing.Optional[BundlePaymentItemType]
    product_folder: typing.Optional[types.Meta]
    sale_prices: typing.Optional[typing.List[dict]]
    shared: typing.Optional[bool]
    sync_id: typing.Optional[str]
    tax_system: typing.Optional[BundleTaxSystem]
    tnved: typing.Optional[str]
    tracking_type: typing.Optional[str]
    uom: typing.Optional[types.Meta]
    updated: typing.Optional[datetime.datetime]
    use_parent_vat: typing.Optional[bool]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]
    volume: typing.Optional[float]
    weight: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Bundle":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.article = dict_data.get("article")
        instance.attributes = dict_data.get("attributes")
        instance.barcodes = dict_data.get("barcodes")
        instance.code = dict_data.get("code")
        instance.components = dict_data.get("components")
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
        instance.meta = dict_data.get("meta")
        instance.min_price = dict_data.get("minPrice")
        instance.name = dict_data.get("name")
        instance.overhead = dict_data.get("overhead")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.partial_disposal = dict_data.get("partialDisposal")
        instance.path_name = dict_data.get("pathName")
        instance.payment_item_type = dict_data.get("paymentItemType")
        instance.product_folder = helpers.get_meta(dict_data.get("productFolder"))
        instance.sale_prices = dict_data.get("salePrices")
        instance.shared = dict_data.get("shared")
        instance.sync_id = dict_data.get("syncId")
        instance.tax_system = dict_data.get("taxSystem")
        instance.tnved = dict_data.get("tnved")
        instance.tracking_type = dict_data.get("trackingType")
        instance.uom = helpers.get_meta(dict_data.get("uom"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.use_parent_vat = dict_data.get("useParentVat")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.volume = dict_data.get("volume")
        instance.weight = dict_data.get("weight")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("bundle",)


def _build_bundle_json(
    name: typing.Union[Unset, str] = Unset,
    archived: typing.Union[Unset, bool] = Unset,
    article: typing.Union[Unset, str] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    country: typing.Union[Unset, types.Meta] = Unset,
    description: typing.Union[Unset, str] = Unset,
    discount_prohibited: typing.Union[Unset, bool] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, typing.List[dict]] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    images: typing.Union[Unset, typing.List[dict]] = Unset,
    min_price: typing.Union[Unset, dict] = Unset,
    overhead: typing.Union[Unset, dict] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    partial_disposal: typing.Union[Unset, bool] = Unset,
    payment_item_type: typing.Union[Unset, BundlePaymentItemType] = Unset,
    product_folder: typing.Union[Unset, types.Meta] = Unset,
    sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    tax_system: typing.Union[Unset, BundleTaxSystem] = Unset,
    tnved: typing.Union[Unset, str] = Unset,
    tracking_type: typing.Union[Unset, str] = Unset,
    uom: typing.Union[Unset, types.Meta] = Unset,
    use_parent_vat: typing.Union[Unset, bool] = Unset,
    vat: typing.Union[Unset, int] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
    volume: typing.Union[Unset, float] = Unset,
    weight: typing.Union[Unset, float] = Unset,
) -> dict:
    json_data = {}
    if name != Unset:
        json_data["name"] = name
    if archived != Unset:
        json_data["archived"] = archived
    if article != Unset:
        json_data["article"] = article
    if attributes != Unset:
        json_data["attributes"] = attributes
    if barcodes != Unset:
        json_data["barcodes"] = barcodes
    if code != Unset:
        json_data["code"] = code
    if country != Unset:
        json_data["country"] = {"meta": country}
    if description != Unset:
        json_data["description"] = description
    if discount_prohibited != Unset:
        json_data["discountProhibited"] = discount_prohibited
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if group != Unset:
        json_data["group"] = {"meta": group}
    if images != Unset:
        json_data["images"] = images
    if min_price != Unset:
        json_data["minPrice"] = min_price
    if overhead != Unset:
        json_data["overhead"] = overhead
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if partial_disposal != Unset:
        json_data["partialDisposal"] = partial_disposal
    if payment_item_type != Unset:
        json_data["paymentItemType"] = payment_item_type
    if product_folder != Unset:
        json_data["productFolder"] = {"meta": product_folder}
    if sale_prices != Unset:
        json_data["salePrices"] = sale_prices
    if shared != Unset:
        json_data["shared"] = shared
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if tax_system != Unset:
        json_data["taxSystem"] = tax_system
    if tnved != Unset:
        json_data["tnved"] = tnved
    if tracking_type != Unset:
        json_data["trackingType"] = tracking_type
    if uom != Unset:
        json_data["uom"] = {"meta": uom}
    if use_parent_vat != Unset:
        json_data["useParentVat"] = use_parent_vat
    if vat != Unset:
        json_data["vat"] = vat
    if vat_enabled != Unset:
        json_data["vatEnabled"] = vat_enabled
    if volume != Unset:
        json_data["volume"] = volume
    if weight != Unset:
        json_data["weight"] = weight
    return json_data


class GetBundlesRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.search != Unset:
            params["search"] = self.search
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bundle",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Bundle]:
        return [Bundle.from_json(x) for x in result["rows"]]


class CreateBundleRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        archived: typing.Union[Unset, bool] = Unset,
        article: typing.Union[Unset, str] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        country: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        images: typing.Union[Unset, typing.List[dict]] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        partial_disposal: typing.Union[Unset, bool] = Unset,
        payment_item_type: typing.Union[Unset, BundlePaymentItemType] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, BundleTaxSystem] = Unset,
        tnved: typing.Union[Unset, str] = Unset,
        tracking_type: typing.Union[Unset, str] = Unset,
        uom: typing.Union[Unset, types.Meta] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        volume: typing.Union[Unset, float] = Unset,
        weight: typing.Union[Unset, float] = Unset,
        components: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.name = name
        self.archived = archived
        self.article = article
        self.attributes = attributes
        self.barcodes = barcodes
        self.code = code
        self.country = country
        self.description = description
        self.discount_prohibited = discount_prohibited
        self.external_code = external_code
        self.files = files
        self.group = group
        self.images = images
        self.min_price = min_price
        self.overhead = overhead
        self.owner = owner
        self.partial_disposal = partial_disposal
        self.payment_item_type = payment_item_type
        self.product_folder = product_folder
        self.sale_prices = sale_prices
        self.shared = shared
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.tnved = tnved
        self.tracking_type = tracking_type
        self.uom = uom
        self.use_parent_vat = use_parent_vat
        self.vat = vat
        self.vat_enabled = vat_enabled
        self.volume = volume
        self.weight = weight
        self.components = components

    def to_request(self) -> RequestData:
        json_data = _build_bundle_json(
            name=self.name,
            archived=self.archived,
            article=self.article,
            attributes=self.attributes,
            barcodes=self.barcodes,
            code=self.code,
            country=self.country,
            description=self.description,
            discount_prohibited=self.discount_prohibited,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            images=self.images,
            min_price=self.min_price,
            overhead=self.overhead,
            owner=self.owner,
            partial_disposal=self.partial_disposal,
            payment_item_type=self.payment_item_type,
            product_folder=self.product_folder,
            sale_prices=self.sale_prices,
            shared=self.shared,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            tnved=self.tnved,
            tracking_type=self.tracking_type,
            uom=self.uom,
            use_parent_vat=self.use_parent_vat,
            vat=self.vat,
            vat_enabled=self.vat_enabled,
            volume=self.volume,
            weight=self.weight,
        )
        if self.components != Unset:
            json_data["components"] = {"rows": self.components}
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/bundle",
            json=json_data,
        )

    def from_response(self, result: dict) -> Bundle:
        return Bundle.from_json(result)


class DeleteBundleRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetBundleRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.id}",
        )

    def from_response(self, result: dict) -> Bundle:
        return Bundle.from_json(result)


class UpdateBundleRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        article: typing.Union[Unset, str] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        country: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        images: typing.Union[Unset, typing.List[dict]] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        partial_disposal: typing.Union[Unset, bool] = Unset,
        payment_item_type: typing.Union[Unset, BundlePaymentItemType] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, BundleTaxSystem] = Unset,
        tnved: typing.Union[Unset, str] = Unset,
        tracking_type: typing.Union[Unset, str] = Unset,
        uom: typing.Union[Unset, types.Meta] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        volume: typing.Union[Unset, float] = Unset,
        weight: typing.Union[Unset, float] = Unset,
        components: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.id = id_
        self.name = name
        self.archived = archived
        self.article = article
        self.attributes = attributes
        self.barcodes = barcodes
        self.code = code
        self.country = country
        self.description = description
        self.discount_prohibited = discount_prohibited
        self.external_code = external_code
        self.files = files
        self.group = group
        self.images = images
        self.min_price = min_price
        self.overhead = overhead
        self.owner = owner
        self.partial_disposal = partial_disposal
        self.payment_item_type = payment_item_type
        self.product_folder = product_folder
        self.sale_prices = sale_prices
        self.shared = shared
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.tnved = tnved
        self.tracking_type = tracking_type
        self.uom = uom
        self.use_parent_vat = use_parent_vat
        self.vat = vat
        self.vat_enabled = vat_enabled
        self.volume = volume
        self.weight = weight
        self.components = components

    def to_request(self) -> RequestData:
        json_data = _build_bundle_json(
            name=self.name,
            archived=self.archived,
            article=self.article,
            attributes=self.attributes,
            barcodes=self.barcodes,
            code=self.code,
            country=self.country,
            description=self.description,
            discount_prohibited=self.discount_prohibited,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            images=self.images,
            min_price=self.min_price,
            overhead=self.overhead,
            owner=self.owner,
            partial_disposal=self.partial_disposal,
            payment_item_type=self.payment_item_type,
            product_folder=self.product_folder,
            sale_prices=self.sale_prices,
            shared=self.shared,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            tnved=self.tnved,
            tracking_type=self.tracking_type,
            uom=self.uom,
            use_parent_vat=self.use_parent_vat,
            vat=self.vat,
            vat_enabled=self.vat_enabled,
            volume=self.volume,
            weight=self.weight,
        )
        if self.components != Unset:
            json_data["components"] = {"rows": self.components}
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Bundle:
        return Bundle.from_json(result)


class BundleComponent(types.MoySkladBaseClass):
    """
    id         | UUID  | ID компонента. Только для чтения
    meta       | Meta  | Метаданные компонента
    accountId  | UUID  | ID учетной записи. Только для чтения
    assortment | Meta  | Метаданные товара/услуги/модификации. Необходимо при создании, Expand
    quantity   | Float | Количество. Необходимо при создании
    """

    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    quantity: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "BundleComponent":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.quantity = dict_data.get("quantity")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("bundle", "components")


class GetBundleComponentsRequest(types.ApiRequest):
    def __init__(
        self,
        bundle_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.bundle_id = bundle_id
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.bundle_id}/components",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[BundleComponent]:
        return [BundleComponent.from_json(x) for x in result["rows"]]


class AddBundleComponentRequest(types.ApiRequest):
    def __init__(self, bundle_id: str, assortment: types.Meta, quantity: float):
        self.bundle_id = bundle_id
        self.assortment = assortment
        self.quantity = quantity

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.bundle_id}/components",
            json={"assortment": {"meta": self.assortment}, "quantity": self.quantity},
        )

    def from_response(self, result: dict) -> BundleComponent:
        return BundleComponent.from_json(result)


class GetBundleComponentRequest(types.ApiRequest):
    def __init__(self, bundle_id: str, component_id: str):
        self.bundle_id = bundle_id
        self.component_id = component_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.bundle_id}/components/{self.component_id}",
        )

    def from_response(self, result: dict) -> BundleComponent:
        return BundleComponent.from_json(result)


class UpdateBundleComponentRequest(types.ApiRequest):
    def __init__(
        self,
        bundle_id: str,
        component_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
    ):
        self.bundle_id = bundle_id
        self.component_id = component_id
        self.assortment = assortment
        self.quantity = quantity

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.bundle_id}/components/{self.component_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> BundleComponent:
        return BundleComponent.from_json(result)


class DeleteBundleComponentRequest(types.ApiRequest):
    def __init__(self, bundle_id: str, component_id: str):
        self.bundle_id = bundle_id
        self.component_id = component_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/bundle/{self.bundle_id}/components/{self.component_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

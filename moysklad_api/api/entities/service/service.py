import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

PaymentItemType = typing.Literal[
    "SERVICE",
    "WORK",
    "PROVIDING_RID",
    "COMPOUND_PAYMENT_ITEM",
    "ANOTHER_PAYMENT_ITEM",
]

TaxSystem = typing.Literal[
    "GENERAL_TAX_SYSTEM",
    "PATENT_BASED",
    "PRESUMPTIVE_TAX_SYSTEM",
    "SIMPLIFIED_TAX_SYSTEM_INCOME",
    "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
    "TAX_SYSTEM_SAME_AS_GROUP",
    "UNIFIED_AGRICULTURAL_TAX",
]


class Service(types.MoySkladBaseClass):
    """
    accountId           | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived            | Boolean     | Добавлена ли Услуга в архив. Обязательное при ответе
    attributes          | Array(Object)| Коллекция доп. полей
    barcodes            | Array(Object)| Штрихкоды Услуги
    buyPrice            | Object      | Закупочная цена {"value": Float, "currency": Meta}
    code                | String(255) | Код Услуги
    description         | String(4096)| Описание Услуги
    discountProhibited  | Boolean     | Признак запрета скидок. Обязательное при ответе
    effectiveVat        | Int         | Реальный НДС %. Только для чтения
    effectiveVatEnabled | Boolean     | Только для чтения
    externalCode        | String(255) | Внешний код Услуги. Обязательное при ответе
    files                | MetaArray   | Файлы. Expand
    group                | Meta        | Метаданные отдела сотрудника. Обязательное при ответе, Expand
    id                   | UUID        | ID Услуги. Обязательное при ответе, Только для чтения
    meta                 | Meta        | Метаданные Услуги. Обязательное при ответе
    minPrice             | Object      | Минимальная цена {"value": Float, "currency": Meta}
    name                 | String(255) | Наименование Услуги. Обязательное при ответе, Необходимо при создании
    owner                | Meta        | Метаданные владельца. Expand
    pathName             | String      | Наименование группы. Обязательное при ответе, Только для чтения
    paymentItemType       | Enum        | Признак предмета расчета
    productFolder         | Meta        | Метаданные группы Услуги. Expand
    salePrices            | Array(Object)| Цены продажи
    shared                | Boolean     | Общий доступ. Обязательное при ответе
    syncId                | UUID        | ID синхронизации. Только для чтения, Заполнение при создании
    taxSystem             | Enum        | Код системы налогообложения
    uom                    | Meta        | Единица измерения. Expand
    updated                | DateTime    | Момент последнего обновления. Обязательное при ответе, Только для чтения
    useParentVat            | Boolean     | Используется ли ставка НДС родительской группы. Обязательное при ответе
    vat                     | Int         | НДС %
    vatEnabled              | Boolean     | Включен ли НДС
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    barcodes: typing.Optional[typing.List[dict]]
    buy_price: typing.Optional[dict]
    code: typing.Optional[str]
    description: typing.Optional[str]
    discount_prohibited: typing.Optional[bool]
    effective_vat: typing.Optional[int]
    effective_vat_enabled: typing.Optional[bool]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    min_price: typing.Optional[dict]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    path_name: typing.Optional[str]
    payment_item_type: typing.Optional[PaymentItemType]
    product_folder: typing.Optional[types.Meta]
    sale_prices: typing.Optional[typing.List[dict]]
    shared: typing.Optional[bool]
    sync_id: typing.Optional[str]
    tax_system: typing.Optional[TaxSystem]
    uom: typing.Optional[types.Meta]
    updated: typing.Optional[datetime.datetime]
    use_parent_vat: typing.Optional[bool]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Service":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.barcodes = dict_data.get("barcodes")
        instance.buy_price = dict_data.get("buyPrice")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.discount_prohibited = dict_data.get("discountProhibited")
        instance.effective_vat = dict_data.get("effectiveVat")
        instance.effective_vat_enabled = dict_data.get("effectiveVatEnabled")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.min_price = dict_data.get("minPrice")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.path_name = dict_data.get("pathName")
        instance.payment_item_type = dict_data.get("paymentItemType")
        instance.product_folder = helpers.get_meta(dict_data.get("productFolder"))
        instance.sale_prices = dict_data.get("salePrices")
        instance.shared = dict_data.get("shared")
        instance.sync_id = dict_data.get("syncId")
        instance.tax_system = dict_data.get("taxSystem")
        instance.uom = helpers.get_meta(dict_data.get("uom"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.use_parent_vat = dict_data.get("useParentVat")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("service",)


def _build_service_json(
    name: typing.Union[Unset, str] = Unset,
    archived: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
    buy_price: typing.Union[Unset, dict] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    discount_prohibited: typing.Union[Unset, bool] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, typing.List[dict]] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    min_price: typing.Union[Unset, dict] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    payment_item_type: typing.Union[Unset, PaymentItemType] = Unset,
    product_folder: typing.Union[Unset, types.Meta] = Unset,
    sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    tax_system: typing.Union[Unset, TaxSystem] = Unset,
    uom: typing.Union[Unset, types.Meta] = Unset,
    use_parent_vat: typing.Union[Unset, bool] = Unset,
    vat: typing.Union[Unset, int] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if name != Unset:
        json_data["name"] = name
    if archived != Unset:
        json_data["archived"] = archived
    if attributes != Unset:
        json_data["attributes"] = attributes
    if barcodes != Unset:
        json_data["barcodes"] = barcodes
    if buy_price != Unset:
        json_data["buyPrice"] = buy_price
    if code != Unset:
        json_data["code"] = code
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
    if min_price != Unset:
        json_data["minPrice"] = min_price
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
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
    if uom != Unset:
        json_data["uom"] = {"meta": uom}
    if use_parent_vat != Unset:
        json_data["useParentVat"] = use_parent_vat
    if vat != Unset:
        json_data["vat"] = vat
    if vat_enabled != Unset:
        json_data["vatEnabled"] = vat_enabled
    return json_data


class GetServicesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/service",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Service]:
        return [Service.from_json(x) for x in result["rows"]]


class CreateServiceRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        buy_price: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payment_item_type: typing.Union[Unset, PaymentItemType] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, TaxSystem] = Unset,
        uom: typing.Union[Unset, types.Meta] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
    ):
        self.name = name
        self.archived = archived
        self.attributes = attributes
        self.barcodes = barcodes
        self.buy_price = buy_price
        self.code = code
        self.description = description
        self.discount_prohibited = discount_prohibited
        self.external_code = external_code
        self.files = files
        self.group = group
        self.min_price = min_price
        self.owner = owner
        self.payment_item_type = payment_item_type
        self.product_folder = product_folder
        self.sale_prices = sale_prices
        self.shared = shared
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.uom = uom
        self.use_parent_vat = use_parent_vat
        self.vat = vat
        self.vat_enabled = vat_enabled

    def to_request(self) -> RequestData:
        json_data = _build_service_json(
            name=self.name,
            archived=self.archived,
            attributes=self.attributes,
            barcodes=self.barcodes,
            buy_price=self.buy_price,
            code=self.code,
            description=self.description,
            discount_prohibited=self.discount_prohibited,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            min_price=self.min_price,
            owner=self.owner,
            payment_item_type=self.payment_item_type,
            product_folder=self.product_folder,
            sale_prices=self.sale_prices,
            shared=self.shared,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            uom=self.uom,
            use_parent_vat=self.use_parent_vat,
            vat=self.vat,
            vat_enabled=self.vat_enabled,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/service",
            json=json_data,
        )

    def from_response(self, result: dict) -> Service:
        return Service.from_json(result)


class DeleteServiceRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/service/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetServiceRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/service/{self.id}",
        )

    def from_response(self, result: dict) -> Service:
        return Service.from_json(result)


class UpdateServiceRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        buy_price: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payment_item_type: typing.Union[Unset, PaymentItemType] = Unset,
        product_folder: typing.Union[Unset, types.Meta] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, TaxSystem] = Unset,
        uom: typing.Union[Unset, types.Meta] = Unset,
        use_parent_vat: typing.Union[Unset, bool] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.name = name
        self.archived = archived
        self.attributes = attributes
        self.barcodes = barcodes
        self.buy_price = buy_price
        self.code = code
        self.description = description
        self.discount_prohibited = discount_prohibited
        self.external_code = external_code
        self.files = files
        self.group = group
        self.min_price = min_price
        self.owner = owner
        self.payment_item_type = payment_item_type
        self.product_folder = product_folder
        self.sale_prices = sale_prices
        self.shared = shared
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.uom = uom
        self.use_parent_vat = use_parent_vat
        self.vat = vat
        self.vat_enabled = vat_enabled

    def to_request(self) -> RequestData:
        json_data = _build_service_json(
            name=self.name,
            archived=self.archived,
            attributes=self.attributes,
            barcodes=self.barcodes,
            buy_price=self.buy_price,
            code=self.code,
            description=self.description,
            discount_prohibited=self.discount_prohibited,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            min_price=self.min_price,
            owner=self.owner,
            payment_item_type=self.payment_item_type,
            product_folder=self.product_folder,
            sale_prices=self.sale_prices,
            shared=self.shared,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            uom=self.uom,
            use_parent_vat=self.use_parent_vat,
            vat=self.vat,
            vat_enabled=self.vat_enabled,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/service/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Service:
        return Service.from_json(result)

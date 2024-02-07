import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


# https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-assortiment-poluchit-assortiment


class Assortment(types.MoySkladBaseClass):
    meta: types.Meta
    id: str
    account_id: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    group: typing.Optional[types.Meta]
    updated: typing.Optional[datetime.datetime]
    name: str
    code: str
    external_code: typing.Optional[str]
    archived: bool
    path_name: typing.Optional[str]
    use_parent_vat: bool
    vat: float
    vat_enabled: bool
    effective_vat: float
    effective_vat_enabled: bool
    uom: typing.Optional[types.Meta]
    images: typing.Optional[types.Meta]
    min_price: typing.Optional[dict]
    sale_prices: typing.List[dict]
    supplier: typing.Optional[types.Meta]
    buy_price: typing.Optional[dict]
    article: str
    weight: typing.Optional[float]
    volume: typing.Optional[float]
    barcodes: typing.List[dict]
    variants_count: int
    is_serial_trackable: bool
    stock: float
    reserve: float
    in_transit: float
    quantity: float

    @classmethod
    def from_json(cls, dict_data: dict) -> "Assortment":
        instance = cls()
        instance.meta = helpers.get_meta(dict_data.get("meta"))
        instance.id = dict_data.get("id")
        instance.account_id = dict_data.get("accountId")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.shared = dict_data.get("shared")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.name = dict_data.get("name")
        instance.code = dict_data.get("code")
        instance.external_code = dict_data.get("externalCode")
        instance.archived = dict_data.get("archived")
        instance.path_name = dict_data.get("pathName")
        instance.use_parent_vat = dict_data.get("useParentVat")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.effective_vat = dict_data.get("effectiveVat")
        instance.effective_vat_enabled = dict_data.get("effectiveVatEnabled")
        instance.uom = helpers.get_meta(dict_data.get("uom"))
        instance.images = helpers.get_meta(dict_data.get("images"))
        instance.min_price = dict_data.get("minPrice")
        instance.sale_prices = dict_data.get("salePrices") or []
        instance.supplier = helpers.get_meta(dict_data.get("supplier"))
        instance.buy_price = dict_data.get("buyPrice")
        instance.article = dict_data.get("article")
        instance.weight = dict_data.get("weight")
        instance.volume = dict_data.get("volume")
        instance.barcodes = dict_data.get("barcodes") or []
        instance.variants_count = dict_data.get("variantsCount")
        instance.is_serial_trackable = dict_data.get("isSerialTrackable")
        instance.stock = dict_data.get("stock")
        instance.reserve = dict_data.get("reserve")
        instance.in_transit = dict_data.get("inTransit")
        instance.quantity = dict_data.get("quantity")
        return instance


class AssortmentSettingsUniqueCodeRules(types.MoySkladBaseClass):
    check_unique_code: bool
    fill_unique_code: bool

    @classmethod
    def from_json(cls, dict_data: dict) -> "AssortmentSettingsUniqueCodeRules":
        instance = cls()
        instance.check_unique_code = dict_data.get("checkUniqueCodeBoolean")
        instance.fill_unique_code = dict_data.get("fillUniqueCode")
        return instance


class AssortmentSettingsBarcodeRules(types.MoySkladBaseClass):
    fill_ean13_barcode: bool
    weight_barcode_prefix: int

    @classmethod
    def from_json(cls, dict_data: dict) -> "AssortmentSettingsBarcodeRules":
        instance = cls()
        instance.fill_ean13_barcode = dict_data.get("fillEAN13Barcode")
        instance.weight_barcode_prefix = dict_data.get("weightBarcodePrefix")
        return instance


class AssortmentSettings(types.MoySkladBaseClass):
    unique_code_rules: AssortmentSettingsUniqueCodeRules
    barcode_rules: AssortmentSettingsBarcodeRules
    created_shared: bool
    meta: types.Meta

    @classmethod
    def from_json(cls, dict_data: dict) -> "AssortmentSettings":
        instance = cls()
        instance.unique_code_rules = AssortmentSettingsUniqueCodeRules.from_json(
            dict_data.get("uniqueCodeRules")
        )
        instance.barcode_rules = AssortmentSettingsBarcodeRules.from_json(
            dict_data.get("barcodeRules")
        )
        instance.created_shared = dict_data.get("createdShared")
        instance.meta = helpers.get_meta(dict_data.get("meta"))
        return instance


class GetAssortmentListRequest(types.ApiRequest):
    def __init__(
        self,
        limit: int = 1000,
        offset: int = 0,
        group_by: typing.Union[Unset, str] = Unset,
        filter_: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.group_by = group_by
        self.filter = filter_

    def to_request(self) -> RequestData:
        params = {
            "limit": self.limit,
            "offset": self.offset,
        }
        if self.group_by != Unset:
            params["groupBy"] = self.group_by

        if self.filter != Unset:
            params["filter"] = self.filter
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/assortment", params=params
        )

    def from_response(self, result: dict) -> typing.List["Assortment"]:
        return [Assortment.from_json(x) for x in result["rows"]]


class DeleteAssortmentsRequest(types.ApiRequest):
    def __init__(self, assortment_ids: typing.List[str]):
        self.assortment_ids = assortment_ids

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/assortment",
            json=[
                {
                    {
                        "meta": {
                            "href": f"{helpers.BASE_URL}/entity/product/{x}",
                            "metadataHref": f"{helpers.BASE_URL}/entity/product/metadata",
                            "type": "product",
                            "mediaType": "application/json",
                        }
                    }
                }
                for x in self.assortment_ids
            ],
        )

    def from_response(self, result: list) -> typing.List[dict]:
        return result


class GetAssortmentSettingsRequest(types.ApiRequest):
    def __init__(self):
        ...

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/assortment/settings",
        )

    def from_response(self, result: dict) -> Assortment:
        return Assortment.from_json(result)


class EditAssortmentSettingsRequest(types.ApiRequest):
    class AssortmentSettingsBarcodeRules(typing.TypedDict):
        fillEAN13Barcode: bool
        weightBarcodePrefix: int

    class AssortmentSettingsUniqueCodeRules(typing.TypedDict):
        checkUniqueCodeBoolean: bool
        fillUniqueCode: bool

    def __init__(
        self,
        unique_code_rules: AssortmentSettingsUniqueCodeRules,
        barcode_rules: AssortmentSettingsBarcodeRules,
        created_shared: bool,
    ):
        self.unique_code_rules = unique_code_rules
        self.barcode_rules = barcode_rules
        self.created_shared = created_shared

    def to_request(self) -> RequestData:
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/assortment/settings",
            json={
                "uniqueCodeRules": self.unique_code_rules,
                "barcodeRules": self.barcode_rules,
                "createdShared": self.created_shared,
            },
        )

    def from_response(self, result: dict) -> Assortment:
        return Assortment.from_json(result)

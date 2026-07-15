import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ProductionStageCompletion(types.MoySkladBaseClass):
    """Выполнение этапа производства (entity/productionstagecompletion)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    created: typing.Optional[datetime.datetime]
    defect: typing.Optional[bool]
    description: typing.Optional[str]
    enable_hour_accounting: typing.Optional[bool]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    labour_unit_cost: typing.Optional[float]
    standard_hour_unit: typing.Optional[float]
    materials: typing.Optional[dict]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    performer: typing.Optional[types.Meta]
    processing_unit_cost: typing.Optional[float]
    production_stage: typing.Optional[types.Meta]
    production_volume: typing.Optional[float]
    products: typing.Optional[dict]
    service: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    standard_hour_cost: typing.Optional[float]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductionStageCompletion":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.defect = dict_data.get("defect")
        instance.description = dict_data.get("description")
        instance.enable_hour_accounting = dict_data.get("enableHourAccounting")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.labour_unit_cost = dict_data.get("labourUnitCost")
        instance.standard_hour_unit = dict_data.get("standardHourUnit")
        instance.materials = dict_data.get("materials")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.performer = helpers.get_meta(dict_data.get("performer"))
        instance.processing_unit_cost = dict_data.get("processingUnitCost")
        instance.production_stage = helpers.get_meta(dict_data.get("productionStage"))
        instance.production_volume = dict_data.get("productionVolume")
        instance.products = dict_data.get("products")
        instance.service = helpers.get_meta(dict_data.get("service"))
        instance.shared = dict_data.get("shared")
        instance.standard_hour_cost = dict_data.get("standardHourCost")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("productionstagecompletion",)


class Material(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    consumed_quantity: typing.Optional[float]
    things: typing.Optional[typing.List[str]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Material":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.consumed_quantity = dict_data.get("consumedQuantity")
        instance.things = dict_data.get("things")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "productionstagecompletion", "materials"


class Product(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    produced_quantity: typing.Optional[float]
    things: typing.Optional[typing.List[str]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Product":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.produced_quantity = dict_data.get("producedQuantity")
        instance.things = dict_data.get("things")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "productionstagecompletion", "products"


def _build_json(
    production_stage: typing.Union[Unset, types.Meta] = Unset,
    production_volume: typing.Union[Unset, float] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    defect: typing.Union[Unset, bool] = Unset,
    description: typing.Union[Unset, str] = Unset,
    enable_hour_accounting: typing.Union[Unset, bool] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    labour_unit_cost: typing.Union[Unset, float] = Unset,
    standard_hour_unit: typing.Union[Unset, float] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    performer: typing.Union[Unset, types.Meta] = Unset,
    processing_unit_cost: typing.Union[Unset, float] = Unset,
    service: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    standard_hour_cost: typing.Union[Unset, float] = Unset,
) -> dict:
    json_data = {}
    if production_stage != Unset:
        json_data["productionStage"] = {"meta": production_stage}
    if production_volume != Unset:
        json_data["productionVolume"] = production_volume
    if applicable != Unset:
        json_data["applicable"] = applicable
    if defect != Unset:
        json_data["defect"] = defect
    if description != Unset:
        json_data["description"] = description
    if enable_hour_accounting != Unset:
        json_data["enableHourAccounting"] = enable_hour_accounting
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if group != Unset:
        json_data["group"] = {"meta": group}
    if labour_unit_cost != Unset:
        json_data["labourUnitCost"] = labour_unit_cost
    if standard_hour_unit != Unset:
        json_data["standardHourUnit"] = standard_hour_unit
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if performer != Unset:
        json_data["performer"] = {"meta": performer}
    if processing_unit_cost != Unset:
        json_data["processingUnitCost"] = processing_unit_cost
    if service != Unset:
        json_data["service"] = {"meta": service}
    if shared != Unset:
        json_data["shared"] = shared
    if standard_hour_cost != Unset:
        json_data["standardHourCost"] = standard_hour_cost
    return json_data


class GetProductionStageCompletionsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProductionStageCompletion]:
        return [ProductionStageCompletion.from_json(x) for x in result["rows"]]


class CreateProductionStageCompletionRequest(types.ApiRequest):
    def __init__(
        self,
        production_stage: types.Meta,
        production_volume: float,
        applicable: typing.Union[Unset, bool] = Unset,
        defect: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        enable_hour_accounting: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        labour_unit_cost: typing.Union[Unset, float] = Unset,
        standard_hour_unit: typing.Union[Unset, float] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        performer: typing.Union[Unset, types.Meta] = Unset,
        processing_unit_cost: typing.Union[Unset, float] = Unset,
        service: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        standard_hour_cost: typing.Union[Unset, float] = Unset,
    ):
        self.production_stage = production_stage
        self.production_volume = production_volume
        self.applicable = applicable
        self.defect = defect
        self.description = description
        self.enable_hour_accounting = enable_hour_accounting
        self.external_code = external_code
        self.group = group
        self.labour_unit_cost = labour_unit_cost
        self.standard_hour_unit = standard_hour_unit
        self.moment = moment
        self.name = name
        self.owner = owner
        self.performer = performer
        self.processing_unit_cost = processing_unit_cost
        self.service = service
        self.shared = shared
        self.standard_hour_cost = standard_hour_cost

    def to_request(self) -> RequestData:
        json_data = _build_json(
            production_stage=self.production_stage,
            production_volume=self.production_volume,
            applicable=self.applicable,
            defect=self.defect,
            description=self.description,
            enable_hour_accounting=self.enable_hour_accounting,
            external_code=self.external_code,
            group=self.group,
            labour_unit_cost=self.labour_unit_cost,
            standard_hour_unit=self.standard_hour_unit,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            performer=self.performer,
            processing_unit_cost=self.processing_unit_cost,
            service=self.service,
            shared=self.shared,
            standard_hour_cost=self.standard_hour_cost,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionStageCompletion:
        return ProductionStageCompletion.from_json(result)


class DeleteProductionStageCompletionRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProductionStageCompletionRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.id}",
        )

    def from_response(self, result: dict) -> ProductionStageCompletion:
        return ProductionStageCompletion.from_json(result)


class UpdateProductionStageCompletionRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        applicable: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        enable_hour_accounting: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        labour_unit_cost: typing.Union[Unset, float] = Unset,
        standard_hour_unit: typing.Union[Unset, float] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        performer: typing.Union[Unset, types.Meta] = Unset,
        processing_unit_cost: typing.Union[Unset, float] = Unset,
        production_volume: typing.Union[Unset, float] = Unset,
        service: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        standard_hour_cost: typing.Union[Unset, float] = Unset,
    ):
        self.id = id_
        self.applicable = applicable
        self.description = description
        self.enable_hour_accounting = enable_hour_accounting
        self.external_code = external_code
        self.group = group
        self.labour_unit_cost = labour_unit_cost
        self.standard_hour_unit = standard_hour_unit
        self.moment = moment
        self.name = name
        self.owner = owner
        self.performer = performer
        self.processing_unit_cost = processing_unit_cost
        self.production_volume = production_volume
        self.service = service
        self.shared = shared
        self.standard_hour_cost = standard_hour_cost

    def to_request(self) -> RequestData:
        json_data = _build_json(
            applicable=self.applicable,
            description=self.description,
            enable_hour_accounting=self.enable_hour_accounting,
            external_code=self.external_code,
            group=self.group,
            labour_unit_cost=self.labour_unit_cost,
            standard_hour_unit=self.standard_hour_unit,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            performer=self.performer,
            processing_unit_cost=self.processing_unit_cost,
            production_volume=self.production_volume,
            service=self.service,
            shared=self.shared,
            standard_hour_cost=self.standard_hour_cost,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionStageCompletion:
        return ProductionStageCompletion.from_json(result)


class GetProductionStageCompletionMaterialsRequest(types.ApiRequest):
    def __init__(
        self,
        productionstagecompletion_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.productionstagecompletion_id = productionstagecompletion_id
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
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.productionstagecompletion_id}/materials",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Material]:
        return [Material.from_json(x) for x in result["rows"]]


class CreateProductionStageCompletionMaterialRequest(types.ApiRequest):
    def __init__(
        self,
        productionstagecompletion_id: str,
        assortment: types.Meta,
        consumed_quantity: typing.Union[Unset, float] = Unset,
        things: typing.Union[Unset, typing.List[str]] = Unset,
    ):
        self.productionstagecompletion_id = productionstagecompletion_id
        self.assortment = assortment
        self.consumed_quantity = consumed_quantity
        self.things = things

    def to_request(self) -> RequestData:
        json_data = {"assortment": {"meta": self.assortment}}
        if self.consumed_quantity != Unset:
            json_data["consumedQuantity"] = self.consumed_quantity
        if self.things != Unset:
            json_data["things"] = self.things
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.productionstagecompletion_id}/materials",
            json=json_data,
        )

    def from_response(self, result: dict) -> Material:
        return Material.from_json(result)


class UpdateProductionStageCompletionMaterialRequest(types.ApiRequest):
    def __init__(
        self,
        productionstagecompletion_id: str,
        material_id: str,
        consumed_quantity: typing.Union[Unset, float] = Unset,
        things: typing.Union[Unset, typing.List[str]] = Unset,
    ):
        self.productionstagecompletion_id = productionstagecompletion_id
        self.material_id = material_id
        self.consumed_quantity = consumed_quantity
        self.things = things

    def to_request(self) -> RequestData:
        json_data = {}
        if self.consumed_quantity != Unset:
            json_data["consumedQuantity"] = self.consumed_quantity
        if self.things != Unset:
            json_data["things"] = self.things
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.productionstagecompletion_id}/materials/{self.material_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Material:
        return Material.from_json(result)


class GetProductionStageCompletionProductsRequest(types.ApiRequest):
    def __init__(
        self,
        productionstagecompletion_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.productionstagecompletion_id = productionstagecompletion_id
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
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.productionstagecompletion_id}/products",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Product]:
        return [Product.from_json(x) for x in result["rows"]]


class UpdateProductionStageCompletionProductRequest(types.ApiRequest):
    def __init__(
        self,
        productionstagecompletion_id: str,
        product_id: str,
        produced_quantity: typing.Union[Unset, float] = Unset,
        things: typing.Union[Unset, typing.List[str]] = Unset,
    ):
        self.productionstagecompletion_id = productionstagecompletion_id
        self.product_id = product_id
        self.produced_quantity = produced_quantity
        self.things = things

    def to_request(self) -> RequestData:
        json_data = {}
        if self.produced_quantity != Unset:
            json_data["producedQuantity"] = self.produced_quantity
        if self.things != Unset:
            json_data["things"] = self.things
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productionstagecompletion/{self.productionstagecompletion_id}/products/{self.product_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Product:
        return Product.from_json(result)

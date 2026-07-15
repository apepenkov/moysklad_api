import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ProductionTask(types.MoySkladBaseClass):
    """Производственное задание (entity/productiontask)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    awaiting: typing.Optional[bool]
    code: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    delivery_planned_moment: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    materials_store: typing.Optional[types.Meta]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    printed: typing.Optional[bool]
    production_rows: typing.Optional[dict]
    production_end: typing.Optional[datetime.datetime]
    production_start: typing.Optional[datetime.datetime]
    products: typing.Optional[dict]
    products_store: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    reserve: typing.Optional[bool]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    updated: typing.Optional[datetime.datetime]
    customer_orders: typing.Optional[typing.List[types.Meta]]
    demands: typing.Optional[typing.List[types.Meta]]
    emission_orders: typing.Optional[typing.List[types.Meta]]
    internal_orders: typing.Optional[typing.List[types.Meta]]
    moves: typing.Optional[typing.List[types.Meta]]
    production_tasks: typing.Optional[typing.List[types.Meta]]
    production_task_supplies: typing.Optional[typing.List[types.Meta]]
    purchase_orders: typing.Optional[typing.List[types.Meta]]
    supplies: typing.Optional[typing.List[types.Meta]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductionTask":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.awaiting = dict_data.get("awaiting")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.delivery_planned_moment = helpers.parse_date(
            dict_data.get("deliveryPlannedMoment")
        )
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.materials_store = helpers.get_meta(dict_data.get("materialsStore"))
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.printed = dict_data.get("printed")
        instance.production_rows = dict_data.get("productionRows")
        instance.production_end = helpers.parse_date(dict_data.get("productionEnd"))
        instance.production_start = helpers.parse_date(
            dict_data.get("productionStart")
        )
        instance.products = dict_data.get("products")
        instance.products_store = helpers.get_meta(dict_data.get("productsStore"))
        instance.published = dict_data.get("published")
        instance.reserve = dict_data.get("reserve")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.customer_orders = [
            helpers.get_meta(x, must=True) for x in dict_data.get("customerOrders", [])
        ]
        instance.demands = [
            helpers.get_meta(x, must=True) for x in dict_data.get("demands", [])
        ]
        instance.emission_orders = [
            helpers.get_meta(x, must=True) for x in dict_data.get("emissionOrders", [])
        ]
        instance.internal_orders = [
            helpers.get_meta(x, must=True) for x in dict_data.get("internalOrders", [])
        ]
        instance.moves = [
            helpers.get_meta(x, must=True) for x in dict_data.get("moves", [])
        ]
        instance.production_tasks = [
            helpers.get_meta(x, must=True)
            for x in dict_data.get("productionTasks", [])
        ]
        instance.production_task_supplies = [
            helpers.get_meta(x, must=True)
            for x in dict_data.get("productionTaskSupplies", [])
        ]
        instance.purchase_orders = [
            helpers.get_meta(x, must=True) for x in dict_data.get("purchaseOrders", [])
        ]
        instance.supplies = [
            helpers.get_meta(x, must=True) for x in dict_data.get("supplies", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("productiontask",)


class ProductionRow(types.MoySkladBaseClass):
    """Позиция Производственного задания (entity/productiontask/{id}/productionrows)."""

    account_id: typing.Optional[str]
    external_code: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    processing_plan: typing.Optional[types.Meta]
    production_volume: typing.Optional[float]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductionRow":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.processing_plan = helpers.get_meta(dict_data.get("processingPlan"))
        instance.production_volume = dict_data.get("productionVolume")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "productiontask", "productionrows"


class ProductionTaskResult(types.MoySkladBaseClass):
    """Продукт Производственного задания (entity/productiontask/{id}/products)."""

    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    plan_quantity: typing.Optional[float]
    production_row: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductionTaskResult":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.plan_quantity = dict_data.get("planQuantity")
        instance.production_row = helpers.get_meta(dict_data.get("productionRow"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "productiontask", "products"


class ProductionStage(types.MoySkladBaseClass):
    """Производственный этап (entity/productionstage)."""

    account_id: typing.Optional[str]
    enable_hour_accounting: typing.Optional[bool]
    files: typing.Optional[dict]
    id: typing.Optional[str]
    instruction: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    labour_unit_cost: typing.Optional[float]
    materials: typing.Optional[dict]
    material_store: typing.Optional[types.Meta]
    ordering_position: typing.Optional[int]
    stage: typing.Optional[types.Meta]
    production_row: typing.Optional[types.Meta]
    total_quantity: typing.Optional[float]
    completed_quantity: typing.Optional[float]
    available_quantity: typing.Optional[float]
    blocked_quantity: typing.Optional[float]
    skipped_quantity: typing.Optional[float]
    processing_unit_cost: typing.Optional[float]
    standard_hour_cost: typing.Optional[float]
    standard_hour_unit: typing.Optional[float]
    planned_end_date: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductionStage":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.enable_hour_accounting = dict_data.get("enableHourAccounting")
        instance.files = dict_data.get("files")
        instance.id = dict_data.get("id")
        instance.instruction = dict_data.get("instruction")
        instance.meta = dict_data.get("meta")
        instance.labour_unit_cost = dict_data.get("labourUnitCost")
        instance.materials = dict_data.get("materials")
        instance.material_store = helpers.get_meta(dict_data.get("materialStore"))
        instance.ordering_position = dict_data.get("orderingPosition")
        instance.stage = helpers.get_meta(dict_data.get("stage"))
        instance.production_row = helpers.get_meta(dict_data.get("productionRow"))
        instance.total_quantity = dict_data.get("totalQuantity")
        instance.completed_quantity = dict_data.get("completedQuantity")
        instance.available_quantity = dict_data.get("availableQuantity")
        instance.blocked_quantity = dict_data.get("blockedQuantity")
        instance.skipped_quantity = dict_data.get("skippedQuantity")
        instance.processing_unit_cost = dict_data.get("processingUnitCost")
        instance.standard_hour_cost = dict_data.get("standardHourCost")
        instance.standard_hour_unit = dict_data.get("standardHourUnit")
        instance.planned_end_date = helpers.parse_date(dict_data.get("plannedEndDate"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("productionstage",)


class ProductionStageMaterial(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    plan_quantity: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductionStageMaterial":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.plan_quantity = dict_data.get("planQuantity")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "productionstage", "materials"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    materials_store: typing.Union[Unset, types.Meta] = Unset,
    products_store: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    awaiting: typing.Union[Unset, bool] = Unset,
    code: typing.Union[Unset, str] = Unset,
    delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    production_start: typing.Union[Unset, datetime.datetime] = Unset,
    products: typing.Union[Unset, typing.List[dict]] = Unset,
    reserve: typing.Union[Unset, bool] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if materials_store != Unset:
        json_data["materialsStore"] = {"meta": materials_store}
    if products_store != Unset:
        json_data["productsStore"] = {"meta": products_store}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if awaiting != Unset:
        json_data["awaiting"] = awaiting
    if code != Unset:
        json_data["code"] = code
    if delivery_planned_moment != Unset:
        json_data["deliveryPlannedMoment"] = helpers.date_to_str(
            delivery_planned_moment
        )
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if group != Unset:
        json_data["group"] = {"meta": group}
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if positions != Unset:
        json_data["positions"] = []
        for position in positions:
            new_position: dict = position.copy()
            if "processingPlan" in new_position:
                new_position["processingPlan"] = {
                    "meta": new_position["processingPlan"]
                }
            json_data["positions"].append(new_position)
    if production_start != Unset:
        json_data["productionStart"] = helpers.date_to_str(production_start)
    if products != Unset:
        json_data["products"] = []
        for product in products:
            new_product: dict = product.copy()
            if "assortment" in new_product:
                new_product["assortment"] = {"meta": new_product["assortment"]}
            if "productionRow" in new_product:
                new_product["productionRow"] = {
                    "meta": new_product["productionRow"]
                }
            json_data["products"].append(new_product)
    if reserve != Unset:
        json_data["reserve"] = reserve
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    return json_data


class GetProductionTasksRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/productiontask",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProductionTask]:
        return [ProductionTask.from_json(x) for x in result["rows"]]


class CreateProductionTaskRequest(types.ApiRequest):
    class CreateProductionRow(typing.TypedDict):
        processingPlan: types.Meta
        productionVolume: typing.NotRequired[float]

    class CreateProduct(typing.TypedDict):
        assortment: types.Meta
        planQuantity: float
        productionRow: types.Meta

    def __init__(
        self,
        organization: types.Meta,
        materials_store: types.Meta,
        products_store: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        awaiting: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreateProductionRow]] = Unset,
        production_start: typing.Union[Unset, datetime.datetime] = Unset,
        products: typing.Union[Unset, typing.List[CreateProduct]] = Unset,
        reserve: typing.Union[Unset, bool] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.organization = organization
        self.materials_store = materials_store
        self.products_store = products_store
        self.applicable = applicable
        self.attributes = attributes
        self.awaiting = awaiting
        self.code = code
        self.delivery_planned_moment = delivery_planned_moment
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.production_start = production_start
        self.products = products
        self.reserve = reserve
        self.shared = shared
        self.state = state

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            materials_store=self.materials_store,
            products_store=self.products_store,
            applicable=self.applicable,
            attributes=self.attributes,
            awaiting=self.awaiting,
            code=self.code,
            delivery_planned_moment=self.delivery_planned_moment,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            production_start=self.production_start,
            products=self.products,
            reserve=self.reserve,
            shared=self.shared,
            state=self.state,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/productiontask",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionTask:
        return ProductionTask.from_json(result)


class DeleteProductionTaskRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProductionTaskRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/productiontask/{self.id}"
        )

    def from_response(self, result: dict) -> ProductionTask:
        return ProductionTask.from_json(result)


class UpdateProductionTaskRequest(types.ApiRequest):
    CreateProductionRow = CreateProductionTaskRequest.CreateProductionRow
    CreateProduct = CreateProductionTaskRequest.CreateProduct

    def __init__(
        self,
        id_: str,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        awaiting: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        materials_store: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreateProductionRow]] = Unset,
        production_start: typing.Union[Unset, datetime.datetime] = Unset,
        products: typing.Union[Unset, typing.List[CreateProduct]] = Unset,
        products_store: typing.Union[Unset, types.Meta] = Unset,
        reserve: typing.Union[Unset, bool] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.id = id_
        self.applicable = applicable
        self.attributes = attributes
        self.awaiting = awaiting
        self.code = code
        self.delivery_planned_moment = delivery_planned_moment
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.materials_store = materials_store
        self.moment = moment
        self.name = name
        self.organization = organization
        self.owner = owner
        self.positions = positions
        self.production_start = production_start
        self.products = products
        self.products_store = products_store
        self.reserve = reserve
        self.shared = shared
        self.state = state

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            materials_store=self.materials_store,
            products_store=self.products_store,
            applicable=self.applicable,
            attributes=self.attributes,
            awaiting=self.awaiting,
            code=self.code,
            delivery_planned_moment=self.delivery_planned_moment,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            production_start=self.production_start,
            products=self.products,
            reserve=self.reserve,
            shared=self.shared,
            state=self.state,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionTask:
        return ProductionTask.from_json(result)


class GetProductionTaskRowsRequest(types.ApiRequest):
    def __init__(self, productiontask_id: str):
        self.productiontask_id = productiontask_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/productionrows",
        )

    def from_response(self, result: dict) -> typing.List[ProductionRow]:
        return [ProductionRow.from_json(x) for x in result["rows"]]


class GetProductionTaskRowRequest(types.ApiRequest):
    def __init__(self, productiontask_id: str, row_id: str):
        self.productiontask_id = productiontask_id
        self.row_id = row_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/productionrows/{self.row_id}",
        )

    def from_response(self, result: dict) -> ProductionRow:
        return ProductionRow.from_json(result)


class UpdateProductionTaskRowRequest(types.ApiRequest):
    def __init__(
        self,
        productiontask_id: str,
        row_id: str,
        production_volume: float,
    ):
        self.productiontask_id = productiontask_id
        self.row_id = row_id
        self.production_volume = production_volume

    def to_request(self) -> RequestData:
        json_data = {"productionVolume": self.production_volume}
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/productionrows/{self.row_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionRow:
        return ProductionRow.from_json(result)


class DeleteProductionTaskRowRequest(types.ApiRequest):
    def __init__(self, productiontask_id: str, row_id: str):
        self.productiontask_id = productiontask_id
        self.row_id = row_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/productionrows/{self.row_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProductionTaskProductsRequest(types.ApiRequest):
    def __init__(
        self,
        productiontask_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.productiontask_id = productiontask_id
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
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/products",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProductionTaskResult]:
        return [ProductionTaskResult.from_json(x) for x in result["rows"]]


class GetProductionTaskProductRequest(types.ApiRequest):
    def __init__(self, productiontask_id: str, product_id: str):
        self.productiontask_id = productiontask_id
        self.product_id = product_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/products/{self.product_id}",
        )

    def from_response(self, result: dict) -> ProductionTaskResult:
        return ProductionTaskResult.from_json(result)


class CreateProductionTaskProductRequest(types.ApiRequest):
    """Создать продукт (entity/productiontask/{id}/product, единственное число)."""

    def __init__(
        self,
        productiontask_id: str,
        assortment: types.Meta,
        plan_quantity: float,
        production_row: types.Meta,
    ):
        self.productiontask_id = productiontask_id
        self.assortment = assortment
        self.plan_quantity = plan_quantity
        self.production_row = production_row

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "planQuantity": self.plan_quantity,
            "productionRow": {"meta": self.production_row},
        }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/product",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionTaskResult:
        return ProductionTaskResult.from_json(result)


class UpdateProductionTaskProductRequest(types.ApiRequest):
    def __init__(
        self,
        productiontask_id: str,
        product_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        plan_quantity: typing.Union[Unset, float] = Unset,
    ):
        self.productiontask_id = productiontask_id
        self.product_id = product_id
        self.assortment = assortment
        self.plan_quantity = plan_quantity

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.plan_quantity != Unset:
            json_data["planQuantity"] = self.plan_quantity
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/products/{self.product_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionTaskResult:
        return ProductionTaskResult.from_json(result)


class DeleteProductionTaskProductRequest(types.ApiRequest):
    def __init__(self, productiontask_id: str, product_id: str):
        self.productiontask_id = productiontask_id
        self.product_id = product_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}/products/{self.product_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProductionStagesRequest(types.ApiRequest):
    """Список Производственных этапов данного Производственного задания (обязателен filter по productionTask)."""

    def __init__(
        self,
        productiontask_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.productiontask_id = productiontask_id
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {
            "filter": f"productionTask={helpers.BASE_URL}/entity/productiontask/{self.productiontask_id}"
        }
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/productionstage",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProductionStage]:
        return [ProductionStage.from_json(x) for x in result["rows"]]


class GetProductionStageRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/productionstage/{self.id}"
        )

    def from_response(self, result: dict) -> ProductionStage:
        return ProductionStage.from_json(result)


class UpdateProductionStageRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        enable_hour_accounting: typing.Union[Unset, bool] = Unset,
        labour_unit_cost: typing.Union[Unset, float] = Unset,
        processing_unit_cost: typing.Union[Unset, float] = Unset,
        standard_hour_cost: typing.Union[Unset, float] = Unset,
        standard_hour_unit: typing.Union[Unset, float] = Unset,
        planned_end_date: typing.Union[Unset, datetime.datetime] = Unset,
    ):
        self.id = id_
        self.enable_hour_accounting = enable_hour_accounting
        self.labour_unit_cost = labour_unit_cost
        self.processing_unit_cost = processing_unit_cost
        self.standard_hour_cost = standard_hour_cost
        self.standard_hour_unit = standard_hour_unit
        self.planned_end_date = planned_end_date

    def to_request(self) -> RequestData:
        json_data = {}
        if self.enable_hour_accounting != Unset:
            json_data["enableHourAccounting"] = self.enable_hour_accounting
        if self.labour_unit_cost != Unset:
            json_data["labourUnitCost"] = self.labour_unit_cost
        if self.processing_unit_cost != Unset:
            json_data["processingUnitCost"] = self.processing_unit_cost
        if self.standard_hour_cost != Unset:
            json_data["standardHourCost"] = self.standard_hour_cost
        if self.standard_hour_unit != Unset:
            json_data["standardHourUnit"] = self.standard_hour_unit
        if self.planned_end_date != Unset:
            json_data["plannedEndDate"] = helpers.date_to_str(self.planned_end_date)
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productionstage/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionStage:
        return ProductionStage.from_json(result)


class GetProductionStageMaterialsRequest(types.ApiRequest):
    def __init__(
        self,
        productionstage_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.productionstage_id = productionstage_id
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
            url=f"{helpers.BASE_URL}/entity/productionstage/{self.productionstage_id}/materials",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProductionStageMaterial]:
        return [ProductionStageMaterial.from_json(x) for x in result["rows"]]


class CreateProductionStageMaterialRequest(types.ApiRequest):
    """Ответ API - список материалов (в т.ч. добавленный)."""

    def __init__(
        self,
        productionstage_id: str,
        assortment: types.Meta,
        plan_quantity: float,
    ):
        self.productionstage_id = productionstage_id
        self.assortment = assortment
        self.plan_quantity = plan_quantity

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "planQuantity": self.plan_quantity,
        }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/productionstage/{self.productionstage_id}/materials",
            json=json_data,
        )

    def from_response(
        self, result: typing.List[dict]
    ) -> typing.List[ProductionStageMaterial]:
        return [ProductionStageMaterial.from_json(x) for x in result]


class UpdateProductionStageMaterialRequest(types.ApiRequest):
    def __init__(
        self,
        productionstage_id: str,
        material_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        plan_quantity: typing.Union[Unset, float] = Unset,
    ):
        self.productionstage_id = productionstage_id
        self.material_id = material_id
        self.assortment = assortment
        self.plan_quantity = plan_quantity

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.plan_quantity != Unset:
            json_data["planQuantity"] = self.plan_quantity
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/productionstage/{self.productionstage_id}/materials/{self.material_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProductionStageMaterial:
        return ProductionStageMaterial.from_json(result)


class DeleteProductionStageMaterialRequest(types.ApiRequest):
    def __init__(self, productionstage_id: str, material_id: str):
        self.productionstage_id = productionstage_id
        self.material_id = material_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/productionstage/{self.productionstage_id}/materials/{self.material_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

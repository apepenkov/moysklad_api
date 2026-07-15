import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

CostDistributionType = typing.Literal["BY_PRICE", "BY_PRODUCTION"]


class ProcessingPlan(types.MoySkladBaseClass):
    """
    accountId           | UUID   | ID учетной записи. Обязательное при ответе, Только для чтения
    archived            | Boolean| Добавлена ли Техкарта в архив. Обязательное при ответе
    code                | String(255)| Код Техкарты
    cost                | Double | Стоимость производства
    costDistributionType | Enum  | Тип распределения себестоимости. Обязательное при ответе, Только для чтения
    externalCode         | String(255)| Внешний код Техкарты. Обязательное при ответе
    group                 | Meta  | Отдел сотрудника. Обязательное при ответе, Expand
    id                     | UUID  | ID Техкарты. Обязательное при ответе, Только для чтения
    stages                 | MetaArray| Коллекция этапов Техкарты. Обязательное при ответе, Expand
    materials               | MetaArray| Коллекция материалов Техкарты. Обязательное при ответе, Expand
    meta                     | Meta  | Метаданные Техкарты. Обязательное при ответе
    name                      | String(255)| Наименование Техкарты. Обязательное при ответе, Необходимо при создании
    owner                      | Meta  | Владелец (Сотрудник). Expand
    parent                      | Meta  | Метаданные группы Техкарты. Обязательное при ответе, Expand
    pathName                     | String| Наименование группы. Обязательное при ответе, Только для чтения
    processingProcess              | Meta  | Метаданные Техпроцесса. Обязательное при ответе, Expand
    products                        | MetaArray| Коллекция готовых продуктов. Обязательное при ответе, Expand, Необходимо при создании
    shared                          | Boolean| Общий доступ. Обязательное при ответе
    updated                          | DateTime| Момент последнего обновления Техкарты. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    code: typing.Optional[str]
    cost: typing.Optional[float]
    cost_distribution_type: typing.Optional[CostDistributionType]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    stages: typing.Optional[dict]
    materials: typing.Optional[dict]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    parent: typing.Optional[types.Meta]
    path_name: typing.Optional[str]
    processing_process: typing.Optional[types.Meta]
    products: typing.Optional[dict]
    shared: typing.Optional[bool]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingPlan":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.code = dict_data.get("code")
        instance.cost = dict_data.get("cost")
        instance.cost_distribution_type = dict_data.get("costDistributionType")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.stages = dict_data.get("stages")
        instance.materials = dict_data.get("materials")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.parent = helpers.get_meta(dict_data.get("parent"))
        instance.path_name = dict_data.get("pathName")
        instance.processing_process = helpers.get_meta(
            dict_data.get("processingProcess")
        )
        instance.products = dict_data.get("products")
        instance.shared = dict_data.get("shared")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingplan",)


class ProcessingPlanStage(types.MoySkladBaseClass):
    """
    accountId               | UUID  | ID учетной записи. Только для чтения
    enableHourAccounting     | Boolean| Учет по нормо-часам. Обязательное при ответе
    id                        | UUID  | ID этапа Техкарты. Только для чтения
    cost                       | Double| Стоимость производства на этапе. Обязательное при ответе
    labourCost                  | Double| Оплата труда на этапе. Обязательное при ответе
    standardHour                 | Double| Нормо-часы на этапе. Обязательное при ответе
    processingProcessPosition     | Meta  | Метаданные позиции техпроцесса. Обязательное при ответе
    standardHourCost               | Double| Стоимость нормо-часа. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    enable_hour_accounting: typing.Optional[bool]
    id: typing.Optional[str]
    cost: typing.Optional[float]
    labour_cost: typing.Optional[float]
    standard_hour: typing.Optional[float]
    processing_process_position: typing.Optional[types.Meta]
    standard_hour_cost: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingPlanStage":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.enable_hour_accounting = dict_data.get("enableHourAccounting")
        instance.id = dict_data.get("id")
        instance.cost = dict_data.get("cost")
        instance.labour_cost = dict_data.get("labourCost")
        instance.standard_hour = dict_data.get("standardHour")
        instance.processing_process_position = helpers.get_meta(
            dict_data.get("processingProcessPosition")
        )
        instance.standard_hour_cost = dict_data.get("standardHourCost")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingplan", "stages")


class ProcessingPlanMaterial(types.MoySkladBaseClass):
    """
    accountId                 | UUID | ID учетной записи. Только для чтения
    assortment                 | Meta | Метаданные товара/модификации. Обязательное при ответе, Expand
    id                           | UUID | ID Материала. Только для чтения
    product                       | Meta | Метаданные товара позиции. Обязательное при ответе, Expand
    quantity                       | Float| Количество. Обязательное при ответе
    processingProcessPosition       | Meta | Метаданные позиции Техпроцесса. Обязательное при ответе
    materialProcessingPlan           | Meta | Метаданные техкарты материала. Только для чтения
    """

    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    product: typing.Optional[types.Meta]
    quantity: typing.Optional[float]
    processing_process_position: typing.Optional[types.Meta]
    material_processing_plan: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingPlanMaterial":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.product = helpers.get_meta(dict_data.get("product"))
        instance.quantity = dict_data.get("quantity")
        instance.processing_process_position = helpers.get_meta(
            dict_data.get("processingProcessPosition")
        )
        instance.material_processing_plan = helpers.get_meta(
            dict_data.get("materialProcessingPlan")
        )
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingplan", "materials")


class ProcessingPlanProduct(types.MoySkladBaseClass):
    """
    accountId | UUID | ID учетной записи. Только для чтения
    assortment | Meta | Метаданные товара/модификации. Обязательное при ответе, Expand
    id         | UUID | ID Продукта. Только для чтения
    product     | Meta | Метаданные товара позиции. Обязательное при ответе, Expand
    quantity     | Float| Количество. Обязательное при ответе
    """

    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    product: typing.Optional[types.Meta]
    quantity: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingPlanProduct":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.product = helpers.get_meta(dict_data.get("product"))
        instance.quantity = dict_data.get("quantity")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingplan", "products")


def _build_processingplan_json(
    name: typing.Union[Unset, str] = Unset,
    products: typing.Union[Unset, typing.List[dict]] = Unset,
    archived: typing.Union[Unset, bool] = Unset,
    code: typing.Union[Unset, str] = Unset,
    cost: typing.Union[Unset, float] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    materials: typing.Union[Unset, typing.List[dict]] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    parent: typing.Union[Unset, types.Meta] = Unset,
    processing_process: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if name != Unset:
        json_data["name"] = name
    if products != Unset:
        json_data["products"] = products
    if archived != Unset:
        json_data["archived"] = archived
    if code != Unset:
        json_data["code"] = code
    if cost != Unset:
        json_data["cost"] = cost
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if group != Unset:
        json_data["group"] = {"meta": group}
    if materials != Unset:
        json_data["materials"] = materials
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if parent != Unset:
        json_data["parent"] = {"meta": parent}
    if processing_process != Unset:
        json_data["processingProcess"] = {"meta": processing_process}
    if shared != Unset:
        json_data["shared"] = shared
    return json_data


class GetProcessingPlansRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/processingplan",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingPlan]:
        return [ProcessingPlan.from_json(x) for x in result["rows"]]


class CreateProcessingPlanRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        products: typing.List[dict],
        archived: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        cost: typing.Union[Unset, float] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        materials: typing.Union[Unset, typing.List[dict]] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent: typing.Union[Unset, types.Meta] = Unset,
        processing_process: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.name = name
        self.products = products
        self.archived = archived
        self.code = code
        self.cost = cost
        self.external_code = external_code
        self.group = group
        self.materials = materials
        self.owner = owner
        self.parent = parent
        self.processing_process = processing_process
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = _build_processingplan_json(
            name=self.name,
            products=self.products,
            archived=self.archived,
            code=self.code,
            cost=self.cost,
            external_code=self.external_code,
            group=self.group,
            materials=self.materials,
            owner=self.owner,
            parent=self.parent,
            processing_process=self.processing_process,
            shared=self.shared,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingplan",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingPlan:
        return ProcessingPlan.from_json(result)


class DeleteProcessingPlanRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProcessingPlanRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.id}",
        )

    def from_response(self, result: dict) -> ProcessingPlan:
        return ProcessingPlan.from_json(result)


class UpdateProcessingPlanRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        products: typing.Union[Unset, typing.List[dict]] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        cost: typing.Union[Unset, float] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        materials: typing.Union[Unset, typing.List[dict]] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent: typing.Union[Unset, types.Meta] = Unset,
        processing_process: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.name = name
        self.products = products
        self.archived = archived
        self.code = code
        self.cost = cost
        self.external_code = external_code
        self.group = group
        self.materials = materials
        self.owner = owner
        self.parent = parent
        self.processing_process = processing_process
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = _build_processingplan_json(
            name=self.name,
            products=self.products,
            archived=self.archived,
            code=self.code,
            cost=self.cost,
            external_code=self.external_code,
            group=self.group,
            materials=self.materials,
            owner=self.owner,
            parent=self.parent,
            processing_process=self.processing_process,
            shared=self.shared,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingPlan:
        return ProcessingPlan.from_json(result)


# --- Этапы Техкарты (только чтение/обновление) ---


class GetProcessingPlanStagesRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processingplan_id = processingplan_id
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
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/stages",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingPlanStage]:
        return [ProcessingPlanStage.from_json(x) for x in result["rows"]]


class GetProcessingPlanStageRequest(types.ApiRequest):
    def __init__(self, processingplan_id: str, stage_id: str):
        self.processingplan_id = processingplan_id
        self.stage_id = stage_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/stages/{self.stage_id}",
        )

    def from_response(self, result: dict) -> ProcessingPlanStage:
        return ProcessingPlanStage.from_json(result)


class UpdateProcessingPlanStageRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        stage_id: str,
        enable_hour_accounting: typing.Union[Unset, bool] = Unset,
        cost: typing.Union[Unset, float] = Unset,
        labour_cost: typing.Union[Unset, float] = Unset,
    ):
        self.processingplan_id = processingplan_id
        self.stage_id = stage_id
        self.enable_hour_accounting = enable_hour_accounting
        self.cost = cost
        self.labour_cost = labour_cost

    def to_request(self) -> RequestData:
        json_data = {}
        if self.enable_hour_accounting != Unset:
            json_data["enableHourAccounting"] = self.enable_hour_accounting
        if self.cost != Unset:
            json_data["cost"] = self.cost
        if self.labour_cost != Unset:
            json_data["labourCost"] = self.labour_cost
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/stages/{self.stage_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingPlanStage:
        return ProcessingPlanStage.from_json(result)


# --- Материалы Техкарты ---


class GetProcessingPlanMaterialsRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processingplan_id = processingplan_id
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
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/materials",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingPlanMaterial]:
        return [ProcessingPlanMaterial.from_json(x) for x in result["rows"]]


class GetProcessingPlanMaterialRequest(types.ApiRequest):
    def __init__(self, processingplan_id: str, material_id: str):
        self.processingplan_id = processingplan_id
        self.material_id = material_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/materials/{self.material_id}",
        )

    def from_response(self, result: dict) -> ProcessingPlanMaterial:
        return ProcessingPlanMaterial.from_json(result)


class CreateProcessingPlanMaterialRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        assortment: types.Meta,
        quantity: float,
        processing_process_position: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.processingplan_id = processingplan_id
        self.assortment = assortment
        self.quantity = quantity
        self.processing_process_position = processing_process_position

    def to_request(self) -> RequestData:
        json_data = {"assortment": {"meta": self.assortment}, "quantity": self.quantity}
        if self.processing_process_position != Unset:
            json_data["processingProcessPosition"] = {
                "meta": self.processing_process_position
            }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/materials",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingPlanMaterial:
        return ProcessingPlanMaterial.from_json(result)


class UpdateProcessingPlanMaterialRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        material_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        processing_process_position: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.processingplan_id = processingplan_id
        self.material_id = material_id
        self.assortment = assortment
        self.quantity = quantity
        self.processing_process_position = processing_process_position

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.processing_process_position != Unset:
            json_data["processingProcessPosition"] = {
                "meta": self.processing_process_position
            }
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/materials/{self.material_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingPlanMaterial:
        return ProcessingPlanMaterial.from_json(result)


class DeleteProcessingPlanMaterialRequest(types.ApiRequest):
    def __init__(self, processingplan_id: str, material_id: str):
        self.processingplan_id = processingplan_id
        self.material_id = material_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/materials/{self.material_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


# --- Продукты Техкарты ---


class GetProcessingPlanProductsRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processingplan_id = processingplan_id
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
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/products",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingPlanProduct]:
        return [ProcessingPlanProduct.from_json(x) for x in result["rows"]]


class GetProcessingPlanProductRequest(types.ApiRequest):
    def __init__(self, processingplan_id: str, product_id: str):
        self.processingplan_id = processingplan_id
        self.product_id = product_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/products/{self.product_id}",
        )

    def from_response(self, result: dict) -> ProcessingPlanProduct:
        return ProcessingPlanProduct.from_json(result)


class CreateProcessingPlanProductRequest(types.ApiRequest):
    def __init__(self, processingplan_id: str, assortment: types.Meta, quantity: float):
        self.processingplan_id = processingplan_id
        self.assortment = assortment
        self.quantity = quantity

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/products",
            json={"assortment": {"meta": self.assortment}, "quantity": self.quantity},
        )

    def from_response(self, result: dict) -> ProcessingPlanProduct:
        return ProcessingPlanProduct.from_json(result)


class UpdateProcessingPlanProductRequest(types.ApiRequest):
    def __init__(
        self,
        processingplan_id: str,
        product_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
    ):
        self.processingplan_id = processingplan_id
        self.product_id = product_id
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
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/products/{self.product_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingPlanProduct:
        return ProcessingPlanProduct.from_json(result)


class DeleteProcessingPlanProductRequest(types.ApiRequest):
    def __init__(self, processingplan_id: str, product_id: str):
        self.processingplan_id = processingplan_id
        self.product_id = product_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingplan/{self.processingplan_id}/products/{self.product_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

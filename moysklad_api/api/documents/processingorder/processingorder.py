import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ProcessingOrder(types.MoySkladBaseClass):
    """Заказ на производство (entity/processingorder)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    delivery_planned_moment: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    positions: typing.Optional[dict]
    printed: typing.Optional[bool]
    processing_plan: typing.Optional[types.Meta]
    project: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    quantity: typing.Optional[float]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    processings: typing.Optional[typing.List[types.Meta]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingOrder":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
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
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.processing_plan = helpers.get_meta(dict_data.get("processingPlan"))
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.quantity = dict_data.get("quantity")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.processings = [
            helpers.get_meta(x, must=True) for x in dict_data.get("processings", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingorder",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    quantity: typing.Optional[float]
    reserve: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.quantity = dict_data.get("quantity")
        instance.reserve = dict_data.get("reserve")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "processingorder", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    processing_plan: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
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
    project: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if processing_plan != Unset:
        json_data["processingPlan"] = {"meta": processing_plan}
    if store != Unset:
        json_data["store"] = {"meta": store}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
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
            new_position["assortment"] = {"meta": new_position["assortment"]}
            json_data["positions"].append(new_position)
    if project != Unset:
        json_data["project"] = {"meta": project}
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetProcessingOrdersRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/processingorder",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingOrder]:
        return [ProcessingOrder.from_json(x) for x in result["rows"]]


class CreateProcessingOrderRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        reserve: typing.NotRequired[float]

    def __init__(
        self,
        organization: types.Meta,
        processing_plan: types.Meta,
        positions: typing.List[CreatePosition],
        store: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.processing_plan = processing_plan
        self.positions = positions
        self.store = store
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.delivery_planned_moment = delivery_planned_moment
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.project = project
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            processing_plan=self.processing_plan,
            store=self.store,
            positions=self.positions,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            delivery_planned_moment=self.delivery_planned_moment,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            project=self.project,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingorder",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingOrder:
        return ProcessingOrder.from_json(result)


class DeleteProcessingOrderRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingorder/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProcessingOrderRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/processingorder/{self.id}"
        )

    def from_response(self, result: dict) -> ProcessingOrder:
        return ProcessingOrder.from_json(result)


class UpdateProcessingOrderRequest(types.ApiRequest):
    class UpdatePosition(typing.TypedDict):
        id: typing.NotRequired[str]
        quantity: typing.NotRequired[float]
        reserve: typing.NotRequired[float]

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        processing_plan: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List["UpdateProcessingOrderRequest.UpdatePosition"]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.processing_plan = processing_plan
        self.store = store
        self.applicable = applicable
        self.attributes = attributes
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
        self.project = project
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = {}
        if self.positions != Unset:
            json_data["positions"] = self.positions
        base = _build_json(
            organization=self.organization,
            processing_plan=self.processing_plan,
            store=self.store,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            delivery_planned_moment=self.delivery_planned_moment,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            project=self.project,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        base.update(json_data)
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingorder/{self.id}",
            json=base,
        )

    def from_response(self, result: dict) -> ProcessingOrder:
        return ProcessingOrder.from_json(result)


class GetProcessingOrderPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        processingorder_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processingorder_id = processingorder_id
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
            url=f"{helpers.BASE_URL}/entity/processingorder/{self.processingorder_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetProcessingOrderPositionRequest(types.ApiRequest):
    def __init__(self, processingorder_id: str, position_id: str):
        self.processingorder_id = processingorder_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingorder/{self.processingorder_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class UpdateProcessingOrderPositionRequest(types.ApiRequest):
    def __init__(
        self,
        processingorder_id: str,
        position_id: str,
        quantity: typing.Union[Unset, float] = Unset,
        reserve: typing.Union[Unset, float] = Unset,
    ):
        self.processingorder_id = processingorder_id
        self.position_id = position_id
        self.quantity = quantity
        self.reserve = reserve

    def to_request(self) -> RequestData:
        json_data = {}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.reserve != Unset:
            json_data["reserve"] = self.reserve
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingorder/{self.processingorder_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeleteProcessingOrderPositionRequest(types.ApiRequest):
    def __init__(self, processingorder_id: str, position_id: str):
        self.processingorder_id = processingorder_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingorder/{self.processingorder_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

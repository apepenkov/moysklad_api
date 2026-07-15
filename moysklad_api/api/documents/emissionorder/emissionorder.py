import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

EmissionType = typing.Literal["LOCAL", "FOREIGN", "REMAINS", "COMMISSION"]
TrackingType = typing.Literal[
    "ELECTRONICS", "LP_CLOTHES", "LP_LINENS", "MILK", "NCP", "NOT_TRACKED",
    "OTP", "PERFUMERY", "SHOES", "TIRES", "TOBACCO", "WATER",
]
DocumentState = typing.Literal["CREATED", "SUZ_CREATED", "SUZ_SEND", "SUZ_COMPLETED"]


class EmissionOrder(types.MoySkladBaseClass):
    """Заказ кодов маркировки (entity/emissionorder)."""

    account_id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    document_state: typing.Optional[str]
    emission_type: typing.Optional[str]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    positions: typing.Optional[dict]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    tracking_type: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    production_tasks: typing.Optional[typing.List[types.Meta]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "EmissionOrder":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.document_state = dict_data.get("documentState")
        instance.emission_type = dict_data.get("emissionType")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.tracking_type = dict_data.get("trackingType")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.production_tasks = [
            helpers.get_meta(x, must=True)
            for x in dict_data.get("productionTasks", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("emissionorder",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    quantity: typing.Optional[float]
    status: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.quantity = dict_data.get("quantity")
        instance.status = dict_data.get("status")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "emissionorder", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    emission_type: typing.Union[Unset, EmissionType] = Unset,
    tracking_type: typing.Union[Unset, TrackingType] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if emission_type != Unset:
        json_data["emissionType"] = emission_type
    if tracking_type != Unset:
        json_data["trackingType"] = tracking_type
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
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
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    return json_data


class GetEmissionOrdersRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/emissionorder", params=params
        )

    def from_response(self, result: dict) -> typing.List[EmissionOrder]:
        return [EmissionOrder.from_json(x) for x in result["rows"]]


class CreateEmissionOrderRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float

    def __init__(
        self,
        organization: types.Meta,
        emission_type: EmissionType,
        tracking_type: TrackingType,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.organization = organization
        self.emission_type = emission_type
        self.tracking_type = tracking_type
        self.description = description
        self.external_code = external_code
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            emission_type=self.emission_type,
            tracking_type=self.tracking_type,
            description=self.description,
            external_code=self.external_code,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/emissionorder",
            json=json_data,
        )

    def from_response(self, result: dict) -> EmissionOrder:
        return EmissionOrder.from_json(result)


class GetEmissionOrderRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/emissionorder/{self.id}"
        )

    def from_response(self, result: dict) -> EmissionOrder:
        return EmissionOrder.from_json(result)


class UpdateEmissionOrderRequest(types.ApiRequest):
    UpdatePosition = CreateEmissionOrderRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        emission_type: typing.Union[Unset, EmissionType] = Unset,
        tracking_type: typing.Union[Unset, TrackingType] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.emission_type = emission_type
        self.tracking_type = tracking_type
        self.description = description
        self.external_code = external_code
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            emission_type=self.emission_type,
            tracking_type=self.tracking_type,
            description=self.description,
            external_code=self.external_code,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/emissionorder/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> EmissionOrder:
        return EmissionOrder.from_json(result)


class GetEmissionOrderPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        emissionorder_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.emissionorder_id = emissionorder_id
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
            url=f"{helpers.BASE_URL}/entity/emissionorder/{self.emissionorder_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetEmissionOrderPositionRequest(types.ApiRequest):
    def __init__(self, emissionorder_id: str, position_id: str):
        self.emissionorder_id = emissionorder_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/emissionorder/{self.emissionorder_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class CreateEmissionOrderPositionRequest(types.ApiRequest):
    """Создать позицию. Ответ API - список позиций (в т.ч. созданная)."""

    def __init__(self, emissionorder_id: str, assortment: types.Meta, quantity: float):
        self.emissionorder_id = emissionorder_id
        self.assortment = assortment
        self.quantity = quantity

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/emissionorder/{self.emissionorder_id}/positions",
            json=json_data,
        )

    def from_response(self, result: typing.List[dict]) -> typing.List[Position]:
        return [Position.from_json(x) for x in result]


class UpdateEmissionOrderPositionRequest(types.ApiRequest):
    def __init__(
        self,
        emissionorder_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
    ):
        self.emissionorder_id = emissionorder_id
        self.position_id = position_id
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
            url=f"{helpers.BASE_URL}/entity/emissionorder/{self.emissionorder_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)

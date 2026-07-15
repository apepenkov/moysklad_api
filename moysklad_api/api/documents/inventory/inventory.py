import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Inventory(types.MoySkladBaseClass):
    """Инвентаризация (entity/inventory)."""

    account_id: typing.Optional[str]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
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
    published: typing.Optional[bool]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    enters: typing.Optional[types.Meta]
    losses: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Inventory":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
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
        instance.published = dict_data.get("published")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.enters = helpers.get_meta(dict_data.get("enters"))
        instance.losses = helpers.get_meta(dict_data.get("losses"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("inventory",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    calculated_quantity: typing.Optional[float]
    correction_amount: typing.Optional[float]
    correction_sum: typing.Optional[float]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    price: typing.Optional[float]
    quantity: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.calculated_quantity = dict_data.get("calculatedQuantity")
        instance.correction_amount = dict_data.get("correctionAmount")
        instance.correction_sum = dict_data.get("correctionSum")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "inventory", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if store != Unset:
        json_data["store"] = {"meta": store}
    if attributes != Unset:
        json_data["attributes"] = attributes
    if code != Unset:
        json_data["code"] = code
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
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetInventoriesRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/inventory", params=params
        )

    def from_response(self, result: dict) -> typing.List[Inventory]:
        return [Inventory.from_json(x) for x in result["rows"]]


class CreateInventoryRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]

    def __init__(
        self,
        organization: types.Meta,
        store: types.Meta,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.store = store
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            store=self.store,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/inventory", json=json_data
        )

    def from_response(self, result: dict) -> Inventory:
        return Inventory.from_json(result)


class DeleteInventoryRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/inventory/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetInventoryRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/inventory/{self.id}"
        )

    def from_response(self, result: dict) -> Inventory:
        return Inventory.from_json(result)


class UpdateInventoryRequest(types.ApiRequest):
    UpdatePosition = CreateInventoryRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.store = store
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            store=self.store,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/inventory/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Inventory:
        return Inventory.from_json(result)


class GetInventoryPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        inventory_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.inventory_id = inventory_id
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
            url=f"{helpers.BASE_URL}/entity/inventory/{self.inventory_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetInventoryPositionRequest(types.ApiRequest):
    def __init__(self, inventory_id: str, position_id: str):
        self.inventory_id = inventory_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/inventory/{self.inventory_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)

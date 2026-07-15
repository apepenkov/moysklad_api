import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Loss(types.MoySkladBaseClass):
    """Списание (entity/loss)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    expense_item: typing.Optional[types.Meta]
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
    project: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    sales_return: typing.Optional[types.Meta]
    inventory: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Loss":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.expense_item = helpers.get_meta(dict_data.get("expenseItem"))
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
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.sales_return = helpers.get_meta(dict_data.get("salesReturn"))
        instance.inventory = helpers.get_meta(dict_data.get("inventory"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("loss",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    declaration: typing.Optional[typing.List[dict]]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    price: typing.Optional[float]
    quantity: typing.Optional[float]
    reason: typing.Optional[str]
    slot: typing.Optional[types.Meta]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.declaration = dict_data.get("declaration")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.reason = dict_data.get("reason")
        instance.slot = helpers.get_meta(dict_data.get("slot"))
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "loss", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    expense_item: typing.Union[Unset, types.Meta] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if store != Unset:
        json_data["store"] = {"meta": store}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if code != Unset:
        json_data["code"] = code
    if description != Unset:
        json_data["description"] = description
    if expense_item != Unset:
        json_data["expenseItem"] = {"meta": expense_item}
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
    if rate != Unset:
        json_data["rate"] = rate
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetLossesRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/loss", params=params
        )

    def from_response(self, result: dict) -> typing.List[Loss]:
        return [Loss.from_json(x) for x in result["rows"]]


class CreateLossRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        reason: typing.NotRequired[str]
        vat: typing.NotRequired[int]

    def __init__(
        self,
        organization: types.Meta,
        store: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        expense_item: typing.Union[Unset, types.Meta] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.store = store
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.expense_item = expense_item
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            store=self.store,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            expense_item=self.expense_item,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            project=self.project,
            rate=self.rate,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/loss", json=json_data
        )

    def from_response(self, result: dict) -> Loss:
        return Loss.from_json(result)


class DeleteLossRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/loss/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetLossRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(method="GET", url=f"{helpers.BASE_URL}/entity/loss/{self.id}")

    def from_response(self, result: dict) -> Loss:
        return Loss.from_json(result)


class UpdateLossRequest(types.ApiRequest):
    UpdatePosition = CreateLossRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        expense_item: typing.Union[Unset, types.Meta] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.store = store
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.expense_item = expense_item
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            store=self.store,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            expense_item=self.expense_item,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            project=self.project,
            rate=self.rate,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/loss/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Loss:
        return Loss.from_json(result)


class GetLossPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        loss_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.loss_id = loss_id
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
            url=f"{helpers.BASE_URL}/entity/loss/{self.loss_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class CreateLossPositionRequest(types.ApiRequest):
    def __init__(
        self,
        loss_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, float] = Unset,
        reason: typing.Union[Unset, str] = Unset,
        vat: typing.Union[Unset, int] = Unset,
    ):
        self.loss_id = loss_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.reason = reason
        self.vat = vat

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.price != Unset:
            json_data["price"] = self.price
        if self.reason != Unset:
            json_data["reason"] = self.reason
        if self.vat != Unset:
            json_data["vat"] = self.vat
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/loss/{self.loss_id}/positions",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class GetLossPositionRequest(types.ApiRequest):
    def __init__(self, loss_id: str, position_id: str):
        self.loss_id = loss_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/loss/{self.loss_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class UpdateLossPositionRequest(types.ApiRequest):
    def __init__(
        self,
        loss_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        price: typing.Union[Unset, float] = Unset,
        reason: typing.Union[Unset, str] = Unset,
        vat: typing.Union[Unset, int] = Unset,
    ):
        self.loss_id = loss_id
        self.position_id = position_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.reason = reason
        self.vat = vat

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.price != Unset:
            json_data["price"] = self.price
        if self.reason != Unset:
            json_data["reason"] = self.reason
        if self.vat != Unset:
            json_data["vat"] = self.vat
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/loss/{self.loss_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeleteLossPositionRequest(types.ApiRequest):
    def __init__(self, loss_id: str, position_id: str):
        self.loss_id = loss_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/loss/{self.loss_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

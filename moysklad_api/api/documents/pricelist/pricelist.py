import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Column(typing.TypedDict):
    name: str
    percentageDiscount: typing.NotRequired[int]


class Cell(typing.TypedDict):
    column: str
    sum: int


class PriceList(types.MoySkladBaseClass):
    """Прайс-лист (entity/pricelist)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    columns: typing.Optional[typing.List[dict]]
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
    price_type: typing.Optional[dict]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PriceList":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.columns = dict_data.get("columns")
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
        instance.price_type = dict_data.get("priceType")
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("pricelist",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    cells: typing.Optional[typing.List[dict]]
    id: typing.Optional[str]
    pack: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.cells = dict_data.get("cells")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "pricelist", "positions"


def _build_json(
    columns: typing.Union[Unset, typing.List[Column]] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    organization: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if columns != Unset:
        json_data["columns"] = columns
    if applicable != Unset:
        json_data["applicable"] = applicable
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
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if positions != Unset:
        json_data["positions"] = []
        for position in positions:
            new_position: dict = position.copy()
            if "assortment" in new_position:
                new_position["assortment"] = {"meta": new_position["assortment"]}
            json_data["positions"].append(new_position)
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetPriceListsRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/pricelist", params=params
        )

    def from_response(self, result: dict) -> typing.List[PriceList]:
        return [PriceList.from_json(x) for x in result["rows"]]


class CreatePriceListRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: typing.NotRequired[types.Meta]
        cells: typing.NotRequired[typing.List[Cell]]

    def __init__(
        self,
        columns: typing.List[Column],
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.columns = columns
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization = organization
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            columns=self.columns,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            organization=self.organization,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/pricelist", json=json_data
        )

    def from_response(self, result: dict) -> PriceList:
        return PriceList.from_json(result)


class DeletePriceListRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetPriceListRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/pricelist/{self.id}"
        )

    def from_response(self, result: dict) -> PriceList:
        return PriceList.from_json(result)


class UpdatePriceListRequest(types.ApiRequest):
    UpdatePosition = CreatePriceListRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization = organization
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            organization=self.organization,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> PriceList:
        return PriceList.from_json(result)


class GetPriceListPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        pricelist_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.pricelist_id = pricelist_id
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
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.pricelist_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetPriceListPositionRequest(types.ApiRequest):
    def __init__(self, pricelist_id: str, position_id: str):
        self.pricelist_id = pricelist_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.pricelist_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class CreatePriceListPositionRequest(types.ApiRequest):
    def __init__(
        self,
        pricelist_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        cells: typing.Union[Unset, typing.List[Cell]] = Unset,
    ):
        self.pricelist_id = pricelist_id
        self.assortment = assortment
        self.cells = cells

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.cells != Unset:
            json_data["cells"] = self.cells
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.pricelist_id}/positions",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class UpdatePriceListPositionRequest(types.ApiRequest):
    def __init__(
        self,
        pricelist_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        cells: typing.Union[Unset, typing.List[Cell]] = Unset,
    ):
        self.pricelist_id = pricelist_id
        self.position_id = position_id
        self.assortment = assortment
        self.cells = cells

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.cells != Unset:
            json_data["cells"] = self.cells
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.pricelist_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeletePriceListPositionRequest(types.ApiRequest):
    def __init__(self, pricelist_id: str, position_id: str):
        self.pricelist_id = pricelist_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/pricelist/{self.pricelist_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

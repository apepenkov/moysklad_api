import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class PrepaymentReturn(types.MoySkladBaseClass):
    """Возврат предоплаты (entity/prepaymentreturn)."""

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    cash_sum: typing.Optional[float]
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
    no_cash_sum: typing.Optional[float]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    positions: typing.Optional[dict]
    prepayment: typing.Optional[types.Meta]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    qr_sum: typing.Optional[float]
    rate: typing.Optional[dict]
    retail_shift: typing.Optional[types.Meta]
    retail_store: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    tax_system: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    vat_enabled: typing.Optional[bool]
    vat_included: typing.Optional[bool]
    vat_sum: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PrepaymentReturn":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.cash_sum = dict_data.get("cashSum")
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
        instance.no_cash_sum = dict_data.get("noCashSum")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.prepayment = helpers.get_meta(dict_data.get("prepayment"))
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.qr_sum = dict_data.get("qrSum")
        instance.rate = dict_data.get("rate")
        instance.retail_shift = helpers.get_meta(dict_data.get("retailShift"))
        instance.retail_store = helpers.get_meta(dict_data.get("retailStore"))
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.tax_system = dict_data.get("taxSystem")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("prepaymentreturn",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    discount: typing.Optional[float]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    price: typing.Optional[float]
    quantity: typing.Optional[float]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.discount = dict_data.get("discount")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "prepaymentreturn", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    retail_shift: typing.Union[Unset, types.Meta] = Unset,
    prepayment: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    cash_sum: typing.Union[Unset, float] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    no_cash_sum: typing.Union[Unset, float] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    qr_sum: typing.Union[Unset, float] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    retail_store: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    tax_system: typing.Union[Unset, str] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
    vat_included: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
    if retail_shift != Unset:
        json_data["retailShift"] = {"meta": retail_shift}
    if prepayment != Unset:
        json_data["prepayment"] = {"meta": prepayment}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if cash_sum != Unset:
        json_data["cashSum"] = cash_sum
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
    if no_cash_sum != Unset:
        json_data["noCashSum"] = no_cash_sum
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if positions != Unset:
        json_data["positions"] = []
        for position in positions:
            new_position: dict = position.copy()
            new_position["assortment"] = {"meta": new_position["assortment"]}
            json_data["positions"].append(new_position)
    if qr_sum != Unset:
        json_data["qrSum"] = qr_sum
    if rate != Unset:
        json_data["rate"] = rate
    if retail_store != Unset:
        json_data["retailStore"] = {"meta": retail_store}
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if tax_system != Unset:
        json_data["taxSystem"] = tax_system
    if vat_enabled != Unset:
        json_data["vatEnabled"] = vat_enabled
    if vat_included != Unset:
        json_data["vatIncluded"] = vat_included
    return json_data


class GetPrepaymentReturnsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/prepaymentreturn",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[PrepaymentReturn]:
        return [PrepaymentReturn.from_json(x) for x in result["rows"]]


class CreatePrepaymentReturnRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        discount: typing.NotRequired[float]
        vat: typing.NotRequired[int]

    def __init__(
        self,
        retail_shift: types.Meta,
        prepayment: types.Meta,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        cash_sum: typing.Union[Unset, float] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        no_cash_sum: typing.Union[Unset, float] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        qr_sum: typing.Union[Unset, float] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.retail_shift = retail_shift
        self.prepayment = prepayment
        self.organization = organization
        self.agent = agent
        self.applicable = applicable
        self.attributes = attributes
        self.cash_sum = cash_sum
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.no_cash_sum = no_cash_sum
        self.owner = owner
        self.positions = positions
        self.qr_sum = qr_sum
        self.rate = rate
        self.retail_store = retail_store
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            retail_shift=self.retail_shift,
            prepayment=self.prepayment,
            agent=self.agent,
            applicable=self.applicable,
            attributes=self.attributes,
            cash_sum=self.cash_sum,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            no_cash_sum=self.no_cash_sum,
            owner=self.owner,
            positions=self.positions,
            qr_sum=self.qr_sum,
            rate=self.rate,
            retail_store=self.retail_store,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/prepaymentreturn",
            json=json_data,
        )

    def from_response(self, result: dict) -> PrepaymentReturn:
        return PrepaymentReturn.from_json(result)


class DeletePrepaymentReturnRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/prepaymentreturn/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetPrepaymentReturnRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/prepaymentreturn/{self.id}"
        )

    def from_response(self, result: dict) -> PrepaymentReturn:
        return PrepaymentReturn.from_json(result)


class UpdatePrepaymentReturnRequest(types.ApiRequest):
    UpdatePosition = CreatePrepaymentReturnRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        retail_shift: typing.Union[Unset, types.Meta] = Unset,
        prepayment: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        cash_sum: typing.Union[Unset, float] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        no_cash_sum: typing.Union[Unset, float] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        qr_sum: typing.Union[Unset, float] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.agent = agent
        self.retail_shift = retail_shift
        self.prepayment = prepayment
        self.applicable = applicable
        self.attributes = attributes
        self.cash_sum = cash_sum
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.no_cash_sum = no_cash_sum
        self.owner = owner
        self.positions = positions
        self.qr_sum = qr_sum
        self.rate = rate
        self.retail_store = retail_store
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            retail_shift=self.retail_shift,
            prepayment=self.prepayment,
            agent=self.agent,
            applicable=self.applicable,
            attributes=self.attributes,
            cash_sum=self.cash_sum,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            no_cash_sum=self.no_cash_sum,
            owner=self.owner,
            positions=self.positions,
            qr_sum=self.qr_sum,
            rate=self.rate,
            retail_store=self.retail_store,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/prepaymentreturn/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> PrepaymentReturn:
        return PrepaymentReturn.from_json(result)


class GetPrepaymentReturnPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        prepaymentreturn_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.prepaymentreturn_id = prepaymentreturn_id
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
            url=f"{helpers.BASE_URL}/entity/prepaymentreturn/{self.prepaymentreturn_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetPrepaymentReturnPositionRequest(types.ApiRequest):
    def __init__(self, prepaymentreturn_id: str, position_id: str):
        self.prepaymentreturn_id = prepaymentreturn_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/prepaymentreturn/{self.prepaymentreturn_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)

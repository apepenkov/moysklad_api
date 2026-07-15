import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class CommissionReportOut(types.MoySkladBaseClass):
    """Выданный отчет комиссионера (entity/commissionreportout)."""

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    agent_account: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    commission_period_end: typing.Optional[datetime.datetime]
    commission_period_start: typing.Optional[datetime.datetime]
    commitent_sum: typing.Optional[float]
    contract: typing.Optional[types.Meta]
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
    organization_account: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    payed_sum: typing.Optional[float]
    positions: typing.Optional[dict]
    printed: typing.Optional[bool]
    project: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    reward_percent: typing.Optional[int]
    reward_type: typing.Optional[str]
    shared: typing.Optional[bool]
    sales_channel: typing.Optional[types.Meta]
    state: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    vat_enabled: typing.Optional[bool]
    vat_included: typing.Optional[bool]
    vat_sum: typing.Optional[float]
    payments: typing.Optional[typing.List[types.Meta]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CommissionReportOut":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount"))
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.commission_period_end = helpers.parse_date(
            dict_data.get("commissionPeriodEnd")
        )
        instance.commission_period_start = helpers.parse_date(
            dict_data.get("commissionPeriodStart")
        )
        instance.commitent_sum = dict_data.get("commitentSum")
        instance.contract = helpers.get_meta(dict_data.get("contract"))
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
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.payed_sum = dict_data.get("payedSum")
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.reward_percent = dict_data.get("rewardPercent")
        instance.reward_type = dict_data.get("rewardType")
        instance.shared = dict_data.get("shared")
        instance.sales_channel = helpers.get_meta(dict_data.get("salesChannel"))
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        instance.payments = [
            helpers.get_meta(x, must=True) for x in dict_data.get("payments", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("commissionreportout",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    price: typing.Optional[float]
    quantity: typing.Optional[float]
    reward: typing.Optional[float]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.reward = dict_data.get("reward")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "commissionreportout", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    contract: typing.Union[Unset, types.Meta] = Unset,
    commission_period_start: typing.Union[Unset, datetime.datetime] = Unset,
    commission_period_end: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    agent_account: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    organization_account: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    reward_percent: typing.Union[Unset, int] = Unset,
    reward_type: typing.Union[Unset, str] = Unset,
    sales_channel: typing.Union[Unset, types.Meta] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
    vat_included: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
    if contract != Unset:
        json_data["contract"] = {"meta": contract}
    if commission_period_start != Unset:
        json_data["commissionPeriodStart"] = helpers.date_to_str(
            commission_period_start
        )
    if commission_period_end != Unset:
        json_data["commissionPeriodEnd"] = helpers.date_to_str(commission_period_end)
    if name != Unset:
        json_data["name"] = name
    if agent_account != Unset:
        json_data["agentAccount"] = {"meta": agent_account}
    if applicable != Unset:
        json_data["applicable"] = applicable
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
    if organization_account != Unset:
        json_data["organizationAccount"] = {"meta": organization_account}
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
    if reward_percent != Unset:
        json_data["rewardPercent"] = reward_percent
    if reward_type != Unset:
        json_data["rewardType"] = reward_type
    if sales_channel != Unset:
        json_data["salesChannel"] = {"meta": sales_channel}
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if vat_enabled != Unset:
        json_data["vatEnabled"] = vat_enabled
    if vat_included != Unset:
        json_data["vatIncluded"] = vat_included
    return json_data


class GetCommissionReportOutsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/commissionreportout",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[CommissionReportOut]:
        return [CommissionReportOut.from_json(x) for x in result["rows"]]


class CreateCommissionReportOutRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        reward: typing.NotRequired[float]
        vat: typing.NotRequired[int]
        vat_enabled: typing.NotRequired[bool]

    def __init__(
        self,
        agent: types.Meta,
        organization: types.Meta,
        contract: types.Meta,
        commission_period_start: datetime.datetime,
        commission_period_end: datetime.datetime,
        name: str,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        reward_percent: typing.Union[Unset, int] = Unset,
        reward_type: typing.Union[Unset, str] = Unset,
        sales_channel: typing.Union[Unset, types.Meta] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.agent = agent
        self.organization = organization
        self.contract = contract
        self.commission_period_start = commission_period_start
        self.commission_period_end = commission_period_end
        self.name = name
        self.agent_account = agent_account
        self.applicable = applicable
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.organization_account = organization_account
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.reward_percent = reward_percent
        self.reward_type = reward_type
        self.sales_channel = sales_channel
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            agent=self.agent,
            contract=self.contract,
            commission_period_start=self.commission_period_start,
            commission_period_end=self.commission_period_end,
            name=self.name,
            agent_account=self.agent_account,
            applicable=self.applicable,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            organization_account=self.organization_account,
            owner=self.owner,
            positions=self.positions,
            project=self.project,
            rate=self.rate,
            reward_percent=self.reward_percent,
            reward_type=self.reward_type,
            sales_channel=self.sales_channel,
            state=self.state,
            sync_id=self.sync_id,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/commissionreportout",
            json=json_data,
        )

    def from_response(self, result: dict) -> CommissionReportOut:
        return CommissionReportOut.from_json(result)


class DeleteCommissionReportOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetCommissionReportOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.id}",
        )

    def from_response(self, result: dict) -> CommissionReportOut:
        return CommissionReportOut.from_json(result)


class UpdateCommissionReportOutRequest(types.ApiRequest):
    UpdatePosition = CreateCommissionReportOutRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        commission_period_start: typing.Union[Unset, datetime.datetime] = Unset,
        commission_period_end: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        reward_percent: typing.Union[Unset, int] = Unset,
        reward_type: typing.Union[Unset, str] = Unset,
        sales_channel: typing.Union[Unset, types.Meta] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.agent = agent
        self.contract = contract
        self.commission_period_start = commission_period_start
        self.commission_period_end = commission_period_end
        self.name = name
        self.agent_account = agent_account
        self.applicable = applicable
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.organization_account = organization_account
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.reward_percent = reward_percent
        self.reward_type = reward_type
        self.sales_channel = sales_channel
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            agent=self.agent,
            contract=self.contract,
            commission_period_start=self.commission_period_start,
            commission_period_end=self.commission_period_end,
            name=self.name,
            agent_account=self.agent_account,
            applicable=self.applicable,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            organization_account=self.organization_account,
            owner=self.owner,
            positions=self.positions,
            project=self.project,
            rate=self.rate,
            reward_percent=self.reward_percent,
            reward_type=self.reward_type,
            sales_channel=self.sales_channel,
            state=self.state,
            sync_id=self.sync_id,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> CommissionReportOut:
        return CommissionReportOut.from_json(result)


class GetCommissionReportOutPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        commissionreportout_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.commissionreportout_id = commissionreportout_id
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
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.commissionreportout_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetCommissionReportOutPositionRequest(types.ApiRequest):
    def __init__(self, commissionreportout_id: str, position_id: str):
        self.commissionreportout_id = commissionreportout_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.commissionreportout_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class CreateCommissionReportOutPositionRequest(types.ApiRequest):
    def __init__(
        self,
        commissionreportout_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, float] = Unset,
        reward: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
    ):
        self.commissionreportout_id = commissionreportout_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.reward = reward
        self.vat = vat
        self.vat_enabled = vat_enabled

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.price != Unset:
            json_data["price"] = self.price
        if self.reward != Unset:
            json_data["reward"] = self.reward
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.commissionreportout_id}/positions",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class UpdateCommissionReportOutPositionRequest(types.ApiRequest):
    def __init__(
        self,
        commissionreportout_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        price: typing.Union[Unset, float] = Unset,
        reward: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
    ):
        self.commissionreportout_id = commissionreportout_id
        self.position_id = position_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.reward = reward
        self.vat = vat
        self.vat_enabled = vat_enabled

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.price != Unset:
            json_data["price"] = self.price
        if self.reward != Unset:
            json_data["reward"] = self.reward
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.commissionreportout_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeleteCommissionReportOutPositionRequest(types.ApiRequest):
    def __init__(self, commissionreportout_id: str, position_id: str):
        self.commissionreportout_id = commissionreportout_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/commissionreportout/{self.commissionreportout_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

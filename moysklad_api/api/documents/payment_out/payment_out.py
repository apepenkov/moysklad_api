import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class PaymentOut(types.MoySkladBaseClass):
    """Исходящий платеж (entity/paymentout). Плоский документ без позиций."""

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    agent_account: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    contract: typing.Optional[types.Meta]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    expense_item: typing.Optional[types.Meta]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    no_closing_docs: typing.Optional[bool]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    organization_account: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    payment_purpose: typing.Optional[str]
    printed: typing.Optional[bool]
    project: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    sales_channel: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    vat_sum: typing.Optional[float]
    facture_in: typing.Optional[types.Meta]
    operations: typing.Optional[typing.List[dict]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PaymentOut":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount"))
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.contract = helpers.get_meta(dict_data.get("contract"))
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.expense_item = helpers.get_meta(dict_data.get("expenseItem"))
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.no_closing_docs = dict_data.get("noClosingDocs")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.payment_purpose = dict_data.get("paymentPurpose")
        instance.printed = dict_data.get("printed")
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.sales_channel = helpers.get_meta(dict_data.get("salesChannel"))
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_sum = dict_data.get("vatSum")
        instance.facture_in = helpers.get_meta(dict_data.get("factureIn"))
        instance.operations = dict_data.get("operations")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("paymentout",)


def _build_paymentout_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    agent_account: typing.Union[Unset, types.Meta] = Unset,
    expense_item: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    contract: typing.Union[Unset, types.Meta] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    no_closing_docs: typing.Union[Unset, bool] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    organization_account: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    payment_purpose: typing.Union[Unset, str] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    sales_channel: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sum_: typing.Union[Unset, float] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    operations: typing.Union[Unset, typing.List[dict]] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
    if agent_account != Unset:
        json_data["agentAccount"] = {"meta": agent_account}
    if expense_item != Unset:
        json_data["expenseItem"] = {"meta": expense_item}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if code != Unset:
        json_data["code"] = code
    if contract != Unset:
        json_data["contract"] = {"meta": contract}
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if group != Unset:
        json_data["group"] = {"meta": group}
    if no_closing_docs != Unset:
        json_data["noClosingDocs"] = no_closing_docs
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if organization_account != Unset:
        json_data["organizationAccount"] = {"meta": organization_account}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if payment_purpose != Unset:
        json_data["paymentPurpose"] = payment_purpose
    if project != Unset:
        json_data["project"] = {"meta": project}
    if rate != Unset:
        json_data["rate"] = rate
    if sales_channel != Unset:
        json_data["salesChannel"] = {"meta": sales_channel}
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sum_ != Unset:
        json_data["sum"] = sum_
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if operations != Unset:
        json_data["operations"] = [{"meta": m} for m in operations]
    return json_data


class GetPaymentOutsRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/paymentout", params=params
        )

    def from_response(self, result: dict) -> typing.List[PaymentOut]:
        return [PaymentOut.from_json(x) for x in result["rows"]]


class CreatePaymentOutRequest(types.ApiRequest):
    def __init__(
        self,
        organization: types.Meta,
        agent: types.Meta,
        expense_item: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        no_closing_docs: typing.Union[Unset, bool] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payment_purpose: typing.Union[Unset, str] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sum_: typing.Union[Unset, float] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        operations: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    ):
        self.organization = organization
        self.agent = agent
        self.expense_item = expense_item
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.no_closing_docs = no_closing_docs
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.payment_purpose = payment_purpose
        self.project = project
        self.rate = rate
        self.sales_channel = sales_channel
        self.shared = shared
        self.state = state
        self.sum = sum_
        self.sync_id = sync_id
        self.operations = operations

    def to_request(self) -> RequestData:
        json_data = _build_paymentout_json(
            organization=self.organization,
            agent=self.agent,
            agent_account=self.agent_account,
            expense_item=self.expense_item,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            contract=self.contract,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            no_closing_docs=self.no_closing_docs,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            payment_purpose=self.payment_purpose,
            project=self.project,
            rate=self.rate,
            sales_channel=self.sales_channel,
            shared=self.shared,
            state=self.state,
            sum_=self.sum,
            sync_id=self.sync_id,
            operations=self.operations,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/paymentout", json=json_data
        )

    def from_response(self, result: dict) -> PaymentOut:
        return PaymentOut.from_json(result)


class DeletePaymentOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/paymentout/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetPaymentOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/paymentout/{self.id}"
        )

    def from_response(self, result: dict) -> PaymentOut:
        return PaymentOut.from_json(result)


class UpdatePaymentOutRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        expense_item: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        no_closing_docs: typing.Union[Unset, bool] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payment_purpose: typing.Union[Unset, str] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sum_: typing.Union[Unset, float] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        operations: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.agent = agent
        self.agent_account = agent_account
        self.expense_item = expense_item
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.no_closing_docs = no_closing_docs
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.payment_purpose = payment_purpose
        self.project = project
        self.rate = rate
        self.sales_channel = sales_channel
        self.shared = shared
        self.state = state
        self.sum = sum_
        self.sync_id = sync_id
        self.operations = operations

    def to_request(self) -> RequestData:
        json_data = _build_paymentout_json(
            organization=self.organization,
            agent=self.agent,
            agent_account=self.agent_account,
            expense_item=self.expense_item,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            contract=self.contract,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            no_closing_docs=self.no_closing_docs,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            payment_purpose=self.payment_purpose,
            project=self.project,
            rate=self.rate,
            sales_channel=self.sales_channel,
            shared=self.shared,
            state=self.state,
            sum_=self.sum,
            sync_id=self.sync_id,
            operations=self.operations,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/paymentout/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> PaymentOut:
        return PaymentOut.from_json(result)

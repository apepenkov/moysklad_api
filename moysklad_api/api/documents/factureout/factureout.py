import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class FactureOut(types.MoySkladBaseClass):
    """Счет-фактура выданный (entity/factureout). Без позиций."""

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
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
    owner: typing.Optional[types.Meta]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    state_contract_id: typing.Optional[str]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    advance_payment_vat: typing.Optional[int]
    payment_purpose: typing.Optional[str]
    vat_sum: typing.Optional[float]
    demands: typing.Optional[typing.List[types.Meta]]
    payments: typing.Optional[typing.List[types.Meta]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "FactureOut":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
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
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.state_contract_id = dict_data.get("stateContractId")
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.advance_payment_vat = dict_data.get("advancePaymentVat")
        instance.payment_purpose = dict_data.get("paymentPurpose")
        instance.vat_sum = dict_data.get("vatSum")
        instance.demands = [
            helpers.get_meta(x, must=True) for x in dict_data.get("demands", [])
        ]
        instance.payments = [
            helpers.get_meta(x, must=True) for x in dict_data.get("payments", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("factureout",)


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    contract: typing.Union[Unset, types.Meta] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    state_contract_id: typing.Union[Unset, str] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    advance_payment_vat: typing.Union[Unset, int] = Unset,
    payment_purpose: typing.Union[Unset, str] = Unset,
    demands: typing.Union[Unset, typing.List[types.Meta]] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
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
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if rate != Unset:
        json_data["rate"] = rate
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if state_contract_id != Unset:
        json_data["stateContractId"] = state_contract_id
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if advance_payment_vat != Unset:
        json_data["advancePaymentVat"] = advance_payment_vat
    if payment_purpose != Unset:
        json_data["paymentPurpose"] = payment_purpose
    if demands != Unset:
        json_data["demands"] = [{"meta": m} for m in demands]
    return json_data


class GetFactureOutsRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/factureout", params=params
        )

    def from_response(self, result: dict) -> typing.List[FactureOut]:
        return [FactureOut.from_json(x) for x in result["rows"]]


class CreateFactureOutRequest(types.ApiRequest):
    def __init__(
        self,
        organization: types.Meta,
        agent: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        state_contract_id: typing.Union[Unset, str] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        advance_payment_vat: typing.Union[Unset, int] = Unset,
        payment_purpose: typing.Union[Unset, str] = Unset,
        demands: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    ):
        self.organization = organization
        self.agent = agent
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.rate = rate
        self.shared = shared
        self.state = state
        self.state_contract_id = state_contract_id
        self.sync_id = sync_id
        self.advance_payment_vat = advance_payment_vat
        self.payment_purpose = payment_purpose
        self.demands = demands

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            agent=self.agent,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            contract=self.contract,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            rate=self.rate,
            shared=self.shared,
            state=self.state,
            state_contract_id=self.state_contract_id,
            sync_id=self.sync_id,
            advance_payment_vat=self.advance_payment_vat,
            payment_purpose=self.payment_purpose,
            demands=self.demands,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/factureout", json=json_data
        )

    def from_response(self, result: dict) -> FactureOut:
        return FactureOut.from_json(result)


class DeleteFactureOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/factureout/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetFactureOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/factureout/{self.id}"
        )

    def from_response(self, result: dict) -> FactureOut:
        return FactureOut.from_json(result)


class UpdateFactureOutRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        state_contract_id: typing.Union[Unset, str] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        advance_payment_vat: typing.Union[Unset, int] = Unset,
        payment_purpose: typing.Union[Unset, str] = Unset,
        demands: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.agent = agent
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.rate = rate
        self.shared = shared
        self.state = state
        self.state_contract_id = state_contract_id
        self.sync_id = sync_id
        self.advance_payment_vat = advance_payment_vat
        self.payment_purpose = payment_purpose
        self.demands = demands

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            agent=self.agent,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            contract=self.contract,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            rate=self.rate,
            shared=self.shared,
            state=self.state,
            state_contract_id=self.state_contract_id,
            sync_id=self.sync_id,
            advance_payment_vat=self.advance_payment_vat,
            payment_purpose=self.payment_purpose,
            demands=self.demands,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/factureout/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> FactureOut:
        return FactureOut.from_json(result)

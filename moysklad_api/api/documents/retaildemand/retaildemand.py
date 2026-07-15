import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class RetailDemand(types.MoySkladBaseClass):
    """Розничная продажа (entity/retaildemand)."""

    account_id: typing.Optional[str]
    advance_payment_sum: typing.Optional[float]
    agent: typing.Optional[types.Meta]
    agent_account: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    cash_sum: typing.Optional[float]
    check_number: typing.Optional[int]
    check_sum: typing.Optional[float]
    cheque: typing.Optional[dict]
    code: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    customer_order: typing.Optional[types.Meta]
    deleted: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    document_number: typing.Optional[int]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    gift_cards: typing.Optional[typing.List[dict]]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    no_cash_sum: typing.Optional[float]
    organization: typing.Optional[types.Meta]
    organization_account: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    payed_sum: typing.Optional[float]
    positions: typing.Optional[dict]
    prepayment_cash_sum: typing.Optional[float]
    prepayment_no_cash_sum: typing.Optional[float]
    prepayment_qr_sum: typing.Optional[float]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    qr_sum: typing.Optional[float]
    rate: typing.Optional[dict]
    retail_shift: typing.Optional[types.Meta]
    retail_store: typing.Optional[types.Meta]
    session_number: typing.Optional[int]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    tax_system: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    vat_enabled: typing.Optional[bool]
    vat_included: typing.Optional[bool]
    vat_sum: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "RetailDemand":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.advance_payment_sum = dict_data.get("advancePaymentSum")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount"))
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.cash_sum = dict_data.get("cashSum")
        instance.check_number = dict_data.get("checkNumber")
        instance.check_sum = dict_data.get("checkSum")
        instance.cheque = dict_data.get("cheque")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.customer_order = helpers.get_meta(dict_data.get("customerOrder"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.document_number = dict_data.get("documentNumber")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.gift_cards = dict_data.get("giftCards")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.no_cash_sum = dict_data.get("noCashSum")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.payed_sum = dict_data.get("payedSum")
        instance.positions = dict_data.get("positions")
        instance.prepayment_cash_sum = dict_data.get("prepaymentCashSum")
        instance.prepayment_no_cash_sum = dict_data.get("prepaymentNoCashSum")
        instance.prepayment_qr_sum = dict_data.get("prepaymentQrSum")
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.qr_sum = dict_data.get("qrSum")
        instance.rate = dict_data.get("rate")
        instance.retail_shift = helpers.get_meta(dict_data.get("retailShift"))
        instance.retail_store = helpers.get_meta(dict_data.get("retailStore"))
        instance.session_number = dict_data.get("sessionNumber")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
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
        return ("retaildemand",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    cost: typing.Optional[int]
    declaration: typing.Optional[typing.List[dict]]
    discount: typing.Optional[float]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    price: typing.Optional[float]
    quantity: typing.Optional[float]
    tracking_codes: typing.Optional[typing.List[dict]]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.cost = dict_data.get("cost")
        instance.declaration = dict_data.get("declaration")
        instance.discount = dict_data.get("discount")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.tracking_codes = dict_data.get("trackingCodes")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "retaildemand", "positions"


def _build_json(
    retail_shift: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    agent_account: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    cash_sum: typing.Union[Unset, float] = Unset,
    code: typing.Union[Unset, str] = Unset,
    customer_order: typing.Union[Unset, types.Meta] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    gift_cards: typing.Union[Unset, typing.List[dict]] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    no_cash_sum: typing.Union[Unset, float] = Unset,
    organization_account: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    prepayment_cash_sum: typing.Union[Unset, float] = Unset,
    prepayment_no_cash_sum: typing.Union[Unset, float] = Unset,
    prepayment_qr_sum: typing.Union[Unset, float] = Unset,
    qr_sum: typing.Union[Unset, float] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    tax_system: typing.Union[Unset, str] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
    vat_included: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if retail_shift != Unset:
        json_data["retailShift"] = {"meta": retail_shift}
    if store != Unset:
        json_data["store"] = {"meta": store}
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
    if agent_account != Unset:
        json_data["agentAccount"] = {"meta": agent_account}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if cash_sum != Unset:
        json_data["cashSum"] = cash_sum
    if code != Unset:
        json_data["code"] = code
    if customer_order != Unset:
        json_data["customerOrder"] = {"meta": customer_order}
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if gift_cards != Unset:
        json_data["giftCards"] = gift_cards
    if group != Unset:
        json_data["group"] = {"meta": group}
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if no_cash_sum != Unset:
        json_data["noCashSum"] = no_cash_sum
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
    if prepayment_cash_sum != Unset:
        json_data["prepaymentCashSum"] = prepayment_cash_sum
    if prepayment_no_cash_sum != Unset:
        json_data["prepaymentNoCashSum"] = prepayment_no_cash_sum
    if prepayment_qr_sum != Unset:
        json_data["prepaymentQrSum"] = prepayment_qr_sum
    if qr_sum != Unset:
        json_data["qrSum"] = qr_sum
    if rate != Unset:
        json_data["rate"] = rate
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


class GetRetailDemandsRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/retaildemand", params=params
        )

    def from_response(self, result: dict) -> typing.List[RetailDemand]:
        return [RetailDemand.from_json(x) for x in result["rows"]]


class CreateRetailDemandRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        discount: typing.NotRequired[float]
        vat: typing.NotRequired[int]

    def __init__(
        self,
        retail_shift: types.Meta,
        store: types.Meta,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        cash_sum: typing.Union[Unset, float] = Unset,
        code: typing.Union[Unset, str] = Unset,
        customer_order: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        gift_cards: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        no_cash_sum: typing.Union[Unset, float] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        prepayment_cash_sum: typing.Union[Unset, float] = Unset,
        prepayment_no_cash_sum: typing.Union[Unset, float] = Unset,
        prepayment_qr_sum: typing.Union[Unset, float] = Unset,
        qr_sum: typing.Union[Unset, float] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.retail_shift = retail_shift
        self.store = store
        self.agent = agent
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.cash_sum = cash_sum
        self.code = code
        self.customer_order = customer_order
        self.description = description
        self.external_code = external_code
        self.files = files
        self.gift_cards = gift_cards
        self.group = group
        self.moment = moment
        self.name = name
        self.no_cash_sum = no_cash_sum
        self.organization_account = organization_account
        self.owner = owner
        self.positions = positions
        self.prepayment_cash_sum = prepayment_cash_sum
        self.prepayment_no_cash_sum = prepayment_no_cash_sum
        self.prepayment_qr_sum = prepayment_qr_sum
        self.qr_sum = qr_sum
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            retail_shift=self.retail_shift,
            store=self.store,
            agent=self.agent,
            agent_account=self.agent_account,
            applicable=self.applicable,
            attributes=self.attributes,
            cash_sum=self.cash_sum,
            code=self.code,
            customer_order=self.customer_order,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            gift_cards=self.gift_cards,
            group=self.group,
            moment=self.moment,
            name=self.name,
            no_cash_sum=self.no_cash_sum,
            organization_account=self.organization_account,
            owner=self.owner,
            positions=self.positions,
            prepayment_cash_sum=self.prepayment_cash_sum,
            prepayment_no_cash_sum=self.prepayment_no_cash_sum,
            prepayment_qr_sum=self.prepayment_qr_sum,
            qr_sum=self.qr_sum,
            rate=self.rate,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/retaildemand", json=json_data
        )

    def from_response(self, result: dict) -> RetailDemand:
        return RetailDemand.from_json(result)


class DeleteRetailDemandRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/retaildemand/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetRetailDemandRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/retaildemand/{self.id}"
        )

    def from_response(self, result: dict) -> RetailDemand:
        return RetailDemand.from_json(result)


class UpdateRetailDemandRequest(types.ApiRequest):
    UpdatePosition = CreateRetailDemandRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        retail_shift: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        cash_sum: typing.Union[Unset, float] = Unset,
        code: typing.Union[Unset, str] = Unset,
        customer_order: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        gift_cards: typing.Union[Unset, typing.List[dict]] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        no_cash_sum: typing.Union[Unset, float] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        prepayment_cash_sum: typing.Union[Unset, float] = Unset,
        prepayment_no_cash_sum: typing.Union[Unset, float] = Unset,
        prepayment_qr_sum: typing.Union[Unset, float] = Unset,
        qr_sum: typing.Union[Unset, float] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.retail_shift = retail_shift
        self.store = store
        self.agent = agent
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.cash_sum = cash_sum
        self.code = code
        self.customer_order = customer_order
        self.description = description
        self.external_code = external_code
        self.files = files
        self.gift_cards = gift_cards
        self.group = group
        self.moment = moment
        self.name = name
        self.no_cash_sum = no_cash_sum
        self.organization_account = organization_account
        self.owner = owner
        self.positions = positions
        self.prepayment_cash_sum = prepayment_cash_sum
        self.prepayment_no_cash_sum = prepayment_no_cash_sum
        self.prepayment_qr_sum = prepayment_qr_sum
        self.qr_sum = qr_sum
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            retail_shift=self.retail_shift,
            store=self.store,
            agent=self.agent,
            agent_account=self.agent_account,
            applicable=self.applicable,
            attributes=self.attributes,
            cash_sum=self.cash_sum,
            code=self.code,
            customer_order=self.customer_order,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            gift_cards=self.gift_cards,
            group=self.group,
            moment=self.moment,
            name=self.name,
            no_cash_sum=self.no_cash_sum,
            organization_account=self.organization_account,
            owner=self.owner,
            positions=self.positions,
            prepayment_cash_sum=self.prepayment_cash_sum,
            prepayment_no_cash_sum=self.prepayment_no_cash_sum,
            prepayment_qr_sum=self.prepayment_qr_sum,
            qr_sum=self.qr_sum,
            rate=self.rate,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/retaildemand/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetailDemand:
        return RetailDemand.from_json(result)


class GetRetailDemandPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        retaildemand_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.retaildemand_id = retaildemand_id
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
            url=f"{helpers.BASE_URL}/entity/retaildemand/{self.retaildemand_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetRetailDemandPositionRequest(types.ApiRequest):
    def __init__(self, retaildemand_id: str, position_id: str):
        self.retaildemand_id = retaildemand_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/retaildemand/{self.retaildemand_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)

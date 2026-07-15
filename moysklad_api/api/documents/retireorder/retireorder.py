import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

RetireOrderType = typing.Literal[
    "SALE", "DAMAGE", "EXPORT", "GIVEN_FOR_FREE", "DISPOSE", "OTHER", "LOST",
    "INSUFFICIENCY", "CONFISCATE", "DESTROY", "RETURN_TO_SUPPLIER", "RECYCLE",
]
TrackingType = typing.Literal[
    "ELECTRONICS", "LP_CLOTHES", "LP_LINENS", "MILK", "NCP", "NOT_TRACKED",
    "OTP", "PERFUMERY", "SHOES", "TIRES", "TOBACCO", "WATER",
]


class RetireOrder(types.MoySkladBaseClass):
    """Вывод кодов маркировки из оборота (entity/retireorder)."""

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    destination_country: typing.Optional[types.Meta]
    document_state: typing.Optional[str]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    positions: typing.Optional[dict]
    primary_document_name: typing.Optional[str]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    reason_description: typing.Optional[str]
    retire_order_type: typing.Optional[RetireOrderType]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    state_contract_id: typing.Optional[str]
    supporting_transaction: typing.Optional[str]
    supporting_transaction_date: typing.Optional[datetime.datetime]
    supporting_transaction_number: typing.Optional[str]
    sync_id: typing.Optional[str]
    tracking_type: typing.Optional[TrackingType]
    updated: typing.Optional[datetime.datetime]
    sum: typing.Optional[float]
    vat_enabled: typing.Optional[bool]
    vat_included: typing.Optional[bool]
    vat_sum: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "RetireOrder":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.destination_country = helpers.get_meta(
            dict_data.get("destinationCountry")
        )
        instance.document_state = dict_data.get("documentState")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.primary_document_name = dict_data.get("primaryDocumentName")
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.reason_description = dict_data.get("reasonDescription")
        instance.retire_order_type = dict_data.get("retireOrderType")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.state_contract_id = dict_data.get("stateContractId")
        instance.supporting_transaction = dict_data.get("supportingTransaction")
        instance.supporting_transaction_date = helpers.parse_date(
            dict_data.get("supportingTransactionDate")
        )
        instance.supporting_transaction_number = dict_data.get(
            "supportingTransactionNumber"
        )
        instance.sync_id = dict_data.get("syncId")
        instance.tracking_type = dict_data.get("trackingType")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.sum = dict_data.get("sum")
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("retireorder",)


class Position(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
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
        instance.id = dict_data.get("id")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.tracking_codes = dict_data.get("trackingCodes")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "retireorder", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    retire_order_type: typing.Union[Unset, RetireOrderType] = Unset,
    tracking_type: typing.Union[Unset, TrackingType] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    description: typing.Union[Unset, str] = Unset,
    destination_country: typing.Union[Unset, types.Meta] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    primary_document_name: typing.Union[Unset, str] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    reason_description: typing.Union[Unset, str] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    state_contract_id: typing.Union[Unset, str] = Unset,
    supporting_transaction: typing.Union[Unset, str] = Unset,
    supporting_transaction_date: typing.Union[Unset, datetime.datetime] = Unset,
    supporting_transaction_number: typing.Union[Unset, str] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
    vat_included: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if retire_order_type != Unset:
        json_data["retireOrderType"] = retire_order_type
    if tracking_type != Unset:
        json_data["trackingType"] = tracking_type
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
    if description != Unset:
        json_data["description"] = description
    if destination_country != Unset:
        json_data["destinationCountry"] = {"meta": destination_country}
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
    if primary_document_name != Unset:
        json_data["primaryDocumentName"] = primary_document_name
    if rate != Unset:
        json_data["rate"] = rate
    if reason_description != Unset:
        json_data["reasonDescription"] = reason_description
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if state_contract_id != Unset:
        json_data["stateContractId"] = state_contract_id
    if supporting_transaction != Unset:
        json_data["supportingTransaction"] = supporting_transaction
    if supporting_transaction_date != Unset:
        json_data["supportingTransactionDate"] = helpers.date_to_str(
            supporting_transaction_date
        )
    if supporting_transaction_number != Unset:
        json_data["supportingTransactionNumber"] = supporting_transaction_number
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if vat_enabled != Unset:
        json_data["vatEnabled"] = vat_enabled
    if vat_included != Unset:
        json_data["vatIncluded"] = vat_included
    return json_data


class GetRetireOrdersRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/retireorder", params=params
        )

    def from_response(self, result: dict) -> typing.List[RetireOrder]:
        return [RetireOrder.from_json(x) for x in result["rows"]]


class CreateRetireOrderRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        tracking_codes: typing.List[dict]
        price: typing.NotRequired[float]
        vat: typing.NotRequired[int]

    def __init__(
        self,
        organization: types.Meta,
        retire_order_type: RetireOrderType,
        tracking_type: TrackingType,
        agent: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        destination_country: typing.Union[Unset, types.Meta] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        primary_document_name: typing.Union[Unset, str] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        reason_description: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.organization = organization
        self.retire_order_type = retire_order_type
        self.tracking_type = tracking_type
        self.agent = agent
        self.description = description
        self.destination_country = destination_country
        self.external_code = external_code
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.primary_document_name = primary_document_name
        self.rate = rate
        self.reason_description = reason_description
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            retire_order_type=self.retire_order_type,
            tracking_type=self.tracking_type,
            agent=self.agent,
            description=self.description,
            destination_country=self.destination_country,
            external_code=self.external_code,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            primary_document_name=self.primary_document_name,
            rate=self.rate,
            reason_description=self.reason_description,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/retireorder", json=json_data
        )

    def from_response(self, result: dict) -> RetireOrder:
        return RetireOrder.from_json(result)


class DeleteRetireOrderRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/retireorder/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetRetireOrderRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/retireorder/{self.id}"
        )

    def from_response(self, result: dict) -> RetireOrder:
        return RetireOrder.from_json(result)


class UpdateRetireOrderRequest(types.ApiRequest):
    UpdatePosition = CreateRetireOrderRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        retire_order_type: typing.Union[Unset, RetireOrderType] = Unset,
        tracking_type: typing.Union[Unset, TrackingType] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        destination_country: typing.Union[Unset, types.Meta] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        primary_document_name: typing.Union[Unset, str] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        reason_description: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.retire_order_type = retire_order_type
        self.tracking_type = tracking_type
        self.agent = agent
        self.description = description
        self.destination_country = destination_country
        self.external_code = external_code
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.primary_document_name = primary_document_name
        self.rate = rate
        self.reason_description = reason_description
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            retire_order_type=self.retire_order_type,
            tracking_type=self.tracking_type,
            agent=self.agent,
            description=self.description,
            destination_country=self.destination_country,
            external_code=self.external_code,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            primary_document_name=self.primary_document_name,
            rate=self.rate,
            reason_description=self.reason_description,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/retireorder/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetireOrder:
        return RetireOrder.from_json(result)


class GetRetireOrderPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        retireorder_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.retireorder_id = retireorder_id
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
            url=f"{helpers.BASE_URL}/entity/retireorder/{self.retireorder_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetRetireOrderPositionRequest(types.ApiRequest):
    def __init__(self, retireorder_id: str, position_id: str):
        self.retireorder_id = retireorder_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/retireorder/{self.retireorder_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)

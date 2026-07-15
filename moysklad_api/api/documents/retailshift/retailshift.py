import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class RetailShift(types.MoySkladBaseClass):
    """Розничная смена (entity/retailshift)."""

    account_id: typing.Optional[str]
    acquire: typing.Optional[types.Meta]
    agent_account: typing.Optional[types.Meta]
    attributes: typing.Optional[typing.List[dict]]
    bank_comission: typing.Optional[float]
    bank_percent: typing.Optional[float]
    cheque: typing.Optional[dict]
    close_date: typing.Optional[datetime.datetime]
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
    operations: typing.Optional[typing.List[dict]]
    organization: typing.Optional[types.Meta]
    organization_account: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    payment_operations: typing.Optional[typing.List[dict]]
    printed: typing.Optional[bool]
    proceeds_cash: typing.Optional[float]
    proceeds_no_cash: typing.Optional[float]
    published: typing.Optional[bool]
    qr_acquire: typing.Optional[types.Meta]
    qr_bank_comission: typing.Optional[float]
    qr_bank_percent: typing.Optional[float]
    received_cash: typing.Optional[float]
    received_no_cash: typing.Optional[float]
    retail_store: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    store: typing.Optional[types.Meta]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    vat_enabled: typing.Optional[bool]
    vat_included: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "RetailShift":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.acquire = helpers.get_meta(dict_data.get("acquire"))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount"))
        instance.attributes = dict_data.get("attributes")
        instance.bank_comission = dict_data.get("bankComission")
        instance.bank_percent = dict_data.get("bankPercent")
        instance.cheque = dict_data.get("cheque")
        instance.close_date = helpers.parse_date(dict_data.get("closeDate"))
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
        instance.operations = dict_data.get("operations")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.payment_operations = dict_data.get("paymentOperations")
        instance.printed = dict_data.get("printed")
        instance.proceeds_cash = dict_data.get("proceedsCash")
        instance.proceeds_no_cash = dict_data.get("proceedsNoCash")
        instance.published = dict_data.get("published")
        instance.qr_acquire = helpers.get_meta(dict_data.get("qrAcquire"))
        instance.qr_bank_comission = dict_data.get("qrBankComission")
        instance.qr_bank_percent = dict_data.get("qrBankPercent")
        instance.received_cash = dict_data.get("receivedCash")
        instance.received_no_cash = dict_data.get("receivedNoCash")
        instance.retail_store = helpers.get_meta(dict_data.get("retailStore"))
        instance.shared = dict_data.get("shared")
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("retailshift",)


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    retail_store: typing.Union[Unset, types.Meta] = Unset,
    acquire: typing.Union[Unset, types.Meta] = Unset,
    qr_acquire: typing.Union[Unset, types.Meta] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    bank_comission: typing.Union[Unset, float] = Unset,
    bank_percent: typing.Union[Unset, float] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    organization_account: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    qr_bank_comission: typing.Union[Unset, float] = Unset,
    qr_bank_percent: typing.Union[Unset, float] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if retail_store != Unset:
        json_data["retailStore"] = {"meta": retail_store}
    if acquire != Unset:
        json_data["acquire"] = {"meta": acquire}
    if qr_acquire != Unset:
        json_data["qrAcquire"] = {"meta": qr_acquire}
    if attributes != Unset:
        json_data["attributes"] = attributes
    if bank_comission != Unset:
        json_data["bankComission"] = bank_comission
    if bank_percent != Unset:
        json_data["bankPercent"] = bank_percent
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
    if organization_account != Unset:
        json_data["organizationAccount"] = {"meta": organization_account}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if qr_bank_comission != Unset:
        json_data["qrBankComission"] = qr_bank_comission
    if qr_bank_percent != Unset:
        json_data["qrBankPercent"] = qr_bank_percent
    if shared != Unset:
        json_data["shared"] = shared
    if store != Unset:
        json_data["store"] = {"meta": store}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetRetailShiftsRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/retailshift", params=params
        )

    def from_response(self, result: dict) -> typing.List[RetailShift]:
        return [RetailShift.from_json(x) for x in result["rows"]]


class CreateRetailShiftRequest(types.ApiRequest):
    def __init__(
        self,
        organization: types.Meta,
        retail_store: types.Meta,
        acquire: typing.Union[Unset, types.Meta] = Unset,
        qr_acquire: typing.Union[Unset, types.Meta] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        bank_comission: typing.Union[Unset, float] = Unset,
        bank_percent: typing.Union[Unset, float] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        qr_bank_comission: typing.Union[Unset, float] = Unset,
        qr_bank_percent: typing.Union[Unset, float] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.retail_store = retail_store
        self.acquire = acquire
        self.qr_acquire = qr_acquire
        self.attributes = attributes
        self.bank_comission = bank_comission
        self.bank_percent = bank_percent
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.qr_bank_comission = qr_bank_comission
        self.qr_bank_percent = qr_bank_percent
        self.shared = shared
        self.store = store
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            retail_store=self.retail_store,
            acquire=self.acquire,
            qr_acquire=self.qr_acquire,
            attributes=self.attributes,
            bank_comission=self.bank_comission,
            bank_percent=self.bank_percent,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            qr_bank_comission=self.qr_bank_comission,
            qr_bank_percent=self.qr_bank_percent,
            shared=self.shared,
            store=self.store,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/retailshift", json=json_data
        )

    def from_response(self, result: dict) -> RetailShift:
        return RetailShift.from_json(result)


class DeleteRetailShiftRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/retailshift/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetRetailShiftRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/retailshift/{self.id}"
        )

    def from_response(self, result: dict) -> RetailShift:
        return RetailShift.from_json(result)


class UpdateRetailShiftRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        acquire: typing.Union[Unset, types.Meta] = Unset,
        qr_acquire: typing.Union[Unset, types.Meta] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        bank_comission: typing.Union[Unset, float] = Unset,
        bank_percent: typing.Union[Unset, float] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        qr_bank_comission: typing.Union[Unset, float] = Unset,
        qr_bank_percent: typing.Union[Unset, float] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.retail_store = retail_store
        self.acquire = acquire
        self.qr_acquire = qr_acquire
        self.attributes = attributes
        self.bank_comission = bank_comission
        self.bank_percent = bank_percent
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.qr_bank_comission = qr_bank_comission
        self.qr_bank_percent = qr_bank_percent
        self.shared = shared
        self.store = store
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            retail_store=self.retail_store,
            acquire=self.acquire,
            qr_acquire=self.qr_acquire,
            attributes=self.attributes,
            bank_comission=self.bank_comission,
            bank_percent=self.bank_percent,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            qr_bank_comission=self.qr_bank_comission,
            qr_bank_percent=self.qr_bank_percent,
            shared=self.shared,
            store=self.store,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/retailshift/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetailShift:
        return RetailShift.from_json(result)

import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class RetailDrawerCashOut(types.MoySkladBaseClass):
    """Выплата денег (entity/retaildrawercashout). Плоский документ без позиций."""

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
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
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    retail_shift: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "RetailDrawerCashOut":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.applicable = dict_data.get("applicable")
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
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.retail_shift = helpers.get_meta(dict_data.get("retailShift"))
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("retaildrawercashout",)


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    agent: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    retail_shift: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sum_: typing.Union[Unset, float] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
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
    if retail_shift != Unset:
        json_data["retailShift"] = {"meta": retail_shift}
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sum_ != Unset:
        json_data["sum"] = sum_
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetRetailDrawerCashOutsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/retaildrawercashout",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[RetailDrawerCashOut]:
        return [RetailDrawerCashOut.from_json(x) for x in result["rows"]]


class CreateRetailDrawerCashOutRequest(types.ApiRequest):
    def __init__(
        self,
        organization: types.Meta,
        agent: types.Meta,
        retail_shift: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
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
        sum_: typing.Union[Unset, float] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.agent = agent
        self.retail_shift = retail_shift
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
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
        self.sum = sum_
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            agent=self.agent,
            retail_shift=self.retail_shift,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
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
            sum_=self.sum,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/retaildrawercashout",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetailDrawerCashOut:
        return RetailDrawerCashOut.from_json(result)


class DeleteRetailDrawerCashOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/retaildrawercashout/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetRetailDrawerCashOutRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/retaildrawercashout/{self.id}",
        )

    def from_response(self, result: dict) -> RetailDrawerCashOut:
        return RetailDrawerCashOut.from_json(result)


class UpdateRetailDrawerCashOutRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        retail_shift: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
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
        sum_: typing.Union[Unset, float] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.agent = agent
        self.retail_shift = retail_shift
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
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
        self.sum = sum_
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            agent=self.agent,
            retail_shift=self.retail_shift,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
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
            sum_=self.sum,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/retaildrawercashout/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetailDrawerCashOut:
        return RetailDrawerCashOut.from_json(result)

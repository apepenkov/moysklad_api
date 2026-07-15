import datetime
import typing

from ... import types, helpers
from ...types import Unset, RequestData


class AuditContext(types.MoySkladBaseClass):
    """Контекст аудита (audit/{id})."""

    entity_type: typing.Optional[str]
    event_type: typing.Optional[str]
    events: typing.Optional[typing.List[dict]]
    id: typing.Optional[str]
    info: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    object_count: typing.Optional[int]
    object_type: typing.Optional[str]
    source: typing.Optional[str]
    support_access: typing.Optional[bool]
    uid: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "AuditContext":
        instance = cls()
        instance.entity_type = dict_data.get("entityType")
        instance.event_type = dict_data.get("eventType")
        instance.events = dict_data.get("events")
        instance.id = dict_data.get("id")
        instance.info = dict_data.get("info")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.object_count = dict_data.get("objectCount")
        instance.object_type = dict_data.get("objectType")
        instance.source = dict_data.get("source")
        instance.support_access = dict_data.get("supportAccess")
        instance.uid = dict_data.get("uid")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("audit",)


class AuditEvent(types.MoySkladBaseClass):
    """Событие аудита (audit/{id}/events, entity/{type}/{id}/audit)."""

    additional_info: typing.Optional[str]
    audit: typing.Optional[types.Meta]
    diff: typing.Optional[dict]
    entity: typing.Optional[types.Meta]
    entity_type: typing.Optional[str]
    event_type: typing.Optional[str]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    object_count: typing.Optional[int]
    object_type: typing.Optional[str]
    source: typing.Optional[str]
    support_access: typing.Optional[bool]
    uid: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "AuditEvent":
        instance = cls()
        instance.additional_info = dict_data.get("additionalInfo")
        instance.audit = helpers.get_meta(dict_data.get("audit"))
        instance.diff = dict_data.get("diff")
        instance.entity = helpers.get_meta(dict_data.get("entity"))
        instance.entity_type = dict_data.get("entityType")
        instance.event_type = dict_data.get("eventType")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.object_count = dict_data.get("objectCount")
        instance.object_type = dict_data.get("objectType")
        instance.source = dict_data.get("source")
        instance.support_access = dict_data.get("supportAccess")
        instance.uid = dict_data.get("uid")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class AuditFilters(types.MoySkladBaseClass):
    event_type: typing.Optional[typing.List[str]]
    source: typing.Optional[typing.List[str]]
    entity_type: typing.Optional[typing.List[str]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "AuditFilters":
        instance = cls()
        instance.event_type = dict_data.get("eventType")
        instance.source = dict_data.get("source")
        instance.entity_type = dict_data.get("entitytype")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetAuditContextsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        filter_: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.filter = filter_

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.filter != Unset:
            params["filter"] = self.filter
        return RequestData(method="GET", url=f"{helpers.BASE_URL}/audit", params=params)

    def from_response(self, result: dict) -> typing.List[AuditContext]:
        return [AuditContext.from_json(x) for x in result["rows"]]


class GetAuditEventsByContextRequest(types.ApiRequest):
    def __init__(
        self,
        audit_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.audit_id = audit_id
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
            url=f"{helpers.BASE_URL}/audit/{self.audit_id}/events",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[AuditEvent]:
        return [AuditEvent.from_json(x) for x in result["rows"]]


class GetAuditEventsByEntityRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
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
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/audit",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[AuditEvent]:
        return [AuditEvent.from_json(x) for x in result["rows"]]


class GetAuditFiltersRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/audit/metadata/filters"
        )

    def from_response(self, result: dict) -> AuditFilters:
        return AuditFilters.from_json(result)

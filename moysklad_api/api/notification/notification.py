import datetime
import typing

from ... import types, helpers
from ...types import Unset, RequestData


class Notification(types.MoySkladBaseClass):
    """Уведомление (notification/{id}).

    Уведомления полиморфны: конкретный подтип (NotificationTaskAssigned,
    NotificationGoodCountTooLow, NotificationImportCompleted, и т.д.) указан в
    meta.type, а специфичные для подтипа поля доступны через `extra`.
    """

    account_id: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    read: typing.Optional[bool]
    title: typing.Optional[str]
    extra: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Notification":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.read = dict_data.get("read")
        instance.title = dict_data.get("title")
        known_fields = {
            "accountId",
            "created",
            "description",
            "id",
            "meta",
            "read",
            "title",
        }
        instance.extra = {
            k: v for k, v in dict_data.items() if k not in known_fields
        }
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("notification",)


class NotificationChannelsEnabled(typing.TypedDict):
    email: typing.NotRequired[bool]
    push: typing.NotRequired[bool]
    interface: typing.NotRequired[bool]


class NotificationGroupSettings(typing.TypedDict):
    enabled: typing.NotRequired[bool]
    channelsEnabled: typing.NotRequired[NotificationChannelsEnabled]


class NotificationSettings(types.MoySkladBaseClass):
    customer_order: typing.Optional[dict]
    data_exchange: typing.Optional[dict]
    invoice: typing.Optional[dict]
    retail: typing.Optional[dict]
    scripts: typing.Optional[dict]
    stock: typing.Optional[dict]
    task: typing.Optional[dict]
    mentions: typing.Optional[dict]
    online_stores: typing.Optional[dict]
    followed_events: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "NotificationSettings":
        instance = cls()
        instance.customer_order = dict_data.get("customerOrder")
        instance.data_exchange = dict_data.get("dataExchange")
        instance.invoice = dict_data.get("invoice")
        instance.retail = dict_data.get("retail")
        instance.scripts = dict_data.get("scripts")
        instance.stock = dict_data.get("stock")
        instance.task = dict_data.get("task")
        instance.mentions = dict_data.get("mentions")
        instance.online_stores = dict_data.get("onlineStores")
        instance.followed_events = dict_data.get("followedEvents")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetNotificationsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/notification", params=params
        )

    def from_response(self, result: dict) -> typing.List[Notification]:
        return [Notification.from_json(x) for x in result["rows"]]


class GetNotificationRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/notification/{self.id}"
        )

    def from_response(self, result: dict) -> Notification:
        return Notification.from_json(result)


class DeleteNotificationRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/notification/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class MarkNotificationAsReadRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/notification/{self.id}/markasread",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class MarkAllNotificationsAsReadRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/notification/markasreadall",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetNotificationSettingsRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/notification/settings"
        )

    def from_response(self, result: dict) -> NotificationSettings:
        return NotificationSettings.from_json(result)


class UpdateNotificationSettingsRequest(types.ApiRequest):
    def __init__(
        self,
        customer_order: typing.Union[Unset, NotificationGroupSettings] = Unset,
        data_exchange: typing.Union[Unset, NotificationGroupSettings] = Unset,
        invoice: typing.Union[Unset, NotificationGroupSettings] = Unset,
        retail: typing.Union[Unset, NotificationGroupSettings] = Unset,
        scripts: typing.Union[Unset, NotificationGroupSettings] = Unset,
        stock: typing.Union[Unset, NotificationGroupSettings] = Unset,
        task: typing.Union[Unset, NotificationGroupSettings] = Unset,
        mentions: typing.Union[Unset, NotificationGroupSettings] = Unset,
        online_stores: typing.Union[Unset, NotificationGroupSettings] = Unset,
        followed_events: typing.Union[Unset, NotificationGroupSettings] = Unset,
    ):
        self.customer_order = customer_order
        self.data_exchange = data_exchange
        self.invoice = invoice
        self.retail = retail
        self.scripts = scripts
        self.stock = stock
        self.task = task
        self.mentions = mentions
        self.online_stores = online_stores
        self.followed_events = followed_events

    def to_request(self) -> RequestData:
        json_data = {}
        if self.customer_order != Unset:
            json_data["customerOrder"] = self.customer_order
        if self.data_exchange != Unset:
            json_data["dataExchange"] = self.data_exchange
        if self.invoice != Unset:
            json_data["invoice"] = self.invoice
        if self.retail != Unset:
            json_data["retail"] = self.retail
        if self.scripts != Unset:
            json_data["scripts"] = self.scripts
        if self.stock != Unset:
            json_data["stock"] = self.stock
        if self.task != Unset:
            json_data["task"] = self.task
        if self.mentions != Unset:
            json_data["mentions"] = self.mentions
        if self.online_stores != Unset:
            json_data["onlineStores"] = self.online_stores
        if self.followed_events != Unset:
            json_data["followedEvents"] = self.followed_events
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/notification/settings",
            json=json_data,
        )

    def from_response(self, result: dict) -> NotificationSettings:
        return NotificationSettings.from_json(result)

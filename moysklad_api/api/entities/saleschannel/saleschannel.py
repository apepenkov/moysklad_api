import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

SalesChannelType = typing.Literal[
    "MESSENGER",
    "SOCIAL_NETWORK",
    "MARKETPLACE",
    "ECOMMERCE",
    "CLASSIFIED_ADS",
    "DIRECT_SALES",
    "RETAIL_SALES",
    "OTHER",
]


class SalesChannel(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived     | Boolean     | Добавлен ли Канал продаж в архив. Обязательное при ответе
    code         | String(255) | Код Канала продаж
    description  | String(4096)| Описание Канала продаж
    externalCode | String(255) | Внешний код Канала продаж. Обязательное при ответе
    group        | Meta        | Метаданные отдела сотрудника. Обязательное при ответе, Expand
    id           | UUID        | ID Канала продаж. Обязательное при ответе, Только для чтения
    meta         | Meta        | Метаданные Канала продаж. Обязательное при ответе
    name         | String(255) | Наименование Канала продаж. Обязательное при ответе, Необходимо при создании
    owner        | Meta        | Метаданные владельца. Expand
    shared       | Boolean     | Общий доступ. Обязательное при ответе
    type         | Enum        | Тип Канала продаж. Обязательное при ответе, Необходимо при создании
    updated      | DateTime    | Момент последнего обновления сущности. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    code: typing.Optional[str]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    type: typing.Optional[SalesChannelType]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "SalesChannel":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.shared = dict_data.get("shared")
        instance.type = dict_data.get("type")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("saleschannel",)


class GetSalesChannelsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/saleschannel",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[SalesChannel]:
        return [SalesChannel.from_json(x) for x in result["rows"]]


class CreateSalesChannelRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        type_: SalesChannelType,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.name = name
        self.type = type_
        self.code = code
        self.description = description
        self.external_code = external_code
        self.archived = archived
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {"name": self.name, "type": self.type}
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/saleschannel",
            json=json_data,
        )

    def from_response(self, result: dict) -> SalesChannel:
        return SalesChannel.from_json(result)


class DeleteSalesChannelRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/saleschannel/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetSalesChannelRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/saleschannel/{self.id}",
        )

    def from_response(self, result: dict) -> SalesChannel:
        return SalesChannel.from_json(result)


class UpdateSalesChannelRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        type_: typing.Union[Unset, SalesChannelType] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.name = name
        self.type = type_
        self.code = code
        self.description = description
        self.external_code = external_code
        self.archived = archived
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.type != Unset:
            json_data["type"] = self.type
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/saleschannel/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> SalesChannel:
        return SalesChannel.from_json(result)

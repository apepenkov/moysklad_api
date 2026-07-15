import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Group(types.MoySkladBaseClass):
    """
    accountId | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    id        | UUID        | ID отдела. Обязательное при ответе, Только для чтения
    index     | Int         | Порядковый номер в списке отделов
    meta      | Meta        | Метаданные Отдела. Обязательное при ответе
    name      | String(255) | Наименование Отдела. Обязательное при ответе
    """

    account_id: typing.Optional[str]
    id: typing.Optional[str]
    index: typing.Optional[int]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Group":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.id = dict_data.get("id")
        instance.index = dict_data.get("index")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("group",)


class GetGroupsRequest(types.ApiRequest):
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
            method="GET",
            url=f"{helpers.BASE_URL}/entity/group",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Group]:
        return [Group.from_json(x) for x in result["rows"]]


class CreateGroupRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        index: typing.Union[Unset, int] = Unset,
    ):
        self.name = name
        self.index = index

    def to_request(self) -> RequestData:
        json_data = {"name": self.name}
        if self.index != Unset:
            json_data["index"] = self.index
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/group",
            json=json_data,
        )

    def from_response(self, result: dict) -> Group:
        return Group.from_json(result)


class DeleteGroupRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/group/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetGroupRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/group/{self.id}",
        )

    def from_response(self, result: dict) -> Group:
        return Group.from_json(result)


class UpdateGroupRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        index: typing.Union[Unset, int] = Unset,
    ):
        self.id = id_
        self.name = name
        self.index = index

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.index != Unset:
            json_data["index"] = self.index
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/group/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Group:
        return Group.from_json(result)

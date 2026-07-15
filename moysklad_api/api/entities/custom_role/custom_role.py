# Пользовательские роли (entity/role). permissions - большой объект с
# разрешениями по каждому типу документа/операции, передается как raw dict.
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class CustomRole(types.MoySkladBaseClass):
    """
    id          | UUID          | ID пользовательской роли. Обязательное при ответе, Только для чтения
    meta        | Meta          | Метаданные пользовательской роли. Обязательное при ответе
    name        | String(255)   | Наименование пользовательской роли. Обязательное при ответе, Необходимо при создании
    permissions | Object        | Список пермиссий. Обязательное при ответе
    """

    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    permissions: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CustomRole":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.permissions = dict_data.get("permissions")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("role",)


class GetCustomRolesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/role",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[CustomRole]:
        return [CustomRole.from_json(x) for x in result["rows"]]


class CreateCustomRoleRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        permissions: typing.Union[Unset, dict] = Unset,
    ):
        self.name = name
        self.permissions = permissions

    def to_request(self) -> RequestData:
        json_data = {"name": self.name}
        if self.permissions != Unset:
            json_data["permissions"] = self.permissions
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/role",
            json=json_data,
        )

    def from_response(self, result: dict) -> CustomRole:
        return CustomRole.from_json(result)


class DeleteCustomRoleRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/role/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetCustomRoleRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/role/{self.id}",
        )

    def from_response(self, result: dict) -> CustomRole:
        return CustomRole.from_json(result)


class UpdateCustomRoleRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        permissions: typing.Union[Unset, dict] = Unset,
    ):
        self.id = id_
        self.name = name
        self.permissions = permissions

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.permissions != Unset:
            json_data["permissions"] = self.permissions
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/role/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> CustomRole:
        return CustomRole.from_json(result)

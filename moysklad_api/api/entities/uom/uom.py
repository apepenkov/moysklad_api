import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Uom(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    code         | String(255) | Код Единицы измерения
    description  | String(4096)| Описание Единицы измерения
    externalCode | String(255) | Внешний код Единицы измерения. Обязательное при ответе
    group        | Meta        | Отдел сотрудника (для пользовательских ед. измерений)
    id           | UUID        | ID Единицы измерения. Обязательное при ответе, Только для чтения
    meta         | Meta        | Метаданные Единицы измерения. Обязательное при ответе
    name         | String(255) | Наименование Единицы измерения. Обязательное при ответе, Необходимо при создании
    owner        | Meta        | Владелец (Сотрудник) (для пользовательских ед. измерений)
    shared       | Boolean     | Общий доступ (для пользовательских ед. измерений)
    updated      | DateTime    | Момент последнего обновления Единицы измерения. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    code: typing.Optional[str]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Uom":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.shared = dict_data.get("shared")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("uom",)


class GetUomsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/uom",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Uom]:
        return [Uom.from_json(x) for x in result["rows"]]


class CreateUomRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {"name": self.name}
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/uom",
            json=json_data,
        )

    def from_response(self, result: dict) -> Uom:
        return Uom.from_json(result)


class DeleteUomRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/uom/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetUomRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/uom/{self.id}",
        )

    def from_response(self, result: dict) -> Uom:
        return Uom.from_json(result)


class UpdateUomRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/uom/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Uom:
        return Uom.from_json(result)

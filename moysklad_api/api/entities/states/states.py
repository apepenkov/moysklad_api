import typing

from .... import types, helpers
from ....types import Unset, RequestData


class State(types.MoySkladBaseClass):
    """
    accountId  | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    color      | Int         | Цвет Статуса (ARGB, как одно целое число). Обязательное при ответе, Необходимо при создании
    entityType | String(255) | Тип сущности, к которой относится Статус. Обязательное при ответе, Только для чтения
    id         | UUID        | ID Статуса. Обязательное при ответе, Только для чтения
    meta       | Meta        | Метаданные Статуса. Обязательное при ответе, Только для чтения
    name       | String(255) | Наименование Статуса. Обязательное при ответе, Необходимо при создании
    stateType  | Enum        | Тип Статуса: Regular, Successful, Unsuccessful. Обязательное при ответе, Необходимо при создании
    """

    account_id: typing.Optional[str]
    color: typing.Optional[int]
    entity_type: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    state_type: typing.Optional[typing.Literal["Regular", "Successful", "Unsuccessful"]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "State":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.color = dict_data.get("color")
        instance.entity_type = dict_data.get("entityType")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.state_type = dict_data.get("stateType")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("state",)


class GetStatesRequest(types.ApiRequest):
    """
    Получить статусы документов конкретной сущности через ее метаданные
    (entity/{entityType}/metadata).
    """

    def __init__(self, entity_type: str):
        self.entity_type = entity_type

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata",
        )

    def from_response(self, result: dict) -> typing.List[State]:
        return [State.from_json(x) for x in result.get("states", [])]


class CreateStateRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        name: str,
        color: int,
        state_type: typing.Union[
            Unset, typing.Literal["Regular", "Successful", "Unsuccessful"]
        ] = Unset,
    ):
        self.entity_type = entity_type
        self.name = name
        self.color = color
        self.state_type = state_type

    def to_request(self) -> RequestData:
        json_data = {"name": self.name, "color": self.color}
        if self.state_type != Unset:
            json_data["stateType"] = self.state_type
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/states",
            json=json_data,
        )

    def from_response(self, result: dict) -> State:
        return State.from_json(result)


class UpdateStateRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        color: typing.Union[Unset, int] = Unset,
        state_type: typing.Union[
            Unset, typing.Literal["Regular", "Successful", "Unsuccessful"]
        ] = Unset,
    ):
        self.entity_type = entity_type
        self.id = id_
        self.name = name
        self.color = color
        self.state_type = state_type

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.color != Unset:
            json_data["color"] = self.color
        if self.state_type != Unset:
            json_data["stateType"] = self.state_type
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/states/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> State:
        return State.from_json(result)


class DeleteStateRequest(types.ApiRequest):
    def __init__(self, entity_type: str, id_: str):
        self.entity_type = entity_type
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/states/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

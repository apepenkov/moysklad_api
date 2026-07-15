import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Thing(types.MoySkladBaseClass):
    """
    accountId   | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    description | String(4096)| Описание Серийного номера
    id          | UUID        | ID Серийного номера. Обязательное при ответе, Только для чтения
    meta        | Meta        | Метаданные о Серийном номере. Обязательное при ответе
    name        | String(255) | Наименование Серийного номера. Обязательное при ответе, Необходимо при создании

    Серийные номера доступны через API только для чтения.
    """

    account_id: typing.Optional[str]
    description: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Thing":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.description = dict_data.get("description")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("thing",)


class GetThingsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/thing",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Thing]:
        return [Thing.from_json(x) for x in result["rows"]]


class GetThingRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/thing/{self.id}",
        )

    def from_response(self, result: dict) -> Thing:
        return Thing.from_json(result)

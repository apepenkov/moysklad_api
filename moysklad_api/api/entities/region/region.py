import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Region(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    code         | String(255) | Код Региона
    externalCode | String(255) | Внешний код Региона. Обязательное при ответе
    id           | UUID        | ID Региона. Обязательное при ответе, Только для чтения
    meta         | Meta        | Метаданные о Регионе. Обязательное при ответе
    name         | String(255) | Наименование Региона. Обязательное при ответе, Необходимо при создании
    updated      | DateTime    | Момент последнего обновления сущности. Обязательное при ответе, Только для чтения
    version      | Int         | Версия сущности. Обязательное при ответе, Только для чтения

    Регионы - справочник только для чтения (регионы РФ), создание/изменение/удаление через API недоступны.
    """

    account_id: typing.Optional[str]
    code: typing.Optional[str]
    external_code: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    version: typing.Optional[int]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Region":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.code = dict_data.get("code")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.version = dict_data.get("version")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("region",)


class GetRegionsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/region",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Region]:
        return [Region.from_json(x) for x in result["rows"]]


class GetRegionRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/region/{self.id}",
        )

    def from_response(self, result: dict) -> Region:
        return Region.from_json(result)

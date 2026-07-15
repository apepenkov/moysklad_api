import typing

from .... import types, helpers
from ....types import Unset, RequestData

SalePlatformGroup = typing.Literal[
    "MARKETPLACES",
    "MESSENGERS",
    "OFFLINE_STORES",
    "ONLINE_STORES",
    "SOCIAL_NETWORKS",
]


class SalePlatform(types.MoySkladBaseClass):
    """
    id                | UUID        | ID Площадки для продаж. Обязательное при ответе, Только для чтения
    meta              | Meta        | Метаданные Площадки для продаж. Обязательное при ответе
    name              | String(255) | Наименование Площадки для продаж. Обязательное при ответе
    salePlatformGroup | Enum        | Группа площадок для продаж. Обязательное при ответе

    Площадки для продаж доступны через API только для чтения.
    """

    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    sale_platform_group: typing.Optional[SalePlatformGroup]

    @classmethod
    def from_json(cls, dict_data: dict) -> "SalePlatform":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.sale_platform_group = dict_data.get("salePlatformGroup")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("saleplatform",)


class GetSalePlatformsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/saleplatform",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[SalePlatform]:
        return [SalePlatform.from_json(x) for x in result["rows"]]


class GetSalePlatformRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/saleplatform/{self.id}",
        )

    def from_response(self, result: dict) -> SalePlatform:
        return SalePlatform.from_json(result)

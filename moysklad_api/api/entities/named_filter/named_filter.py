# Сохраненные фильтры (namedfilter) - вложенная сущность конкретного типа
# entity/document. Доступны только для чтения.
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class NamedFilter(types.MoySkladBaseClass):
    """
    accountId | UUID | ID учетной записи. Обязательное при ответе, Только для чтения
    id        | UUID | ID фильтра. Обязательное при ответе, Только для чтения
    meta      | Meta | Метаданные фильтра. Обязательное при ответе
    name      | String| Название фильтра. Обязательное при ответе, Необходимо при создании
    owner     | Meta | Владелец (Сотрудник). Обязательное при ответе, Только для чтения, Expand
    """

    account_id: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "NamedFilter":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("namedfilter",)


class GetNamedFiltersRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        owner: typing.Union[Unset, str] = Unset,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """
        :param entity_type: Тип сущности/документа (например "product", "supply")
        :param owner: href сотрудника, чьи фильтры нужно получить (для администратора/решения)
        """
        self.entity_type = entity_type
        self.owner = owner
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {}
        if self.owner != Unset:
            params["owner"] = self.owner
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/namedfilter",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[NamedFilter]:
        return [NamedFilter.from_json(x) for x in result["rows"]]


class GetNamedFilterRequest(types.ApiRequest):
    def __init__(self, entity_type: str, id_: str):
        self.entity_type = entity_type
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/namedfilter/{self.id}",
        )

    def from_response(self, result: dict) -> NamedFilter:
        return NamedFilter.from_json(result)

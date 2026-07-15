import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class TaxRate(types.MoySkladBaseClass):
    """
    accountId | UUID     | ID учетной записи. Обязательное при ответе
    archived  | Boolean  | Флаг принадлежности ставки к архивным ставкам
    comment   | String   | Комментарий к налоговой ставке
    group     | Meta     | Отдел-владелец (для пользовательских ставок)
    id        | UUID     | ID налоговой ставки. Обязательное при ответе, Только для чтения
    meta      | Meta     | Метаданные налоговой ставки. Обязательное при ответе
    rate      | Number   | Значение налоговой ставки. Обязательное при ответе, Необходимо при создании
    owner     | Meta     | Сотрудник-владелец (для пользовательских ставок)
    shared    | Boolean  | Флаг общего доступа (для пользовательских ставок)
    updated   | DateTime | Момент последнего обновления сущности. Обязательное при ответе
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    comment: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    rate: typing.Optional[float]
    owner: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TaxRate":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.comment = dict_data.get("comment")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.rate = dict_data.get("rate")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.shared = dict_data.get("shared")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("taxrate",)


class GetTaxRatesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/taxrate",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[TaxRate]:
        return [TaxRate.from_json(x) for x in result["rows"]]


class CreateTaxRateRequest(types.ApiRequest):
    def __init__(
        self,
        rate: float,
        comment: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.rate = rate
        self.comment = comment
        self.archived = archived
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {"rate": self.rate}
        if self.comment != Unset:
            json_data["comment"] = self.comment
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
            url=f"{helpers.BASE_URL}/entity/taxrate",
            json=json_data,
        )

    def from_response(self, result: dict) -> TaxRate:
        return TaxRate.from_json(result)


class DeleteTaxRateRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/taxrate/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetTaxRateRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/taxrate/{self.id}",
        )

    def from_response(self, result: dict) -> TaxRate:
        return TaxRate.from_json(result)


class UpdateTaxRateRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        rate: typing.Union[Unset, float] = Unset,
        comment: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.rate = rate
        self.comment = comment
        self.archived = archived
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {}
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.comment != Unset:
            json_data["comment"] = self.comment
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
            url=f"{helpers.BASE_URL}/entity/taxrate/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> TaxRate:
        return TaxRate.from_json(result)

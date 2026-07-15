import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ExpenseItem(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    code         | String(255) | Код Статьи расходов
    description  | String(4096)| Описание Статьи расходов
    externalCode | String(255) | Внешний код Статьи расходов. Обязательное при ответе
    id           | UUID        | ID Cтатьи расходов. Обязательное при ответе, Только для чтения
    meta         | Meta        | Метаданные о Статье расходов. Обязательное при ответе
    name         | String(255) | Наименование Статьи расходов. Обязательное при ответе, Необходимо при создании
    updated      | DateTime    | Момент последнего обновления сущности. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    code: typing.Optional[str]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ExpenseItem":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("expenseitem",)


class GetExpenseItemsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/expenseitem",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ExpenseItem]:
        return [ExpenseItem.from_json(x) for x in result["rows"]]


class GetExpenseItemRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/expenseitem/{self.id}",
        )

    def from_response(self, result: dict) -> ExpenseItem:
        return ExpenseItem.from_json(result)


class CreateExpenseItemRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
    ):
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code

    def to_request(self) -> RequestData:
        json_data = {"name": self.name}
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/expenseitem",
            json=json_data,
        )

    def from_response(self, result: dict) -> ExpenseItem:
        return ExpenseItem.from_json(result)


class UpdateExpenseItemRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code

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
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/expenseitem/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ExpenseItem:
        return ExpenseItem.from_json(result)


class DeleteExpenseItemRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/expenseitem/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

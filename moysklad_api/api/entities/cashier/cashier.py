import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Cashier(types.MoySkladBaseClass):
    """
    accountId   | UUID | ID учетной записи Кассира. Обязательное при ответе, Только для чтения
    employee    | Meta | Метаданные сотрудника, которого представляет собой кассир. Обязательное при ответе, Expand
    id          | UUID | ID Кассира. Обязательное при ответе, Только для чтения
    meta        | Meta | Метаданные Кассира. Обязательное при ответе, Только для чтения
    retailStore | Meta | Метаданные точки продаж, к которой прикреплен кассир. Обязательное при ответе, Expand

    Кассиры доступны через API только для чтения.
    """

    account_id: typing.Optional[str]
    employee: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    retail_store: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Cashier":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.employee = helpers.get_meta(dict_data.get("employee"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.retail_store = helpers.get_meta(dict_data.get("retailStore"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("retailstore", "cashiers")


class GetCashiersRequest(types.ApiRequest):
    def __init__(
        self,
        retail_store_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.retail_store_id = retail_store_id
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
            url=f"{helpers.BASE_URL}/entity/retailstore/{self.retail_store_id}/cashiers",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Cashier]:
        return [Cashier.from_json(x) for x in result["rows"]]


class GetCashierRequest(types.ApiRequest):
    def __init__(self, retail_store_id: str, cashier_id: str):
        self.retail_store_id = retail_store_id
        self.cashier_id = cashier_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/retailstore/{self.retail_store_id}/cashiers/{self.cashier_id}",
        )

    def from_response(self, result: dict) -> Cashier:
        return Cashier.from_json(result)

import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class CounterpartyReportEntry(types.MoySkladBaseClass):
    meta: typing.Optional[types.Meta]
    counterparty: typing.Optional[dict]
    average_receipt: typing.Optional[float]
    balance: typing.Optional[float]
    bonus_balance: typing.Optional[float]
    demands_count: typing.Optional[int]
    demands_sum: typing.Optional[float]
    discounts_sum: typing.Optional[float]
    first_demand_date: typing.Optional[datetime.datetime]
    last_demand_date: typing.Optional[datetime.datetime]
    last_event_date: typing.Optional[datetime.datetime]
    last_event_text: typing.Optional[str]
    profit: typing.Optional[float]
    returns_count: typing.Optional[int]
    returns_sum: typing.Optional[float]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CounterpartyReportEntry":
        instance = cls()
        instance.meta = dict_data.get("meta")
        instance.counterparty = dict_data.get("counterparty")
        instance.average_receipt = dict_data.get("averageReceipt")
        instance.balance = dict_data.get("balance")
        instance.bonus_balance = dict_data.get("bonusBalance")
        instance.demands_count = dict_data.get("demandsCount")
        instance.demands_sum = dict_data.get("demandsSum")
        instance.discounts_sum = dict_data.get("discountsSum")
        instance.first_demand_date = helpers.parse_date(
            dict_data.get("firstDemandDate")
        )
        instance.last_demand_date = helpers.parse_date(dict_data.get("lastDemandDate"))
        instance.last_event_date = helpers.parse_date(dict_data.get("lastEventDate"))
        instance.last_event_text = dict_data.get("lastEventText")
        instance.profit = dict_data.get("profit")
        instance.returns_count = dict_data.get("returnsCount")
        instance.returns_sum = dict_data.get("returnsSum")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetCounterpartyReportsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        filter_: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.filter = filter_

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.filter != Unset:
            params["filter"] = self.filter
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/report/counterparty", params=params
        )

    def from_response(self, result: dict) -> typing.List[CounterpartyReportEntry]:
        return [CounterpartyReportEntry.from_json(x) for x in result["rows"]]


class GetSelectedCounterpartyReportsRequest(types.ApiRequest):
    def __init__(self, counterparties: typing.List[types.Meta]):
        self.counterparties = counterparties

    def to_request(self) -> RequestData:
        json_data = {
            "counterparties": [
                {"counterparty": {"meta": c}} for c in self.counterparties
            ]
        }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/report/counterparty",
            json=json_data,
        )

    def from_response(self, result: dict) -> typing.List[CounterpartyReportEntry]:
        return [CounterpartyReportEntry.from_json(x) for x in result["rows"]]


class GetCounterpartyReportRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str):
        self.counterparty_id = counterparty_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/counterparty/{self.counterparty_id}",
        )

    def from_response(self, result: dict) -> CounterpartyReportEntry:
        return CounterpartyReportEntry.from_json(result)

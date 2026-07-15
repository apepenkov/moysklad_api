import typing

from .... import types, helpers
from ....types import Unset, RequestData


class PeriodMetric(types.MoySkladBaseClass):
    count: typing.Optional[int]
    amount: typing.Optional[int]
    movement_amount: typing.Optional[int]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PeriodMetric":
        instance = cls()
        instance.count = dict_data.get("count")
        instance.amount = dict_data.get("amount")
        instance.movement_amount = dict_data.get("movementAmount")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class MoneyMetric(types.MoySkladBaseClass):
    income: typing.Optional[int]
    outcome: typing.Optional[float]
    balance: typing.Optional[float]
    today_movement: typing.Optional[float]
    movement: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "MoneyMetric":
        instance = cls()
        instance.income = dict_data.get("income")
        instance.outcome = dict_data.get("outcome")
        instance.balance = dict_data.get("balance")
        instance.today_movement = dict_data.get("todayMovement")
        instance.movement = dict_data.get("movement")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class DashboardMetrics(types.MoySkladBaseClass):
    """Показатели (report/dashboard/{day|week|month})."""

    sales: typing.Optional[PeriodMetric]
    orders: typing.Optional[PeriodMetric]
    money: typing.Optional[MoneyMetric]

    @classmethod
    def from_json(cls, dict_data: dict) -> "DashboardMetrics":
        instance = cls()
        instance.sales = (
            PeriodMetric.from_json(dict_data["sales"])
            if dict_data.get("sales") is not None
            else None
        )
        instance.orders = (
            PeriodMetric.from_json(dict_data["orders"])
            if dict_data.get("orders") is not None
            else None
        )
        instance.money = (
            MoneyMetric.from_json(dict_data["money"])
            if dict_data.get("money") is not None
            else None
        )
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetDashboardDayRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(method="GET", url=f"{helpers.BASE_URL}/report/dashboard/day")

    def from_response(self, result: dict) -> DashboardMetrics:
        return DashboardMetrics.from_json(result)


class GetDashboardWeekRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/report/dashboard/week"
        )

    def from_response(self, result: dict) -> DashboardMetrics:
        return DashboardMetrics.from_json(result)


class GetDashboardMonthRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/report/dashboard/month"
        )

    def from_response(self, result: dict) -> DashboardMetrics:
        return DashboardMetrics.from_json(result)

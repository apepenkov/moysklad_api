import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class MoneyPlotSeriesPoint(types.MoySkladBaseClass):
    date: typing.Optional[datetime.datetime]
    credit: typing.Optional[float]
    debit: typing.Optional[float]
    balance: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "MoneyPlotSeriesPoint":
        instance = cls()
        instance.date = helpers.parse_date(dict_data.get("date"))
        instance.credit = dict_data.get("credit")
        instance.debit = dict_data.get("debit")
        instance.balance = dict_data.get("balance")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class MoneyPlotSeries(types.MoySkladBaseClass):
    credit: typing.Optional[float]
    debit: typing.Optional[float]
    series: typing.Optional[typing.List[MoneyPlotSeriesPoint]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "MoneyPlotSeries":
        instance = cls()
        instance.credit = dict_data.get("credit")
        instance.debit = dict_data.get("debit")
        instance.series = [
            MoneyPlotSeriesPoint.from_json(x) for x in dict_data.get("series", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class MoneyByAccountRow(types.MoySkladBaseClass):
    account: typing.Optional[dict]
    organization: typing.Optional[dict]
    balance: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "MoneyByAccountRow":
        instance = cls()
        instance.account = dict_data.get("account")
        instance.organization = dict_data.get("organization")
        instance.balance = dict_data.get("balance")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetMoneyPlotSeriesRequest(types.ApiRequest):
    def __init__(
        self,
        moment_from: datetime.datetime,
        moment_to: datetime.datetime,
        interval: typing.Literal["hour", "day", "month"],
        filter_organization: typing.Union[Unset, types.Meta] = Unset,
        filter_project: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.interval = interval
        self.filter_organization = filter_organization
        self.filter_project = filter_project

    def to_request(self) -> RequestData:
        params = {
            "momentFrom": helpers.date_to_str(self.moment_from),
            "momentTo": helpers.date_to_str(self.moment_to),
            "interval": self.interval,
        }
        filters = []
        if self.filter_organization != Unset:
            filters.append(f"organization={self.filter_organization['href']}")
        if self.filter_project != Unset:
            filters.append(f"project={self.filter_project['href']}")
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/money/plotseries",
            params=params,
        )

    def from_response(self, result: dict) -> MoneyPlotSeries:
        return MoneyPlotSeries.from_json(result)


class GetMoneyByAccountRequest(types.ApiRequest):
    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/report/money/byaccount"
        )

    def from_response(self, result: dict) -> typing.List[MoneyByAccountRow]:
        return [MoneyByAccountRow.from_json(x) for x in result["rows"]]

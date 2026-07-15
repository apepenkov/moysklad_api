import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class SalesOrdersSeriesPoint(types.MoySkladBaseClass):
    date: typing.Optional[datetime.datetime]
    quantity: typing.Optional[int]
    sum: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "SalesOrdersSeriesPoint":
        instance = cls()
        instance.date = helpers.parse_date(dict_data.get("date"))
        instance.quantity = dict_data.get("quantity")
        instance.sum = dict_data.get("sum")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class SalesOrdersPlotSeries(types.MoySkladBaseClass):
    series: typing.Optional[typing.List[SalesOrdersSeriesPoint]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "SalesOrdersPlotSeries":
        instance = cls()
        instance.series = [
            SalesOrdersSeriesPoint.from_json(x) for x in dict_data.get("series", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetOrdersPlotSeriesRequest(types.ApiRequest):
    def __init__(
        self,
        moment_from: datetime.datetime,
        moment_to: datetime.datetime,
        interval: typing.Literal["hour", "day", "month"],
        filter_organization: typing.Union[Unset, types.Meta] = Unset,
        filter_store: typing.Union[Unset, types.Meta] = Unset,
        filter_project: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.interval = interval
        self.filter_organization = filter_organization
        self.filter_store = filter_store
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
        if self.filter_store != Unset:
            filters.append(f"store={self.filter_store['href']}")
        if self.filter_project != Unset:
            filters.append(f"project={self.filter_project['href']}")
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/orders/plotseries",
            params=params,
        )

    def from_response(self, result: dict) -> SalesOrdersPlotSeries:
        return SalesOrdersPlotSeries.from_json(result)


class GetSalesPlotSeriesRequest(types.ApiRequest):
    def __init__(
        self,
        moment_from: datetime.datetime,
        moment_to: datetime.datetime,
        interval: typing.Literal["hour", "day", "month"],
        filter_organization: typing.Union[Unset, types.Meta] = Unset,
        filter_store: typing.Union[Unset, types.Meta] = Unset,
        filter_project: typing.Union[Unset, types.Meta] = Unset,
        filter_retail_store: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.interval = interval
        self.filter_organization = filter_organization
        self.filter_store = filter_store
        self.filter_project = filter_project
        self.filter_retail_store = filter_retail_store

    def to_request(self) -> RequestData:
        params = {
            "momentFrom": helpers.date_to_str(self.moment_from),
            "momentTo": helpers.date_to_str(self.moment_to),
            "interval": self.interval,
        }
        filters = []
        if self.filter_organization != Unset:
            filters.append(f"organization={self.filter_organization['href']}")
        if self.filter_store != Unset:
            filters.append(f"store={self.filter_store['href']}")
        if self.filter_project != Unset:
            filters.append(f"project={self.filter_project['href']}")
        if self.filter_retail_store != Unset:
            filters.append(f"retailStore={self.filter_retail_store['href']}")
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/sales/plotseries",
            params=params,
        )

    def from_response(self, result: dict) -> SalesOrdersPlotSeries:
        return SalesOrdersPlotSeries.from_json(result)

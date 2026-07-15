import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class StockByOperationRow(types.MoySkladBaseClass):
    assortment: typing.Optional[types.Meta]
    avg_stock_days: typing.Optional[float]
    cost_per_unit: typing.Optional[float]
    moment: typing.Optional[datetime.datetime]
    operation: typing.Optional[types.Meta]
    stock: typing.Optional[float]
    store: typing.Optional[types.Meta]
    sum_cost: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "StockByOperationRow":
        instance = cls()
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.avg_stock_days = dict_data.get("avgStockDays")
        instance.cost_per_unit = dict_data.get("costPerUnit")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.operation = helpers.get_meta(dict_data.get("operation"))
        instance.stock = dict_data.get("stock")
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sum_cost = dict_data.get("sumCost")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class ReserveByOperationRow(types.MoySkladBaseClass):
    assortment: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    operation: typing.Optional[types.Meta]
    reserve: typing.Optional[float]
    store: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ReserveByOperationRow":
        instance = cls()
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.operation = helpers.get_meta(dict_data.get("operation"))
        instance.reserve = dict_data.get("reserve")
        instance.store = helpers.get_meta(dict_data.get("store"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class InTransitByOperationRow(types.MoySkladBaseClass):
    assortment: typing.Optional[types.Meta]
    in_transit: typing.Optional[float]
    moment: typing.Optional[datetime.datetime]
    operation: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "InTransitByOperationRow":
        instance = cls()
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.in_transit = dict_data.get("inTransit")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.operation = helpers.get_meta(dict_data.get("operation"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class GetByOperationsStockRequest(types.ApiRequest):
    def __init__(
        self,
        assortment: types.Meta,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.assortment = assortment
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {"filter": f"assortment={self.assortment['href']}"}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/byoperations/stock",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[StockByOperationRow]:
        return [StockByOperationRow.from_json(x) for x in result["rows"]]


class GetByOperationsReserveRequest(types.ApiRequest):
    def __init__(
        self,
        assortment: types.Meta,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.assortment = assortment
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {"filter": f"assortment={self.assortment['href']}"}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/byoperations/reserve",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ReserveByOperationRow]:
        return [ReserveByOperationRow.from_json(x) for x in result["rows"]]


class GetByOperationsInTransitRequest(types.ApiRequest):
    def __init__(
        self,
        assortment: types.Meta,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.assortment = assortment
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {"filter": f"assortment={self.assortment['href']}"}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/byoperations/intransit",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[InTransitByOperationRow]:
        return [InTransitByOperationRow.from_json(x) for x in result["rows"]]

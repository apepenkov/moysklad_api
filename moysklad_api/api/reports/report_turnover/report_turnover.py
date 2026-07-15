import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class TurnoverMetric(types.MoySkladBaseClass):
    sum: typing.Optional[float]
    quantity: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TurnoverMetric":
        instance = cls()
        instance.sum = dict_data.get("sum")
        instance.quantity = dict_data.get("quantity")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class TurnoverByProductRow(types.MoySkladBaseClass):
    assortment: typing.Optional[dict]
    on_period_start: typing.Optional[TurnoverMetric]
    on_period_end: typing.Optional[TurnoverMetric]
    income: typing.Optional[TurnoverMetric]
    outcome: typing.Optional[TurnoverMetric]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TurnoverByProductRow":
        instance = cls()
        instance.assortment = dict_data.get("assortment")
        instance.on_period_start = (
            TurnoverMetric.from_json(dict_data["onPeriodStart"])
            if dict_data.get("onPeriodStart") is not None
            else None
        )
        instance.on_period_end = (
            TurnoverMetric.from_json(dict_data["onPeriodEnd"])
            if dict_data.get("onPeriodEnd") is not None
            else None
        )
        instance.income = (
            TurnoverMetric.from_json(dict_data["income"])
            if dict_data.get("income") is not None
            else None
        )
        instance.outcome = (
            TurnoverMetric.from_json(dict_data["outcome"])
            if dict_data.get("outcome") is not None
            else None
        )
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class TurnoverStoreDetail(types.MoySkladBaseClass):
    store: typing.Optional[dict]
    on_period_start: typing.Optional[TurnoverMetric]
    on_period_end: typing.Optional[TurnoverMetric]
    income: typing.Optional[TurnoverMetric]
    outcome: typing.Optional[TurnoverMetric]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TurnoverStoreDetail":
        instance = cls()
        instance.store = dict_data.get("store")
        instance.on_period_start = (
            TurnoverMetric.from_json(dict_data["onPeriodStart"])
            if dict_data.get("onPeriodStart") is not None
            else None
        )
        instance.on_period_end = (
            TurnoverMetric.from_json(dict_data["onPeriodEnd"])
            if dict_data.get("onPeriodEnd") is not None
            else None
        )
        instance.income = (
            TurnoverMetric.from_json(dict_data["income"])
            if dict_data.get("income") is not None
            else None
        )
        instance.outcome = (
            TurnoverMetric.from_json(dict_data["outcome"])
            if dict_data.get("outcome") is not None
            else None
        )
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class TurnoverByStoreRow(types.MoySkladBaseClass):
    assortment: typing.Optional[dict]
    stock_by_store: typing.Optional[typing.List[TurnoverStoreDetail]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TurnoverByStoreRow":
        instance = cls()
        instance.assortment = dict_data.get("assortment")
        stock_by_store = dict_data.get("stockByStore")
        if isinstance(stock_by_store, dict):
            stock_by_store = stock_by_store.get("rows", [])
        instance.stock_by_store = [
            TurnoverStoreDetail.from_json(x) for x in (stock_by_store or [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class TurnoverByOperationRow(types.MoySkladBaseClass):
    assortment: typing.Optional[dict]
    store: typing.Optional[dict]
    operation: typing.Optional[dict]
    quantity: typing.Optional[float]
    cost: typing.Optional[float]
    sum: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TurnoverByOperationRow":
        instance = cls()
        instance.assortment = dict_data.get("assortment")
        instance.store = dict_data.get("store")
        instance.operation = dict_data.get("operation")
        instance.quantity = dict_data.get("quantity")
        instance.cost = dict_data.get("cost")
        instance.sum = dict_data.get("sum")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


def _build_common_filter(
    agent: typing.Union[Unset, types.Meta] = Unset,
    agent_tag: typing.Union[Unset, str] = Unset,
    contract: typing.Union[Unset, types.Meta] = Unset,
    organization: typing.Union[Unset, types.Meta] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    retail_store: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    type_: typing.Union[Unset, str] = Unset,
) -> typing.List[str]:
    parts = []
    if agent != Unset:
        parts.append(f"agent={agent['href']}")
    if agent_tag != Unset:
        parts.append(f"agentTag={agent_tag}")
    if contract != Unset:
        parts.append(f"contract={contract['href']}")
    if organization != Unset:
        parts.append(f"organization={organization['href']}")
    if project != Unset:
        parts.append(f"project={project['href']}")
    if retail_store != Unset:
        parts.append(f"retailStore={retail_store['href']}")
    if store != Unset:
        for s in store:
            parts.append(f"store={s['href']}")
    if type_ != Unset:
        parts.append(f"type={type_}")
    return parts


TurnoverDocType = typing.Literal[
    "supply", "purchasereturn", "demand", "salesreturn", "loss", "enter", "move",
    "processing", "retaildemand", "retailsalesreturn", "productionstagecompletion",
]


class GetTurnoverAllRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        moment_from: typing.Union[Unset, datetime.datetime] = Unset,
        moment_to: typing.Union[Unset, datetime.datetime] = Unset,
        group_by: typing.Union[Unset, typing.Literal["product", "variant"]] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_tag: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        product: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        supplier: typing.Union[Unset, types.Meta] = Unset,
        type_: typing.Union[Unset, TurnoverDocType] = Unset,
        variant: typing.Union[Unset, types.Meta] = Unset,
        without_turnover: typing.Union[Unset, bool] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.group_by = group_by
        self.agent = agent
        self.agent_tag = agent_tag
        self.contract = contract
        self.organization = organization
        self.product = product
        self.project = project
        self.retail_store = retail_store
        self.store = store
        self.supplier = supplier
        self.type_ = type_
        self.variant = variant
        self.without_turnover = without_turnover
        self.archived = archived

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.moment_from != Unset:
            params["momentFrom"] = helpers.date_to_str(self.moment_from)
        if self.moment_to != Unset:
            params["momentTo"] = helpers.date_to_str(self.moment_to)
        if self.group_by != Unset:
            params["groupBy"] = self.group_by
        filters = _build_common_filter(
            agent=self.agent,
            agent_tag=self.agent_tag,
            contract=self.contract,
            organization=self.organization,
            project=self.project,
            retail_store=self.retail_store,
            store=self.store,
            type_=self.type_,
        )
        if self.product != Unset:
            filters.append(f"product={self.product['href']}")
        if self.supplier != Unset:
            filters.append(f"supplier={self.supplier['href']}")
        if self.variant != Unset:
            filters.append(f"variant={self.variant['href']}")
        if self.without_turnover != Unset:
            filters.append(
                f"withoutturnover={'true' if self.without_turnover else 'false'}"
            )
        if self.archived != Unset:
            filters.append(f"archived={'true' if self.archived else 'false'}")
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/report/turnover/all", params=params
        )

    def from_response(self, result: dict) -> typing.List[TurnoverByProductRow]:
        return [TurnoverByProductRow.from_json(x) for x in result["rows"]]


class GetTurnoverByStoreRequest(types.ApiRequest):
    def __init__(
        self,
        product: typing.Union[Unset, types.Meta] = Unset,
        variant: typing.Union[Unset, types.Meta] = Unset,
        moment_from: typing.Union[Unset, datetime.datetime] = Unset,
        moment_to: typing.Union[Unset, datetime.datetime] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_tag: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        type_: typing.Union[Unset, TurnoverDocType] = Unset,
    ):
        self.product = product
        self.variant = variant
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.agent = agent
        self.agent_tag = agent_tag
        self.contract = contract
        self.organization = organization
        self.project = project
        self.retail_store = retail_store
        self.store = store
        self.type_ = type_

    def to_request(self) -> RequestData:
        params = {}
        if self.moment_from != Unset:
            params["momentFrom"] = helpers.date_to_str(self.moment_from)
        if self.moment_to != Unset:
            params["momentTo"] = helpers.date_to_str(self.moment_to)
        filters = _build_common_filter(
            agent=self.agent,
            agent_tag=self.agent_tag,
            contract=self.contract,
            organization=self.organization,
            project=self.project,
            retail_store=self.retail_store,
            store=self.store,
            type_=self.type_,
        )
        if self.product != Unset:
            filters.append(f"product={self.product['href']}")
        if self.variant != Unset:
            filters.append(f"variant={self.variant['href']}")
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/turnover/bystore",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[TurnoverByStoreRow]:
        return [TurnoverByStoreRow.from_json(x) for x in result["rows"]]


class GetTurnoverByOperationsRequest(types.ApiRequest):
    def __init__(
        self,
        moment_from: datetime.datetime,
        moment_to: datetime.datetime,
        product: typing.Union[Unset, types.Meta] = Unset,
        variant: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_tag: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        type_: typing.Union[Unset, TurnoverDocType] = Unset,
    ):
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.product = product
        self.variant = variant
        self.agent = agent
        self.agent_tag = agent_tag
        self.contract = contract
        self.organization = organization
        self.project = project
        self.retail_store = retail_store
        self.store = store
        self.type_ = type_

    def to_request(self) -> RequestData:
        params = {
            "momentFrom": helpers.date_to_str(self.moment_from),
            "momentTo": helpers.date_to_str(self.moment_to),
        }
        store_list = [self.store] if self.store != Unset else Unset
        filters = _build_common_filter(
            agent=self.agent,
            agent_tag=self.agent_tag,
            contract=self.contract,
            organization=self.organization,
            project=self.project,
            retail_store=self.retail_store,
            store=store_list,
            type_=self.type_,
        )
        if self.product != Unset:
            filters.append(f"product={self.product['href']}")
        if self.variant != Unset:
            filters.append(f"variant={self.variant['href']}")
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/turnover/byoperations",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[TurnoverByOperationRow]:
        return [TurnoverByOperationRow.from_json(x) for x in result["rows"]]

import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ProfitByProductRow(types.MoySkladBaseClass):
    assortment: typing.Optional[dict]
    margin: typing.Optional[float]
    sales_margin: typing.Optional[float]
    profit: typing.Optional[float]
    return_cost: typing.Optional[float]
    return_cost_sum: typing.Optional[float]
    return_price: typing.Optional[float]
    return_quantity: typing.Optional[float]
    return_sum: typing.Optional[float]
    sell_cost: typing.Optional[float]
    sell_cost_sum: typing.Optional[float]
    sell_price: typing.Optional[float]
    sell_quantity: typing.Optional[float]
    sell_sum: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProfitByProductRow":
        instance = cls()
        instance.assortment = dict_data.get("assortment")
        instance.margin = dict_data.get("margin")
        instance.sales_margin = dict_data.get("salesMargin")
        instance.profit = dict_data.get("profit")
        instance.return_cost = dict_data.get("returnCost")
        instance.return_cost_sum = dict_data.get("returnCostSum")
        instance.return_price = dict_data.get("returnPrice")
        instance.return_quantity = dict_data.get("returnQuantity")
        instance.return_sum = dict_data.get("returnSum")
        instance.sell_cost = dict_data.get("sellCost")
        instance.sell_cost_sum = dict_data.get("sellCostSum")
        instance.sell_price = dict_data.get("sellPrice")
        instance.sell_quantity = dict_data.get("sellQuantity")
        instance.sell_sum = dict_data.get("sellSum")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


class ProfitByAgentRow(types.MoySkladBaseClass):
    """Общая форма для отчетов по сотрудникам/покупателям/каналам продаж."""

    key_object: typing.Optional[dict]
    margin: typing.Optional[float]
    sales_margin: typing.Optional[float]
    profit: typing.Optional[float]
    return_avg_check: typing.Optional[float]
    return_cost_sum: typing.Optional[float]
    return_count: typing.Optional[int]
    return_sum: typing.Optional[float]
    sales_avg_check: typing.Optional[float]
    sales_count: typing.Optional[int]
    sell_cost_sum: typing.Optional[float]
    sell_sum: typing.Optional[float]

    @classmethod
    def from_json(
        cls, dict_data: dict, key_field: str = "employee"
    ) -> "ProfitByAgentRow":
        instance = cls()
        instance.key_object = dict_data.get(key_field)
        instance.margin = dict_data.get("margin")
        instance.sales_margin = dict_data.get("salesMargin")
        instance.profit = dict_data.get("profit")
        instance.return_avg_check = dict_data.get("returnAvgCheck")
        instance.return_cost_sum = dict_data.get("returnCostSum")
        instance.return_count = dict_data.get("returnCount")
        instance.return_sum = dict_data.get("returnSum")
        instance.sales_avg_check = dict_data.get("salesAvgCheck")
        instance.sales_count = dict_data.get("salesCount")
        instance.sell_cost_sum = dict_data.get("sellCostSum")
        instance.sell_sum = dict_data.get("sellSum")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return None


def _build_filter(
    product: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    product_folder: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    with_sub_folders: typing.Union[Unset, bool] = Unset,
    agent_tag: typing.Union[Unset, str] = Unset,
    entity_type: typing.Union[Unset, typing.Literal["demand", "retaildemand"]] = Unset,
    counterparty: typing.Union[Unset, types.Meta] = Unset,
    organization: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    retail_store: typing.Union[Unset, types.Meta] = Unset,
    supplier: typing.Union[Unset, types.Meta] = Unset,
    sales_channel: typing.Union[Unset, typing.List[types.Meta]] = Unset,
) -> typing.List[str]:
    parts = []
    if product != Unset:
        for p in product:
            parts.append(f"product={p['href']}")
    if product_folder != Unset:
        for p in product_folder:
            parts.append(f"productFolder={p['href']}")
    if with_sub_folders != Unset:
        parts.append(f"withSubFolders={'true' if with_sub_folders else 'false'}")
    if agent_tag != Unset:
        parts.append(f"agentTag={agent_tag}")
    if entity_type != Unset:
        parts.append(f"entityType={entity_type}")
    if counterparty != Unset:
        parts.append(f"counterparty={counterparty['href']}")
    if organization != Unset:
        parts.append(f"organization={organization['href']}")
    if store != Unset:
        parts.append(f"store={store['href']}")
    if project != Unset:
        parts.append(f"project={project['href']}")
    if retail_store != Unset:
        parts.append(f"retailStore={retail_store['href']}")
    if supplier != Unset:
        parts.append(f"supplier={supplier['href']}")
    if sales_channel != Unset:
        for s in sales_channel:
            parts.append(f"salesChannel={s['href']}")
    return parts


class _BaseProfitRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        moment_from: typing.Union[Unset, datetime.datetime] = Unset,
        moment_to: typing.Union[Unset, datetime.datetime] = Unset,
        product: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        product_folder: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        with_sub_folders: typing.Union[Unset, bool] = Unset,
        agent_tag: typing.Union[Unset, str] = Unset,
        entity_type: typing.Union[
            Unset, typing.Literal["demand", "retaildemand"]
        ] = Unset,
        counterparty: typing.Union[Unset, types.Meta] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        retail_store: typing.Union[Unset, types.Meta] = Unset,
        supplier: typing.Union[Unset, types.Meta] = Unset,
        sales_channel: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.moment_from = moment_from
        self.moment_to = moment_to
        self.product = product
        self.product_folder = product_folder
        self.with_sub_folders = with_sub_folders
        self.agent_tag = agent_tag
        self.entity_type = entity_type
        self.counterparty = counterparty
        self.organization = organization
        self.store = store
        self.project = project
        self.retail_store = retail_store
        self.supplier = supplier
        self.sales_channel = sales_channel

    def _endpoint(self) -> str:
        raise NotImplementedError

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
        filters = _build_filter(
            product=self.product,
            product_folder=self.product_folder,
            with_sub_folders=self.with_sub_folders,
            agent_tag=self.agent_tag,
            entity_type=self.entity_type,
            counterparty=self.counterparty,
            organization=self.organization,
            store=self.store,
            project=self.project,
            retail_store=self.retail_store,
            supplier=self.supplier,
            sales_channel=self.sales_channel,
        )
        if filters:
            params["filter"] = ";".join(filters)
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/profit/{self._endpoint()}",
            params=params,
        )


class GetProfitByProductRequest(_BaseProfitRequest):
    def _endpoint(self) -> str:
        return "byproduct"

    def from_response(self, result: dict) -> typing.List[ProfitByProductRow]:
        return [ProfitByProductRow.from_json(x) for x in result["rows"]]


class GetProfitByVariantRequest(_BaseProfitRequest):
    def _endpoint(self) -> str:
        return "byvariant"

    def from_response(self, result: dict) -> typing.List[ProfitByProductRow]:
        return [ProfitByProductRow.from_json(x) for x in result["rows"]]


class GetProfitByEmployeeRequest(_BaseProfitRequest):
    def _endpoint(self) -> str:
        return "byemployee"

    def from_response(self, result: dict) -> typing.List[ProfitByAgentRow]:
        return [
            ProfitByAgentRow.from_json(x, key_field="employee")
            for x in result["rows"]
        ]


class GetProfitByCounterpartyRequest(_BaseProfitRequest):
    def _endpoint(self) -> str:
        return "bycounterparty"

    def from_response(self, result: dict) -> typing.List[ProfitByAgentRow]:
        return [
            ProfitByAgentRow.from_json(x, key_field="counterparty")
            for x in result["rows"]
        ]


class GetProfitBySalesChannelRequest(_BaseProfitRequest):
    def _endpoint(self) -> str:
        return "bysaleschannel"

    def from_response(self, result: dict) -> typing.List[ProfitByAgentRow]:
        return [
            ProfitByAgentRow.from_json(x, key_field="salesChannel")
            for x in result["rows"]
        ]

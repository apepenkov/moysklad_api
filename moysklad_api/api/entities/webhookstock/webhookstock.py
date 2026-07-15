import typing

from .... import types, helpers
from ....types import Unset, RequestData

StockType = typing.Literal["stock"]
ReportType = typing.Literal["all", "bystore"]


class WebhookStock(types.MoySkladBaseClass):
    """
    accountId         | UUID | ID учетной записи. Обязательное при ответе
    authorApplication | Meta | Метаданные Решения, создавшего вебхук. Только для чтения
    enabled           | Boolean | Включен/отключен. Обязательное при ответе
    stockType         | Enum | Тип остатков ("stock"). Обязательное при ответе, Необходимо при создании
    reportType        | Enum | Тип отчета остатков ("all"/"bystore"). Обязательное при ответе, Необходимо при создании
    id                | UUID | ID вебхука. Обязательное при ответе
    meta              | Meta | Метаданные вебхука. Обязательное при ответе
    url               | URL  | URL обработки вебхука. Обязательное при ответе, Необходимо при создании
    """

    account_id: typing.Optional[str]
    author_application: typing.Optional[types.Meta]
    enabled: typing.Optional[bool]
    stock_type: typing.Optional[StockType]
    report_type: typing.Optional[ReportType]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    url: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "WebhookStock":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.author_application = helpers.get_meta(
            dict_data.get("authorApplication")
        )
        instance.enabled = dict_data.get("enabled")
        instance.stock_type = dict_data.get("stockType")
        instance.report_type = dict_data.get("reportType")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.url = dict_data.get("url")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("webhookstock",)


class GetWebhookStocksRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
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
            url=f"{helpers.BASE_URL}/entity/webhookstock",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[WebhookStock]:
        return [WebhookStock.from_json(x) for x in result["rows"]]


class CreateWebhookStockRequest(types.ApiRequest):
    def __init__(
        self,
        stock_type: StockType,
        report_type: ReportType,
        url: str,
        enabled: typing.Union[Unset, bool] = Unset,
    ):
        self.stock_type = stock_type
        self.report_type = report_type
        self.url = url
        self.enabled = enabled

    def to_request(self) -> RequestData:
        json_data = {
            "stockType": self.stock_type,
            "reportType": self.report_type,
            "url": self.url,
        }
        if self.enabled != Unset:
            json_data["enabled"] = self.enabled
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/webhookstock",
            json=json_data,
        )

    def from_response(self, result: dict) -> WebhookStock:
        return WebhookStock.from_json(result)


class DeleteWebhookStockRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/webhookstock/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetWebhookStockRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/webhookstock/{self.id}",
        )

    def from_response(self, result: dict) -> WebhookStock:
        return WebhookStock.from_json(result)


class UpdateWebhookStockRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        stock_type: typing.Union[Unset, StockType] = Unset,
        report_type: typing.Union[Unset, ReportType] = Unset,
        url: typing.Union[Unset, str] = Unset,
        enabled: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.stock_type = stock_type
        self.report_type = report_type
        self.url = url
        self.enabled = enabled

    def to_request(self) -> RequestData:
        json_data = {}
        if self.stock_type != Unset:
            json_data["stockType"] = self.stock_type
        if self.report_type != Unset:
            json_data["reportType"] = self.report_type
        if self.url != Unset:
            json_data["url"] = self.url
        if self.enabled != Unset:
            json_data["enabled"] = self.enabled
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/webhookstock/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> WebhookStock:
        return WebhookStock.from_json(result)

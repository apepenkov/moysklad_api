import typing

from .... import types, helpers
from ....types import Unset, RequestData

DiscountStrategy = typing.Literal["bySum", "byPriority"]


class CompanySettings(types.MoySkladBaseClass):
    """
    checkMinPrice            | Boolean | Автоматически устанавливать минимальную цену. Обязательное при ответе
    checkShippingStock       | Boolean | Запретить отгрузку отсутствующих товаров. Обязательное при ответе
    companyAddress           | String(255)| Адрес компании для электронных писем
    currency                 | Meta    | Метаданные стандартной валюты. Обязательное при ответе
    discountStrategy         | Enum    | Совместное применение скидок. Обязательное при ответе, Необходимо при создании
    globalOperationNumbering | Boolean | Использовать сквозную нумерацию документов. Обязательное при ответе
    meta                     | Meta    | Метаданные Настроек компании. Обязательное при ответе
    priceTypes               | Array(Object)| Коллекция всех существующих типов цен. Обязательное при ответе
    useCompanyAddress        | Boolean | Использовать адрес компании для электронных писем. Обязательное при ответе
    useRecycleBin            | Boolean | Использовать корзину. Обязательное при ответе
    accountCountry           | String(255)| Страновая конфигурация аккаунта (RU, BY, KZ). Обязательное при ответе, Только для чтения
    """

    check_min_price: typing.Optional[bool]
    check_shipping_stock: typing.Optional[bool]
    company_address: typing.Optional[str]
    currency: typing.Optional[dict]
    discount_strategy: typing.Optional[DiscountStrategy]
    global_operation_numbering: typing.Optional[bool]
    meta: typing.Optional[types.Meta]
    price_types: typing.Optional[typing.List[dict]]
    use_company_address: typing.Optional[bool]
    use_recycle_bin: typing.Optional[bool]
    account_country: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CompanySettings":
        instance = cls()
        instance.check_min_price = dict_data.get("checkMinPrice")
        instance.check_shipping_stock = dict_data.get("checkShippingStock")
        instance.company_address = dict_data.get("companyAddress")
        instance.currency = dict_data.get("currency")
        instance.discount_strategy = dict_data.get("discountStrategy")
        instance.global_operation_numbering = dict_data.get("globalOperationNumbering")
        instance.meta = dict_data.get("meta")
        instance.price_types = dict_data.get("priceTypes")
        instance.use_company_address = dict_data.get("useCompanyAddress")
        instance.use_recycle_bin = dict_data.get("useRecycleBin")
        instance.account_country = dict_data.get("accountCountry")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("companysettings",)


class GetCompanySettingsRequest(types.ApiRequest):
    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/context/companysettings",
        )

    def from_response(self, result: dict) -> CompanySettings:
        return CompanySettings.from_json(result)


class UpdateCompanySettingsRequest(types.ApiRequest):
    def __init__(
        self,
        check_min_price: typing.Union[Unset, bool] = Unset,
        check_shipping_stock: typing.Union[Unset, bool] = Unset,
        company_address: typing.Union[Unset, str] = Unset,
        discount_strategy: typing.Union[Unset, DiscountStrategy] = Unset,
        global_operation_numbering: typing.Union[Unset, bool] = Unset,
        use_company_address: typing.Union[Unset, bool] = Unset,
        use_recycle_bin: typing.Union[Unset, bool] = Unset,
    ):
        self.check_min_price = check_min_price
        self.check_shipping_stock = check_shipping_stock
        self.company_address = company_address
        self.discount_strategy = discount_strategy
        self.global_operation_numbering = global_operation_numbering
        self.use_company_address = use_company_address
        self.use_recycle_bin = use_recycle_bin

    def to_request(self) -> RequestData:
        json_data = {}
        if self.check_min_price != Unset:
            json_data["checkMinPrice"] = self.check_min_price
        if self.check_shipping_stock != Unset:
            json_data["checkShippingStock"] = self.check_shipping_stock
        if self.company_address != Unset:
            json_data["companyAddress"] = self.company_address
        if self.discount_strategy != Unset:
            json_data["discountStrategy"] = self.discount_strategy
        if self.global_operation_numbering != Unset:
            json_data["globalOperationNumbering"] = self.global_operation_numbering
        if self.use_company_address != Unset:
            json_data["useCompanyAddress"] = self.use_company_address
        if self.use_recycle_bin != Unset:
            json_data["useRecycleBin"] = self.use_recycle_bin
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/context/companysettings",
            json=json_data,
        )

    def from_response(self, result: dict) -> CompanySettings:
        return CompanySettings.from_json(result)

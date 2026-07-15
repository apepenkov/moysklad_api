import typing

from .... import types, helpers
from ....types import Unset, RequestData


class UserSettings(types.MoySkladBaseClass):
    """
    autoShowReports             | Boolean | Строить ли отчеты автоматически. Обязательное при ответе
    defaultCompany              | Meta    | Организация по умолчанию. Обязательное при ответе
    defaultCustomerCounterparty | Meta    | Покупатель по умолчанию. Обязательное при ответе
    defaultPlace                | Meta    | Склад по умолчанию. Обязательное при ответе
    defaultProject              | Meta    | Проект по умолчанию. Обязательное при ответе
    defaultPurchaseCounterparty | Meta    | Поставщик по умолчанию. Обязательное при ответе
    defaultScreen               | Enum    | Стартовый экран. Обязательное при ответе
    fieldsPerRow                | Int     | Количество столбцов доп. полей. Обязательное при ответе
    locale                      | Enum    | Язык системы ("ru_RU"/"en_US"). Обязательное при ответе
    mailFooter                  | Boolean | Подпись в письмах. Обязательное при ответе
    meta                        | Meta    | Метаданные настроек. Обязательное при ответе
    printFormat                 | Enum    | Правила печати документов. Обязательное при ответе
    """

    auto_show_reports: typing.Optional[bool]
    default_company: typing.Optional[types.Meta]
    default_customer_counterparty: typing.Optional[types.Meta]
    default_place: typing.Optional[types.Meta]
    default_project: typing.Optional[types.Meta]
    default_purchase_counterparty: typing.Optional[types.Meta]
    default_screen: typing.Optional[str]
    fields_per_row: typing.Optional[int]
    locale: typing.Optional[typing.Literal["ru_RU", "en_US"]]
    mail_footer: typing.Optional[bool]
    meta: typing.Optional[types.Meta]
    print_format: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "UserSettings":
        instance = cls()
        instance.auto_show_reports = dict_data.get("autoShowReports")
        instance.default_company = helpers.get_meta(dict_data.get("defaultCompany"))
        instance.default_customer_counterparty = helpers.get_meta(
            dict_data.get("defaultCustomerCounterparty")
        )
        instance.default_place = helpers.get_meta(dict_data.get("defaultPlace"))
        instance.default_project = helpers.get_meta(dict_data.get("defaultProject"))
        instance.default_purchase_counterparty = helpers.get_meta(
            dict_data.get("defaultPurchaseCounterparty")
        )
        instance.default_screen = dict_data.get("defaultScreen")
        instance.fields_per_row = dict_data.get("fieldsPerRow")
        instance.locale = dict_data.get("locale")
        instance.mail_footer = dict_data.get("mailFooter")
        instance.meta = dict_data.get("meta")
        instance.print_format = dict_data.get("printFormat")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("usersettings",)


class GetUserSettingsRequest(types.ApiRequest):
    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/context/usersettings",
        )

    def from_response(self, result: dict) -> UserSettings:
        return UserSettings.from_json(result)


class UpdateUserSettingsRequest(types.ApiRequest):
    def __init__(
        self,
        auto_show_reports: typing.Union[Unset, bool] = Unset,
        default_company: typing.Union[Unset, types.Meta] = Unset,
        default_customer_counterparty: typing.Union[Unset, types.Meta] = Unset,
        default_place: typing.Union[Unset, types.Meta] = Unset,
        default_project: typing.Union[Unset, types.Meta] = Unset,
        default_purchase_counterparty: typing.Union[Unset, types.Meta] = Unset,
        default_screen: typing.Union[Unset, str] = Unset,
        fields_per_row: typing.Union[Unset, int] = Unset,
        locale: typing.Union[Unset, typing.Literal["ru_RU", "en_US"]] = Unset,
        mail_footer: typing.Union[Unset, bool] = Unset,
        print_format: typing.Union[Unset, str] = Unset,
    ):
        self.auto_show_reports = auto_show_reports
        self.default_company = default_company
        self.default_customer_counterparty = default_customer_counterparty
        self.default_place = default_place
        self.default_project = default_project
        self.default_purchase_counterparty = default_purchase_counterparty
        self.default_screen = default_screen
        self.fields_per_row = fields_per_row
        self.locale = locale
        self.mail_footer = mail_footer
        self.print_format = print_format

    def to_request(self) -> RequestData:
        json_data = {}
        if self.auto_show_reports != Unset:
            json_data["autoShowReports"] = self.auto_show_reports
        if self.default_company != Unset:
            json_data["defaultCompany"] = {"meta": self.default_company}
        if self.default_customer_counterparty != Unset:
            json_data["defaultCustomerCounterparty"] = {
                "meta": self.default_customer_counterparty
            }
        if self.default_place != Unset:
            json_data["defaultPlace"] = {"meta": self.default_place}
        if self.default_project != Unset:
            json_data["defaultProject"] = {"meta": self.default_project}
        if self.default_purchase_counterparty != Unset:
            json_data["defaultPurchaseCounterparty"] = {
                "meta": self.default_purchase_counterparty
            }
        if self.default_screen != Unset:
            json_data["defaultScreen"] = self.default_screen
        if self.fields_per_row != Unset:
            json_data["fieldsPerRow"] = self.fields_per_row
        if self.locale != Unset:
            json_data["locale"] = self.locale
        if self.mail_footer != Unset:
            json_data["mailFooter"] = self.mail_footer
        if self.print_format != Unset:
            json_data["printFormat"] = self.print_format
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/context/usersettings",
            json=json_data,
        )

    def from_response(self, result: dict) -> UserSettings:
        return UserSettings.from_json(result)

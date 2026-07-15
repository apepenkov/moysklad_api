import typing

from .... import types, helpers
from ....types import RequestData

Tariff = typing.Literal[
    "BASIC",
    "CORPORATE",
    "FREE",
    "MINIMAL",
    "PROFESSIONAL",
    "RETAIL",
    "START",
    "TRIAL",
]


class CompanySubscription(types.MoySkladBaseClass):
    """
    role                          | String(255) | Роль авторизованного пользователя (USER/ADMIN). Обязательное при ответе, Только для чтения
    tariff                        | String(255) | Действующий тариф Аккаунта. Обязательное при ответе, Только для чтения
    isSubscriptionChangeAvailable | Boolean     | Доступность изменения подписки. Обязательное при ответе, Только для чтения
    subscriptionEndDate           | Long        | Дата (в мс) окончания действия текущего тарифа. Обязательное при ответе, Только для чтения

    Только для чтения (accountSettings/subscription).
    """

    role: typing.Optional[str]
    tariff: typing.Optional[Tariff]
    is_subscription_change_available: typing.Optional[bool]
    subscription_end_date: typing.Optional[int]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CompanySubscription":
        instance = cls()
        instance.role = dict_data.get("role")
        instance.tariff = dict_data.get("tariff")
        instance.is_subscription_change_available = dict_data.get(
            "isSubscriptionChangeAvailable"
        )
        instance.subscription_end_date = dict_data.get("subscriptionEndDate")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("subscription",)


class GetCompanySubscriptionRequest(types.ApiRequest):
    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/accountSettings/subscription",
        )

    def from_response(self, result: dict) -> CompanySubscription:
        return CompanySubscription.from_json(result)

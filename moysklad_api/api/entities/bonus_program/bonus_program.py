import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class BonusProgram(types.MoySkladBaseClass):
    """
    accountId                 | UUID                 | ID учетной записи
    active                    | Boolean              | Индикатор, является ли бонусная программа активной на данный момент
    agentTags                 | Array(String)        | Тэги контрагентов, к которым применяется бонусная программа. В случае пустого значения контрагентов в результате выводится пустой массив.
    allAgents                 | Boolean              | Индикатор, действует ли скидка на всех контрагентов (см. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-skidki)
    allProducts               | Boolean              | Индикатор, действует ли бонусная программа на все товары (всегда `true`, см. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-skidki)
    earnRateRoublesToPoint    | Int                  | Курс начисления
    earnWhileRedeeming        | Boolean              | Разрешить одновременное начисление и списание бонусов. Если `true` - бонусы будут начислены на денежную часть покупки, даже при частичной оплате покупки баллами.
    id                        | UUID                 | ID Бонусной программы
    maxPaidRatePercents       | Int                  | Максимальный процент оплаты баллами
    meta                      | Meta                 | Метаданные Бонусной программы
    name                      | String(255)          | Наименование Бонусной программы
    postponedBonusesDelayDays | Int                  | Баллы начисляются через [N] дней `+Тарифная опция «Расширенная бонусная программа»`
    spendRatePointsToRouble   | Int                  | Курс списания
    welcomeBonusesEnabled     | Boolean              | Возможность начисления приветственных баллов
    welcomeBonusesMode        | Enum                 | Условие начисления приветственных баллов. Не может быть пустым, если `welcomeBonusesEnabled` = true. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-bonusnaq-programma-bonusnye-programmy-atributy-suschnosti-uslowiq-bonusnyh-ballow
    welcomeBonusesValue       | Int                  | Количество приветственных баллов, начисляемых участникам бонусной программы. Не может быть отрицательным. Не может быть пустым, если `welcomeBonusesEnabled` = true
    """

    account_id: str
    active: bool
    agent_tags: typing.List[str]
    all_agents: bool
    all_products: bool
    earn_rate_roubles_to_point: int
    earn_while_redeeming: bool
    id: str
    max_paid_rate_percents: int
    meta: types.Meta
    name: str
    postponed_bonuses_delay_days: int
    spend_rate_points_to_rouble: int
    welcome_bonuses_enabled: bool
    welcome_bonuses_mode: str
    welcome_bonuses_value: int

    @classmethod
    def from_json(cls, dict_data: dict) -> "BonusProgram":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.active = dict_data.get("active")
        instance.agent_tags = dict_data.get("agentTags")
        instance.all_agents = dict_data.get("allAgents")
        instance.all_products = dict_data.get("allProducts")
        instance.earn_rate_roubles_to_point = dict_data.get("earnRateRoublesToPoint")
        instance.earn_while_redeeming = dict_data.get("earnWhileRedeeming")
        instance.id = dict_data.get("id")
        instance.max_paid_rate_percents = dict_data.get("maxPaidRatePercents")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.postponed_bonuses_delay_days = dict_data.get(
            "postponedBonusesDelayDays"
        )
        instance.spend_rate_points_to_rouble = dict_data.get("spendRatePointsToRouble")
        instance.welcome_bonuses_enabled = dict_data.get("welcomeBonusesEnabled")
        instance.welcome_bonuses_mode = dict_data.get("welcomeBonusesMode")
        instance.welcome_bonuses_value = dict_data.get("welcomeBonusesValue")
        return instance


class CreateBonusProgramRequest(types.ApiRequest):
    def __init__(
        self,
        account_id: typing.Union[Unset, str] = Unset,
        active: typing.Union[Unset, bool] = Unset,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        all_agents: typing.Union[Unset, bool] = Unset,
        all_products: typing.Union[Unset, bool] = Unset,
        earn_rate_roubles_to_point: typing.Union[Unset, int] = Unset,
        earn_while_redeeming: typing.Union[Unset, bool] = Unset,
        id: typing.Union[Unset, str] = Unset,
        max_paid_rate_percents: typing.Union[Unset, int] = Unset,
        name: typing.Union[Unset, str] = Unset,
        postponed_bonuses_delay_days: typing.Union[Unset, int] = Unset,
        spend_rate_points_to_rouble: typing.Union[Unset, int] = Unset,
        welcome_bonuses_enabled: typing.Union[Unset, bool] = Unset,
        welcome_bonuses_mode: typing.Union[Unset, str] = Unset,
        welcome_bonuses_value: typing.Union[Unset, int] = Unset,
    ):
        self.account_id = account_id
        self.active = active
        self.agent_tags = agent_tags
        self.all_agents = all_agents
        self.all_products = all_products
        self.earn_rate_roubles_to_point = earn_rate_roubles_to_point
        self.earn_while_redeeming = earn_while_redeeming
        self.id = id
        self.max_paid_rate_percents = max_paid_rate_percents
        self.name = name
        self.postponed_bonuses_delay_days = postponed_bonuses_delay_days
        self.spend_rate_points_to_rouble = spend_rate_points_to_rouble
        self.welcome_bonuses_enabled = welcome_bonuses_enabled
        self.welcome_bonuses_mode = welcome_bonuses_mode
        self.welcome_bonuses_value = welcome_bonuses_value

    def to_request(self) -> RequestData:
        json_data = {}
        if self.account_id != Unset:
            json_data["accountId"] = self.account_id
        if self.active != Unset:
            json_data["active"] = self.active
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.all_agents != Unset:
            json_data["allAgents"] = self.all_agents
        if self.all_products != Unset:
            json_data["allProducts"] = self.all_products
        if self.earn_rate_roubles_to_point != Unset:
            json_data["earnRateRoublesToPoint"] = self.earn_rate_roubles_to_point
        if self.earn_while_redeeming != Unset:
            json_data["earnWhileRedeeming"] = self.earn_while_redeeming
        if self.id != Unset:
            json_data["id"] = self.id
        if self.max_paid_rate_percents != Unset:
            json_data["maxPaidRatePercents"] = self.max_paid_rate_percents
        if self.name != Unset:
            json_data["name"] = self.name
        if self.postponed_bonuses_delay_days != Unset:
            json_data["postponedBonusesDelayDays"] = self.postponed_bonuses_delay_days
        if self.spend_rate_points_to_rouble != Unset:
            json_data["spendRatePointsToRouble"] = self.spend_rate_points_to_rouble
        if self.welcome_bonuses_enabled != Unset:
            json_data["welcomeBonusesEnabled"] = self.welcome_bonuses_enabled
        if self.welcome_bonuses_mode != Unset:
            json_data["welcomeBonusesMode"] = self.welcome_bonuses_mode
        if self.welcome_bonuses_value != Unset:
            json_data["welcomeBonusesValue"] = self.welcome_bonuses_value
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/REPLACEME", json=json_data
        )

    def from_response(self, response: dict) -> BonusProgram:
        return BonusProgram.from_json(response)


class DeleteBonusProgramRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/bonusprogram/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, response: dict) -> None:
        return None


class UpdateBonusProgramRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        account_id: typing.Union[Unset, str] = Unset,
        active: typing.Union[Unset, bool] = Unset,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        all_agents: typing.Union[Unset, bool] = Unset,
        all_products: typing.Union[Unset, bool] = Unset,
        earn_rate_roubles_to_point: typing.Union[Unset, int] = Unset,
        earn_while_redeeming: typing.Union[Unset, bool] = Unset,
        id: typing.Union[Unset, str] = Unset,
        max_paid_rate_percents: typing.Union[Unset, int] = Unset,
        name: typing.Union[Unset, str] = Unset,
        postponed_bonuses_delay_days: typing.Union[Unset, int] = Unset,
        spend_rate_points_to_rouble: typing.Union[Unset, int] = Unset,
        welcome_bonuses_enabled: typing.Union[Unset, bool] = Unset,
        welcome_bonuses_mode: typing.Union[Unset, str] = Unset,
        welcome_bonuses_value: typing.Union[Unset, int] = Unset,
    ):
        self.id = id_
        self.account_id = account_id
        self.active = active
        self.agent_tags = agent_tags
        self.all_agents = all_agents
        self.all_products = all_products
        self.earn_rate_roubles_to_point = earn_rate_roubles_to_point
        self.earn_while_redeeming = earn_while_redeeming
        self.id = id
        self.max_paid_rate_percents = max_paid_rate_percents
        self.name = name
        self.postponed_bonuses_delay_days = postponed_bonuses_delay_days
        self.spend_rate_points_to_rouble = spend_rate_points_to_rouble
        self.welcome_bonuses_enabled = welcome_bonuses_enabled
        self.welcome_bonuses_mode = welcome_bonuses_mode
        self.welcome_bonuses_value = welcome_bonuses_value

    def to_request(self) -> RequestData:
        json_data = {}
        if self.account_id != Unset:
            json_data["accountId"] = self.account_id
        if self.active != Unset:
            json_data["active"] = self.active
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.all_agents != Unset:
            json_data["allAgents"] = self.all_agents
        if self.all_products != Unset:
            json_data["allProducts"] = self.all_products
        if self.earn_rate_roubles_to_point != Unset:
            json_data["earnRateRoublesToPoint"] = self.earn_rate_roubles_to_point
        if self.earn_while_redeeming != Unset:
            json_data["earnWhileRedeeming"] = self.earn_while_redeeming
        if self.id != Unset:
            json_data["id"] = self.id
        if self.max_paid_rate_percents != Unset:
            json_data["maxPaidRatePercents"] = self.max_paid_rate_percents
        if self.name != Unset:
            json_data["name"] = self.name
        if self.postponed_bonuses_delay_days != Unset:
            json_data["postponedBonusesDelayDays"] = self.postponed_bonuses_delay_days
        if self.spend_rate_points_to_rouble != Unset:
            json_data["spendRatePointsToRouble"] = self.spend_rate_points_to_rouble
        if self.welcome_bonuses_enabled != Unset:
            json_data["welcomeBonusesEnabled"] = self.welcome_bonuses_enabled
        if self.welcome_bonuses_mode != Unset:
            json_data["welcomeBonusesMode"] = self.welcome_bonuses_mode
        if self.welcome_bonuses_value != Unset:
            json_data["welcomeBonusesValue"] = self.welcome_bonuses_value
        return RequestData(
            method="PUT", url=f"{helpers.BASE_URL}/entity/bonusprogram/{self.id}", json=json_data
        )

    def from_response(self, response: dict) -> BonusProgram:
        return BonusProgram.from_json(response)


class GetBonusProgramsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: int = 1000,
        offset: int = 0,
    ):
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {
            "limit": self.limit,
            "offset": self.offset,
        }
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bonusprogram",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[BonusProgram]:
        return [BonusProgram.from_json(x) for x in result["rows"]]


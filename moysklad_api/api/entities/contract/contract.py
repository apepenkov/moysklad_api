import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Contract(types.MoySkladBaseClass):
    """
    accountId           | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    agent               | Meta        | Метаданные Контрагента. Обязательное при ответе, Необходимо при создании, Expand
    agentAccount        | Meta        | Метаданные счета контрагента. Обязательное при ответе, Expand
    archived            | Boolean     | Добавлен ли Договор в архив. Обязательное при ответе
    attributes          | Array(Object)| Коллекция доп. полей
    code                | String(255) | Код Договора
    contractType         | Enum        | Тип Договора: Commission, Sales. Обязательное при ответе
    description         | String(4096)| Описание Договора
    externalCode        | String(255) | Внешний код Договора. Обязательное при ответе
    group               | Meta        | Метаданные отдела сотрудника. Обязательное при ответе, Expand
    id                  | UUID        | ID Договора. Обязательное при ответе, Только для чтения
    meta                | Meta        | Метаданные Договора. Обязательное при ответе
    moment              | DateTime    | Дата Договора. Обязательное при ответе
    name                | String(255) | Номер договора. Обязательное при ответе
    organizationAccount  | Meta        | Метаданные счета вашего юрлица. Expand
    ownAgent            | Meta        | Метаданные вашего юрлица. Обязательное при ответе, Необходимо при создании, Expand
    owner               | Meta        | Метаданные владельца (Сотрудника). Expand
    rate                | Meta        | Метаданные валюты. Обязательное при ответе, Expand
    rewardPercent        | Int         | Вознаграждение в процентах (от 0 до 100)
    rewardType           | Enum        | Тип Вознаграждения: PercentOfSales, None
    shared               | Boolean     | Общий доступ. Обязательное при ответе
    state                | Meta        | Метаданные статуса договора. Expand
    sum                  | Int         | Сумма Договора. Обязательное при ответе
    printed              | Boolean     | Напечатан ли документ. Обязательное при ответе, Только для чтения
    published            | Boolean     | Опубликован ли документ. Обязательное при ответе, Только для чтения
    updated              | DateTime    | Момент последнего обновления сущности. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    agent_account: typing.Optional[types.Meta]
    archived: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    contract_type: typing.Optional[typing.Literal["Commission", "Sales"]]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization_account: typing.Optional[types.Meta]
    own_agent: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    rate: typing.Optional[dict]
    reward_percent: typing.Optional[int]
    reward_type: typing.Optional[typing.Literal["PercentOfSales", "None"]]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sum: typing.Optional[int]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Contract":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount"))
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.contract_type = dict_data.get("contractType")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.own_agent = helpers.get_meta(dict_data.get("ownAgent"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.rate = dict_data.get("rate")
        instance.reward_percent = dict_data.get("rewardPercent")
        instance.reward_type = dict_data.get("rewardType")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("contract",)


class GetContractsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.search != Unset:
            params["search"] = self.search
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/contract",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Contract]:
        return [Contract.from_json(x) for x in result["rows"]]


class CreateContractRequest(types.ApiRequest):
    def __init__(
        self,
        agent: types.Meta,
        own_agent: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract_type: typing.Union[
            Unset, typing.Literal["Commission", "Sales"]
        ] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Meta] = Unset,
        reward_percent: typing.Union[Unset, int] = Unset,
        reward_type: typing.Union[
            Unset, typing.Literal["PercentOfSales", "None"]
        ] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sum_: typing.Union[Unset, int] = Unset,
    ):
        self.agent = agent
        self.own_agent = own_agent
        self.agent_account = agent_account
        self.archived = archived
        self.attributes = attributes
        self.code = code
        self.contract_type = contract_type
        self.description = description
        self.external_code = external_code
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.rate = rate
        self.reward_percent = reward_percent
        self.reward_type = reward_type
        self.shared = shared
        self.state = state
        self.sum = sum_

    def to_request(self) -> RequestData:
        json_data = {
            "agent": {"meta": self.agent},
            "ownAgent": {"meta": self.own_agent},
        }
        if self.agent_account != Unset:
            json_data["agentAccount"] = {"meta": self.agent_account}
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.contract_type != Unset:
            json_data["contractType"] = self.contract_type
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization_account != Unset:
            json_data["organizationAccount"] = {"meta": self.organization_account}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.rate != Unset:
            json_data["rate"] = {"meta": self.rate}
        if self.reward_percent != Unset:
            json_data["rewardPercent"] = self.reward_percent
        if self.reward_type != Unset:
            json_data["rewardType"] = self.reward_type
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.state != Unset:
            json_data["state"] = {"meta": self.state}
        if self.sum != Unset:
            json_data["sum"] = self.sum
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/contract",
            json=json_data,
        )

    def from_response(self, result: dict) -> Contract:
        return Contract.from_json(result)


class DeleteContractRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/contract/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetContractRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/contract/{self.id}",
        )

    def from_response(self, result: dict) -> Contract:
        return Contract.from_json(result)


class UpdateContractRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        agent: typing.Union[Unset, types.Meta] = Unset,
        own_agent: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract_type: typing.Union[
            Unset, typing.Literal["Commission", "Sales"]
        ] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Meta] = Unset,
        reward_percent: typing.Union[Unset, int] = Unset,
        reward_type: typing.Union[
            Unset, typing.Literal["PercentOfSales", "None"]
        ] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sum_: typing.Union[Unset, int] = Unset,
    ):
        self.id = id_
        self.agent = agent
        self.own_agent = own_agent
        self.agent_account = agent_account
        self.archived = archived
        self.attributes = attributes
        self.code = code
        self.contract_type = contract_type
        self.description = description
        self.external_code = external_code
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.rate = rate
        self.reward_percent = reward_percent
        self.reward_type = reward_type
        self.shared = shared
        self.state = state
        self.sum = sum_

    def to_request(self) -> RequestData:
        json_data = {}
        if self.agent != Unset:
            json_data["agent"] = {"meta": self.agent}
        if self.own_agent != Unset:
            json_data["ownAgent"] = {"meta": self.own_agent}
        if self.agent_account != Unset:
            json_data["agentAccount"] = {"meta": self.agent_account}
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.contract_type != Unset:
            json_data["contractType"] = self.contract_type
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization_account != Unset:
            json_data["organizationAccount"] = {"meta": self.organization_account}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.rate != Unset:
            json_data["rate"] = {"meta": self.rate}
        if self.reward_percent != Unset:
            json_data["rewardPercent"] = self.reward_percent
        if self.reward_type != Unset:
            json_data["rewardType"] = self.reward_type
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.state != Unset:
            json_data["state"] = {"meta": self.state}
        if self.sum != Unset:
            json_data["sum"] = self.sum
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/contract/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Contract:
        return Contract.from_json(result)

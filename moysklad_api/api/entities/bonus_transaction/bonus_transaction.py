import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


# https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-bonusnaq-operaciq-bonusnye-operacii
class BonusTransaction(types.MoySkladBaseClass):
    """
    accountId 	        UUID 	= != 	ID учетной записи  Обязательное при ответе Только для чтения
    agent 	            Meta 	= != 	Метаданные Контрагента, связанного с бонусной операцией Обязательное при ответе Expand Необходимо при создании
    applicable 	        Boolean 	= != 	Отметка о проведении Обязательное при ответе
    bonusProgram 	    Meta 	= != 	Метаданные бонусной программы Expand
    bonusValue 	        Int 	= != < > <= >= 	Количество бонусных баллов
    categoryType 	    Enum 		Категория бонусной операции. Возможные значения: REGULAR, WELCOME Только для чтения
    code 	            String(255) 	= != ~ ~= =~ 	Код Бонусной операции
    created 	        DateTime 	= != < > <= >= 	Момент создания Бонусной операции Обязательное при ответе
    executionDate 	    DateTime 		Дата начисления бонусной операции.
    externalCode 	    String(255) 	= != ~ ~= =~ 	Внешний код Бонусной операции Обязательное при ответе
    group 	            Meta 	= != 	Отдел сотрудника Обязательное при ответе Expand
    id 	                UUID 	= != 	ID Бонусной операции Обязательное при ответе Только для чтения
    meta 	            Meta 		Метаданные Бонусной операции Обязательное при ответе
    moment 	            DateTime 	= != < > <= >= 	Время проведения бонусной операции
    name 	            String(255) 	= != ~ ~= =~ 	Наименование Бонусной операции
    organization 	    Meta 	= != 	Метаданные юрлица Expand
    owner 	            Meta 	= != 	Владелец (Сотрудник) Expand
    parentDocument 	    Meta 		Метаданные связанного документа бонусной операции Expand
    shared 	            Boolean 	= != 	Общий доступ Обязательное при ответе
    transactionStatus 	Enum 		Статус бонусной операции. Возможные значения: WAIT_PROCESSING, COMPLETED, CANCELED Только для чтения
    transactionType 	Enum 		Тип бонусной операции. Возможные значения: EARNING, SPENDING Обязательное при ответе Необходимо при создании
    updated 	        DateTime 	= != < > <= >= 	Момент последнего обновления Бонусной операции Обязательное при ответе
    updatedBy 	        UID 	= != 	Автор последнего обновления бонусной операции в формате uid (admin@admin) (Атрибут используется только для фильтрации)
    """

    meta: types.Meta
    id: str
    account_id: str
    agent: types.Meta
    applicable: bool
    bonus_program: typing.Optional[types.Meta]
    bonus_value: typing.Optional[int]
    category_type: typing.Optional[str]
    code: typing.Optional[str]
    created: datetime.datetime
    execution_date: typing.Optional[datetime.datetime]
    external_code: str
    group: types.Meta
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    parent_document: typing.Optional[types.Meta]
    shared: bool
    transaction_status: typing.Optional[
        typing.Literal["WAIT_PROCESSING", "COMPLETED", "CANCELED"]
    ]
    transaction_type: typing.Literal["EARNING", "SPENDING"]
    updated: datetime.datetime
    updated_by: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "BonusTransaction":
        instance = cls()

        instance.meta = dict_data.get("meta")
        instance.id = dict_data.get("id")
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.applicable = dict_data.get("applicable")
        instance.bonus_program = helpers.get_meta(dict_data.get("bonusProgram"))
        instance.bonus_value = dict_data.get("bonusValue")
        instance.category_type = dict_data.get("categoryType")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.execution_date = helpers.parse_date(dict_data.get("executionDate"))
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.parent_document = helpers.get_meta(dict_data.get("parentDocument"))
        instance.shared = dict_data.get("shared")
        instance.transaction_status = dict_data.get("transactionStatus")
        instance.transaction_type = dict_data.get("transactionType")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.updated_by = dict_data.get("updatedBy")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return ("bonustransaction",)


class GetBonusTransactionsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: int = 1000,
        offset: int = 0,
        filter_: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.filter = filter_

    def to_request(self) -> RequestData:
        params = {
            "limit": self.limit,
            "offset": self.offset,
        }
        if self.filter != Unset:
            params["filter"] = self.filter
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bonustransaction",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List["BonusTransaction"]:
        return [BonusTransaction.from_json(x) for x in result["rows"]]


class CreateBonusTransactionRequest(types.ApiRequest):
    def __init__(
        self,
        agent: types.Meta,
        bonus_program: types.Meta,
        transaction_type: str,
        applicable: typing.Union[Unset, bool] = Unset,
        bonus_value: typing.Union[Unset, int] = Unset,
        code: typing.Union[Unset, str] = Unset,
        created: typing.Union[Unset, datetime.datetime] = Unset,
        execution_date: typing.Union[Unset, datetime.datetime] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent_document: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.agent = agent
        self.bonus_program = bonus_program
        self.transaction_type = transaction_type
        self.applicable = applicable
        self.bonus_value = bonus_value
        self.code = code
        self.created = created
        self.execution_date = execution_date
        self.group = group
        self.moment = moment
        self.name = name
        self.organization = organization
        self.owner = owner
        self.parent_document = parent_document
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {
            "agent": self.agent,
            "bonusProgram": self.bonus_program,
            "transactionType": self.transaction_type,
        }
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.bonus_value != Unset:
            json_data["bonusValue"] = self.bonus_value
        if self.code != Unset:
            json_data["code"] = self.code
        if self.created != Unset:
            json_data["created"] = helpers.date_to_str(self.created)
        if self.execution_date != Unset:
            json_data["executionDate"] = helpers.date_to_str(self.execution_date)
        if self.group != Unset:
            json_data["group"] = self.group
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization != Unset:
            json_data["organization"] = self.organization
        if self.owner != Unset:
            json_data["owner"] = self.owner
        if self.parent_document != Unset:
            json_data["parentDocument"] = self.parent_document
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/bonustransaction",
            json=json_data,
        )

    def from_response(self, result: dict) -> BonusTransaction:
        return BonusTransaction.from_json(result)


class DeleteBonusTransactionRequest(types.ApiRequest):
    def __init__(self, bonus_transaction_id: str):
        self.bonus_transaction_id = bonus_transaction_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/bonustransaction/{self.bonus_transaction_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetBonusTransactionRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/bonustransaction/{self.id}",
        )

    def from_response(self, result: dict) -> BonusTransaction:
        return BonusTransaction.from_json(result)


class UpdateBonusTransactionRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        agent: typing.Union[Unset, types.Meta] = Unset,
        bonus_program: typing.Union[Unset, types.Meta] = Unset,
        transaction_type: typing.Union[Unset, str] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        bonus_value: typing.Union[Unset, int] = Unset,
        code: typing.Union[Unset, str] = Unset,
        created: typing.Union[Unset, datetime.datetime] = Unset,
        execution_date: typing.Union[Unset, datetime.datetime] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent_document: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.agent = agent
        self.bonus_program = bonus_program
        self.transaction_type = transaction_type
        self.applicable = applicable
        self.bonus_value = bonus_value
        self.code = code
        self.created = created
        self.execution_date = execution_date
        self.group = group
        self.moment = moment
        self.name = name
        self.organization = organization
        self.owner = owner
        self.parent_document = parent_document
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {}
        if self.agent != Unset:
            json_data["agent"] = self.agent
        if self.bonus_program != Unset:
            json_data["bonusProgram"] = self.bonus_program
        if self.transaction_type != Unset:
            json_data["transactionType"] = self.transaction_type
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.bonus_value != Unset:
            json_data["bonusValue"] = self.bonus_value
        if self.code != Unset:
            json_data["code"] = self.code
        if self.created != Unset:
            json_data["created"] = helpers.date_to_str(self.created)
        if self.execution_date != Unset:
            json_data["executionDate"] = helpers.date_to_str(self.execution_date)
        if self.group != Unset:
            json_data["group"] = self.group
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization != Unset:
            json_data["organization"] = self.organization
        if self.owner != Unset:
            json_data["owner"] = self.owner
        if self.parent_document != Unset:
            json_data["parentDocument"] = self.parent_document
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/bonustransaction/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> BonusTransaction:
        return BonusTransaction.from_json(result)


# TODO: implement friendly methods

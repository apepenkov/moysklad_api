import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Employee(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived     | Boolean     | Добавлен ли Сотрудник в архив. Обязательное при ответе
    attributes   | Array(Object)| Дополнительные поля Сотрудника
    cashiers     | MetaArray   | Массив кассиров. Только для чтения, Expand
    created      | DateTime    | Момент создания Сотрудника. Обязательное при ответе, Только для чтения
    description  | String(4096)| Комментарий к Сотруднику
    email        | String(255) | Электронная почта сотрудника
    externalCode | String(255) | Внешний код Сотрудника. Обязательное при ответе
    firstName    | String(255) | Имя
    fullName     | String(255) | Имя Отчество Фамилия. Только для чтения
    group        | Meta        | Отдел сотрудника. Обязательное при ответе, Expand
    id           | UUID        | ID Сотрудника. Обязательное при ответе, Только для чтения
    image        | Object      | Фотография сотрудника
    inn          | String(255) | ИНН сотрудника
    lastName     | String(255) | Фамилия. Обязательное при ответе, Необходимо при создании
    meta         | Meta        | Метаданные Сотрудника. Обязательное при ответе
    middleName   | String(255) | Отчество
    name         | String(255) | Наименование Сотрудника. Обязательное при ответе, Только для чтения
    owner        | Meta        | Владелец (Сотрудник). Обязательное при ответе, Expand
    phone        | String(255) | Телефон сотрудника
    position     | String(255) | Должность сотрудника
    salary       | Object      | Оклад сотрудника ({"value": float})
    shared       | Boolean     | Общий доступ. Обязательное при ответе
    shortFio     | String(255) | Краткое ФИО. Только для чтения
    uid          | String(255) | Логин Сотрудника. Только для чтения
    updated      | DateTime    | Момент последнего обновления Сотрудника. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    cashiers: typing.Optional[dict]
    created: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    email: typing.Optional[str]
    external_code: typing.Optional[str]
    first_name: typing.Optional[str]
    full_name: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    image: typing.Optional[dict]
    inn: typing.Optional[str]
    last_name: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    middle_name: typing.Optional[str]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    phone: typing.Optional[str]
    position: typing.Optional[str]
    salary: typing.Optional[dict]
    shared: typing.Optional[bool]
    short_fio: typing.Optional[str]
    uid: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Employee":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.cashiers = dict_data.get("cashiers")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.email = dict_data.get("email")
        instance.external_code = dict_data.get("externalCode")
        instance.first_name = dict_data.get("firstName")
        instance.full_name = dict_data.get("fullName")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.image = dict_data.get("image")
        instance.inn = dict_data.get("inn")
        instance.last_name = dict_data.get("lastName")
        instance.meta = dict_data.get("meta")
        instance.middle_name = dict_data.get("middleName")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.phone = dict_data.get("phone")
        instance.position = dict_data.get("position")
        instance.salary = dict_data.get("salary")
        instance.shared = dict_data.get("shared")
        instance.short_fio = dict_data.get("shortFio")
        instance.uid = dict_data.get("uid")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("employee",)


class GetEmployeesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/employee",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Employee]:
        return [Employee.from_json(x) for x in result["rows"]]


class GetEmployeeRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/employee/{self.id}",
        )

    def from_response(self, result: dict) -> Employee:
        return Employee.from_json(result)


class CreateEmployeeRequest(types.ApiRequest):
    def __init__(
        self,
        last_name: str,
        first_name: typing.Union[Unset, str] = Unset,
        middle_name: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        email: typing.Union[Unset, str] = Unset,
        phone: typing.Union[Unset, str] = Unset,
        position: typing.Union[Unset, str] = Unset,
        inn: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        salary: typing.Union[Unset, dict] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.description = description
        self.email = email
        self.phone = phone
        self.position = position
        self.inn = inn
        self.external_code = external_code
        self.archived = archived
        self.group = group
        self.owner = owner
        self.shared = shared
        self.salary = salary
        self.attributes = attributes

    def to_request(self) -> RequestData:
        json_data = {"lastName": self.last_name}
        if self.first_name != Unset:
            json_data["firstName"] = self.first_name
        if self.middle_name != Unset:
            json_data["middleName"] = self.middle_name
        if self.description != Unset:
            json_data["description"] = self.description
        if self.email != Unset:
            json_data["email"] = self.email
        if self.phone != Unset:
            json_data["phone"] = self.phone
        if self.position != Unset:
            json_data["position"] = self.position
        if self.inn != Unset:
            json_data["inn"] = self.inn
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.salary != Unset:
            json_data["salary"] = self.salary
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/employee",
            json=json_data,
        )

    def from_response(self, result: dict) -> Employee:
        return Employee.from_json(result)


class DeleteEmployeeRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/employee/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class UpdateEmployeeRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        first_name: typing.Union[Unset, str] = Unset,
        last_name: typing.Union[Unset, str] = Unset,
        middle_name: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        email: typing.Union[Unset, str] = Unset,
        phone: typing.Union[Unset, str] = Unset,
        position: typing.Union[Unset, str] = Unset,
        inn: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        salary: typing.Union[Unset, dict] = Unset,
        image: typing.Union[Unset, dict] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.id = id_
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.description = description
        self.email = email
        self.phone = phone
        self.position = position
        self.inn = inn
        self.archived = archived
        self.group = group
        self.owner = owner
        self.shared = shared
        self.salary = salary
        self.image = image
        self.attributes = attributes

    def to_request(self) -> RequestData:
        json_data = {}
        if self.first_name != Unset:
            json_data["firstName"] = self.first_name
        if self.last_name != Unset:
            json_data["lastName"] = self.last_name
        if self.middle_name != Unset:
            json_data["middleName"] = self.middle_name
        if self.description != Unset:
            json_data["description"] = self.description
        if self.email != Unset:
            json_data["email"] = self.email
        if self.phone != Unset:
            json_data["phone"] = self.phone
        if self.position != Unset:
            json_data["position"] = self.position
        if self.inn != Unset:
            json_data["inn"] = self.inn
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.group != Unset:
            json_data["group"] = {"meta": self.group}
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.salary != Unset:
            json_data["salary"] = self.salary
        if self.image != Unset:
            json_data["image"] = self.image
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/employee/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Employee:
        return Employee.from_json(result)

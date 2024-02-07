import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Organization(types.MoySkladBaseClass):
    """
    Название               Тип          Описание
    accountId              UUID         ID учетной записи  Обязательное при ответе, Только для чтения
    actualAddress          String(255)  Фактический адрес Юрлица
    actualAddressFull      Object       Фактический адрес Юрлица с детализацией по отдельным полям. Подробнее тут
    archived               Boolean      Добавлено ли Юрлицо в архив Обязательное при ответе
    attributes             Array        Массив метаданных доп. полей Обязательное при ответе
    bonusPoints            Int          Бонусные баллы по активной бонусной программе Только для чтения
    bonusProgram           Meta         Метаданные активной бонусной программы
    code                   String(255)  Код Юрлица
    companyType            Enum         Тип Юрлица . В зависимости от значения данного поля набор выводимых реквизитов контрагента может меняться. Подробнее тут Обязательное при ответе
    created                DateTime     Дата создания Обязательное при ответе
    description            String(4096) Комментарий к Юрлицу
    externalCode           String(255)  Внешний код Юрлица Обязательное при ответе
    group                  Meta         Отдел сотрудника  Обязательное при ответе
    id                     UUID         ID Юрлица  Обязательное при ответе, Только для чтения
    meta                   Meta         Метаданные Юрлица Обязательное при ответе
    name                   String(255)  Наименование Юрлица  Обязательное при ответе
    owner                  Meta         Владелец (Сотрудник)
    shared                 Boolean      Общий доступ Обязательное при ответе
    syncId                 UUID         ID синхронизации
    trackingContractDate   DateTime     Дата договора с ЦРПТ
    trackingContractNumber String(255)  Номер договора с ЦРПТ
    updated                DateTime     Момент последнего обновления Юрлица  Обязательное при ответе, Только для чтения
    """

    account_id: str
    actual_address: typing.Optional[str]
    actual_address_full: typing.Optional[dict]
    archived: bool
    attributes: typing.List[dict]
    bonus_points: typing.Optional[int]
    bonus_program: typing.Optional[types.Meta]
    code: typing.Optional[str]
    company_type: typing.Literal["legal", "entrepreneur", "individual"]
    created: datetime.datetime
    description: typing.Optional[str]
    external_code: str
    group: types.Meta
    id: str
    meta: types.Meta
    name: str
    owner: typing.Optional[types.Meta]
    shared: bool
    sync_id: typing.Optional[str]
    tracking_contract_date: typing.Optional[datetime.datetime]
    tracking_contract_number: typing.Optional[str]
    updated: datetime.datetime

    @classmethod
    def from_json(cls, dict_data: dict) -> "Organization":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.actual_address = dict_data.get("actualAddress")
        instance.actual_address_full = dict_data.get("actualAddressFull")
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.bonus_points = dict_data.get("bonusPoints")
        instance.bonus_program = helpers.get_meta(dict_data.get("bonusProgram"))
        instance.code = dict_data.get("code")
        instance.company_type = dict_data.get("companyType")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.shared = dict_data.get("shared")
        instance.sync_id = dict_data.get("syncId")
        instance.tracking_contract_date = helpers.parse_date(
            dict_data.get("trackingContractDate")
        )
        instance.tracking_contract_number = dict_data.get("trackingContractNumber")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return ("organization",)


class GetOrganizationsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-jurlico-poluchit-spisok-urlic

    Параметр 	Описание
    limit 	number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """

        :param limit:  Limit (макс. )
        :param offset: Offset (Смещение)
        """
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
            url=f"{helpers.BASE_URL}/entity/organization",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Organization]:
        return [Organization.from_json(org) for org in result["rows"]]


class CreateOrganizationRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-jurlico-sozdat-urlico

    """

    def __init__(
        self,
        name: str,
        actual_address: typing.Union[Unset, str] = Unset,
        actual_address_full: typing.Union[Unset, dict] = Unset,
        archived: bool = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        bonus_program: typing.Union[Unset, types.Meta] = Unset,
        code: typing.Union[Unset, str] = Unset,
        company_type: typing.Literal["legal", "entrepreneur", "individual"] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: str = Unset,
        group: types.Meta = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: bool = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tracking_contract_date: typing.Union[Unset, datetime.datetime] = Unset,
        tracking_contract_number: typing.Union[Unset, str] = Unset,
    ):
        """

        :param name: Name of organization (Название организации)
        :param actual_address: Actual address (Фактический адрес)
        :param actual_address_full: Actual address full (Полный фактический адрес)
        :param archived: Is archived (Архивирован)
        :param attributes: Attributes (Массив метаданных доп. полей)
        :param bonus_program: Bonus program (Бонусная программа)
        :param code: Code (Код)
        :param company_type: Company type (Тип компании)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param group: Group (Группа)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий доступ)
        :param sync_id: Sync id (Синхронизационный id)
        :param tracking_contract_date: Tracking contract date (Дата договора отслеживания)
        :param tracking_contract_number: Tracking contract number (Номер договора отслеживания)
        """
        self.name = name
        self.actual_address = actual_address
        self.actual_address_full = actual_address_full
        self.attributes = attributes
        self.archived = archived
        self.bonus_program = bonus_program
        self.code = code
        self.company_type = company_type
        self.description = description
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.shared = shared
        self.sync_id = sync_id
        self.tracking_contract_date = tracking_contract_date
        self.tracking_contract_number = tracking_contract_number

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
        }
        if self.actual_address != Unset:
            json_data["actualAddress"] = self.actual_address
        if self.actual_address_full != Unset:
            json_data["actualAddressFull"] = self.actual_address_full
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.bonus_program != Unset:
            json_data["bonusProgram"] = (
                {"meta": self.bonus_program} if self.bonus_program is not None else None
            )
        if self.code != Unset:
            json_data["code"] = self.code
        if self.company_type != Unset:
            json_data["companyType"] = self.company_type
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group} if self.group is not None else None
            )
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.tracking_contract_date != Unset:
            json_data["trackingContractDate"] = helpers.date_to_str(
                self.tracking_contract_date
            )
        if self.tracking_contract_number != Unset:
            json_data["trackingContractNumber"] = self.tracking_contract_number

        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/organization",
            json=json_data,
        )

    def from_response(self, result: dict) -> Organization:
        return Organization.from_json(result)


class DeleteOrganizationRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-jurlico-udalit-urlico

    """

    def __init__(self, organization_id: str):
        self.id = organization_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/organization/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return


class GetOrganizationRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-jurlico-poluchit-urlico

    """

    def __init__(self, organization_id: str):
        self.id = organization_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/organization/{self.id}",
        )

    def from_response(self, result: dict) -> Organization:
        return Organization.from_json(result)


class UpdateOrganizationRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-jurlico-obnovit-urlico

    """

    def __init__(
        self,
        organization_id: str,
        name: typing.Union[Unset, str] = Unset,
        actual_address: typing.Union[Unset, str] = Unset,
        actual_address_full: typing.Union[Unset, dict] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        bonus_program: typing.Union[Unset, types.Meta] = Unset,
        code: typing.Union[Unset, str] = Unset,
        company_type: typing.Literal["legal", "entrepreneur", "individual"] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: types.Meta = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tracking_contract_date: typing.Union[Unset, datetime.datetime] = Unset,
        tracking_contract_number: typing.Union[Unset, str] = Unset,
    ):
        """

        :param organization_id: Organization id (Идентификатор организации)
        :param name: Name of organization (Название организации)
        :param actual_address: Actual address (Фактический адрес)
        :param actual_address_full: Actual address full (Полный фактический адрес)
        :param archived: Is archived (Архивирован)
        :param attributes: Attributes (Массив метаданных доп. полей)
        :param bonus_program: Bonus program (Бонусная программа)
        :param code: Code (Код)
        :param company_type: Company type (Тип компании)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param group: Group (Группа)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий доступ)
        :param sync_id: Sync id (Синхронизационный id)
        :param tracking_contract_date: Tracking contract date (Дата договора отслеживания)
        :param tracking_contract_number: Tracking contract number (Номер договора отслеживания)
        """
        self.id = organization_id
        self.name = name
        self.actual_address = actual_address
        self.actual_address_full = actual_address_full
        self.archived = archived
        self.attributes = attributes
        self.bonus_program = bonus_program
        self.code = code
        self.company_type = company_type
        self.description = description
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.shared = shared
        self.sync_id = sync_id
        self.tracking_contract_date = tracking_contract_date
        self.tracking_contract_number = tracking_contract_number

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.actual_address != Unset:
            json_data["actualAddress"] = self.actual_address
        if self.actual_address_full != Unset:
            json_data["actualAddressFull"] = self.actual_address_full
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.bonus_program != Unset:
            json_data["bonusProgram"] = (
                {"meta": self.bonus_program} if self.bonus_program is not None else None
            )
        if self.code != Unset:
            json_data["code"] = self.code
        if self.company_type != Unset:
            json_data["companyType"] = self.company_type
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group} if self.group is not None else None
            )
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.tracking_contract_date != Unset:
            json_data["trackingContractDate"] = helpers.date_to_str(
                self.tracking_contract_date
            )
        if self.tracking_contract_number != Unset:
            json_data["trackingContractNumber"] = self.tracking_contract_number

        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/organization/" + self.id,
            json=json_data,
        )

    def from_response(self, result: dict) -> Organization:
        return Organization.from_json(result)

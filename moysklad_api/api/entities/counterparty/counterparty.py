import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

CompanyType = typing.Literal["legal", "entrepreneur", "individual"]


class Counterparty(types.MoySkladBaseClass):
    """
    Контрагент. Полный перечень полей (в т.ч. регионоспецифичных реквизитов) -
    см. W:\\stuff\\api-remap-1.2-doc\\md\\dictionaries\\_counterparty.md
    Ниже перечислены основные поля; редкие регионоспецифичные объекты
    (mod__requisites__uz/kz, addressFull) переданы как dict.

    accountId           | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    accounts            | MetaArray   | Счета Контрагента. Обязательное при ответе, Expand
    actualAddress        | String(255) | Фактический адрес
    actualAddressFull     | Object      | Фактический адрес (детализированный)
    archived               | Boolean     | Добавлен ли Контрагент в архив. Обязательное при ответе
    attributes              | Array(Object)| Доп. поля
    bonusPoints               | Int         | Бонусные баллы. Только для чтения
    bonusProgram                | Meta        | Активная бонусная программа. Expand
    code                          | String(255) | Код Контрагента
    companyType                    | Enum        | Тип Контрагента. Обязательное при ответе
    contactpersons                   | MetaArray   | Контактные лица. Expand
    created                            | DateTime    | Момент создания. Обязательное при ответе, Только для чтения
    description                          | String(4096)| Комментарий
    discountCardNumber                     | String(255) | Номер дисконтной карты
    discounts                                | Array(Object)| Скидки Контрагента
    email                                      | String(255) | Email
    externalCode                                | String(255) | Внешний код. Обязательное при ответе
    fax                                           | String(255) | Факс
    files                                          | MetaArray   | Файлы. Обязательное при ответе, Expand
    group                                            | Meta        | Отдел сотрудника. Обязательное при ответе, Expand
    id                                                 | UUID        | ID Контрагента. Обязательное при ответе, Только для чтения
    meta                                                | Meta        | Метаданные Контрагента. Обязательное при ответе
    name                                                  | String(255) | Наименование. Обязательное при ответе, Необходимо при создании
    notes                                                   | MetaArray   | События Контрагента. Expand
    owner                                                     | Meta        | Владелец. Expand
    phone                                                       | String(255) | Телефон
    priceType                                                     | Object      | Тип цены Контрагента
    salesAmount                                                     | Int         | Сумма продаж. Обязательное при ответе, Только для чтения
    shared                                                            | Boolean     | Общий доступ. Обязательное при ответе
    state                                                               | Meta        | Статус Контрагента. Expand
    syncId                                                                | UUID        | ID синхронизации
    tags                                                                    | Array(String)| Группы контрагента
    updated                                                                  | DateTime    | Момент последнего обновления. Обязательное при ответе, Только для чтения
    birthDate                                                                  | DateTime    | Дата рождения (физлицо)
    certificateDate                                                             | DateTime    | Дата свидетельства
    certificateNumber                                                            | String(255) | Номер свидетельства
    inn                                                                            | String(255) | ИНН
    kpp                                                                             | String(255) | КПП
    legalAddress                                                                     | String(255) | Юридический адрес
    legalAddressFull                                                                   | Object      | Юридический адрес (детализированный)
    legalFirstName                                                                       | String(255) | Имя (ИП/физлицо)
    legalLastName                                                                          | String(255) | Фамилия (ИП/физлицо)
    legalMiddleName                                                                          | String(255) | Отчество (ИП/физлицо)
    legalTitle                                                                                 | String(4096)| Полное наименование (юрлицо)
    ogrn                                                                                          | String(255) | ОГРН
    ogrnip                                                                                          | String(255) | ОГРНИП
    okpo                                                                                            | String(255) | ОКПО
    sex                                                                                              | String(255) | Пол
    """

    account_id: typing.Optional[str]
    accounts: typing.Optional[dict]
    actual_address: typing.Optional[str]
    actual_address_full: typing.Optional[dict]
    archived: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    bonus_points: typing.Optional[int]
    bonus_program: typing.Optional[types.Meta]
    code: typing.Optional[str]
    company_type: typing.Optional[CompanyType]
    contactpersons: typing.Optional[dict]
    created: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    discount_card_number: typing.Optional[str]
    discounts: typing.Optional[typing.List[dict]]
    email: typing.Optional[str]
    external_code: typing.Optional[str]
    fax: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    notes: typing.Optional[dict]
    owner: typing.Optional[types.Meta]
    phone: typing.Optional[str]
    price_type: typing.Optional[dict]
    sales_amount: typing.Optional[int]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sync_id: typing.Optional[str]
    tags: typing.Optional[typing.List[str]]
    updated: typing.Optional[datetime.datetime]
    birth_date: typing.Optional[datetime.datetime]
    certificate_date: typing.Optional[datetime.datetime]
    certificate_number: typing.Optional[str]
    inn: typing.Optional[str]
    kpp: typing.Optional[str]
    legal_address: typing.Optional[str]
    legal_address_full: typing.Optional[dict]
    legal_first_name: typing.Optional[str]
    legal_last_name: typing.Optional[str]
    legal_middle_name: typing.Optional[str]
    legal_title: typing.Optional[str]
    ogrn: typing.Optional[str]
    ogrnip: typing.Optional[str]
    okpo: typing.Optional[str]
    sex: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Counterparty":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.accounts = dict_data.get("accounts")
        instance.actual_address = dict_data.get("actualAddress")
        instance.actual_address_full = dict_data.get("actualAddressFull")
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.bonus_points = dict_data.get("bonusPoints")
        instance.bonus_program = helpers.get_meta(dict_data.get("bonusProgram"))
        instance.code = dict_data.get("code")
        instance.company_type = dict_data.get("companyType")
        instance.contactpersons = dict_data.get("contactpersons")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.discount_card_number = dict_data.get("discountCardNumber")
        instance.discounts = dict_data.get("discounts")
        instance.email = dict_data.get("email")
        instance.external_code = dict_data.get("externalCode")
        instance.fax = dict_data.get("fax")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.notes = dict_data.get("notes")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.phone = dict_data.get("phone")
        instance.price_type = dict_data.get("priceType")
        instance.sales_amount = dict_data.get("salesAmount")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sync_id = dict_data.get("syncId")
        instance.tags = dict_data.get("tags")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.birth_date = helpers.parse_date(dict_data.get("birthDate"))
        instance.certificate_date = helpers.parse_date(
            dict_data.get("certificateDate")
        )
        instance.certificate_number = dict_data.get("certificateNumber")
        instance.inn = dict_data.get("inn")
        instance.kpp = dict_data.get("kpp")
        instance.legal_address = dict_data.get("legalAddress")
        instance.legal_address_full = dict_data.get("legalAddressFull")
        instance.legal_first_name = dict_data.get("legalFirstName")
        instance.legal_last_name = dict_data.get("legalLastName")
        instance.legal_middle_name = dict_data.get("legalMiddleName")
        instance.legal_title = dict_data.get("legalTitle")
        instance.ogrn = dict_data.get("ogrn")
        instance.ogrnip = dict_data.get("ogrnip")
        instance.okpo = dict_data.get("okpo")
        instance.sex = dict_data.get("sex")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("counterparty",)


def _build_counterparty_json(**fields) -> dict:
    name_map = {
        "name": "name",
        "actual_address": "actualAddress",
        "actual_address_full": "actualAddressFull",
        "archived": "archived",
        "attributes": "attributes",
        "bonus_program": "bonusProgram",
        "code": "code",
        "company_type": "companyType",
        "description": "description",
        "discount_card_number": "discountCardNumber",
        "email": "email",
        "external_code": "externalCode",
        "fax": "fax",
        "files": "files",
        "group": "group",
        "owner": "owner",
        "phone": "phone",
        "price_type": "priceType",
        "shared": "shared",
        "state": "state",
        "sync_id": "syncId",
        "tags": "tags",
        "birth_date": "birthDate",
        "certificate_date": "certificateDate",
        "certificate_number": "certificateNumber",
        "inn": "inn",
        "kpp": "kpp",
        "legal_address": "legalAddress",
        "legal_address_full": "legalAddressFull",
        "legal_first_name": "legalFirstName",
        "legal_last_name": "legalLastName",
        "legal_middle_name": "legalMiddleName",
        "legal_title": "legalTitle",
        "ogrn": "ogrn",
        "ogrnip": "ogrnip",
        "okpo": "okpo",
        "sex": "sex",
    }
    meta_fields = {"bonus_program", "group", "owner", "state"}
    date_fields = {"birth_date", "certificate_date"}
    json_data = {}
    for key, value in fields.items():
        if value is Unset:
            continue
        json_key = name_map[key]
        if key in meta_fields:
            json_data[json_key] = {"meta": value}
        elif key in date_fields:
            json_data[json_key] = helpers.date_to_str(value)
        else:
            json_data[json_key] = value
    return json_data


class GetCounterpartiesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/counterparty",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Counterparty]:
        return [Counterparty.from_json(x) for x in result["rows"]]


class CreateCounterpartyRequest(types.ApiRequest):
    def __init__(self, name: str, **kwargs):
        """
        :param name: Наименование Контрагента
        :param kwargs: Остальные необязательные поля (snake_case), см.
            Counterparty/_build_counterparty_json для полного списка ключей.
        """
        self.name = name
        self.kwargs = kwargs

    def to_request(self) -> RequestData:
        json_data = _build_counterparty_json(name=self.name, **self.kwargs)
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/counterparty",
            json=json_data,
        )

    def from_response(self, result: dict) -> Counterparty:
        return Counterparty.from_json(result)


class DeleteCounterpartyRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetCounterpartyRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.id}",
        )

    def from_response(self, result: dict) -> Counterparty:
        return Counterparty.from_json(result)


class UpdateCounterpartyRequest(types.ApiRequest):
    def __init__(self, id_: str, **kwargs):
        """
        :param id_: ID Контрагента
        :param kwargs: Поля для обновления (snake_case), см.
            Counterparty/_build_counterparty_json для полного списка ключей.
        """
        self.id = id_
        self.kwargs = kwargs

    def to_request(self) -> RequestData:
        json_data = _build_counterparty_json(**self.kwargs)
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Counterparty:
        return Counterparty.from_json(result)


# --- Счета Контрагента ---


class CounterpartyAccount(types.MoySkladBaseClass):
    """
    accountId            | UUID | ID учетной записи. Только для чтения
    accountNumber          | String(255)| Номер счета. Необходимо при создании
    bankLocation             | String(255)| Адрес банка
    bankName                  | String(255)| Наименование банка
    bic                         | String(255)| БИК
    correspondentAccount         | String(255)| Корр. счет
    id                             | UUID | ID Счета. Только для чтения
    isDefault                       | Boolean| Основной счет
    meta                              | Meta | Метаданные Счета
    updated                            | DateTime| Момент последнего обновления. Только для чтения
    """

    account_id: typing.Optional[str]
    account_number: typing.Optional[str]
    bank_location: typing.Optional[str]
    bank_name: typing.Optional[str]
    bic: typing.Optional[str]
    correspondent_account: typing.Optional[str]
    id: typing.Optional[str]
    is_default: typing.Optional[bool]
    meta: typing.Optional[types.Meta]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CounterpartyAccount":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.account_number = dict_data.get("accountNumber")
        instance.bank_location = dict_data.get("bankLocation")
        instance.bank_name = dict_data.get("bankName")
        instance.bic = dict_data.get("bic")
        instance.correspondent_account = dict_data.get("correspondentAccount")
        instance.id = dict_data.get("id")
        instance.is_default = dict_data.get("isDefault")
        instance.meta = dict_data.get("meta")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("counterparty", "accounts")


class GetCounterpartyAccountsRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str):
        self.counterparty_id = counterparty_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/accounts",
        )

    def from_response(self, result: dict) -> typing.List[CounterpartyAccount]:
        return [CounterpartyAccount.from_json(x) for x in result["rows"]]


class CreateCounterpartyAccountRequest(types.ApiRequest):
    def __init__(
        self,
        counterparty_id: str,
        account_number: str,
        bank_location: typing.Union[Unset, str] = Unset,
        bank_name: typing.Union[Unset, str] = Unset,
        bic: typing.Union[Unset, str] = Unset,
        correspondent_account: typing.Union[Unset, str] = Unset,
        is_default: typing.Union[Unset, bool] = Unset,
    ):
        self.counterparty_id = counterparty_id
        self.account_number = account_number
        self.bank_location = bank_location
        self.bank_name = bank_name
        self.bic = bic
        self.correspondent_account = correspondent_account
        self.is_default = is_default

    def to_request(self) -> RequestData:
        json_data = {"accountNumber": self.account_number}
        if self.bank_location != Unset:
            json_data["bankLocation"] = self.bank_location
        if self.bank_name != Unset:
            json_data["bankName"] = self.bank_name
        if self.bic != Unset:
            json_data["bic"] = self.bic
        if self.correspondent_account != Unset:
            json_data["correspondentAccount"] = self.correspondent_account
        if self.is_default != Unset:
            json_data["isDefault"] = self.is_default
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/accounts",
            json=json_data,
        )

    def from_response(self, result: dict) -> CounterpartyAccount:
        return CounterpartyAccount.from_json(result)


class GetCounterpartyAccountRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str, account_id: str):
        self.counterparty_id = counterparty_id
        self.account_id = account_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/accounts/{self.account_id}",
        )

    def from_response(self, result: dict) -> CounterpartyAccount:
        return CounterpartyAccount.from_json(result)


class UpdateCounterpartyAccountRequest(types.ApiRequest):
    def __init__(
        self,
        counterparty_id: str,
        account_id: str,
        account_number: typing.Union[Unset, str] = Unset,
        bank_location: typing.Union[Unset, str] = Unset,
        bank_name: typing.Union[Unset, str] = Unset,
        bic: typing.Union[Unset, str] = Unset,
        correspondent_account: typing.Union[Unset, str] = Unset,
        is_default: typing.Union[Unset, bool] = Unset,
    ):
        self.counterparty_id = counterparty_id
        self.account_id = account_id
        self.account_number = account_number
        self.bank_location = bank_location
        self.bank_name = bank_name
        self.bic = bic
        self.correspondent_account = correspondent_account
        self.is_default = is_default

    def to_request(self) -> RequestData:
        json_data = {}
        if self.account_number != Unset:
            json_data["accountNumber"] = self.account_number
        if self.bank_location != Unset:
            json_data["bankLocation"] = self.bank_location
        if self.bank_name != Unset:
            json_data["bankName"] = self.bank_name
        if self.bic != Unset:
            json_data["bic"] = self.bic
        if self.correspondent_account != Unset:
            json_data["correspondentAccount"] = self.correspondent_account
        if self.is_default != Unset:
            json_data["isDefault"] = self.is_default
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/accounts/{self.account_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> CounterpartyAccount:
        return CounterpartyAccount.from_json(result)


# --- Контактные лица Контрагента ---


class ContactPerson(types.MoySkladBaseClass):
    """
    accountId    | UUID | ID учетной записи. Только для чтения
    agent         | Meta | Метаданные контрагента. Expand
    description    | String(4096)| Описание
    email           | String(255)| Email
    externalCode     | String(255)| Внешний код
    id                 | UUID | ID Контактного лица. Только для чтения
    meta                | Meta | Метаданные
    name                 | String(255)| ФИО. Необходимо при создании
    phone                  | String(255)| Телефон
    position                 | String(255)| Должность
    updated                   | DateTime| Момент последнего обновления. Только для чтения
    """

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    description: typing.Optional[str]
    email: typing.Optional[str]
    external_code: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    phone: typing.Optional[str]
    position: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ContactPerson":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.description = dict_data.get("description")
        instance.email = dict_data.get("email")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.phone = dict_data.get("phone")
        instance.position = dict_data.get("position")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("contactperson",)


class GetContactPersonsRequest(types.ApiRequest):
    def __init__(
        self,
        counterparty_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.counterparty_id = counterparty_id
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
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/contactpersons",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ContactPerson]:
        return [ContactPerson.from_json(x) for x in result["rows"]]


class CreateContactPersonRequest(types.ApiRequest):
    def __init__(
        self,
        counterparty_id: str,
        name: str,
        description: typing.Union[Unset, str] = Unset,
        email: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        phone: typing.Union[Unset, str] = Unset,
        position: typing.Union[Unset, str] = Unset,
    ):
        self.counterparty_id = counterparty_id
        self.name = name
        self.description = description
        self.email = email
        self.external_code = external_code
        self.phone = phone
        self.position = position

    def to_request(self) -> RequestData:
        json_data = {"name": self.name}
        if self.description != Unset:
            json_data["description"] = self.description
        if self.email != Unset:
            json_data["email"] = self.email
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.phone != Unset:
            json_data["phone"] = self.phone
        if self.position != Unset:
            json_data["position"] = self.position
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/contactpersons",
            json=json_data,
        )

    def from_response(self, result: dict) -> ContactPerson:
        return ContactPerson.from_json(result)


class GetContactPersonRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str, contactperson_id: str):
        self.counterparty_id = counterparty_id
        self.contactperson_id = contactperson_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/contactpersons/{self.contactperson_id}",
        )

    def from_response(self, result: dict) -> ContactPerson:
        return ContactPerson.from_json(result)


class UpdateContactPersonRequest(types.ApiRequest):
    def __init__(
        self,
        counterparty_id: str,
        contactperson_id: str,
        name: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        email: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        phone: typing.Union[Unset, str] = Unset,
        position: typing.Union[Unset, str] = Unset,
    ):
        self.counterparty_id = counterparty_id
        self.contactperson_id = contactperson_id
        self.name = name
        self.description = description
        self.email = email
        self.external_code = external_code
        self.phone = phone
        self.position = position

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.description != Unset:
            json_data["description"] = self.description
        if self.email != Unset:
            json_data["email"] = self.email
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.phone != Unset:
            json_data["phone"] = self.phone
        if self.position != Unset:
            json_data["position"] = self.position
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/contactpersons/{self.contactperson_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ContactPerson:
        return ContactPerson.from_json(result)


# --- События Контрагента ---


class CounterpartyNote(types.MoySkladBaseClass):
    """
    accountId         | UUID | ID учетной записи. Только для чтения
    agent              | Meta | Метаданные Контрагента. Только для чтения, Expand
    author               | Meta | Метаданные сотрудника-автора. Только для чтения
    authorApplication      | Meta | Метаданные Решения-автора. Только для чтения
    created                  | DateTime | Момент создания. Только для чтения
    description                | String(4096)| Текст события. Необходимо при создании
    id                            | UUID | ID События. Только для чтения
    meta                            | Meta | Метаданные события
    """

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    author: typing.Optional[types.Meta]
    author_application: typing.Optional[types.Meta]
    created: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CounterpartyNote":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.author = helpers.get_meta(dict_data.get("author"))
        instance.author_application = helpers.get_meta(
            dict_data.get("authorApplication")
        )
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("counterparty", "notes")


class GetCounterpartyNotesRequest(types.ApiRequest):
    def __init__(
        self,
        counterparty_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.counterparty_id = counterparty_id
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
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/notes",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[CounterpartyNote]:
        return [CounterpartyNote.from_json(x) for x in result["rows"]]


class AddCounterpartyNoteRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str, description: str):
        self.counterparty_id = counterparty_id
        self.description = description

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/notes",
            json={"description": self.description},
        )

    def from_response(self, result: dict) -> CounterpartyNote:
        return CounterpartyNote.from_json(result)


class GetCounterpartyNoteRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str, note_id: str):
        self.counterparty_id = counterparty_id
        self.note_id = note_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/notes/{self.note_id}",
        )

    def from_response(self, result: dict) -> CounterpartyNote:
        return CounterpartyNote.from_json(result)


class UpdateCounterpartyNoteRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str, note_id: str, description: str):
        self.counterparty_id = counterparty_id
        self.note_id = note_id
        self.description = description

    def to_request(self) -> RequestData:
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/notes/{self.note_id}",
            json={"description": self.description},
        )

    def from_response(self, result: dict) -> CounterpartyNote:
        return CounterpartyNote.from_json(result)


class DeleteCounterpartyNoteRequest(types.ApiRequest):
    def __init__(self, counterparty_id: str, note_id: str):
        self.counterparty_id = counterparty_id
        self.note_id = note_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/counterparty/{self.counterparty_id}/notes/{self.note_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


# --- Настройки справочника Контрагентов ---


class CounterpartySettings(types.MoySkladBaseClass):
    """
    meta            | Meta   | Метаданные Настроек. Обязательное при ответе
    uniqueCodeRules  | Object | {"checkUniqueCode": bool, "fillUniqueCode": bool}. Обязательное при ответе
    createShared      | Boolean| Создавать новые документы с меткой "Общий". Обязательное при ответе
    """

    meta: typing.Optional[types.Meta]
    unique_code_rules: typing.Optional[dict]
    create_shared: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CounterpartySettings":
        instance = cls()
        instance.meta = dict_data.get("meta")
        instance.unique_code_rules = dict_data.get("uniqueCodeRules")
        instance.create_shared = dict_data.get("createShared")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("counterparty", "settings")


class GetCounterpartySettingsRequest(types.ApiRequest):
    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/counterparty/settings",
        )

    def from_response(self, result: dict) -> CounterpartySettings:
        return CounterpartySettings.from_json(result)


class UpdateCounterpartySettingsRequest(types.ApiRequest):
    def __init__(
        self,
        unique_code_rules: typing.Union[Unset, dict] = Unset,
        create_shared: typing.Union[Unset, bool] = Unset,
    ):
        self.unique_code_rules = unique_code_rules
        self.create_shared = create_shared

    def to_request(self) -> RequestData:
        json_data = {}
        if self.unique_code_rules != Unset:
            json_data["uniqueCodeRules"] = self.unique_code_rules
        if self.create_shared != Unset:
            json_data["createShared"] = self.create_shared
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/counterparty/settings",
            json=json_data,
        )

    def from_response(self, result: dict) -> CounterpartySettings:
        return CounterpartySettings.from_json(result)

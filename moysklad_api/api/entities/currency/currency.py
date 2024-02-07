# Auto generated by docs_parser.py
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Currency(types.MoySkladBaseClass):
    """
    archived                  | Boolean              | Добавлена ли Валюта в архив
    code                      | String(255)          | Цифровой код Валюты
    default                   | Boolean              | Является ли валюта валютой учета
    fullName                  | String(255)          | Полное наименование Валюты
    id                        | UUID                 | ID Валюты
    indirect                  | Boolean              | Признак обратного курса Валюты
    isoCode                   | String(255)          | Буквенный код Валюты
    majorUnit                 | Object               | Формы единиц целой части Валюты. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-valuta-formy-edinic
    margin                    | Double               | Наценка при автоматическом обновлении курса
    meta                      | Meta                 | Метаданные Валюты
    minorUnit                 | Object               | Формы единиц дробной части Валюты. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-valuta-formy-edinic
    multiplicity              | Int                  | Кратность курса Валюты
    name                      | String(255)          | Краткое наименование Валюты
    rate                      | Double               | Курс Валюты
    rateUpdateType            | String(255)          | Способ обновления курса Валюты. **auto** или **manual**
    system                    | Boolean              | Основана ли валюта на валюте из системного справочника
    """

    archived: typing.Optional[bool]
    code: typing.Optional[str]
    default: typing.Optional[bool]
    full_name: str
    id: typing.Optional[str]
    indirect: typing.Optional[bool]
    iso_code: typing.Optional[str]
    major_unit: typing.Optional[dict]
    margin: typing.Optional[float]
    meta: typing.Optional[types.Meta]
    minor_unit: typing.Optional[dict]
    multiplicity: typing.Optional[int]
    name: typing.Optional[str]
    rate: typing.Optional[float]
    rate_update_type: typing.Optional[str]
    system: bool

    @classmethod
    def from_json(cls, dict_data: dict) -> "Currency":
        instance = cls()
        instance.archived = dict_data.get("archived")
        instance.code = dict_data.get("code")
        instance.default = dict_data.get("default")
        instance.full_name = dict_data.get("fullName")
        instance.id = dict_data.get("id")
        instance.indirect = dict_data.get("indirect")
        instance.iso_code = dict_data.get("isoCode")
        instance.major_unit = dict_data.get("majorUnit")
        instance.margin = dict_data.get("margin")
        instance.meta = dict_data.get("meta")
        instance.minor_unit = dict_data.get("minorUnit")
        instance.multiplicity = dict_data.get("multiplicity")
        instance.name = dict_data.get("name")
        instance.rate = dict_data.get("rate")
        instance.rate_update_type = dict_data.get("rateUpdateType")
        instance.system = dict_data.get("system")
        return instance


class CreateCurrencyRequest(types.ApiRequest):
    def __init__(
        self,
        code: str,
        iso_code: str,
        name: str,
        archived: typing.Union[Unset, bool] = Unset,
        full_name: typing.Union[Unset, str] = Unset,
        indirect: typing.Union[Unset, bool] = Unset,
        major_unit: typing.Union[Unset, dict] = Unset,
        margin: typing.Union[Unset, float] = Unset,
        minor_unit: typing.Union[Unset, dict] = Unset,
        multiplicity: typing.Union[Unset, int] = Unset,
        rate: typing.Union[Unset, float] = Unset,
        system: typing.Union[Unset, bool] = Unset,
    ):
        """
        :param archived: Добавлена ли Валюта в архив
        :param code: Цифровой код Валюты
        :param full_name: Полное наименование Валюты
        :param indirect: Признак обратного курса Валюты
        :param iso_code: Буквенный код Валюты
        :param major_unit: Формы единиц целой части Валюты. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-valuta-formy-edinic
        :param margin: Наценка при автоматическом обновлении курса
        :param minor_unit: Формы единиц дробной части Валюты. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-valuta-formy-edinic
        :param multiplicity: Кратность курса Валюты
        :param name: Краткое наименование Валюты
        :param rate: Курс Валюты
        :param system: Системная ли валюта
        """
        self.archived = archived
        self.code = code
        self.full_name = full_name
        self.indirect = indirect
        self.iso_code = iso_code
        self.major_unit = major_unit
        self.margin = margin
        self.minor_unit = minor_unit
        self.multiplicity = multiplicity
        self.name = name
        self.rate = rate
        self.system = system

    def to_request(self) -> RequestData:
        json_data = {}
        if self.archived != Unset:
            json_data["archived"] = self.archived
        json_data["code"] = self.code
        if self.full_name != Unset:
            json_data["fullName"] = self.full_name
        if self.indirect != Unset:
            json_data["indirect"] = self.indirect
        json_data["isoCode"] = self.iso_code
        if self.major_unit != Unset:
            json_data["majorUnit"] = self.major_unit
        if self.margin != Unset:
            json_data["margin"] = self.margin
        if self.minor_unit != Unset:
            json_data["minorUnit"] = self.minor_unit
        if self.multiplicity != Unset:
            json_data["multiplicity"] = self.multiplicity
        json_data["name"] = self.name
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.system != Unset:
            json_data["system"] = self.system
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/currency",
            json=json_data,
        )

    def from_response(self, response: dict) -> Currency:
        return Currency.from_json(response)


class DeleteCurrencyRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/currency/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, response: dict) -> None:
        return None


class UpdateCurrencyRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        archived: typing.Union[Unset, bool] = Unset,
        code: typing.Union[Unset, str] = Unset,
        full_name: typing.Union[Unset, str] = Unset,
        indirect: typing.Union[Unset, bool] = Unset,
        iso_code: typing.Union[Unset, str] = Unset,
        major_unit: typing.Union[Unset, dict] = Unset,
        margin: typing.Union[Unset, float] = Unset,
        minor_unit: typing.Union[Unset, dict] = Unset,
        multiplicity: typing.Union[Unset, int] = Unset,
        name: typing.Union[Unset, str] = Unset,
        rate: typing.Union[Unset, float] = Unset,
    ):
        """
        :param id_: ID объекта для обновления
        :param archived: Добавлена ли Валюта в архив
        :param code: Цифровой код Валюты
        :param full_name: Полное наименование Валюты
        :param indirect: Признак обратного курса Валюты
        :param iso_code: Буквенный код Валюты
        :param major_unit: Формы единиц целой части Валюты. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-valuta-formy-edinic
        :param margin: Наценка при автоматическом обновлении курса
        :param minor_unit: Формы единиц дробной части Валюты. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-valuta-formy-edinic
        :param multiplicity: Кратность курса Валюты
        :param name: Краткое наименование Валюты
        :param rate: Курс Валюты
        """
        self.id = id_
        self.archived = archived
        self.code = code
        self.full_name = full_name
        self.indirect = indirect
        self.iso_code = iso_code
        self.major_unit = major_unit
        self.margin = margin
        self.minor_unit = minor_unit
        self.multiplicity = multiplicity
        self.name = name
        self.rate = rate

    def to_request(self) -> RequestData:
        json_data = {}
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.code != Unset:
            json_data["code"] = self.code
        if self.full_name != Unset:
            json_data["fullName"] = self.full_name
        if self.indirect != Unset:
            json_data["indirect"] = self.indirect
        if self.iso_code != Unset:
            json_data["isoCode"] = self.iso_code
        if self.major_unit != Unset:
            json_data["majorUnit"] = self.major_unit
        if self.margin != Unset:
            json_data["margin"] = self.margin
        if self.minor_unit != Unset:
            json_data["minorUnit"] = self.minor_unit
        if self.multiplicity != Unset:
            json_data["multiplicity"] = self.multiplicity
        if self.name != Unset:
            json_data["name"] = self.name
        if self.rate != Unset:
            json_data["rate"] = self.rate
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/currency/{self.id}",
            json=json_data,
        )

    def from_response(self, response: dict) -> Currency:
        return Currency.from_json(response)


class GetCurrenciesRequest(types.ApiRequest):
    def __init__(
        self,
        limit: int = 1000,
        offset: int = 0,
    ):
        self.limit = limit
        self.offset = offset

    def to_request(self) -> RequestData:
        params = {"limit": self.limit, "offset": self.offset}
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/currency",
            params=params,
        )

    def from_response(self, response: dict) -> typing.List[Currency]:
        return [Currency.from_json(x) for x in response["rows"]]

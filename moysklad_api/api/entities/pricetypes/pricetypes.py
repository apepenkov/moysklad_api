import typing

from .... import types, helpers
from ....types import Unset, RequestData


class PriceType(types.MoySkladBaseClass):
    """
    externalCode | String(255) | Внешний код Типа цены. Обязательное при ответе
    id           | UUID        | ID типа цены. Обязательное при ответе, Только для чтения
    meta         | Meta        | Метаданные Типа цены. Обязательное при ответе, Только для чтения
    name         | String(255) | Наименование Типа цены. Обязательное при ответе, Необходимо при создании

    Типы цен редактируются только полным списком (см. SetPriceTypesRequest):
    сущность в списке = обновление (если передана meta), отсутствие в списке = удаление,
    новый объект без meta = создание. Порядок в списке - порядок отображения,
    первый элемент - тип цены по умолчанию.
    """

    external_code: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PriceType":
        instance = cls()
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("pricetype",)


class GetPriceTypesRequest(types.ApiRequest):
    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/context/companysettings/pricetype",
        )

    def from_response(self, result: list) -> typing.List[PriceType]:
        return [PriceType.from_json(x) for x in result]


class SetPriceTypesRequest(types.ApiRequest):
    """
    Редактирование полного списка типов цен. Каждый элемент списка - либо
    существующий тип цены (с полем meta, для обновления или сохранения),
    либо новый (без meta, с полем name - для создания). Типы цен,
    отсутствующие в переданном списке, будут удалены.
    """

    def __init__(self, price_types: typing.List[dict]):
        """
        :param price_types: Список типов цен для сохранения. Каждый элемент - dict
            с ключами `name` (обязательно для новых), `externalCode` (опционально)
            и `meta` (для существующих типов цен, чтобы их не пересоздавать).
        """
        self.price_types = price_types

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/context/companysettings/pricetype",
            json=self.price_types,
        )

    def from_response(self, result: list) -> typing.List[PriceType]:
        return [PriceType.from_json(x) for x in result]


class GetPriceTypeRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/context/companysettings/pricetype/{self.id}",
        )

    def from_response(self, result: dict) -> PriceType:
        return PriceType.from_json(result)


class GetDefaultPriceTypeRequest(types.ApiRequest):
    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/context/companysettings/pricetype/default",
        )

    def from_response(self, result: dict) -> PriceType:
        return PriceType.from_json(result)

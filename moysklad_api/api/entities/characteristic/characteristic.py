# Характеристики модификаций (variant/metadata/characteristics).
# Поддерживаются только создание и чтение (обновление/удаление через API недоступны).
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Characteristic(types.MoySkladBaseClass):
    """
    id       | UUID        | ID Характеристики. Обязательное при ответе, Только для чтения
    meta     | Meta        | Метаданные характеристики. Обязательное при ответе, Только для чтения
    name     | String(255) | Наименование Характеристики. Обязательное при ответе, Необходимо при создании
    required | Boolean     | Обязательность (всегда false). Обязательное при ответе, Только для чтения
    type     | String(255) | Тип значения (всегда "string"). Обязательное при ответе, Только для чтения
    """

    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    required: typing.Optional[bool]
    type: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Characteristic":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.required = dict_data.get("required")
        instance.type = dict_data.get("type")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("variant", "metadata", "characteristics")


class GetCharacteristicsRequest(types.ApiRequest):
    """Получить список Характеристик через метаданные Модификаций (variant/metadata)."""

    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/variant/metadata",
        )

    def from_response(self, result: dict) -> typing.List[Characteristic]:
        return [
            Characteristic.from_json(x) for x in result.get("characteristics", [])
        ]


class CreateCharacteristicRequest(types.ApiRequest):
    def __init__(self, name: str):
        self.name = name

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/variant/metadata/characteristics",
            json={"name": self.name},
        )

    def from_response(self, result: dict) -> Characteristic:
        return Characteristic.from_json(result)


class GetCharacteristicRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/variant/metadata/characteristics/{self.id}",
        )

    def from_response(self, result: dict) -> Characteristic:
        return Characteristic.from_json(result)

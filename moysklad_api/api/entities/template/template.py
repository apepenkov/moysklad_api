# Шаблоны печатных форм (embeddedtemplate/customtemplate). Только для чтения.
# Общий путь: /entity/{entityType}/metadata/{embeddedtemplate|customtemplate}
# Для шаблонов ценников/этикеток entity_type = "assortment".
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Template(types.MoySkladBaseClass):
    """
    content | URL         | Ссылка на скачивание. Обязательное при ответе
    id      | UUID        | ID шаблона. Обязательное при ответе
    meta    | Meta        | Метаданные шаблона. Обязательное при ответе
    name    | String(255) | Наименование шаблона. Обязательное при ответе
    type    | String(255) | Тип шаблона (entity - документ, mxtemplate - ценник/этикетка). Обязательное при ответе
    """

    content: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    type: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Template":
        instance = cls()
        instance.content = dict_data.get("content")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.type = dict_data.get("type")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("embeddedtemplate",)


class GetEmbeddedTemplatesRequest(types.ApiRequest):
    def __init__(self, entity_type: str):
        self.entity_type = entity_type

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/embeddedtemplate",
        )

    def from_response(self, result: dict) -> typing.List[Template]:
        return [Template.from_json(x) for x in result["rows"]]


class GetEmbeddedTemplateRequest(types.ApiRequest):
    def __init__(self, entity_type: str, id_: str):
        self.entity_type = entity_type
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/embeddedtemplate/{self.id}",
        )

    def from_response(self, result: dict) -> Template:
        return Template.from_json(result)


class GetCustomTemplatesRequest(types.ApiRequest):
    def __init__(self, entity_type: str):
        self.entity_type = entity_type

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/customtemplate",
        )

    def from_response(self, result: dict) -> typing.List[Template]:
        return [Template.from_json(x) for x in result["rows"]]


class GetCustomTemplateRequest(types.ApiRequest):
    def __init__(self, entity_type: str, id_: str):
        self.entity_type = entity_type
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/metadata/customtemplate/{self.id}",
        )

    def from_response(self, result: dict) -> Template:
        return Template.from_json(result)

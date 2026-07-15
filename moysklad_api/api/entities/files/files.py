# Файлы (files) - вложенный ресурс Операции, Номенклатуры, Задачи или
# Контрагента. Общий путь: /entity/{entityType}/{entityId}/files
import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class File(types.MoySkladBaseClass):
    """
    created   | DateTime | Время загрузки Файла на сервер. Обязательное при ответе, Только для чтения
    createdBy | Meta     | Метаданные сотрудника, загрузившего Файл. Обязательное при ответе, Expand
    filename  | String(255)| Имя Файла. Обязательное при ответе
    meta      | Meta     | Метаданные объекта. Обязательное при ответе
    miniature | Meta     | Метаданные миниатюры (только для изображений)
    size      | Int      | Размер Файла в байтах. Обязательное при ответе
    tiny      | Meta     | Метаданные уменьшенного изображения (только для изображений)
    title     | String(255)| Название Файла. Обязательное при ответе
    """

    created: typing.Optional[datetime.datetime]
    created_by: typing.Optional[types.Meta]
    filename: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    miniature: typing.Optional[types.Meta]
    size: typing.Optional[int]
    tiny: typing.Optional[types.Meta]
    title: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "File":
        instance = cls()
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.created_by = helpers.get_meta(dict_data.get("createdBy"))
        instance.filename = dict_data.get("filename")
        instance.meta = dict_data.get("meta")
        instance.miniature = dict_data.get("miniature")
        instance.size = dict_data.get("size")
        instance.tiny = dict_data.get("tiny")
        instance.title = dict_data.get("title")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("files",)


class GetFilesRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
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
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/files",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[File]:
        return [File.from_json(x) for x in result["rows"]]


class AddFilesRequest(types.ApiRequest):
    """Добавить Файлы (макс. 10 за раз). Каждый файл - dict с filename/content (base64)."""

    def __init__(self, entity_type: str, entity_id: str, files: typing.List[dict]):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.files = files

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/files",
            json=self.files,
        )

    def from_response(self, result: list) -> typing.List[File]:
        return [File.from_json(x) for x in result]


class DeleteFileRequest(types.ApiRequest):
    def __init__(self, entity_type: str, entity_id: str, file_id: str):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.file_id = file_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/files/{self.file_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

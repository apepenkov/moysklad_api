# Изображения (image) - вложенный ресурс Товара, Комплекта, Модификации или
# Карточки контента. Общий путь: /entity/{entityType}/{entityId}/images
import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Image(types.MoySkladBaseClass):
    """
    filename  | String(255) | Имя файла. Обязательное при ответе
    meta      | Meta        | Метаданные объекта. Обязательное при ответе
    miniature | Meta        | Метаданные миниатюры изображения. Обязательное при ответе
    size      | Int         | Размер файла в байтах. Обязательное при ответе
    tiny      | Meta        | Метаданные уменьшенного изображения. Обязательное при ответе
    title     | String(255) | Название Изображения. Обязательное при ответе
    updated   | DateTime    | Время загрузки файла на сервер. Обязательное при ответе
    """

    filename: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    miniature: typing.Optional[types.Meta]
    size: typing.Optional[int]
    tiny: typing.Optional[types.Meta]
    title: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Image":
        instance = cls()
        instance.filename = dict_data.get("filename")
        instance.meta = dict_data.get("meta")
        instance.miniature = dict_data.get("miniature")
        instance.size = dict_data.get("size")
        instance.tiny = dict_data.get("tiny")
        instance.title = dict_data.get("title")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("image",)


class GetImagesRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        fields: typing.Union[Unset, typing.Literal["downloadPermanentHref"]] = Unset,
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.limit = limit
        self.offset = offset
        self.fields = fields

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.fields != Unset:
            params["fields"] = self.fields
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/images",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Image]:
        return [Image.from_json(x) for x in result["rows"]]


class AddImageRequest(types.ApiRequest):
    """Добавить одно новое Изображение (filename + content в base64)."""

    def __init__(self, entity_type: str, entity_id: str, filename: str, content: str):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.filename = filename
        self.content = content

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/images",
            json={"filename": self.filename, "content": self.content},
        )

    def from_response(self, result: list) -> typing.List[Image]:
        return [Image.from_json(x) for x in result]


class SetImagesRequest(types.ApiRequest):
    """
    Изменить список Изображений целиком. Каждый элемент - dict: либо
    {"meta": {...}} для существующего изображения (оставить), либо
    {"filename": ..., "content": ...} для нового.
    """

    def __init__(self, entity_type: str, entity_id: str, images: typing.List[dict]):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.images = images

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/images",
            json=self.images,
        )

    def from_response(self, result: list) -> typing.List[Image]:
        return [Image.from_json(x) for x in result]


class DeleteImageRequest(types.ApiRequest):
    def __init__(self, entity_type: str, entity_id: str, image_id: str):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.image_id = image_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/images/{self.image_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class DeleteImagesRequest(types.ApiRequest):
    """Массовое удаление группы Изображений (по meta)."""

    def __init__(self, entity_type: str, entity_id: str, images: typing.List[dict]):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.images = images

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/images/delete",
            json=self.images,
        )

    def from_response(self, result: list) -> list:
        return result

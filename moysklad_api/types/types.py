import typing


class Meta(typing.TypedDict):
    """
    href 	URL 	            Ссылка на объект
    metadataHref 	URL 	    Ссылка на метаданные сущности (Другой вид метаданных. Присутствует не во всех сущностях)
    type 	String(255) 	    Тип объекта
    mediaType 	String(255) 	Тип данных, которые приходят в ответ от сервиса, либо отправляются в теле запроса. В рамках данного API всегда равен application/json
    uuidHref 	URL 	        Ссылка на объект на UI. Присутствует не во всех сущностях. Может быть использована для получения uuid
    downloadHref 	URL 	    Ссылка на скачивание Изображения. Данный параметр указывается только в meta для Изображения у Товара или Комплекта.
    """

    href: str
    type: str
    mediaType: str
    metadataHref: typing.NotRequired[str]
    uuidHref: typing.NotRequired[str]
    downloadHref: typing.NotRequired[str]


class MetaArrayMeta(typing.TypedDict):
    href: str
    type: str
    mediaType: str
    size: int
    limit: int
    offset: int


class MetaArray(typing.TypedDict):
    """Объект с полями meta и rows, где rows - массив объектов. Элементы массива rows можно запросить, используя параметр запроса expand соответствующего поля."""

    meta: MetaArrayMeta
    rows: typing.NotRequired[typing.List[typing.Any]]


class Rate(typing.TypedDict):
    value: int
    currency: Meta


class MoySkladBaseClass:
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            + ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
            + ")"
        )

    @classmethod
    def from_json(cls, dict_data: dict) -> "MoySkladBaseClass":
        raise NotImplementedError


class ApiRequest:
    # method: typing.Literal["GET", "POST", "PUT", "DELETE"], url: str, **kwargs
    def to_request(self) -> dict:
        raise NotImplementedError

    def from_response(self, result: dict):
        raise NotImplementedError


class Unset:
    _singleton = None

    def __new__(cls):
        if cls._singleton is None:
            cls._singleton = super(Unset, cls).__new__(cls)
        return cls._singleton

    def __repr__(self):
        return "Unset"

    def __bool__(self):
        return False

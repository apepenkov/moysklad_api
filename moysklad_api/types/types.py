import abc
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


class MoySkladBaseClass(abc.ABC):
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            + ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
            + ")"
        )

    @classmethod
    @abc.abstractmethod
    def from_json(cls, dict_data: dict) -> "MoySkladBaseClass":
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        """
        This should return either a (name, ) or (name, subname) tuple.
        Subname usecase - for example, a position in an order would have
        ("purchaseorder", "positions") as a name, and
        purchaseorder by itself would just have ("purchaseorder", ) as a name.
        """
        raise NotImplementedError


class RequestData:
    def __init__(
        self,
        method: typing.Literal["GET", "POST", "PUT", "DELETE"],
        url: str,
        allow_non_json: bool = False,
        json: typing.Optional[typing.Union[list, dict]] = None,
        params: typing.Optional[dict] = None,
        headers: typing.Optional[dict] = None,
        **kwargs,
    ):
        self.method = method
        self.url = url
        self.allow_non_json = allow_non_json
        self.json = json
        self.params = params
        self.headers = headers
        self.kwargs = kwargs

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            + ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
            + ")"
        )

    def __str__(self):
        return self.__repr__()

    def to_kwargs(self) -> dict:
        kwargs = {
            "allow_non_json": self.allow_non_json,
            "method": self.method,
            "url": self.url,
        }
        if self.json is not None:
            kwargs["json"] = self.json
        if self.params is not None:
            kwargs["params"] = self.params
        if self.headers is not None:
            kwargs["headers"] = self.headers
        kwargs.update(self.kwargs)
        return kwargs


class ApiRequest(abc.ABC):
    @abc.abstractmethod
    def to_request(self) -> RequestData:
        raise NotImplementedError

    @abc.abstractmethod
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

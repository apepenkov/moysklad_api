import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class CustomEntity(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-pol-zowatel-skie-sprawochniki

    Атрибуты сущности
    Название 	Тип 	        Описание
    id 	        UUID 	        ID Пользовательского справочника     Обязательное при ответе Только для чтения
    meta 	    Метаданные Пользовательского справочника     Обязательное при ответе
    name 	    String(255) 	Наименование Пользовательского справочника     Обязательное при ответе Необходимо при создании
    """

    id: str
    meta: types.Meta
    name: str

    @classmethod
    def from_json(cls, dict_data: dict) -> "CustomEntity":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return None


class CustomEntityElement(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-jelementy-pol-zowatel-skogo-sprawochnika

    Название 	    Тип 	        Описание
    accountId 	    UUID 	        ID учетной записи                                                       Обязательное при ответе Только для чтения
    code 	        String(255)     Код элемента Пользовательского справочника
    description 	String(4096)    Описание элемента Пользовательского справочника
    externalCode 	String(255)     Внешний код элемента Пользовательского справочника                      Обязательное при ответе
    id 	            UUID 	        ID элемента Пользовательского справочника                               Обязательное при ответе Только для чтения
    meta 	        Meta 		    Метаданные элемента Пользовательского справочника                       Обязательное при ответе
    name 	        String(255)     Наименование элементе Пользовательского справочника                     Обязательное при ответе Необходимо при создании
    updated 	    DateTime        Момент последнего обновления элементе Пользовательского справочника     Обязательное при ответе Только для чтения
    group 	        Meta            Отдел сотрудника                                                        Обязательное при ответе Expand
    owner 	        Meta            Владелец (Сотрудник)                                                    Expand
    shared 	        Boolean 	    Общий доступ                                                            Обязательное при ответе
    """

    account_id: str
    code: typing.Optional[str]
    description: typing.Optional[str]
    external_code: str
    id: str
    meta: types.Meta
    name: str
    updated: datetime.datetime
    group: types.Meta
    owner: types.Meta
    shared: bool

    @classmethod
    def from_json(cls, dict_data: dict) -> "CustomEntityElement":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.shared = dict_data.get("shared")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return ("customentity",)


class CreateCustomEntityRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-sozdat-sprawochnik
    """

    def __init__(
        self,
        name: str,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param name: Name of custom entity (Наименование Пользовательского справочника)
        :param meta: Meta of custom entity (Метаданные Пользовательского справочника)
        """
        self.name = name
        self.meta = meta

    def to_request(self) -> RequestData:
        json_request = {"name": self.name}
        if self.meta != Unset:
            json_request["meta"] = self.meta
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/customentity",
            json=json_request,
        )

    def from_response(self, result: dict) -> CustomEntity:
        return CustomEntity.from_json(result)


class UpdateCustomEntityRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-izmenit-sprawochnik
    """

    def __init__(
        self,
        metadata_id: str,
        name: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param metadata_id: ID of custom entity (ID Пользовательского справочника)
        :param name: Name of custom entity (Наименование Пользовательского справочника)
        :param meta: Meta of custom entity (Метаданные Пользовательского справочника)
        """
        self.id = metadata_id
        self.name = name
        self.meta = meta

    def to_request(self) -> RequestData:
        json_request = {}
        if self.name != Unset:
            json_request["name"] = self.name
        if self.meta != Unset:
            json_request["meta"] = self.meta
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/customentity/{self.id}",
            json=json_request,
        )

    def from_response(self, result: dict) -> CustomEntity:
        return CustomEntity.from_json(result)


class DeleteCustomEntityRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-udalit-sprawochnik
    """

    def __init__(self, metadata_id: str):
        """

        :param metadata_id: ID of custom entity (ID Пользовательского справочника)
        """
        self.id = metadata_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/customentity/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class CreateCustomEntityElementRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-sozdat-alement-sprawochnika

    """

    def __init__(
        self,
        metadata_id: str,
        name: str,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param metadata_id: ID of the custom entity (ID справочника)
        :param name: Name of the custom entity element (Наименование элемента справочника)
        :param code: Code of the custom entity element (Код элемента справочника)
        :param description: Description of the custom entity element (Описание элемента справочника)
        :param external_code: External code of the custom entity element (Внешний код элемента справочника)
        :param meta: Metadata of the custom entity element (Метаданные элемента справочника)
        :param group: Group of the custom entity element (Отдел элемента справочника)
        :param owner: Owner of the custom entity element (Владелец элемента справочника)
        :param shared: Shared access of the custom entity element (Общий доступ элемента справочника)
        """
        self.metadata_id = metadata_id
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code
        self.meta = meta
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
        }
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.meta != Unset:
            json_data["meta"] = self.meta
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
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/customentity/{self.metadata_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> "CustomEntityElement":
        return CustomEntityElement.from_json(result)


class UpdateCustomEntityElementRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-izmenit-alement

    """

    def __init__(
        self,
        metadata_id: str,
        element_id: str,
        name: typing.Union[Unset, str] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param metadata_id: ID of the custom entity (ID справочника)
        :param element_id: ID of the custom entity element (ID элемента справочника)
        :param name: Name of the custom entity element (Наименование элемента справочника)
        :param code: Code of the custom entity element (Код элемента справочника)
        :param description: Description of the custom entity element (Описание элемента справочника)
        :param external_code: External code of the custom entity element (Внешний код элемента справочника)
        :param meta: Metadata of the custom entity element (Метаданные элемента справочника)
        :param group: Group of the custom entity element (Отдел элемента справочника)
        :param owner: Owner of the custom entity element (Владелец элемента справочника)
        :param shared: Shared access of the custom entity element (Общий доступ элемента справочника)
        """
        self.metadata_id = metadata_id
        self.element_id = element_id
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code
        self.meta = meta
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.meta != Unset:
            json_data["meta"] = self.meta
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
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/customentity/{self.metadata_id}/{self.element_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> "CustomEntityElement":
        return CustomEntityElement.from_json(result)


class DeleteCustomEntityElementRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-udalit-alement-sprawochnika

    """

    def __init__(self, metadata_id: str, element_id: str):
        """

        :param metadata_id: ID of the custom entity (ID справочника)
        :param element_id: ID of the custom entity element (ID элемента справочника)
        """
        self.metadata_id = metadata_id
        self.element_id = element_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/customentity/{self.metadata_id}/{self.element_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetCustomEntityElementRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-poluchit-alement-sprawochnika

    """

    def __init__(self, metadata_id: str, element_id: str):
        """

        :param metadata_id: ID of the custom entity (ID справочника)
        :param element_id: ID of the custom entity element (ID элемента справочника)
        """
        self.metadata_id = metadata_id
        self.element_id = element_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/customentity/{self.metadata_id}/{self.element_id}",
        )

    def from_response(self, result: dict) -> "CustomEntityElement":
        return CustomEntityElement.from_json(result)


class GetCustomEntityElementsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-poluchit-alementy-sprawochnika

    """

    def __init__(
        self,
        metadata_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """

        :param metadata_id: ID of the custom entity (ID справочника)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        """
        self.metadata_id = metadata_id
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
            url=f"{helpers.BASE_URL}/entity/customentity/{self.metadata_id}",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List["CustomEntityElement"]:
        return [CustomEntityElement.from_json(i) for i in result["rows"]]

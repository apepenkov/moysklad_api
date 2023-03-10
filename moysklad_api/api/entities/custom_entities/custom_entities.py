import datetime
import typing

from .... import types


class CustomEntity(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-pol-zowatel-skie-sprawochniki

    Атрибуты сущности
    Название 	Тип 	        Описание
    id 	        UUID 	        ID Пользовательского справочника     Обязательное при ответе Только для чтения
    meta 	    Метаданные Пользовательского справочника     Обязательное при ответе
    name 	    String(255) 	Наименование Пользовательского справочника     Обязательное при ответе Необходимо при создании
    """

    def __init__(self):
        self.id: str = None
        self.meta: types.Meta = None
        self.name: str = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "CustomEntity":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance


class CreateCustomEntityRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-sozdat-sprawochnik
    """

    def __init__(
        self,
        name: str,
        meta: typing.Optional[types.Meta] = None,
    ):
        """

        :param name: Name of custom entity (Наименование Пользовательского справочника)
        :param meta: Meta of custom entity (Метаданные Пользовательского справочника)
        """
        self.name = name
        self.meta = meta

    def to_request(self) -> dict:
        json_request = {"name": self.name}
        if self.meta is not None:
            json_request["meta"] = self.meta
        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/customentity",
            "json": json_request,
        }

    def from_response(self, result: dict) -> CustomEntity:
        return CustomEntity.from_json(result)


class UpdateCustomEntityRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-izmenit-sprawochnik
    """

    def __init__(
        self,
        metadata_id: str,
        name: typing.Optional[str] = None,
        meta: typing.Optional[types.Meta] = None,
    ):
        """

        :param metadata_id: ID of custom entity (ID Пользовательского справочника)
        :param name: Name of custom entity (Наименование Пользовательского справочника)
        :param meta: Meta of custom entity (Метаданные Пользовательского справочника)
        """
        self.id = metadata_id
        self.name = name
        self.meta = meta

    def to_request(self) -> dict:
        json_request = {}
        if self.name is not None:
            json_request["name"] = self.name
        if self.meta is not None:
            json_request["meta"] = self.meta
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.id}",
            "json": json_request,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.id}",
            "allow_non_json": True,
        }

    def from_response(self, result: dict) -> None:
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

    def __init__(self):
        self.account_id: str = None
        self.code: typing.Optional[str] = None
        self.description: typing.Optional[str] = None
        self.external_code: str = None
        self.id: str = None
        self.meta: types.Meta = None
        self.name: str = None
        self.updated: datetime.datetime = None
        self.group: types.Meta = None
        self.owner: types.Meta = None
        self.shared: bool = None

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
        instance.updated = datetime.datetime.fromisoformat(dict_data.get("updated"))
        group = dict_data.get("group")
        if group:
            instance.group = group["meta"]
        owner = dict_data.get("owner")
        if owner:
            instance.owner = owner["meta"]
        instance.shared = dict_data.get("shared")
        return instance


class CreateCustomEntityElementRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-sozdat-alement-sprawochnika

    """

    def __init__(
        self,
        metadata_id: str,
        name: str,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        meta: typing.Optional[types.Meta] = None,
        group: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
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

    def to_request(self) -> dict:
        json_data = {
            "name": self.name,
        }
        if self.code is not None:
            json_data["code"] = self.code
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.meta is not None:
            json_data["meta"] = self.meta
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.shared is not None:
            json_data["shared"] = self.shared
        return {
            "method": "POST",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.metadata_id}",
            "json": json_data,
        }

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
        name: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        meta: typing.Optional[types.Meta] = None,
        group: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
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

    def to_request(self) -> dict:
        json_data = {}
        if self.name is not None:
            json_data["name"] = self.name
        if self.code is not None:
            json_data["code"] = self.code
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.meta is not None:
            json_data["meta"] = self.meta
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.shared is not None:
            json_data["shared"] = self.shared
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.metadata_id}/{self.element_id}",
            "json": json_data,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.metadata_id}/{self.element_id}",
            "allow_non_json": True,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.metadata_id}/{self.element_id}",
        }

    def from_response(self, result: dict) -> "CustomEntityElement":
        return CustomEntityElement.from_json(result)


class GetCustomEntityElementsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-pol-zowatel-skij-sprawochnik-poluchit-alementy-sprawochnika

    """

    def __init__(
        self,
        metadata_id: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ):
        """

        :param metadata_id: ID of the custom entity (ID справочника)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        """
        self.metadata_id = metadata_id
        self.limit = limit
        self.offset = offset

    def to_request(self) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/customentity/{self.metadata_id}",
            "params": params,
        }

    def from_response(self, result: dict) -> typing.List["CustomEntityElement"]:
        return [CustomEntityElement.from_json(i) for i in result["rows"]]

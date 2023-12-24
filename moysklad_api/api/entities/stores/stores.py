import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Store(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-sklady

    Название 	        Тип 	        Описание
    accountId 	        UUID 	 	    ID учетной записи                                       Обязательное при ответе Только для чтения
    address 	        String(255) 	Адрес склада
    addressFull 	    Object 		    Адрес с детализацией по отдельным полям. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-sklady-attributy-suschnosti-adres
    archived 	        Boolean 	 	Добавлен ли Склад в архив                               Обязательное при ответе
    attributes 	        Array(Object) 	Операторы доп. полей 	Массив метаданных дополнительных полей склада
    code 	            String(255) 	Код Склада
    description 	    String(4096) 	Комментарий к Складу
    externalCode 	    String(255) 	Внешний код Склада                                      Обязательное при ответе
    group 	            Meta 	 	    Отдел сотрудника                                        Обязательное при ответе Expand
    id 	                UUID 	 	    ID Склада                                               Обязательное при ответе Только для чтения
    meta 	            Meta 		    Метаданные Склада                                       Обязательное при ответе
    name 	            String(255) 	Наименование Склада                                     Обязательное при ответе Необходимо при создании
    owner 	            Meta 	 	    Владелец (Сотрудник)                                    Expand
    parent 	            Meta 	 	    Метаданные родительского склада (Группы)                Expand
    pathName 	        String 	 	    Группа Склада                                           Обязательное при ответе
    shared 	            Boolean 	 	Общий доступ                                            Обязательное при ответе
    updated 	        DateTime 		Момент последнего обновления Склада                     Обязательное при ответе Только для чтения
    zones 	            MetaArray 		Зоны склада. Подробнее тут                              Только для чтения Expand
    slots 	            MetaArray 		Ячейки склада. Подробнее тут                            Только для чтения Expand
    """

    def __init__(self):
        self.account_id: str = None
        self.address: typing.Optional[str] = None
        self.address_full: typing.Optional[dict] = None
        self.archived: bool = None
        self.attributes: typing.Optional[typing.List[dict]] = None
        self.code: typing.Optional[str] = None
        self.description: typing.Optional[str] = None
        self.external_code: str = None
        self.group: typing.Optional[types.Meta] = None
        self.id: str = None
        self.meta: types.Meta = None
        self.name: str = None
        self.owner: typing.Optional[types.Meta] = None
        self.parent: typing.Optional[types.Meta] = None
        self.path_name: str = None
        self.shared: bool = None
        self.updated: datetime.datetime = None
        self.zones: typing.Optional[types.MetaArray] = None
        self.slots: typing.Optional[types.MetaArray] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Store":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.address = dict_data.get("address")
        instance.address_full = dict_data.get("addressFull")
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.parent = helpers.get_meta(dict_data.get("parent"))
        instance.path_name = dict_data.get("pathName")
        instance.shared = dict_data.get("shared")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.zones = dict_data.get("zones")
        instance.slots = dict_data.get("slots")
        return instance


class StoreZone(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-zony-sklada

    Атрибуты сущности
    Название 	    Тип 	 	        Описание
    accountId 	    UUID 		        ID учетной записи                   Обязательное при ответе Только для чтения
    externalCode 	String(255) 		Внешний код Зоны                    Обязательное при ответе
    id          	UUID 		        ID Зоны                             Обязательное при ответе Только для чтения
    meta 	        Meta 		        Метаданные Зоны                     Обязательное при ответе
    name 	        String(255) 		Наименование Зоны                   Обязательное при ответе Необходимо при создании
    updated 	    DateTime 		    Момент последнего обновления Зоны   Обязательное при ответе Только для чтения
    """

    def __init__(self):
        self.account_id: str = None
        self.external_code: str = None
        self.id: str = None
        self.meta: types.Meta = None
        self.name: str = None
        self.updated: datetime.datetime = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "StoreZone":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance


class StoreSlot(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-yachejki-sklada

    Название 	    Тип 	 	    Описание
    accountId 	    UUID 		    ID учетной записи                       Обязательное при ответе Только для чтения
    externalCode 	String(255) 	Внешний код Ячейки                      Обязательное при ответе
    id          	UUID 		    ID Ячейки                               Обязательное при ответе Только для чтения
    meta 	        Meta 		    Метаданные Ячейки                       Обязательное при ответе
    name 	        String(255) 	Наименование Ячейки                     Обязательное при ответе Необходимо при создании
    updated 	    DateTime 		Момент последнего обновления Ячейки     Обязательное при ответе Только для чтения
    zone 	        Meta 		    Зона ячейки. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-zony-sklada    Только для чтения Expand
    """

    def __init__(self):
        self.account_id: str = None
        self.external_code: str = None
        self.id: str = None
        self.meta: types.Meta = None
        self.name: str = None
        self.updated: datetime.datetime = None
        self.zone: typing.Optional[types.Meta] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "StoreSlot":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.zone = helpers.get_meta(dict_data.get("zone"))
        return instance


class GetStoresRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-poluchit-sklady

    Get Stores
    Получить Склады

    Параметр 	Описание
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """

        :param limit: Limit of entities to extract. (Лимит сущностей для извлечения.)
        :param offset: Offset in the list of entities. (Отступ в выдаваемом списке сущностей.)
        """
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
            url="https://api.moysklad.ru/api/remap/1.2/entity/store",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Store]:
        return [Store.from_json(item) for item in result["rows"]]


class CreateStoreRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-sozdat-sklad

    Create Store
    Создать Склад

    Склад создается на основе переданного объекта JSON, который содержит представление нового Склада. Необходимое для создания поле - name не должно быть пустым.
    """

    class AddressFull(typing.TypedDict):
        """
        addInfo 	String(255) 	Другое
        apartment 	String(30) 	    Квартира
        city 	    String(255) 	Город
        comment 	String(255) 	Комментарий
        country 	Meta 	        Метаданные страны
        house 	    String(30) 	    Дом
        postalCode 	String(6) 	    Почтовый индекс
        region 	    Meta 	        Метаданные региона
        street 	    String(255) 	Улица
        """

        addInfo: typing.NotRequired[str]
        apartment: typing.NotRequired[str]
        city: typing.NotRequired[str]
        comment: typing.NotRequired[str]
        country: typing.NotRequired[types.Meta]
        house: typing.NotRequired[str]
        postalCode: typing.NotRequired[str]
        region: typing.NotRequired[types.Meta]
        street: typing.NotRequired[str]

    def __init__(
        self,
        name: str,
        address: typing.Union[Unset, str] = Unset,
        address_full: typing.Union[Unset, AddressFull] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent: typing.Union[Unset, types.Meta] = Unset,
        path_name: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param name: Name of the store. (Название склада.)
        :param address: Address of the store. (Адрес склада.)
        :param address_full: Full address of the store. (Полный адрес склада.)
        :param archived: Archived status of the store. (Статус архивности склада.)
        :param attributes: Attributes of the store. (Атрибуты склада.)
        :param code: Code of the store. (Код склада.)
        :param description: Description of the store. (Описание склада.)
        :param external_code: External code of the store. (Внешний код склада.)
        :param group: Group of the store. (Группа склада.)
        :param meta: Meta of the store. (Метаданные склада.)
        :param owner: Owner of the store. (Владелец склада.)
        :param parent: Parent of the store. (Родительский склад.)
        :param path_name: Path name of the store. (Путь склада.)
        :param shared: Shared status of the store. (Статус общего доступа склада.)
        """
        self.name = name
        self.address = address
        self.address_full = address_full
        self.archived = archived
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.group = group
        self.meta = meta
        self.owner = owner
        self.parent = parent
        self.path_name = path_name
        self.shared = shared

    def to_request(self) -> RequestData:
        json_dict = {
            "name": self.name,
        }

        if self.address != Unset:
            json_dict["address"] = self.address

        if self.address_full != Unset:
            json_dict["addressFull"] = self.address_full

        if self.archived != Unset:
            json_dict["archived"] = self.archived

        if self.attributes != Unset:
            json_dict["attributes"] = self.attributes

        if self.code != Unset:
            json_dict["code"] = self.code

        if self.description != Unset:
            json_dict["description"] = self.description

        if self.external_code != Unset:
            json_dict["externalCode"] = self.external_code

        if self.group != Unset:
            json_dict["group"] = {"meta": self.group}

        if self.meta != Unset:
            json_dict["meta"] = self.meta

        if self.owner != Unset:
            json_dict["owner"] = {"meta": self.owner}

        if self.parent != Unset:
            json_dict["parent"] = {"meta": self.parent}

        if self.path_name != Unset:
            json_dict["pathName"] = self.path_name

        if self.shared != Unset:
            json_dict["shared"] = self.shared

        return RequestData(
            method="POST",
            url="https://api.moysklad.ru/api/remap/1.2/entity/store",
            json=json_dict,
        )

    def from_response(self, result: dict) -> Store:
        return Store.from_json(result)


class DeleteStoreRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-udalit-sklad

    Delete store
    Удалить склад
    """

    def __init__(self, store_id: str):
        """
        :param store_id: Store id. (Идентификатор склада.)
        """
        self.id = store_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetStoreRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-poluchit-sklad

    Get store
    Получить склад
    """

    def __init__(
        self,
        store_id: str,
    ):
        """

        :param store_id: Store id. (Идентификатор склада.)
        """
        self.id = store_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.id}",
        )

    def from_response(self, result: dict) -> Store:
        return Store.from_json(result)


class UpdateStoreRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-izmenit-sklad

    Update store
    Изменить склад
    """

    AddressFull = CreateStoreRequest.AddressFull

    def __init__(
        self,
        store_id: str,
        name: typing.Optional[str],
        address: typing.Union[Unset, str] = Unset,
        address_full: typing.Union[Unset, AddressFull] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        parent: typing.Union[Unset, types.Meta] = Unset,
        path_name: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        """
        :param store_id: Store id. (Идентификатор склада.)
        :param name: Name of the store. (Название склада.)
        :param address: Address of the store. (Адрес склада.)
        :param address_full: Full address of the store. (Полный адрес склада.)
        :param archived: Archived status of the store. (Статус архивности склада.)
        :param attributes: Attributes of the store. (Атрибуты склада.)
        :param code: Code of the store. (Код склада.)
        :param description: Description of the store. (Описание склада.)
        :param external_code: External code of the store. (Внешний код склада.)
        :param group: Group of the store. (Группа склада.)
        :param meta: Meta of the store. (Метаданные склада.)
        :param owner: Owner of the store. (Владелец склада.)
        :param parent: Parent of the store. (Родительский склад.)
        :param path_name: Path name of the store. (Путь склада.)
        :param shared: Shared status of the store. (Статус общего доступа склада.)
        """
        self.id = store_id
        self.name = name
        self.address = address
        self.address_full = address_full
        self.archived = archived
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.group = group
        self.meta = meta
        self.owner = owner
        self.parent = parent
        self.path_name = path_name
        self.shared = shared

    def to_request(self) -> RequestData:
        json_dict = {}

        if self.name != Unset:
            json_dict["name"] = self.name

        if self.address != Unset:
            json_dict["address"] = self.address

        if self.address_full != Unset:
            json_dict["addressFull"] = self.address_full

        if self.archived != Unset:
            json_dict["archived"] = self.archived

        if self.attributes != Unset:
            json_dict["attributes"] = self.attributes

        if self.code != Unset:
            json_dict["code"] = self.code

        if self.description != Unset:
            json_dict["description"] = self.description

        if self.external_code != Unset:
            json_dict["externalCode"] = self.external_code

        if self.group != Unset:
            json_dict["group"] = {"meta": self.group}

        if self.meta != Unset:
            json_dict["meta"] = self.meta

        if self.owner != Unset:
            json_dict["owner"] = {"meta": self.owner}

        if self.parent != Unset:
            json_dict["parent"] = {"meta": self.parent}

        if self.path_name != Unset:
            json_dict["pathName"] = self.path_name

        if self.shared != Unset:
            json_dict["shared"] = self.shared

        return RequestData(
            method="PUT",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.id}",
            json=json_dict,
        )

    def from_response(self, result: dict) -> Store:
        return Store.from_json(result)


class GetStoreZonesRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-poluchit-zony-sklada

    Get store zones
    Получить зоны склада

    Параметр 	Описание
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.

    """

    def __init__(
        self,
        store_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """

        :param store_id: Store id. (ID склада.)
        :param limit: Limit of entities to retrieve. (Лимит сущностей для извлечения.)
        :param offset: Offset in the returned list of entities. (Отступ в выдаваемом списке сущностей.)
        """
        self.store_id = store_id
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
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/zones",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List["StoreZone"]:
        return [StoreZone.from_json(item) for item in result.get("rows", [])]


class CreateStoreZoneRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-sozdat-zonu-sklada

    Create store zone
    Создать зону склада
    """

    def __init__(
        self,
        store_id: str,
        name: str,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param store_id: Store id. (ID склада.)
        :param name: Name. (Наименование.)
        :param external_code: External code. (Внешний код.)
        :param meta: Meta. (Метаданные.)
        """
        self.store_id = store_id
        self.name = name
        self.external_code = external_code
        self.meta = meta

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
        }
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.meta != Unset:
            json_data["meta"] = self.meta
        return RequestData(
            method="POST",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/zones",
            json=json_data,
        )

    def from_response(self, result: dict) -> StoreZone:
        return StoreZone.from_json(result)


class GetStoreZoneRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-poluchit-zonu-sklada

    Get store zone
    Получить зону склада
    """

    def __init__(
        self,
        store_id: str,
        zone_id: str,
    ):
        """

        :param store_id: Store id. (ID склада.)
        :param zone_id: Zone id. (ID зоны склада.)
        """
        self.store_id = store_id
        self.zone_id = zone_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/zones/{self.zone_id}",
        )

    def from_response(self, result: dict) -> StoreZone:
        return StoreZone.from_json(result)


class DeleteStoreZoneRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-udalit-zonu-sklada

    Delete store zone
    Удалить зону склада
    """

    def __init__(self, store_id: str, zone_id: str):
        """

        :param store_id: Store id. (ID склада.)
        :param zone_id: Zone id. (ID зоны склада.)
        """
        self.store_id = store_id
        self.zone_id = zone_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/zones/{self.zone_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class UpdateStoreZoneRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-izmenit-zonu-sklada

    Update store zone
    Изменить зону склада
    """

    def __init__(
        self,
        store_id: str,
        zone_id: str,
        name: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param store_id: Store id. (ID склада.)
        :param zone_id: Zone id. (ID зоны склада.)
        :param name: Name. (Наименование.)
        :param external_code: External code. (Внешний код.)
        :param meta: Meta. (Метаданные.)
        """
        self.store_id = store_id
        self.zone_id = zone_id
        self.name = name
        self.external_code = external_code
        self.meta = meta

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.meta != Unset:
            json_data["meta"] = self.meta
        return RequestData(
            method="PUT",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/zones/{self.zone_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> StoreZone:
        return StoreZone.from_json(result)


class GetStoreSlotsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-poluchit-qchejki-sklada

    Get slots of store
    Получить ячейки склада

    Название 	        Тип 	        Описание
    limit 	            Integer 	    Количество возвращаемых сущностей (не более 100) 	По умолчанию 100
    offset 	            Integer 	    Смещение, необходимое для выборки определенного подмножества сущностей 	По умолчанию 0
    """

    def __init__(
        self,
        store_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """

        :param store_id: Store id (ID склада)
        :param limit: Limit of returned entities (Лимит возвращаемых сущностей)
        :param offset: Offset for selecting a specific subset of entities (Смещение, необходимое для выборки определенного подмножества сущностей)
        """

        self.store_id = store_id
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
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/slots",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[StoreSlot]:
        return [StoreSlot.from_json(item) for item in result["rows"]]


class CreateStoreSlotRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-sozdat-qchejku-sklada

    Create slot of store
    Создать ячейку склада
    """

    def __init__(
        self,
        store_id: str,
        name: str,
        external_code: typing.Union[Unset, str] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        zone: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param store_id: Store id (ID склада)
        :param name: Name of slot (Название ячейки)
        :param external_code: External code (Внешний код)
        :param meta: Meta (Метаданные)
        :param zone: Zone (Зона)
        """

        self.store_id = store_id
        self.name = name
        self.external_code = external_code
        self.meta = meta
        self.zone = zone

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
        }
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.meta != Unset:
            json_data["meta"] = self.meta
        if self.zone != Unset:
            json_data["zone"] = {"meta": self.zone} if self.zone is not None else None

        return RequestData(
            method="POST",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/slots",
            json=json_data,
        )

    def from_response(self, result: dict) -> StoreSlot:
        return StoreSlot.from_json(result)


class UpdateStoreSlotRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-izmenit-qchejku-sklada

    Update slot of store
    """

    def __init__(
        self,
        store_id: str,
        slot_id: str,
        name: typing.Optional[str],
        external_code: typing.Optional[str],
        meta: typing.Optional[types.Meta],
        zone: typing.Optional[types.Meta],
    ):
        """

        :param store_id: Store id (ID склада)
        :param slot_id: Slot id (ID ячейки)
        :param name: Name of slot (Название ячейки)
        :param external_code: External code (Внешний код)
        :param meta: Meta (Метаданные)
        :param zone: Zone (Зона)
        """
        self.store_id = store_id
        self.slot_id = slot_id
        self.name = name
        self.external_code = external_code
        self.meta = meta
        self.zone = zone

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.meta != Unset:
            json_data["meta"] = self.meta
        if self.zone != Unset:
            json_data["zone"] = {"meta": self.zone} if self.zone is not None else None

        return RequestData(
            method="PUT",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/slots/{self.slot_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> StoreSlot:
        return StoreSlot.from_json(result)


class DeleteStoreSlotRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-udalit-qchejku-sklada

    Delete slot of store
    Удалить ячейку склада
    """

    def __init__(
        self,
        store_id: str,
        slot_id: str,
    ):
        """

        :param store_id: Store id (ID склада)
        :param slot_id: Slot id (ID ячейки)
        """

        self.store_id = store_id
        self.slot_id = slot_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/slots/{self.slot_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetStoreSlotRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-poluchit-qchejku-sklada

    Get slot of store
    Получить ячейку склада
    """

    def __init__(
        self,
        store_id: str,
        slot_id: str,
    ):
        """

        :param store_id: Store id (ID склада)
        :param slot_id: Slot id (ID ячейки)
        """

        self.store_id = store_id
        self.slot_id = slot_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/store/{self.store_id}/slots/{self.slot_id}",
        )

    def from_response(self, result: dict) -> StoreSlot:
        return StoreSlot.from_json(result)

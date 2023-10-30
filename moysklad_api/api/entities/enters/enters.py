import typing
import datetime
from .... import types
from ....types import Unset


class Enter(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-oprihodowaniq

    Атрибуты сущности
    Название 	    Тип 	        Описание
    accountId 	    UUID 	 	    ID учетной записи           Обязательное при ответе Только для чтения Change-handler
    applicable 	    Boolean 	 	Отметка о проведении        Обязательное при ответе Change-handler Update-provider
    attributes      Array(Object) 	Операторы доп. полей 	    Коллекция метаданных доп. полей. Поля объекта    Change-handler Update-provider
    code 	        String(255) 	Код Оприходования
    created 	    DateTime 	  	Дата создания               Обязательное при ответе Только для чтения Change-handler
    deleted 	    DateTime 	  	Момент последнего удаления Оприходования    Только для чтения
    description 	String(4096) 	Комментарий Оприходования   Change-handler Update-provider
    externalCode 	String(255) 	Внешний код Оприходования   Обязательное при ответе Change-handler
    files 	        MetaArray 		Метаданные массива Файлов   (Максимальное количество файлов - 100)    Обязательное при ответе Expand
    group 	        Meta 	 	    Отдел сотрудника            Обязательное при ответе Expand
    id 	            UUID 	 	    ID Оприходования            Обязательное при ответе Только для чтения Change-handler
    meta 	        Meta 		    Метаданные Оприходования    Обязательное при ответе Change-handler
    moment          DateTime 	  	Дата документа              Обязательное при ответе Change-handler Update-provider
    name 	        String(255) 	Номер Оприходования         Обязательное при ответе Change-handler Update-provider
    organization 	Meta 	 	    Метаданные юрлица           Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    overhead 	    Object 		    Накладные расходы.          Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-oprihodowanie-oprihodowaniq-nakladnye-rashody). Если Позиции Оприходования не заданы, то накладные расходы нельзя задать    Update-provider
    owner 	        Meta 	 	    Владелец (Сотрудник)        Обязательное при ответе Expand
    positions 	    MetaArray 		Метаданные позиций Оприходования    Обязательное при ответе Expand Change-handler Update-provider
    printed 	    Boolean 	 	Напечатан ли документ       Обязательное при ответе Только для чтения
    project 	    Meta 	 	    Метаданные проекта          Expand Change-handler Update-provider
    published 	    Boolean 	 	Опубликован ли документ     Обязательное при ответе Только для чтения
    rate 	        Object 		    Валюта. Подробнее тут       Обязательное при ответе Change-handler Update-provider
    shared 	        Boolean 	 	Общий доступ                Обязательное при ответе
    state 	        Meta 	 	    Метаданные статуса оприходования    Expand Change-handler Update-provider
    store 	        Meta 	 	    Метаданные склада           Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    sum 	        Int 	  	    Сумма Оприходования в копейках    Обязательное при ответе Только для чтения Change-handler
    syncId      	UUID 	 	    ID синхронизации.           После заполнения недоступен для изменения
    updated 	    DateTime 	  	Момент последнего обновления Оприходования    Обязательное при ответе Только для чтения Change-handler

    Накладные расходы

    Описание полей overhead
    Название 	    Тип 	Описание
    sum 	        Int 	Сумма Оприходования в копейках     Обязательное при ответе Update-provider
    distribution 	Enum 	Распределение накладных расходов [weight, volume, price] -> [по весу, по объему, по цене] Обязательное при ответе Update-provider

    """

    def __init__(self):
        self.account_id: str = None
        self.applicable: bool = None
        self.attributes: typing.Optional[list] = None
        self.code: typing.Optional[str] = None
        self.created: datetime.datetime = None
        self.deleted: typing.Optional[datetime.datetime] = None
        self.description: typing.Optional[str] = None
        self.external_code: str = None
        self.files: types.MetaArray = None
        self.group: types.Meta = None
        self.id: str = None
        self.meta: types.Meta = None
        self.moment: datetime.datetime = None
        self.name: str = None
        self.organization: types.Meta = None
        self.overhead: typing.Optional[dict] = None
        self.owner: types.Meta = None
        self.positions: types.MetaArray = None
        self.printed: bool = None
        self.project: typing.Optional[types.Meta] = None
        self.published: bool = None
        self.rate: dict = None
        self.shared: bool = None
        self.state: typing.Optional[types.Meta] = None
        self.store: types.Meta = None
        self.sum: int = None
        self.sync_id: typing.Optional[str] = None
        self.updated: datetime.datetime = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Enter":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        created = dict_data.get("created")
        if created:
            instance.created = datetime.datetime.fromisoformat(created)
        deleted = dict_data.get("deleted")
        if deleted:
            instance.deleted = datetime.datetime.fromisoformat(deleted)
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        group = dict_data.get("group")
        if group:
            instance.group = group["meta"]
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        moment = dict_data.get("moment")
        if moment:
            instance.moment = datetime.datetime.fromisoformat(moment)
        instance.name = dict_data.get("name")
        organization = dict_data.get("organization")
        if organization:
            instance.organization = organization["meta"]
        instance.overhead = dict_data.get("overhead")
        owner = dict_data.get("owner")
        if owner:
            instance.owner = owner["meta"]
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        project = dict_data.get("project")
        if project:
            instance.project = project["meta"]
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.shared = dict_data.get("shared")
        state = dict_data.get("state")
        if state:
            instance.state = state["meta"]
        store = dict_data.get("store")
        if store:
            instance.store = store["meta"]
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        updated = dict_data.get("updated")
        if updated:
            instance.updated = datetime.datetime.fromisoformat(updated)
        return instance


class EnterPosition(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-oprihodowaniq


    Позиции Оприходования

    Позиции Оприходования - это список товаров/модификаций/серий. Объект позиции Оприходования содержит следующие поля:
    Название 	Тип 	        Описание
    accountId 	UUID 	        ID учетной записи Обязательное при ответе Только для чтения Change-handler
    assortment 	Meta 	        Метаданные товара/услуги/серии/модификации, которую представляет собой позиция     Обязательное при ответе Expand Change-handler Update-provider
    country 	Meta 	        Метаданные страны     Expand
    gtd 	    Object 	        ГТД. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruzowaq-tamozhennaq-deklaraciq-gtd
    id 	        UUID 	        ID позиции     Обязательное при ответе Только для чтения Change-handler
    overhead 	Int 	        Накладные расходы. Подробнее тут. https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-oprihodowanie-oprihodowaniq-nakladnye-rashody Если Позиции Оприходования не заданы, то накладные расходы нельзя задать     Обязательное при ответе Только для чтения
    pack 	    Object 	        Упаковка Товара. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-upakowki-towara    Change-handler Update-provider
    price 	    Float 	        Цена товара/услуги в копейках     Обязательное при ответе Change-handler Update-provider
    quantity 	Int 	        Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе.     Обязательное при ответе Change-handler Update-provider
    reason 	    String(255) 	Причина оприходования данной позиции
    slot 	    Meta 	        Ячейка на складе. Подробнее тут     Expand https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-yachejki-sklada
    things 	    Object(String) 	Серийные номера. Значение данного атрибута игнорируется, если товар позиции не находится на серийном учете. В ином случае количество товаров в позиции будет равно количеству серийных номеров, переданных в значении атрибута. Change-handler
    """

    def __init__(self):
        self.account_id: str = None
        self.assortment: types.Meta = None
        self.country: typing.Optional[types.Meta] = None
        self.gtd: typing.Optional[dict] = None
        self.id: str = None
        self.overhead: int = None
        self.pack: typing.Optional[dict] = None
        self.price: float = None
        self.quantity: float = None
        self.reason: typing.Optional[str] = None
        self.slot: typing.Optional[types.Meta] = None
        self.things: typing.Optional[dict] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "EnterPosition":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        assortment = dict_data.get("assortment")
        if assortment:
            instance.assortment = assortment["meta"]
        country = dict_data.get("country")
        if country:
            instance.country = country["meta"]
        instance.gtd = dict_data.get("gtd")
        instance.id = dict_data.get("id")
        instance.overhead = dict_data.get("overhead")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.reason = dict_data.get("reason")
        slot = dict_data.get("slot")
        if slot:
            instance.slot = slot["meta"]
        instance.things = dict_data.get("things")
        return instance


class GetEntersRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-poluchat-oprihodowaniq

    Параметры
    Параметр 	Описание
    limit 	number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    search 	string (optional) Example: 0001 Фильтр документов по указанной поисковой строке.
    """

    def __init__(
        self,
        limit: typing.Optional[int] = 1000,
        offset: typing.Optional[int] = 0,
        search: typing.Union[Unset, str] = Unset,
    ):
        """

        :param limit: Limit of entities to extract. (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке)
        """
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> dict:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.search != Unset:
            params["search"] = self.search
        return {
            "method": "GET",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/enter",
            "params": params,
        }

    def from_response(self, result) -> typing.List[Enter]:
        return [Enter.from_json(row) for row in result["rows"]]


class CreateEnterRequest(types.ApiRequest):
    class CreateEnterPosition(typing.TypedDict):
        """
        Позиции Оприходования - это список товаров/модификаций/серий. Объект позиции Оприходования содержит следующие поля:
        Название 	Тип 	        Описание
        assortment 	Meta 	        Метаданные товара/услуги/серии/модификации, которую представляет собой позиция     Обязательное при ответе Expand Change-handler Update-provider
        country 	Meta 	        Метаданные страны     Expand
        gtd 	    Object 	        ГТД. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruzowaq-tamozhennaq-deklaraciq-gtd
        pack 	    Object 	        Упаковка Товара. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-upakowki-towara    Change-handler Update-provider
        price 	    Float 	        Цена товара/услуги в копейках     Обязательное при ответе Change-handler Update-provider
        quantity 	Int 	        Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе.     Обязательное при ответе Change-handler Update-provider
        reason 	    String(255) 	Причина оприходования данной позиции
        slot 	    Meta 	        Ячейка на складе. Подробнее тут     Expand https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-yachejki-sklada
        things 	    Object(String) 	Серийные номера. Значение данного атрибута игнорируется, если товар позиции не находится на серийном учете. В ином случае количество товаров в позиции будет равно количеству серийных номеров, переданных в значении атрибута. Change-handler
        overhead    Int             Накладные расходы
        """

        assortment: types.Meta
        price: float
        quantity: float
        country: typing.NotRequired[types.Meta]
        gtd: typing.NotRequired[dict]
        pack: typing.NotRequired[dict]
        reason: typing.NotRequired[str]
        slot: typing.NotRequired[types.Meta]
        things: typing.NotRequired[dict]
        overhead: typing.NotRequired[int]

    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-sozdat-oprihodowaniq

    Название 	    Тип 	        Описание
    organization 	Meta 	 	    Метаданные юрлица           Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    store 	        Meta 	 	    Метаданные склада           Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    
    applicable 	    Boolean 	 	[optional] Отметка о проведении        Обязательное при ответе Change-handler Update-provider
    attributes      Array(Object) 	[optional] Операторы доп. полей 	    Коллекция метаданных доп. полей. Поля объекта    Change-handler Update-provider
    code 	        String(255) 	[optional] Код Оприходования
    description 	String(4096) 	[optional] Комментарий Оприходования   Change-handler Update-provider
    externalCode 	String(255) 	[optional] Внешний код Оприходования   Обязательное при ответе Change-handler
    files 	        MetaArray 		[optional] Метаданные массива Файлов   (Максимальное количество файлов - 100)    Обязательное при ответе Expand
    group 	        Meta 	 	    [optional] Отдел сотрудника            Обязательное при ответе Expand
    moment          DateTime 	  	[optional] Дата документа              Обязательное при ответе Change-handler Update-provider
    name 	        String(255) 	[optional] Номер Оприходования         Обязательное при ответе Change-handler Update-provider
    overhead 	    Object 		    [optional] Накладные расходы.          Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-oprihodowanie-oprihodowaniq-nakladnye-rashody). Если Позиции Оприходования не заданы, то накладные расходы нельзя задать    Update-provider
    positions 	    Array(Position) [optional] Метаданные позиций Оприходования    Обязательное при ответе Expand Change-handler Update-provider
    project 	    Meta 	 	    [optional] Метаданные проекта          Expand Change-handler Update-provider
    rate 	        Object 		    [optional] Валюта. Подробнее тут       Обязательное при ответе Change-handler Update-provider
    shared 	        Boolean 	 	[optional] Общий доступ                Обязательное при ответе
    state 	        Meta 	 	    [optional] Метаданные статуса оприходования    Expand Change-handler Update-provider
    syncId      	UUID 	 	    [optional] ID синхронизации.           После заполнения недоступен для изменения
    """

    def __init__(
        self,
        organization: types.Meta,
        store: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, list] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        positions: typing.Union[Unset, typing.List[CreateEnterPosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param organization: Organization meta (Метаданные организации)
        :param store: Store meta (Метаданные склада)
        :param applicable: Mark of the document (Отметка о проведении)
        :param attributes: Attributes (Доп. поля)
        :param code: Code (Код)
        :param description: Description (Комментарий)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Отдел сотрудника)
        :param moment: Moment (Дата документа)
        :param name: Name (Номер)
        :param overhead: Overhead (Накладные расходы)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Валюта)
        :param shared: Shared (Общий доступ)
        """
        self.organization = organization
        self.store = store
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.overhead = overhead
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared

    def to_request(self) -> dict:
        json_data = {
            "organization": {"meta": self.organization},
            "store": {"meta": self.store},
        }
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.files != Unset:
            json_data["files"] = self.files
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group} if self.group is not None else None
            )
        if self.moment != Unset:
            json_data["moment"] = self.moment.strftime("%Y-%m-%d %H:%M:%S")
        if self.name != Unset:
            json_data["name"] = self.name
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                pos = {}
                assortment = position.get("assortment")
                if assortment != Unset:
                    pos["assortment"] = {"meta": assortment}
                else:
                    raise ValueError("Assortment is required for position")
                price = position.get("price")
                if price != Unset:
                    pos["price"] = price
                else:
                    raise ValueError("Price is required for position")
                quantity = position.get("quantity")
                if quantity != Unset:
                    pos["quantity"] = quantity
                else:
                    raise ValueError("Quantity is required for position")
                country = position.get("country")
                if country != Unset:
                    pos["country"] = {"meta": country}
                gtd = position.get("gtd")
                if gtd != Unset:
                    pos["gtd"] = gtd
                pack = position.get("pack")
                if pack != Unset:
                    pos["pack"] = pack
                reason = position.get("reason")
                if reason != Unset:
                    pos["reason"] = {"meta": reason}
                slot = position.get("slot")
                if slot != Unset:
                    pos["slot"] = {"meta": slot}
                things = position.get("things")
                if things != Unset:
                    pos["things"] = things
                pos_overhead = position.get("overhead")
                if pos_overhead != Unset:
                    pos["overhead"] = pos_overhead
                json_data["positions"].append(pos)
        if self.project != Unset:
            json_data["project"] = (
                {"meta": self.project} if self.project is not None else None
            )
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/enter",
            "json": json_data,
        }

    def from_response(self, result) -> Enter:
        return Enter.from_json(result)


class DeleteEnterRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-udalit-oprihodowanie

    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    """

    def __init__(self, enter_id: str):
        """

        :param enter_id: ID of enter (ID оприходования)
        """
        self.enter_id = enter_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}",
            "allow_non_json": True,
        }

    def from_response(self, result) -> None:
        return None


class GetEnterRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-poluchit-oprihodowanie

    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    """

    def __init__(self, enter_id: str):
        """

        :param enter_id: ID (id Оприходования)
        """
        self.enter_id = enter_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}",
        }

    def from_response(self, result) -> Enter:
        return Enter.from_json(result)


class UpdateEnterRequest(types.ApiRequest):
    UpdateEnterPosition = CreateEnterRequest.CreateEnterPosition
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-izmenit-oprihodowanie

    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    """

    def __init__(
        self,
        enter_id: str,
        organization: typing.Union[Unset, str] = Unset,
        store: typing.Union[Unset, str] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, dict] = Unset,
        group: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        positions: typing.Union[Unset, typing.List[UpdateEnterPosition]] = Unset,
        project: typing.Union[Unset, str] = Unset,
        rate: typing.Union[Unset, str] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param enter_id: ID of enter (ID оприходования)
        :param organization: Organization (Организация)
        :param store: Store (Склад)
        :param applicable: Applicable (Проведен)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param moment: Moment (Момент)
        :param name: Name (Название)
        :param overhead: Overhead (Налоги)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Валюта)
        :param shared: Shared (Общий доступ)
        """
        self.enter_id = enter_id
        self.organization = organization
        self.store = store
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.overhead = overhead
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared

    def to_request(self) -> dict:
        json_data = {}
        if self.organization != Unset:
            json_data["organization"] = (
                {"meta": self.organization} if self.organization is not None else None
            )
        if self.store != Unset:
            json_data["store"] = (
                {"meta": self.store} if self.store is not None else None
            )
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.files != Unset:
            json_data["files"] = self.files
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group} if self.group is not None else None
            )
        if self.moment != Unset:
            json_data["moment"] = self.moment.strftime("%Y-%m-%d %H:%M:%S")
        if self.name != Unset:
            json_data["name"] = self.name
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                pos = {}
                assortment = position.get("assortment")
                if assortment != Unset:
                    pos["assortment"] = {"meta": assortment}
                else:
                    raise ValueError("Assortment is required for position")
                price = position.get("price")
                if price != Unset:
                    pos["price"] = price
                else:
                    raise ValueError("Price is required for position")
                quantity = position.get("quantity")
                if quantity != Unset:
                    pos["quantity"] = quantity
                else:
                    raise ValueError("Quantity is required for position")
                country = position.get("country")
                if country != Unset:
                    pos["country"] = {"meta": country}
                gtd = position.get("gtd")
                if gtd != Unset:
                    pos["gtd"] = gtd
                pack = position.get("pack")
                if pack != Unset:
                    pos["pack"] = pack
                reason = position.get("reason")
                if reason != Unset:
                    pos["reason"] = {"meta": reason}
                slot = position.get("slot")
                if slot != Unset:
                    pos["slot"] = {"meta": slot}
                things = position.get("things")
                if things != Unset:
                    pos["things"] = things
                pos_overhead = position.get("overhead")
                if pos_overhead != Unset:
                    pos["overhead"] = pos_overhead
                json_data["positions"].append(pos)
        if self.project != Unset:
            json_data["project"] = (
                {"meta": self.project} if self.project is not None else None
            )
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.shared != Unset:
            json_data["shared"] = self.shared
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}",
            "json": json_data,
        }

    def from_response(self, result) -> Enter:
        return Enter.from_json(result)


class GetEnterPositionsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-poluchit-pozicii-oprihodowaniq

    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    limit 	number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(
        self,
        enter_id: str,
        limit: typing.Optional[int] = 1000,
        offset: typing.Optional[int] = 0,
    ):
        """

        :param enter_id: Enter id (id Оприходования)
        :param limit: Limit of entities to extract. (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей)
        """
        self.enter_id = enter_id
        self.limit = limit
        self.offset = offset

    def to_request(self) -> dict:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}/positions",
            "params": params,
        }

    def from_response(self, result) -> typing.List[EnterPosition]:
        return [EnterPosition.from_json(position) for position in result["rows"]]


class CreateEnterPositionRequest(types.ApiRequest):
    CreateEnterPosition = CreateEnterRequest.CreateEnterPosition
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-sozdat-poziciu-oprihodowaniq

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    positions   Array(Position) (required) 
    """

    def __init__(
        self,
        enter_id: str,
        positions: typing.List[CreateEnterPosition],
    ):
        """

        :param enter_id: Enter id (id Оприходования)
        :param positions: Positions (Позиции)
        """
        self.enter_id = enter_id
        self.positions = positions

    def to_request(self) -> dict:
        json_data = []
        for position in self.positions:
            pos = {}
            assortment = position.get("assortment")
            if assortment != Unset:
                pos["assortment"] = {"meta": assortment}
            else:
                raise ValueError("Assortment is required for position")
            price = position.get("price")
            if price != Unset:
                pos["price"] = price
            else:
                raise ValueError("Price is required for position")
            quantity = position.get("quantity")
            if quantity != Unset:
                pos["quantity"] = quantity
            else:
                raise ValueError("Quantity is required for position")
            country = position.get("country")
            if country != Unset:
                pos["country"] = {"meta": country}
            gtd = position.get("gtd")
            if gtd != Unset:
                pos["gtd"] = gtd
            pack = position.get("pack")
            if pack != Unset:
                pos["pack"] = pack
            reason = position.get("reason")
            if reason != Unset:
                pos["reason"] = {"meta": reason}
            slot = position.get("slot")
            if slot != Unset:
                pos["slot"] = {"meta": slot}
            things = position.get("things")
            if things != Unset:
                pos["things"] = things
            pos_overhead = position.get("overhead")
            if pos_overhead != Unset:
                pos["overhead"] = pos_overhead
            json_data.append(pos)
        return {
            "method": "POST",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}/positions",
            "json": json_data,
        }

    def from_response(self, result) -> typing.List[EnterPosition]:
        return [EnterPosition.from_json(position) for position in result["rows"]]


class GetEnterPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-poluchit-poziciu

    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    positionID 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b20 id позиции.
    """

    def __init__(
        self,
        enter_id: str,
        position_id: str,
    ):
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id позиции)
        """
        self.enter_id = enter_id
        self.position_id = position_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}/positions/{self.position_id}",
        }

    def from_response(self, result) -> EnterPosition:
        return EnterPosition.from_json(result)


class UpdateEnterPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-poluchit-poziciu


    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    positionID 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b20 id позиции.

    assortment 	Meta 	        Метаданные товара/услуги/серии/модификации, которую представляет собой позиция     Обязательное при ответе Expand Change-handler Update-provider
    price 	    Float 	        Цена товара/услуги в копейках     Обязательное при ответе Change-handler Update-provider
    quantity 	Int 	        Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе.     Обязательное при ответе Change-handler Update-provider

    country 	Meta 	        Метаданные страны     Expand
    gtd 	    Object 	        ГТД. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruzowaq-tamozhennaq-deklaraciq-gtd
    pack 	    Object 	        Упаковка Товара. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-upakowki-towara    Change-handler Update-provider
    reason 	    String(255) 	Причина оприходования данной позиции
    slot 	    Meta 	        Ячейка на складе. Подробнее тут     Expand https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-yachejki-sklada
    things 	    Object(String) 	Серийные номера. Значение данного атрибута игнорируется, если товар позиции не находится на серийном учете. В ином случае количество товаров в позиции будет равно количеству серийных номеров, переданных в значении атрибута. Change-handler
    overhead    Int             Накладные расходы

    """

    def __init__(
        self,
        enter_id: str,
        position_id: str,
        assortment: types.Meta,
        price: float,
        quantity: float,
        country: typing.Union[Unset, types.Meta] = Unset,
        gtd: typing.Union[Unset, typing.Dict] = Unset,
        pack: typing.Union[Unset, typing.Dict] = Unset,
        reason: typing.Union[Unset, str] = Unset,
        slot: typing.Union[Unset, types.Meta] = Unset,
        things: typing.Union[Unset, typing.Dict] = Unset,
        overhead: typing.Union[Unset, int] = Unset,
    ):
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id позиции)
        :param assortment: Assortment of position (Метаданные товара/услуги/серии/модификации, которую представляет собой позиция)
        :param price: Price of position (Цена товара/услуги в копейках)
        :param quantity: Quantity of position (Количество товаров/услуг данного вида в позиции)
        :param country: Country of position (Метаданные страны)
        :param gtd: GTD of position (ГТД)
        :param pack: Pack of position (Упаковка Товара)
        :param reason: Reason of position (Причина оприходования данной позиции)
        :param slot: Slot of position (Ячейка на складе)
        :param things: Things of position (Серийные номера)
        :param overhead: Overhead of position (Накладные расходы)
        """
        self.enter_id = enter_id
        self.position_id = position_id
        self.assortment = assortment
        self.price = price
        self.quantity = quantity
        self.country = country
        self.gtd = gtd
        self.pack = pack
        self.reason = reason
        self.slot = slot
        self.things = things
        self.overhead = overhead

    def to_request(self) -> dict:
        json_data = {
            "assortment": {"meta": self.assortment},
            "price": self.price,
            "quantity": self.quantity,
        }
        if self.country:
            json_data["country"] = {"meta": self.country}
        if self.gtd:
            json_data["gtd"] = self.gtd
        if self.pack:
            json_data["pack"] = self.pack
        if self.reason:
            json_data["reason"] = self.reason
        if self.slot:
            json_data["slot"] = {"meta": self.slot}
        if self.things:
            json_data["things"] = self.things
        if self.overhead:
            json_data["overhead"] = self.overhead
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}/positions/{self.position_id}",
            "json": json_data,
        }

    def from_response(self, result: dict) -> "EnterPosition":
        return EnterPosition.from_json(result)


class DeleteEnterPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-oprihodowanie-udalit-poziciu

    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Оприходования.
    positionID 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b20 id позиции.
    """

    def __init__(
        self,
        enter_id: str,
        position_id: str,
    ):
        """

        :param enter_id: Enter id (id Оприходования)
        :param position_id: Position id (id позиции)
        """
        self.enter_id = enter_id
        self.position_id = position_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/enter/{self.enter_id}/positions/{self.position_id}",
            "allow_non_json": True,
        }

    def from_response(self, result: dict) -> None:
        return None

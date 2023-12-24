import typing
import datetime
from .... import types, helpers
from ....types import Unset, RequestData


class Move(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie

    Название 	        Тип  	        Описание
    accountId 	        UUID 	 	    ID учетной записи  Обязательное при ответеТолько для чтения
    applicable 	        Boolean 	 	Отметка о проведении     Обязательное при ответе
    attributes 	        Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта
    code 	            String(255) 	Код Перемещения
    created 	        DateTime 	  	Дата создания     Обязательное при ответе Только для чтения
    deleted 	        DateTime 	  	Момент последнего удаления Перемещения     Только для чтения
    description 	    String(4096) 	Комментарий Перемещения
    externalCode 	    String(255) 	Внешний код Перемещения     Обязательное при ответе
    files 	            MetaArray 		Метаданные массива Файлов (Максимальное количество файлов - 100)     Обязательное при ответе Expand
    group 	            Meta 	 	    Отдел сотрудника     Обязательное при ответе Expand
    id 	                UUID 	 	    ID Перемещения     Обязательное при ответе Только для чтения
    internalOrder 	    Meta 		    Метаданные Внутреннего заказа, связанного с Перемещением    Expand
    customerOrder 	    Meta 		    Метаданные Заказа покупателя, связанного с Перемещением     Expand
    meta 	            Meta 		    Метаданные Перемещения     Обязательное при ответе
    moment 	            DateTime 	  	Дата документа     Обязательное при ответе
    name 	            String(255) 	Наименование Перемещения     Обязательное при ответе
    organization 	    Meta 	 	    Метаданные юрлица     Обязательное при ответе Expand Необходимо при создании
    overhead 	        Object 		    Накладные расходы. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-peremeschenie-peremescheniq-nakladnye-rashody). Если Позиции Перемещения не заданы, то накладные расходы нельзя задать
    owner 	            Meta 	 	    Владелец (Сотрудник)     Обязательное при ответе Expand
    positions 	        MetaArray 		Метаданные позиций Перемещения     Обязательное при ответе Expand
    printed 	        Boolean 	 	Напечатан ли документ     Обязательное при ответе Только для чтения
    project 	        Meta 	 	    Метаданные проекта     Expand
    published 	        Boolean 	 	Опубликован ли документ     Обязательное при ответе Только для чтения
    rate 	            Object 		    Валюта. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-teh-operaciq-valuta-w-dokumentah)    Обязательное при ответе
    shared 	            Boolean 	 	Общий доступ     Обязательное при ответе
    sourceStore 	    Meta 		    Метаданные склада, с которого совершается перемещение     Обязательное при ответе Expand Необходимо при создании
    state 	            Meta 	 	    Метаданные статуса Перемещения     Expand
    sum 	            Int 	  	    Сумма Перемещения в копейках     Обязательное при ответе Только для чтения
    syncId 	            UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    targetStore 	    Meta 		    Метаданные склада, на который совершается перемещение     Обязательное при ответе Expand Необходимо при создании
    updated 	        DateTime 	  	Момент последнего обновления Перемещения     Обязательное при ответе Только для чтения
    """

    account_id: str
    applicable: bool
    attributes: dict
    code: str
    created: datetime.datetime
    deleted: datetime.datetime
    description: str
    external_code: str
    files: types.MetaArray
    group: types.Meta
    id: str
    internal_order: types.Meta
    custom_order: types.Meta
    meta: types.Meta
    moment: datetime.datetime
    name: str
    organization: types.Meta
    overhead: dict
    owner: types.Meta
    positions: types.MetaArray
    printed: bool
    project: types.Meta
    published: bool
    rate: types.Rate
    shared: bool
    source_store: types.Meta
    state: types.Meta
    sum: int
    sync_id: str
    target_store: types.Meta
    updated: datetime.datetime

    @classmethod
    def from_json(cls, dict_data: dict) -> "Move":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.internal_order = helpers.get_meta(dict_data.get("internalOrder"))
        instance.custom_order = helpers.get_meta(dict_data.get("customOrder"))
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.overhead = dict_data.get("overhead")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.shared = dict_data.get("shared")
        instance.source_store = helpers.get_meta(dict_data.get("sourceStore"))
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.target_store = helpers.get_meta(dict_data.get("targetStore"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance


class MovePosition(types.MoySkladBaseClass):
    """
    Название 	Тип 	        Описание
    accountId 	UUID 	        ID учетной записи Обязательное при ответе Только для чтения
    assortment 	Meta 	        Метаданные товара/услуги/серии/модификации, которую представляет собой позиция Обязательное при ответе Expand
    id 	        UUID 	        ID позиции   Обязательное при ответе Только для чтения
    overhead 	Int 	        Накладные расходы. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-oprihodowanie-oprihodowaniq-nakladnye-rashody). Если Позиции Перемещения не заданы, то накладные расходы нельзя задать Обязательное при ответе Только для чтения
    pack 	    Object 	        Упаковка Товара. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-upakowki-towara)
    price 	    Float 	        Цена товара/услуги в копейках     Обязательное при ответе
    quantity 	Int 	        Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе. Обязательное при ответе
    sourceSlot 	Meta 	        Ячейка на складе, с которого совершается перемещение. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-yachejki-sklada
    targetSlot 	Meta 	        Ячейка на складе, на который совершается перемещение. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-sklad-yachejki-sklada
    things 	    Array(String) 	Серийные номера. Значение данного атрибута игнорируется, если товар позиции не находится на серийном учете. В ином случае количество товаров в позиции будет равно количеству серийных номеров, переданных в значении атрибута.
    """

    account_id: str
    assortment: types.Meta
    id: str
    overhead: int
    pack: dict
    price: float
    quantity: float
    source_slot: types.Meta
    target_slot: types.Meta
    things: typing.List[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "MovePosition":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.overhead = dict_data.get("overhead")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.source_slot = helpers.get_meta(dict_data.get("sourceSlot"))
        instance.target_slot = helpers.get_meta(dict_data.get("targetSlot"))
        instance.things = dict_data.get("things")
        return instance


class GetMovesRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-poluchit-peremescheniq

    Параметр 	Описание
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    search 	    string (optional) Example: 0001 Фильтр документов по указанной поисковой строке.
    """

    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ):
        """

        :param limit: Limit of moves to get (Лимит передвижений для получения)
        :param offset: Offset of moves to get (Отступ передвижений для получения)
        :param search: Search string (Строка поиска)
        """
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.search != Unset:
            params["search"] = self.search

        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/move",
            params=params,
        )

    def from_response(self, result) -> typing.List[Move]:
        return [Move.from_json(move) for move in result["rows"]]


class CreateMoveRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-sozdat-peremeschenie

    """

    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        overhead: typing.NotRequired[float]
        reason: typing.NotRequired[str]

    def __init__(
        self,
        organization: types.Meta,
        source_store: types.Meta,
        target_store: types.Meta,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
        customer_order: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        """

        :param organization: Organization (Организация)
        :param source_store: Source store (Склад-источник)
        :param target_store: Target store (Склад-получатель)

        :param applicable: Applicable (Отметка о проведении)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param internal_order: Internal order (Внутренний заказ)
        :param customer_order: Customer order (Заказ покупателя)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param overhead: Overhead (Накладные расходы)
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        """

        self.organization = organization
        self.source_store = source_store
        self.target_store = target_store

        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.internal_order = internal_order
        self.customer_order = customer_order
        self.meta = meta
        self.moment = moment
        self.name = name
        self.overhead = overhead
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = {
            "organization": {"meta": self.organization},
            "sourceStore": {"meta": self.source_store},
            "targetStore": {"meta": self.target_store},
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
            json_data["group"] = {"meta": self.group}
        if self.internal_order != Unset:
            json_data["internalOrder"] = {"meta": self.internal_order}
        if self.customer_order != Unset:
            json_data["customerOrder"] = {"meta": self.customer_order}
        if self.meta != Unset:
            json_data["meta"] = self.meta
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        if self.owner != Unset:
            json_data["owner"] = {"meta": self.owner}
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                new_position: dict = position.copy()
                new_position["assortment"] = {"meta": new_position["assortment"]}
                json_data["positions"].append(new_position)
        if self.project != Unset:
            json_data["project"] = {"meta": self.project}
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.state != Unset:
            json_data["state"] = {"meta": self.state}
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id

        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/move",
            json=json_data,
        )

    def from_response(self, result) -> Move:
        return Move.from_json(result)


class DeleteMoveRequest(types.ApiRequest):
    """
    Delete move (Удалить перемещение)

    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-udalit-peremeschenie
    """

    def __init__(self, move_id: str):
        """

        :param move_id: Move id (ID перемещения)
        """
        self.move_id = move_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}",
            allow_non_json=True,
        )

    def from_response(self, result) -> None:
        return None


class GetMoveRequest(types.ApiRequest):
    """
    Get move (Получить перемещение)

    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-peremeschenie
    """

    def __init__(self, move_id: str):
        """

        :param move_id: Move id (ID перемещения)
        """
        self.move_id = move_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}",
        )

    def from_response(self, result) -> Move:
        return Move.from_json(result)


class UpdateMoveRequest(types.ApiRequest):
    """
    Update move (Обновить перемещение)
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-izmenit-peremeschenie

    """

    def __init__(
        self,
        move_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        source_store: typing.Union[Unset, types.Meta] = Unset,
        target_store: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
        customer_order: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, types.MetaArray] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        """

        :param move_id: Move id (ID перемещения)

        :param organization: Organization (Организация)
        :param source_store: Source store (Склад-источник)
        :param target_store: Target store (Склад-получатель)
        :param applicable: Applicable (Отметка о проведении)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param internal_order: Internal order (Внутренний заказ)
        :param customer_order: Customer order (Заказ покупателя)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param overhead: Overhead (Накладные расходы)
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        """
        self.move_id = move_id

        self.organization = organization
        self.source_store = source_store
        self.target_store = target_store
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.internal_order = internal_order
        self.customer_order = customer_order
        self.meta = meta
        self.moment = moment
        self.name = name
        self.overhead = overhead
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = {}
        if self.organization != Unset:
            json_data["organization"] = (
                {"meta": self.organization} if self.organization is not None else None
            )
        if self.source_store != Unset:
            json_data["sourceStore"] = (
                {"meta": self.source_store} if self.source_store is not None else None
            )
        if self.target_store != Unset:
            json_data["targetStore"] = (
                {"meta": self.target_store} if self.target_store is not None else None
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
        if self.internal_order != Unset:
            json_data["internalOrder"] = (
                {"meta": self.internal_order}
                if self.internal_order is not None
                else None
            )
        if self.customer_order != Unset:
            json_data["order"] = (
                {"meta": self.customer_order}
                if self.customer_order is not None
                else None
            )
        if self.meta != Unset:
            json_data["meta"] = self.meta
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.positions != Unset:
            json_data["positions"] = self.positions
        if self.project != Unset:
            json_data["project"] = (
                {"meta": self.project} if self.project is not None else None
            )
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.state != Unset:
            json_data["state"] = (
                {"meta": self.state} if self.state is not None else None
            )
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}",
            json=json_data,
        )

    def from_response(self, result) -> Move:
        return Move.from_json(result)


class GetMovePositionsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-poluchit-pozicii

    Параметр 	    Описание
    id 	            string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Перемещения.
    limit 	        number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	        number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    search 	        string (optional) Example: 000F1 Фильтр документов по указанной поисковой строке.
    """

    def __init__(
        self,
        move_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ):
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param limit: Limit (Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.)
        :param offset: Offset (Отступ в выдаваемом списке сущностей.)
        :param search: Search (Фильтр документов по указанной поисковой строке.)
        """

        self.move_id = move_id
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.search != Unset:
            params["search"] = self.search

        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}/positions",
            params=params,
        )

    def from_response(self, result) -> typing.List[MovePosition]:
        return [MovePosition.from_json(item) for item in result["rows"]]


class CreateMovePositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-sozdat-poziciu

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Перемещения.

    assortment  Meta (required) - Информация о позиции
    quantity 	number (required) - Количество
    price 	    number (optional) - Цена
    overhead 	    number (optional) - Надбавка
    """

    def __init__(
        self,
        move_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, int] = Unset,
        overhead: typing.Union[Unset, int] = Unset,
    ):
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """
        self.move_id = move_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.overhead = overhead

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.price != Unset:
            json_data["price"] = self.price
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead

        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}/positions",
            json=json_data,
        )

    def from_response(self, result) -> typing.List[MovePosition]:
        return [MovePosition.from_json(item) for item in result["rows"]]


class GetMovePositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-poziciq-peremescheniq
    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Перемещения.
    positionID 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b20 id Перемещения.
    """

    def __init__(
        self,
        move_id: str,
        position_id: str,
    ):
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции перемещения)
        """
        self.move_id = move_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}/positions/{self.position_id}",
        )

    def from_response(self, result) -> MovePosition:
        return MovePosition.from_json(result)


class UpdateMovePositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-izmenit-poziciu

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Перемещения.
    positionID 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b20 id Перемещения.
    assortment  Meta (optional) - Информация о позиции
    quantity 	number (optional) - Количество
    price 	    number (optional) - Цена
    overhead 	    number (optional) - Надбавка
    """

    def __init__(
        self,
        move_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, int] = Unset,
        price: typing.Union[Unset, int] = Unset,
        overhead: typing.Union[Unset, int] = Unset,
    ):
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции)
        :param assortment: Assortment (Информация о позиции)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param overhead: Overhead (Надбавка)
        """
        self.move_id = move_id
        self.position_id = position_id

        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.overhead = overhead

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = (
                {"meta": self.assortment} if self.assortment is not None else None
            )
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.price != Unset:
            json_data["price"] = self.price
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead

        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result) -> MovePosition:
        return MovePosition.from_json(result)


class DeleteMovePositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-peremeschenie-udalit-poziciu

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Перемещения.
    positionID 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b20 id Перемещения.
    """

    def __init__(self, move_id: str, position_id: str):
        """

        :param move_id: Move ID (Идентификатор перемещения)
        :param position_id: Position ID (Идентификатор позиции)
        """
        self.move_id = move_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/move/{self.move_id}/positions/{self.position_id}",
        )

    def from_response(self, result) -> None:
        return None

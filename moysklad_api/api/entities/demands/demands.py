import datetime
import typing

from .... import types
from ....types import Unset


class Demand(types.MoySkladBaseClass):
    """
    Название            Тип           Описание
    accountId           UUID          ID учетной записи    Обязательное при ответе, Только для чтения
    agent               Meta          Метаданные контрагента      Обязательное при ответе
    agentAccount        Meta          Метаданные счета контрагента
    applicable          Boolean       Отметка о проведении    Обязательное при ответе
    attributes          Array(Object) Коллекция метаданных доп. полей. Поля объекта
    code                String(255)   Код Отгрузки
    contract            Meta          Метаданные договора
    created             DateTime      Дата создания    Обязательное при ответе, Только для чтения
    deleted             DateTime      Момент последнего удаления Отгрузки Только для чтения
    description         String(4096)  Комментарий Отгрузки
    externalCode        String(255)   Внешний код Отгрузки   Обязательное при ответе
    files               MetaArray     Метаданные массива Файлов (Максимальное количество файлов - 100)  Обязательное при ответе
    group               Meta          Отдел сотрудника  Обязательное при ответе
    id                  UUID          ID Отгрузки    Обязательное при ответе, Только для чтения
    meta                Meta          Метаданные Отгрузки   Обязательное при ответе
    moment              DateTime      Дата документа    Обязательное при ответе
    name                String(255)   Наименование Отгрузки    Обязательное при ответе
    organization        Meta          Метаданные юрлица      Обязательное при ответе
    organizationAccount Meta          Метаданные счета юрлица
    overhead            Object        Накладные расходы. Подробнее тут. Если Позиции Отгрузки не заданы, то накладные расходы нельзя задать
    owner               Meta          Владелец (Сотрудник)  Обязательное при ответе
    payedSum            Float         Сумма входящих платежей по Отгрузке  Обязательное при ответе, Только для чтения
    positions           MetaArray     Метаданные позиций Отгрузки     Обязательное при ответе
    printed             Boolean       Напечатан ли документ  Обязательное при ответе, Только для чтения
    project             Meta          Метаданные проекта
    published           Boolean       Опубликован ли документ  Обязательное при ответе, Только для чтения
    rate                Object        Валюта. Подробнее тут    Обязательное при ответе
    salesChannel        Meta          Метаданные канала продаж
    shared              Boolean       Общий доступ Обязательное при ответе
    shipmentAddress     String(255)   Адрес доставки Отгрузки
    shipmentAddressFull Object        Адрес доставки Отгрузки с детализацией по отдельным полям. Подробнее тут
    state               Meta          Метаданные статуса Отгрузки
    store               Meta          Метаданные склада      Обязательное при ответе
    sum                 Int           Сумма Отгрузки в копейках    Обязательное при ответе, Только для чтения
    syncId              UUID          ID синхронизации. После заполнения недоступен для изменения
    updated             DateTime      Момент последнего обновления Отгрузки    Обязательное при ответе, Только для чтения
    vatEnabled          Boolean       Учитывается ли НДС    Обязательное при ответе
    vatIncluded         Boolean       Включен ли НДС в цену
    vatSum              Float         Сумма НДС     Только для чтения
    """

    def __init__(self):
        self.account_id: str = None
        self.agent: types.Meta = None
        self.agent_account: typing.Optional[types.Meta] = None
        self.applicable: bool = None
        self.attributes: typing.Optional[typing.List[dict]] = None
        self.code: typing.Optional[str] = None
        self.contract: typing.Optional[types.Meta] = None
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
        self.organization_account: typing.Optional[types.Meta] = None
        self.overhead: typing.Optional[dict] = None
        self.owner: types.Meta = None
        self.payed_sum: float = None
        self.positions: types.MetaArray = None
        self.printed: bool = None
        self.project: typing.Optional[types.Meta] = None
        self.published: bool = None
        self.rate: dict = None
        self.sales_channel: typing.Optional[types.Meta] = None
        self.shared: bool = None
        self.shipment_address: typing.Optional[str] = None
        self.shipment_address_full: typing.Optional[dict] = None
        self.state: typing.Optional[types.Meta] = None
        self.store: types.Meta = None
        self.sum: int = None
        self.sync_id: typing.Optional[str] = None
        self.updated: datetime.datetime = None
        self.vat_enabled: bool = None
        self.vat_included: typing.Optional[bool] = None
        self.vat_sum: typing.Optional[float] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Demand":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        agent = dict_data.get("agent")
        if agent is not None:
            instance.agent = agent["meta"]
        agent_account = dict_data.get("agentAccount")
        if agent_account is not None:
            instance.agent_account = agent_account["meta"]
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        contract = dict_data.get("contract")
        if contract is not None:
            instance.contract = contract["meta"]
        created = dict_data.get("created")
        if created is not None:
            instance.created = datetime.datetime.fromisoformat(created)
        deleted = dict_data.get("deleted")
        if deleted is not None:
            instance.deleted = datetime.datetime.fromisoformat(deleted)
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        group = dict_data.get("group")
        if group is not None:
            instance.group = group["meta"]
        instance.id = dict_data.get("id")
        meta = dict_data.get("meta")
        if meta is not None:
            instance.meta = meta
        moment = dict_data.get("moment")
        if moment is not None:
            instance.moment = datetime.datetime.fromisoformat(moment)
        instance.name = dict_data.get("name")
        organization = dict_data.get("organization")
        if organization is not None:
            instance.organization = organization["meta"]
        organization_account = dict_data.get("organizationAccount")
        if organization_account is not None:
            instance.organization_account = organization_account["meta"]
        instance.overhead = dict_data.get("overhead")
        owner = dict_data.get("owner")
        if owner is not None:
            instance.owner = owner["meta"]
        instance.payed_sum = dict_data.get("payedSum")
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        project = dict_data.get("project")
        if project is not None:
            instance.project = project["meta"]
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        sales_channel = dict_data.get("salesChannel")
        if sales_channel is not None:
            instance.sales_channel = sales_channel["meta"]
        instance.shared = dict_data.get("shared")
        instance.shipment_address = dict_data.get("shipmentAddress")
        instance.shipment_address_full = dict_data.get("shipmentAddressFull")
        state = dict_data.get("state")
        if state is not None:
            instance.state = state["meta"]
        store = dict_data.get("store")
        if store is not None:
            instance.store = store["meta"]
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        updated = dict_data.get("updated")
        if updated is not None:
            instance.updated = datetime.datetime.fromisoformat(updated)
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        return instance


class DemandPosition(types.MoySkladBaseClass):
    """
    Название           Тип           Описание
    accountId          UUID          ID учетной записи
    assortment         Meta          Метаданные товара/услуги/серии/модификации/комплекта, которую представляет собой позиция
    cost               Int           Себестоимость (только для услуг)
    discount           Int           Процент скидки или наценки. Наценка указывается отрицательным числом, т.е. -10 создаст наценку в 10%
    id                 UUID          ID позиции
    pack               Object        Упаковка Товара. Подробнее тут
    price              Float         Цена товара/услуги в копейках
    quantity           Int           Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе.
    slot               Meta          Ячейка на складе. Подробнее тут
    things             Array(String) Серийные номера. Значение данного атрибута игнорируется, если товар позиции не находится на серийном учете. В ином случае количество товаров в позиции будет равно количеству серийных номеров, переданных в значении атрибута.
    trackingCodes      Array(Object) Коды маркировки товаров и транспортных упаковок. Подробнее тут
    trackingCodes_1162 Array(Object) Коды маркировки товаров в формате тега 1162. Подробнее тут
    overhead           Int           Накладные расходы. Подробнее тут. Если Позиции Отгрузки не заданы, то накладные расходы нельзя задать.
    vat                Int           НДС, которым облагается текущая позиция
    vatEnabled         Boolean       Включен ли НДС для позиции. С помощью этого флага для позиции можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%.
    """

    def __init__(self):
        self.account_id: str = None
        self.assortment: types.Meta = None
        self.cost: typing.Optional[int] = None
        self.discount: int = None
        self.id: str = None
        self.pack: typing.Optional[dict] = None
        self.price: float = None
        self.quantity: float = None
        self.slot: typing.Optional[types.Meta] = None
        self.things: typing.Optional[typing.List[str]] = None
        self.tracking_codes: typing.Optional[typing.List[dict]] = None
        self.tracking_codes_1162: typing.Optional[typing.List[dict]] = None
        self.overhead: int = None
        self.vat: int = None
        self.vat_enabled: bool = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "DemandPosition":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        assortment = dict_data.get("assortment")
        if assortment is not None:
            instance.assortment = assortment["meta"]
        instance.cost = dict_data.get("cost")
        instance.discount = dict_data.get("discount")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        slot = dict_data.get("slot")
        if slot is not None:
            instance.slot = slot["meta"]
        instance.things = dict_data.get("things")
        instance.tracking_codes = dict_data.get("trackingCodes")
        instance.tracking_codes_1162 = dict_data.get("trackingCodes_1162")
        instance.overhead = dict_data.get("overhead")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance


class CreateDemandRequest(types.ApiRequest):
    class CreateDemandPosition(typing.TypedDict):
        assortment: types.Meta
        price: float
        quantity: float
        trackingCodes: typing.NotRequired[typing.List[dict]]
        vat: typing.NotRequired[int]
        discount: typing.NotRequired[int]
        reserve: typing.NotRequired[int]
        overhead: typing.NotRequired[int]
        cost: typing.NotRequired[int]
        pack: typing.NotRequired[dict]

    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-sozdat-otgruzku

    Название            Тип           Описание
    agent               Meta          Метаданные контрагента      Обязательное при ответе
    agentAccount        Meta          Метаданные счета контрагента
    applicable          Boolean       Отметка о проведении    Обязательное при ответе
    attributes          Array(Object) Коллекция метаданных доп. полей. Поля объекта
    code                String(255)   Код Отгрузки
    contract            Meta          Метаданные договора
    description         String(4096)  Комментарий Отгрузки
    externalCode        String(255)   Внешний код Отгрузки   Обязательное при ответе
    files               MetaArray     Метаданные массива Файлов (Максимальное количество файлов - 100)  Обязательное при ответе
    group               Meta          Отдел сотрудника  Обязательное при ответе
    meta                Meta          Метаданные Отгрузки   Обязательное при ответе
    moment              DateTime      Дата документа    Обязательное при ответе
    name                String(255)   Наименование Отгрузки    Обязательное при ответе
    organization        Meta          Метаданные юрлица      Обязательное при ответе
    organizationAccount Meta          Метаданные счета юрлица
    overhead            Object        Накладные расходы. Подробнее тут. Если Позиции Отгрузки не заданы, то накладные расходы нельзя задать
    owner               Meta          Владелец (Сотрудник)  Обязательное при ответе
    positions           MetaArray     Метаданные позиций Отгрузки     Обязательное при ответе
    project             Meta          Метаданные проекта
    rate                Object        Валюта. Подробнее тут    Обязательное при ответе
    salesChannel        Meta          Метаданные канала продаж
    shared              Boolean       Общий доступ Обязательное при ответе
    shipmentAddress     String(255)   Адрес доставки Отгрузки
    shipmentAddressFull Object        Адрес доставки Отгрузки с детализацией по отдельным полям. Подробнее тут
    state               Meta          Метаданные статуса Отгрузки
    store               Meta          Метаданные склада      Обязательное при ответе
    syncId              UUID          ID синхронизации. После заполнения недоступен для изменения
    vatEnabled          Boolean       Учитывается ли НДС    Обязательное при ответе
    vatIncluded         Boolean       Включен ли НДС в цену
    """

    def __init__(
        self,
        organization: types.Meta,
        agent: types.Meta,
        store: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, list] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, bool] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, CreateDemandPosition] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, bool] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        shipment_address: typing.Union[Unset, str] = Unset,
        shipment_address_full: typing.Union[Unset, dict] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param organization: Organization (организация)
        :param agent: Agent (контрагент)
        :param store: Store (склад)
        :param agent_account: Agent account (Аккаунт контрагента)
        :param applicable: Is applicable (Проведено(
        :param attributes: Attributes (массив дополнительных полей)
        :param code: Code (код)
        :param contract: Contract (договор)
        :param description: Description (описание)
        :param external_code: External code (внешний код)
        :param files: Files (файлы)
        :param group: Group (группа)
        :param moment: Creation date (Время создания)
        :param name: Name (название)
        :param organization_account: Organization account (аккаунт организации)
        :param overhead: Overhead (накладные расходы)
        :param owner: Owner (владелец)
        :param positions: Positions (позиции)
        :param project: Project (проект)
        :param rate: Rate (валюта)
        :param sales_channel: Sales channel (канал продаж)
        :param shared: Shared (общий доступ)
        :param shipment_address: Shipment address (адрес доставки)
        :param shipment_address_full: Shipment address full (полный адрес доставки)
        :param state: State (статус)
        :param sync_id: Sync id (id синхронизации)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)
        """
        self.organization = organization
        self.agent = agent
        self.store = store
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.overhead = overhead
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.sales_channel = sales_channel
        self.shared = shared
        self.shipment_address = shipment_address
        self.shipment_address_full = shipment_address_full
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> dict:
        json_data = {
            "organization": {"meta": self.organization},
            "agent": {"meta": self.agent},
            "store": {"meta": self.store},
        }
        if self.agent_account != Unset:
            json_data["agenAccount"] = (
                {"meta": self.agent_account} if self.agent_account is not None else None
            )
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.contract != Unset:
            json_data["contract"] = (
                {"meta": self.contract} if self.contract is not None else None
            )
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
        if self.organization_account != Unset:
            json_data["organizationAccount"] = self.organization_account
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
        if self.sales_channel != Unset:
            json_data["salesChannel"] = self.sales_channel
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.shipment_address != Unset:
            json_data["shipmentAddress"] = self.shipment_address
        if self.shipment_address_full != Unset:
            json_data["shipmentAddressFull"] = self.shipment_address_full
        if self.state != Unset:
            json_data["state"] = (
                {"meta": self.state} if self.state is not None else None
            )
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included

        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand",
            "json": json_data,
        }

    @classmethod
    def from_response(cls, dict_data: dict) -> "Demand":
        return Demand.from_json(dict_data)


class GetDemandsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-poluchit-spisok-otgruzok

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

        :param limit: Limit (ограничение)
        :param offset: Offset (смещение)
        :param search: Search (поиск)
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
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand",
            "params": params,
        }

    def from_response(self, result: dict) -> typing.List[Demand]:
        return [Demand.from_json(demand_json) for demand_json in result["rows"]]


class DeleteDemandRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-udalit-otgruzku

    Параметр 	Описание
    id 	        string (path) Example: 3e2f2d2b-8c8d-11e9-9109-f8fc000000b8 Идентификатор отгрузки
    """

    def __init__(self, demand_id: str):
        """

        :param demand_id: Id (идентификатор)
        """
        self.id = demand_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/demand/{self.id}",
            "allow_non_json": True,
        }

    def from_response(self, result: dict) -> None:
        return None


class GetDemandRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-otgruzka

    Параметр 	Описание
    id 	        string (path) Example: 3e2f2d2b-8c8d-11e9-9109-f8fc000000b8 Идентификатор отгрузки
    """

    def __init__(self, demand_id: str):
        """

        :param demand_id: Id (идентификатор)
        """
        self.demand_id = demand_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/demand/{self.demand_id}",
        }

    def from_response(self, result: dict) -> Demand:
        return Demand.from_json(result)


class UpdateDemandRequest(types.ApiRequest):
    UpdateDemandPosition = CreateDemandRequest.CreateDemandPosition

    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-sozdat-otgruzku

    Название            Тип           Описание
    agent               Meta          Метаданные контрагента      Обязательное при ответе
    agentAccount        Meta          Метаданные счета контрагента
    applicable          Boolean       Отметка о проведении    Обязательное при ответе
    attributes          Array(Object) Коллекция метаданных доп. полей. Поля объекта
    code                String(255)   Код Отгрузки
    contract            Meta          Метаданные договора
    description         String(4096)  Комментарий Отгрузки
    externalCode        String(255)   Внешний код Отгрузки   Обязательное при ответе
    files               MetaArray     Метаданные массива Файлов (Максимальное количество файлов - 100)  Обязательное при ответе
    group               Meta          Отдел сотрудника  Обязательное при ответе
    meta                Meta          Метаданные Отгрузки   Обязательное при ответе
    moment              DateTime      Дата документа    Обязательное при ответе
    name                String(255)   Наименование Отгрузки    Обязательное при ответе
    organization        Meta          Метаданные юрлица      Обязательное при ответе
    organizationAccount Meta          Метаданные счета юрлица
    overhead            Object        Накладные расходы. Подробнее тут. Если Позиции Отгрузки не заданы, то накладные расходы нельзя задать
    owner               Meta          Владелец (Сотрудник)  Обязательное при ответе
    positions           MetaArray     Метаданные позиций Отгрузки     Обязательное при ответе
    project             Meta          Метаданные проекта
    rate                Object        Валюта. Подробнее тут    Обязательное при ответе
    salesChannel        Meta          Метаданные канала продаж
    shared              Boolean       Общий доступ Обязательное при ответе
    shipmentAddress     String(255)   Адрес доставки Отгрузки
    shipmentAddressFull Object        Адрес доставки Отгрузки с детализацией по отдельным полям. Подробнее тут
    state               Meta          Метаданные статуса Отгрузки
    store               Meta          Метаданные склада      Обязательное при ответе
    syncId              UUID          ID синхронизации. После заполнения недоступен для изменения
    vatEnabled          Boolean       Учитывается ли НДС    Обязательное при ответе
    vatIncluded         Boolean       Включен ли НДС в цену
    """

    def __init__(
        self,
        demand_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, list] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, bool] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, UpdateDemandPosition] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, bool] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        shipment_address: typing.Union[Unset, str] = Unset,
        shipment_address_full: typing.Union[Unset, dict] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param demand_id: ID (идентификатор)
        :param organization: Organization (организация)
        :param agent: Agent (контрагент)
        :param store: Store (склад)
        :param agent_account: Agent account (Аккаунт контрагента)
        :param applicable: Is applicable (Проведено(
        :param attributes: Attributes (массив дополнительных полей)
        :param code: Code (код)
        :param contract: Contract (договор)
        :param description: Description (описание)
        :param external_code: External code (внешний код)
        :param files: Files (файлы)
        :param group: Group (группа)
        :param moment: Creation date (Время создания)
        :param name: Name (название)
        :param organization_account: Organization account (аккаунт организации)
        :param overhead: Overhead (накладные расходы)
        :param owner: Owner (владелец)
        :param positions: Positions (позиции)
        :param project: Project (проект)
        :param rate: Rate (валюта)
        :param sales_channel: Sales channel (канал продаж)
        :param shared: Shared (общий доступ)
        :param shipment_address: Shipment address (адрес доставки)
        :param shipment_address_full: Shipment address full (полный адрес доставки)
        :param state: State (статус)
        :param sync_id: Sync id (id синхронизации)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)
        """
        self.id = demand_id
        self.organization = organization
        self.agent = agent
        self.store = store
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.overhead = overhead
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.sales_channel = sales_channel
        self.shared = shared
        self.shipment_address = shipment_address
        self.shipment_address_full = shipment_address_full
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> dict:
        json_data = {}
        if self.organization != Unset:
            json_data["organization"] = (
                {"meta": self.organization} if self.organization is not None else None
            )
        if self.agent != Unset:
            json_data["agent"] = (
                {"meta": self.agent} if self.agent is not None else None
            )
        if self.store != Unset:
            json_data["store"] = (
                {"meta": self.store} if self.store is not None else None
            )
        if self.agent_account != Unset:
            json_data["agenAccount"] = (
                {"meta": self.agent_account} if self.agent_account is not None else None
            )
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.contract != Unset:
            json_data["contract"] = (
                {"meta": self.contract} if self.contract is not None else None
            )
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
        if self.organization_account != Unset:
            json_data["organizationAccount"] = self.organization_account
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
        if self.sales_channel != Unset:
            json_data["salesChannel"] = self.sales_channel
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.shipment_address != Unset:
            json_data["shipmentAddress"] = self.shipment_address
        if self.shipment_address_full != Unset:
            json_data["shipmentAddressFull"] = self.shipment_address_full
        if self.state != Unset:
            json_data["state"] = (
                {"meta": self.state} if self.state is not None else None
            )
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included

        return {
            "method": "PUT",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand/"
            + str(self.id),
            "json": json_data,
        }

    @classmethod
    def from_response(cls, dict_data: dict) -> "Demand":
        return Demand.from_json(dict_data)


class GetDemandPositionsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-poluchit-pozicii-otgruzki

    Параметр 	Описание
    demand_id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Отгрузки.
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(self, demand_id: str, limit: int = 1000, offset: int = 0):
        """

        :param demand_id: ID (идентификатор)
        :param limit: Limit (лимит)
        :param offset: Offset (смещение)
        """
        self.id = demand_id
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
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand/"
            + str(self.id)
            + "/positions",
            "params": params,
        }

    @classmethod
    def from_response(cls, dict_data: dict) -> typing.List[DemandPosition]:
        return [DemandPosition.from_json(item) for item in dict_data["rows"]]


class CreateDemandPositionsRequest(types.ApiRequest):
    CreateDemandPositionPosition = CreateDemandRequest.CreateDemandPosition
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-sozdat-poziciu-otgruzki


    """

    def __init__(
        self, demand_id: str, positions: typing.List[CreateDemandPositionPosition]
    ):
        """

        :param demand_id:  ID of demand (ID отгрузки)
        :param positions: List of positions (Список позиций)
        """
        if len(positions) == 0:
            raise ValueError("positions can't be empty")
        self.id = demand_id
        self.positions = positions

    def to_request(self) -> dict:
        json = self.positions
        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand/"
            + str(self.id)
            + "/positions",
            "json": json,
        }

    def from_response(self, result: list) -> typing.List[DemandPosition]:
        return [DemandPosition.from_json(item) for item in result]


class GetDemandPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-poluchit-poziciu
    """

    def __init__(self, demand_id: str, position_id: str):
        """

        :param demand_id: ID of demand (ID отгрузки)
        :param position_id: ID of position (ID позиции)
        """
        self.demand_id = demand_id
        self.position_id = position_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand/"
            + str(self.demand_id)
            + "/positions/"
            + str(self.position_id),
        }

    def from_response(self, result: dict) -> DemandPosition:
        return DemandPosition.from_json(result)


class UpdateDemandPositionRequest(types.ApiRequest):
    UpdateDemandPositionPosition = CreateDemandRequest.CreateDemandPosition
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-obnovit-poziciu-otgruzki
    """

    def __init__(
        self, demand_id: str, position_id: str, position: UpdateDemandPositionPosition
    ):
        """

        :param demand_id: ID of demand (ID отгрузки)
        :param position_id: ID of position (ID позиции)
        :param position: DemandPosition
        """
        self.demand_id = demand_id
        self.position_id = position_id
        self.position = position

    def to_request(self) -> dict:
        json = self.position
        return {
            "method": "PUT",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand/"
            + str(self.demand_id)
            + "/positions/"
            + str(self.position_id),
            "json": json,
        }

    def from_response(self, result: dict) -> DemandPosition:
        return DemandPosition.from_json(result)


class DeleteDemandPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-otgruzka-udalit-poziciu-otgruzki
    """

    def __init__(self, demand_id: str, position_id: str):
        """

        :param demand_id: ID of demand (ID отгрузки)
        :param position_id: ID of position (ID позиции)
        """
        self.demand_id = demand_id
        self.position_id = position_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/demand/"
            + str(self.demand_id)
            + "/positions/"
            + str(self.position_id),
            "allow_non_json": True,
        }

    def from_response(self, result: dict) -> None:
        return None

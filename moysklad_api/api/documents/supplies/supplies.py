import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Supply(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka


    Атрибуты сущности
    Название 	        Тип 	 	    Описание
    accountId 	        UUID 	 	    ID учетной записи                                   Обязательное при ответе Только для чтения Change-handler
    agent 	            Meta 	 	    Метаданные контрагента                              Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    agentAccount 	    Meta 		    Метаданные счета контрагента                        Expand Change-handler Update-provider
    applicable 	        Boolean 	    Отметка о проведении                                Обязательное при ответе Change-handler Update-provider
    attributes 	        Array(Object) 	Коллекция метаданных доп. полей. Поля объекта       Change-handler Update-provider
    code 	            String(255) 	Код Приемки
    contract 	        Meta 	 	    Метаданные договора                                 Expand Change-handler Update-provider
    created 	        DateTime 	  	Дата создания                                       Обязательное при ответе Только для чтения Change-handler
    deleted 	        DateTime 	  	Момент последнего удаления Приемки                  Только для чтения
    description 	    String(4096) 	Комментарий Приемки                                 Change-handler Update-provider
    externalCode 	    String(255) 	Внешний код Приемки                                 Обязательное при ответе Change-handler
    files 	            MetaArray 		Метаданные массива Файлов                           Обязательное при ответе Expand
    group 	            Meta 	 	    Отдел сотрудника                                    Обязательное при ответе Expand
    id 	                UUID 	 	    ID Приемки                                          Обязательное при ответе Только для чтения Change-handler
    incomingDate 	    DateTime 		Входящая дата                                       Change-handler Update-provider
    incomingNumber 	    String(255) 	Входящий номер                                      Change-handler Update-provider
    meta 	            Meta 		    Метаданные Приемки                                  Обязательное при ответе Change-handler
    moment 	            DateTime 	  	Дата документа                                      Обязательное при ответе Change-handler Update-provider
    name 	            String(255) 	Наименование Приемки                                Обязательное при ответе Change-handler Update-provider
    organization 	    Meta 	 	    Метаданные юрлица                                   Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    organizationAccount Meta 		    Метаданные счета юрлица                             Expand Change-handler Update-provider
    overhead 	        Object 		    Накладные расходы. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-priemka-priemki-nakladnye-rashody). Если Позиции Приемки не заданы, то накладные расходы нельзя задать Update-provider
    owner 	            Meta 	 	    Владелец (Сотрудник)                                Обязательное при ответе Expand
    payedSum 	        Float 		    Сумма входящих платежей по Приемке                  Обязательное при ответе Только для чтения
    positions 	        MetaArray 		Метаданные позиций Приемки                          Обязательное при ответе Expand Change-handler Update-provider
    printed 	        Boolean 	 	Напечатан ли документ                               Обязательное при ответе Только для чтения
    project 	        Meta 	 	    Метаданные проекта                                  Expand Change-handler Update-provider
    published 	        Boolean 	 	Опубликован ли документ                             Обязательное при ответе Только для чтения
    rate 	            Object 		    Валюта. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-teh-operaciq-valuta-w-dokumentah Обязательное при ответе Change-handler Update-provider
    shared 	            Boolean 	 	Общий доступ                                        Обязательное при ответе
    state 	            Meta 	 	    Метаданные статуса Приемки                          Expand Change-handler Update-provider
    store 	            Meta 	 	    Метаданные склада                                   Обязательное при ответе Expand Необходимо при создании Change-handler Update-provider
    sum 	            Int 	  	    Сумма Приемки в копейках                            Обязательное при ответе Только для чтения Change-handler
    syncId 	            UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    updated 	        DateTime 	  	Момент последнего обновления Приемки                Обязательное при ответе Только для чтения Change-handler
    vatEnabled 	        Boolean 		Учитывается ли НДС                                  Обязательное при ответе Change-handler Update-provider
    vatIncluded 	    Boolean 		Включен ли НДС в цену                               Change-handler Update-provider
    vatSum 	            Float 		    Сумма НДС                                           Обязательное при ответе Только для чтения Change-handler
    """

    account_id: str
    agent: types.Meta
    agent_account: typing.Optional[types.Meta]
    applicable: bool
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    contract: typing.Optional[types.Meta]
    created: datetime.datetime
    deleted: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    external_code: str
    files: types.MetaArray
    group: types.Meta
    id: str
    incoming_date: datetime.datetime
    incoming_number: typing.Optional[str]
    meta: types.Meta
    moment: datetime.datetime
    name: str
    organization: types.Meta
    organization_account: typing.Optional[types.Meta]
    overhead: typing.Optional[dict]
    owner: types.Meta
    payed_sum: float
    positions: types.MetaArray
    printed: bool
    project: typing.Optional[types.Meta]
    published: bool
    rate: typing.Optional[dict]
    shared: bool
    state: types.Meta
    store: types.Meta
    sum: int
    sync_id: typing.Optional[str]
    updated: datetime.datetime
    vat_enabled: bool
    vat_included: typing.Optional[bool]
    vat_sum: float
    invoices_in: typing.List[types.Meta]
    facture_in: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Supply":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount"))
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.contract = helpers.get_meta(dict_data.get("contract"))
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = helpers.get_meta(dict_data.get("files"))
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.incoming_date = helpers.parse_date(dict_data.get("incomingDate"))
        instance.incoming_number = dict_data.get("incomingNumber")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.overhead = dict_data.get("overhead")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.payed_sum = dict_data.get("payedSum")
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        instance.invoices_in = [
            helpers.get_meta(x, must=True) for x in dict_data.get("invoicesIn", [])
        ]
        instance.facture_in = helpers.get_meta(dict_data.get("factureIn"))
        return instance


class Position(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-priemki

    Название 	        Тип 	        Описание
    accountId 	        UUID 	        ID учетной записи                                                                   Обязательное при ответе Только для чтения Change-handler
    assortment 	        Meta 	        Метаданные товара/услуги/серии/модификации, которую представляет собой позиция      Обязательное при ответе Expand Change-handler Update-provider
    country 	        Meta 	        Метаданные страны                                                                   Expand
    discount 	        Int 	        Процент скидки или наценки. Наценка указывается отрицательным числом, т.е. -10 создаст наценку в 10% Обязательное при ответе Change-handler Update-provider
    gtd 	            Object 	        ГТД. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruzowaq-tamozhennaq-deklaraciq-gtd
    id 	                UUID 	        ID позиции                                                                          Обязательное при ответе Только для чтения Change-handler
    pack 	            Object 	        Упаковка Товара. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-upakowki-towara  Change-handler Update-provider
    price 	            Float 	        Цена товара/услуги в копейках                                                       Обязательное при ответе Change-handler Update-provider
    quantity 	        Int 	        Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе. Обязательное при ответе Change-handler Update-provider
    slot 	            Meta 	        Ячейка на складе. Подробнее тут                                                     Expand
    things 	            Array(String) 	Серийные номера. Значение данного атрибута игнорируется, если товар позиции не находится на серийном учете. В ином случае количество товаров в позиции будет равно количеству серийных номеров, переданных в значении атрибута.
    trackingCodes 	    Array(Object) 	Коды маркировки товаров и транспортных упаковок. Подробнее тут
    overhead 	        Int 	        Накладные расходы. Подробнее тут. Если Позиции Приемки не заданы, то накладные расходы нельзя задать.       Обязательное при ответе Только для чтения
    vat 	            Boolean 	НДС, которым облагается текущая позиция                                                 Обязательное при ответе Change-handler Update-provider
    vatEnabled 	        Boolean 	Включен ли НДС для позиции. С помощью этого флага для позиции можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%. Обязательное при ответе Change-handler Update-provider
    """

    account_id: str
    assortment: types.Meta
    country: typing.Optional[types.Meta]
    discount: int
    gtd: typing.Optional[dict]
    id: str
    pack: typing.Optional[dict]
    price: float
    quantity: float
    slot: typing.Optional[int]
    things: typing.Optional[typing.List[str]]
    overhead: int
    vat: bool
    vat_enabled: bool

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.country = helpers.get_meta(dict_data.get("country"))
        instance.discount = dict_data.get("discount")
        instance.gtd = dict_data.get("gtd")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.slot = helpers.get_meta(dict_data.get("slot"))
        instance.things = dict_data.get("things")
        instance.overhead = dict_data.get("overhead")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance


class GetSuppliesRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-poluchit-spisok-priemok

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

        :param limit: Limit of entities to extract (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities (Отступ в выдаваемом списке сущностей)
        :param search: Filter documents by the specified search string (Фильтр документов по указанной поисковой строке)
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
            url="https://api.moysklad.ru/api/remap/1.2/entity/supply",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Supply]:
        return [Supply.from_json(i) for i in result["rows"]]


class CreateSupplyRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-sozdat-priemku

    Create a new supply (Создать новую приемку)
    """

    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        discount: typing.NotRequired[int]
        vat: typing.NotRequired[int]
        trackingCodes: typing.NotRequired[typing.List[dict]]
        overhead: typing.NotRequired[float]

    def __init__(
        self,
        organization: types.Meta,
        agent: types.Meta,
        store: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        incoming_date: typing.Union[Unset, datetime.datetime] = Unset,
        incoming_number: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param organization: Organization (Организация)
        :param agent: Agent (Контрагент)
        :param store: Store (Склад)
        :param agent_account: Metadata of the agent account (Метаданные счета контрагента)
        :param applicable: Mark as applicable (Пометить как проведенный)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract (Договор)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param incoming_date: Incoming date (Дата поступления)
        :param incoming_number: Incoming number (Номер поступления)
        :param moment: Moment (Время документа)
        :param name: Name (Название)
        :param organization_account: Metadata of the organization account (Метаданные счета организации)
        :param overhead: Overhead (Налоги) https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-priemka-priemki-nakladnye-rashody
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        :param vat_enabled: VAT enabled (НДС включен)
        :param vat_included: VAT included (НДС считается)
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
        self.incoming_date = incoming_date
        self.incoming_number = incoming_number
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.overhead = overhead
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = {
            "organization": {"meta": self.organization},
            "agent": {"meta": self.agent},
            "store": {"meta": self.store},
        }
        if self.agent_account != Unset:
            json_data["agentAccount"] = (
                {"meta": self.agent_account}
                if self.agent_account is not None
                else None
                if self.agent_account is not None
                else None
            )
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.contract != Unset:
            json_data["contract"] = (
                {"meta": self.contract}
                if self.contract is not None
                else None
                if self.contract is not None
                else None
            )
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.files != Unset:
            json_data["files"] = self.files
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group}
                if self.group is not None
                else None
                if self.group is not None
                else None
            )
        if self.incoming_date != Unset:
            json_data["incomingDate"] = helpers.date_to_str(self.incoming_date)
        if self.incoming_number != Unset:
            json_data["incomingNumber"] = self.incoming_number
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization_account != Unset:
            json_data["organizationAccount"] = (
                {"meta": self.organization_account}
                if self.organization_account is not None
                else None
                if self.organization_account is not None
                else None
            )
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner}
                if self.owner is not None
                else None
                if self.owner is not None
                else None
            )
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                new_position: dict = position.copy()
                new_position["assortment"] = {"meta": new_position["assortment"]}
                json_data["positions"].append(new_position)
        if self.project != Unset:
            json_data["project"] = (
                {"meta": self.project}
                if self.project is not None
                else None
                if self.project is not None
                else None
            )
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.state != Unset:
            json_data["state"] = (
                {"meta": self.state}
                if self.state is not None
                else None
                if self.state is not None
                else None
            )
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included
        return RequestData(
            method="POST",
            url="https://api.moysklad.ru/api/remap/1.2/entity/supply",
            json=json_data,
        )

    def from_response(self, result: dict) -> Supply:
        return Supply.from_json(result)


class DeleteSupplyRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-udalit-priemku

    Delete supply (Удалить приемку)
    """

    def __init__(self, supply_id: str):
        """
        Delete supply (Удалить приемку)

        :param supply_id: ID of the supply (ID приемки)
        """
        self.supply_id = supply_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetSupplyRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-poluchit-priemku

    Get supply (Получить приемку)
    """

    def __init__(self, supply_id: str):
        """
        Get supply (Получить приемку)

        :param supply_id: ID of the supply (ID приемки)
        """
        self.supply_id = supply_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}",
        )

    def from_response(self, result: dict) -> Supply:
        return Supply.from_json(result)


class UpdateSupplyRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-izmenit-priemku

    Update supply (Изменить приемку)
    """

    UpdatePosition = CreateSupplyRequest.CreatePosition

    def __init__(
        self,
        supply_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        incoming_date: typing.Union[Unset, datetime.datetime] = Unset,
        incoming_number: typing.Union[Unset, str] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        overhead: typing.Union[Unset, dict] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param supply_id: ID of the supply (ID приемки)
        :param organization: Organization (Организация)
        :param agent: Agent (Контрагент)
        :param store: Store (Склад)
        :param agent_account: Metadata of the agent account (Метаданные счета контрагента)
        :param applicable: Mark as applicable (Пометить как проведенный)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract (Договор)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group (Группа)
        :param incoming_date: Incoming date (Дата поступления)
        :param incoming_number: Incoming number (Номер поступления)
        :param moment: Moment (Время документа)
        :param name: Name (Название)
        :param organization_account: Metadata of the organization account (Метаданные счета организации)
        :param overhead: Overhead (Налоги) https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#dokumenty-priemka-priemki-nakladnye-rashody
        :param owner: Owner (Владелец)
        :param positions: Positions (Позиции)
        :param project: Project (Проект)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State (Статус)
        :param sync_id: Sync ID (Идентификатор синхронизации)
        :param vat_enabled: VAT enabled (НДС включен)
        :param vat_included: VAT included (НДС считается)
        """
        self.supply_id = supply_id
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
        self.incoming_date = incoming_date
        self.incoming_number = incoming_number
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.overhead = overhead
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.sync_id = sync_id
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = {}
        if self.organization != Unset:
            json_data["organization"] = (
                {"meta": self.organization}
                if self.organization is not None
                else None
                if self.organization is not None
                else None
            )
        if self.agent != Unset:
            json_data["agent"] = (
                {"meta": self.agent}
                if self.agent is not None
                else None
                if self.agent is not None
                else None
            )
        if self.store != Unset:
            json_data["store"] = (
                {"meta": self.store}
                if self.store is not None
                else None
                if self.store is not None
                else None
            )
        if self.agent_account != Unset:
            json_data["agentAccount"] = (
                {"meta": self.agent_account}
                if self.agent_account is not None
                else None
                if self.agent_account is not None
                else None
            )
        if self.applicable != Unset:
            json_data["applicable"] = self.applicable
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.contract != Unset:
            json_data["contract"] = (
                {"meta": self.contract}
                if self.contract is not None
                else None
                if self.contract is not None
                else None
            )
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.files != Unset:
            json_data["files"] = self.files
        if self.group != Unset:
            json_data["group"] = (
                {"meta": self.group}
                if self.group is not None
                else None
                if self.group is not None
                else None
            )
        if self.incoming_date != Unset:
            json_data["incomingDate"] = helpers.date_to_str(self.incoming_date)
        if self.incoming_number != Unset:
            json_data["incomingNumber"] = self.incoming_number
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization_account != Unset:
            json_data["organizationAccount"] = (
                {"meta": self.organization_account}
                if self.organization_account is not None
                else None
                if self.organization_account is not None
                else None
            )
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner}
                if self.owner is not None
                else None
                if self.owner is not None
                else None
            )
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                new_position: dict = position.copy()
                new_position["assortment"] = {"meta": new_position["assortment"]}
                json_data["positions"].append(new_position)
        if self.project != Unset:
            json_data["project"] = (
                {"meta": self.project}
                if self.project is not None
                else None
                if self.project is not None
                else None
            )
        if self.rate != Unset:
            json_data["rate"] = self.rate
        if self.shared != Unset:
            json_data["shared"] = self.shared
        if self.state != Unset:
            json_data["state"] = (
                {"meta": self.state}
                if self.state is not None
                else None
                if self.state is not None
                else None
            )
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included

        return RequestData(
            method="PUT",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Supply:
        return Supply.from_json(result)


class GetSupplyPositionsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-poluchit-pozicii-priemki

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Приемки.
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(
        self,
        supply_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        """
        Get supply positions
        Получить позиции приемки

        :param supply_id: ID of supply (ID приемки)
        :param limit: Limit of positions (Максимальное количество позиций)
        :param offset: Offset of positions (Отступ в выдаваемом списке позиций)
        """
        self.supply_id = supply_id
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
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(position) for position in result["rows"]]


class CreateSupplyPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-sozdat-poziciu-priemki

    Create supply position
    Создать позицию приемки
    """

    def __init__(
        self,
        supply_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, int] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        tracking_codes: typing.Union[Unset, typing.List[dict]] = Unset,
        overhead: typing.Union[Unset, float] = Unset,
    ):
        """
        Create supply position
        Создать позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param assortment: Assortment (Информация о товаре)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param discount: Discount (Скидка)
        :param vat: VAT (НДС)
        :param tracking_codes: Tracking codes (Коды отслеживания)
        :param overhead: Overhead (Накладные расходы)
        """
        self.supply_id = supply_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.vat = vat
        self.tracking_codes = tracking_codes
        self.overhead = overhead

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.price != Unset:
            json_data["price"] = self.price
        if self.discount != Unset:
            json_data["discount"] = self.discount
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.tracking_codes != Unset:
            json_data["trackingCodes"] = self.tracking_codes
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        return RequestData(
            method="POST",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class GetSupplyPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-poluchit-poziciu

    Get supply position
    Получить позицию приемки

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Приемки.
    positionID 	string (required) Example: 34f6344f-015e-11e6-9464-e4de0000006c id позиции Приемки.
    """

    def __init__(
        self,
        supply_id: str,
        position_id: str,
    ):
        """
        Get supply position
        Получить позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param position_id: ID of position (ID позиции приемки)
        """
        self.supply_id = supply_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class UpdateSupplyPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-izmenit-poziciu

    Update supply position
    Изменить позицию приемки
    """

    def __init__(
        self,
        supply_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, int] = Unset,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, int] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        tracking_codes: typing.Union[Unset, typing.List[dict]] = Unset,
        overhead: typing.Union[Unset, float] = Unset,
    ):
        """
        Update supply position
        Изменить позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param position_id: ID of position (ID позиции приемки)
        :param assortment: Assortment (Информация о товаре)
        :param quantity: Quantity (Количество)
        :param price: Price (Цена)
        :param discount: Discount (Скидка)
        :param vat: VAT (НДС)
        :param tracking_codes: Tracking codes (Коды отслеживания)
        :param overhead: Overhead (Накладные расходы)
        """
        self.supply_id = supply_id
        self.position_id = position_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.vat = vat
        self.tracking_codes = tracking_codes
        self.overhead = overhead

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = (
                {"meta": self.assortment}
                if self.assortment is not None
                else None
                if self.assortment is not None
                else None
            )
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.price != Unset:
            json_data["price"] = self.price
        if self.discount != Unset:
            json_data["discount"] = self.discount
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.tracking_codes != Unset:
            json_data["trackingCodes"] = self.tracking_codes
        if self.overhead != Unset:
            json_data["overhead"] = self.overhead
        return RequestData(
            method="PUT",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeleteSupplyPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-priemka-udalit-poziciu

    Delete supply position
    Удалить позицию приемки

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Приемки.
    positionID 	string (required) Example: 34f6344f-015e-11e6-9464-e4de0000006c id позиции Приемки.
    """

    def __init__(
        self,
        supply_id: str,
        position_id: str,
    ):
        """
        Delete supply position
        Удалить позицию приемки

        :param supply_id: ID of supply (ID приемки)
        :param position_id: ID of position (ID позиции приемки)
        """
        self.supply_id = supply_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"https://api.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

import datetime
import typing

from .... import types, helpers


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
        self.incoming_date: datetime.datetime = None
        self.incoming_number: typing.Optional[str] = None
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
        self.rate: typing.Optional[dict] = None
        self.shared: bool = None
        self.state: types.Meta = None
        self.store: types.Meta = None
        self.sum: int = None
        self.sync_id: typing.Optional[str] = None
        self.updated: datetime.datetime = None
        self.vat_enabled: bool = None
        self.vat_included: typing.Optional[bool] = None
        self.vat_sum: float = None
        self.invoices_in: typing.List[types.Meta] = None
        self.facture_in: typing.Optional[types.Meta] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Supply":
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
        files = dict_data.get("files")
        if files is not None:
            instance.files = files["meta"]
        group = dict_data.get("group")
        if group is not None:
            instance.group = group["meta"]
        instance.id = dict_data.get("id")
        incoming_date = dict_data.get("incomingDate")
        if incoming_date is not None:
            instance.incoming_date = datetime.datetime.fromisoformat(incoming_date)
        instance.incoming_number = dict_data.get("incomingNumber")
        instance.meta = dict_data.get("meta")
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
        instance.shared = dict_data.get("shared")
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
        instance.invoices_in = [
            helpers.get_meta(x, must=True) for x in dict_data.get("invoicesIn", [])
        ]
        instance.facture_in = helpers.get_meta(dict_data.get("factureIn", None))
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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ):
        """

        :param limit: Limit of entities to extract (Лимит сущностей для извлечения)
        :param offset: Offset in the list of entities (Отступ в выдаваемом списке сущностей)
        :param search: Filter documents by the specified search string (Фильтр документов по указанной поисковой строке)
        """
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.search is not None:
            params["search"] = self.search
        return {
            "method": "GET",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/supply",
            "params": params,
        }

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
        agent_account: typing.Optional[types.Meta] = None,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        contract: typing.Optional[types.Meta] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        incoming_date: typing.Optional[datetime.datetime] = None,
        incoming_number: typing.Optional[str] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        organization_account: typing.Optional[types.Meta] = None,
        overhead: typing.Optional[dict] = None,
        owner: typing.Optional[types.Meta] = None,
        positions: typing.Optional[typing.List[CreatePosition]] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[dict] = None,
        shared: typing.Optional[bool] = None,
        state: typing.Optional[types.Meta] = None,
        sync_id: typing.Optional[str] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
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

    def to_request(self) -> dict:
        json_data = {
            "organization": {"meta": self.organization},
            "agent": {"meta": self.agent},
            "store": {"meta": self.store},
        }
        if self.agent_account is not None:
            json_data["agentAccount"] = {"meta": self.agent_account}
        if self.applicable is not None:
            json_data["applicable"] = self.applicable
        if self.attributes is not None:
            json_data["attributes"] = self.attributes
        if self.code is not None:
            json_data["code"] = self.code
        if self.contract is not None:
            json_data["contract"] = {"meta": self.contract}
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.files is not None:
            json_data["files"] = self.files
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.incoming_date is not None:
            json_data["incomingDate"] = self.incoming_date.strftime("%Y-%m-%d %H:%M:%S")
        if self.incoming_number is not None:
            json_data["incomingNumber"] = self.incoming_number
        if self.moment is not None:
            json_data["moment"] = self.moment.strftime("%Y-%m-%d %H:%M:%S")
        if self.name is not None:
            json_data["name"] = self.name
        if self.organization_account is not None:
            json_data["organizationAccount"] = {"meta": self.organization_account}
        if self.overhead is not None:
            json_data["overhead"] = self.overhead
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.positions is not None:
            json_data["positions"] = []
            for position in self.positions:
                new_position: dict = position.copy()
                new_position["assortment"] = {"meta": new_position["assortment"]}
                json_data["positions"].append(new_position)
        if self.project is not None:
            json_data["project"] = {"meta": self.project}
        if self.rate is not None:
            json_data["rate"] = self.rate
        if self.shared is not None:
            json_data["shared"] = self.shared
        if self.state is not None:
            json_data["state"] = {"meta": self.state}
        if self.sync_id is not None:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled is not None:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included is not None:
            json_data["vatIncluded"] = self.vat_included
        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/supply",
            "json": json_data,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}",
            "allow_non_json": True,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}",
        }

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
        organization: typing.Optional[types.Meta] = None,
        agent: typing.Optional[types.Meta] = None,
        store: typing.Optional[types.Meta] = None,
        agent_account: typing.Optional[types.Meta] = None,
        applicable: typing.Optional[bool] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        contract: typing.Optional[types.Meta] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        files: typing.Optional[types.MetaArray] = None,
        group: typing.Optional[types.Meta] = None,
        incoming_date: typing.Optional[datetime.datetime] = None,
        incoming_number: typing.Optional[str] = None,
        moment: typing.Optional[datetime.datetime] = None,
        name: typing.Optional[str] = None,
        organization_account: typing.Optional[types.Meta] = None,
        overhead: typing.Optional[dict] = None,
        owner: typing.Optional[types.Meta] = None,
        positions: typing.Optional[typing.List[UpdatePosition]] = None,
        project: typing.Optional[types.Meta] = None,
        rate: typing.Optional[dict] = None,
        shared: typing.Optional[bool] = None,
        state: typing.Optional[types.Meta] = None,
        sync_id: typing.Optional[str] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
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

    def to_request(self) -> dict:
        json_data = {}
        if self.organization is not None:
            json_data["organization"] = {"meta": self.organization}
        if self.agent is not None:
            json_data["agent"] = {"meta": self.agent}
        if self.store is not None:
            json_data["store"] = {"meta": self.store}
        if self.agent_account is not None:
            json_data["agentAccount"] = {"meta": self.agent_account}
        if self.applicable is not None:
            json_data["applicable"] = self.applicable
        if self.attributes is not None:
            json_data["attributes"] = self.attributes
        if self.code is not None:
            json_data["code"] = self.code
        if self.contract is not None:
            json_data["contract"] = {"meta": self.contract}
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.files is not None:
            json_data["files"] = self.files
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.incoming_date is not None:
            json_data["incomingDate"] = self.incoming_date.strftime("%Y-%m-%d %H:%M:%S")
        if self.incoming_number is not None:
            json_data["incomingNumber"] = self.incoming_number
        if self.moment is not None:
            json_data["moment"] = self.moment.strftime("%Y-%m-%d %H:%M:%S")
        if self.name is not None:
            json_data["name"] = self.name
        if self.organization_account is not None:
            json_data["organizationAccount"] = {"meta": self.organization_account}
        if self.overhead is not None:
            json_data["overhead"] = self.overhead
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.positions is not None:
            json_data["positions"] = []
            for position in self.positions:
                new_position: dict = position.copy()
                new_position["assortment"] = {"meta": new_position["assortment"]}
                json_data["positions"].append(new_position)
        if self.project is not None:
            json_data["project"] = {"meta": self.project}
        if self.rate is not None:
            json_data["rate"] = self.rate
        if self.shared is not None:
            json_data["shared"] = self.shared
        if self.state is not None:
            json_data["state"] = {"meta": self.state}
        if self.sync_id is not None:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled is not None:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included is not None:
            json_data["vatIncluded"] = self.vat_included

        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}",
            "json": json_data,
        }

    def from_response(self, result: dict) -> Supply:
        return Supply.from_json(result)


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

    def __init__(self):
        self.account_id: str = None
        self.assortment: types.Meta = None
        self.country: typing.Optional[types.Meta] = None
        self.discount: int = None
        self.gtd: typing.Optional[dict] = None
        self.id: str = None
        self.pack: typing.Optional[dict] = None
        self.price: float = None
        self.quantity: float = None
        self.slot: typing.Optional[int] = None
        self.things: typing.Optional[typing.List[str]] = None
        self.overhead: int
        self.vat: bool = None
        self.vat_enabled: bool = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        assortment = dict_data.get("assortment")
        if assortment is not None:
            instance.assortment = assortment["meta"]
        country = dict_data.get("country")
        if country is not None:
            instance.country = country["meta"]
        instance.discount = dict_data.get("discount")
        instance.gtd = dict_data.get("gtd")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        slot = dict_data.get("slot")
        if slot is not None:
            instance.slot = slot["meta"]
        instance.things = dict_data.get("things")
        instance.overhead = dict_data.get("overhead")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance


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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
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

    def to_request(self) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions",
            "params": params,
        }

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
        price: typing.Optional[float] = None,
        discount: typing.Optional[int] = None,
        vat: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[dict]] = None,
        overhead: typing.Optional[float] = None,
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

    def to_request(self) -> dict:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.price is not None:
            json_data["price"] = self.price
        if self.discount is not None:
            json_data["discount"] = self.discount
        if self.vat is not None:
            json_data["vat"] = self.vat
        if self.tracking_codes is not None:
            json_data["trackingCodes"] = self.tracking_codes
        if self.overhead is not None:
            json_data["overhead"] = self.overhead
        return {
            "method": "POST",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions",
            "json": json_data,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions/{self.position_id}",
        }

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
        assortment: typing.Optional[types.Meta] = None,
        quantity: typing.Optional[int] = None,
        price: typing.Optional[float] = None,
        discount: typing.Optional[int] = None,
        vat: typing.Optional[int] = None,
        tracking_codes: typing.Optional[typing.List[dict]] = None,
        overhead: typing.Optional[float] = None,
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

    def to_request(self) -> dict:
        json_data = {}
        if self.assortment is not None:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity is not None:
            json_data["quantity"] = self.quantity
        if self.price is not None:
            json_data["price"] = self.price
        if self.discount is not None:
            json_data["discount"] = self.discount
        if self.vat is not None:
            json_data["vat"] = self.vat
        if self.tracking_codes is not None:
            json_data["trackingCodes"] = self.tracking_codes
        if self.overhead is not None:
            json_data["overhead"] = self.overhead
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions/{self.position_id}",
            "json": json_data,
        }

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

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/supply/{self.supply_id}/positions/{self.position_id}",
            "allow_non_json": True,
        }

    def from_response(self, result: dict) -> None:
        return None

import typing
import datetime
from .... import types
from .... import helpers
from ....types import Unset


class InvoiceIn(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-scheta-postawschikow

    Атрибуты сущности
    Название 	            Тип 	 	Описание
    accountId 	            UUID 	 	ID учетной записи Обязательное при ответе Только для чтения Change-handler
    agent 	                Meta 	 	Метаданные контрагента Обязательное при ответе Expand Необходимо при создании Change-handler
    agentAccount 	        Meta 		Метаданные счета контрагента Expand Change-handler
    applicable 	            Boolean 	 	Отметка о проведении Обязательное при ответе Change-handler
    attributes 	            Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта Change-handler
    code 	                String(255) 	  	Код Счета поставщика
    contract 	            Meta 	 	Метаданные договора Expand Change-handler
    created 	            DateTime 	  	Дата создания Обязательное при ответе Только для чтения Change-handler
    deleted 	            DateTime 	  	Момент последнего удаления Счета поставщика Только для чтения
    description 	        String(4096) 	  	Комментарий Счета поставщика Change-handler
    externalCode 	        String(255) 	  	Внешний код Счета поставщика Обязательное при ответе Change-handler
    files 	                MetaArray 		Метаданные массива Файлов (Максимальное количество файлов - 100) Обязательное при ответе Expand
    group 	                Meta 	 	Отдел сотрудника Обязательное при ответе Expand
    id 	                    UUID 	 	ID Счета поставщика Обязательное при ответе Только для чтения Change-handler
    incomingDate 	        DateTime 	  	Входящая дата Change-handler
    incomingNumber 	        Float 	  	Входящий номер Change-handler
    meta 	                Meta 		Метаданные Счета поставщика Обязательное при ответе Change-handler
    moment 	                DateTime 	  	Дата документа Обязательное при ответе Change-handler
    name 	                String(255) 	  	Наименование Счета поставщика Обязательное при ответе Change-handler
    organization 	        Meta 	 	Метаданные юрлица Обязательное при ответе Expand Необходимо при создании Change-handler
    organizationAccount 	Meta 		Метаданные счета юрлица Expand Change-handler
    owner 	                Meta 	 	Владелец (Сотрудник) Обязательное при ответе Expand
    payedSum 	            Float 		Сумма входящих платежей по Счету поставщика Обязательное при ответе Только для чтения Change-handler
    paymentPlannedMoment 	DateTime 	  	Планируемая дата оплаты Change-handler
    positions 	            MetaArray 		Метаданные позиций Счета поставщика Обязательное при ответе Expand Change-handler
    printed 	            Boolean 	 	Напечатан ли документ Обязательное при ответе Только для чтения
    project 	            Meta 	 	Метаданные проекта Expand Change-handler
    published 	            Boolean 	 	Опубликован ли документ Обязательное при ответе Только для чтения
    rate 	                Object 		Валюта. Подробнее тут Обязательное при ответе Change-handler
    shared 	                Boolean 	 	Общий доступ Обязательное при ответе
    shippedSum 	            Float 		Сумма отгруженного Обязательное при ответе Только для чтения Change-handler
    state 	                Meta 	 	Метаданные статуса счета Expand Change-handler
    store 	                Meta 		Метаданные склада Expand Change-handler
    sum 	                Int 	  	Сумма Счета в установленной валюте Обязательное при ответе Только для чтения Change-handler
    syncId 	                UUID 	 	ID синхронизации. После заполнения недоступен для изменения
    updated 	            DateTime 	  	Момент последнего обновления Счета поставщика Обязательное при ответе Только для чтения Change-handler
    vatEnabled 	            Boolean 		Учитывается ли НДС Обязательное при ответе Change-handler
    vatIncluded 	        Boolean 		Включен ли НДС в цену Change-handler
    vatSum 	                Float 		Сумма НДС Обязательное при ответе Только для чтения Change-handler
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
        self.files: typing.Optional[types.MetaArray] = None
        self.group: types.Meta = None
        self.id: str = None
        self.incoming_date: typing.Optional[datetime.datetime] = None
        self.incoming_number: typing.Optional[float] = None
        self.meta: types.Meta = None
        self.moment: datetime.datetime = None
        self.name: str = None
        self.organization: types.Meta = None
        self.organization_account: typing.Optional[types.Meta] = None
        self.owner: types.Meta = None
        self.payed_sum: float = None
        self.payment_planned_moment: typing.Optional[datetime.datetime] = None
        self.positions: types.MetaArray = None
        self.printed: bool = None
        self.project: typing.Optional[types.Meta] = None
        self.published: bool = None
        self.rate: dict = None
        self.shared: bool = None
        self.shipped_sum: float = None
        self.state: typing.Optional[types.Meta] = None
        self.store: typing.Optional[types.Meta] = None
        self.sum: int = None
        self.sync_id: typing.Optional[str] = None
        self.updated: datetime.datetime = None
        self.vat_enabled: bool = None
        self.vat_included: typing.Optional[bool] = None
        self.vat_sum: float = None
        self.supplies: typing.List[types.Meta] = None
        self.purchase_order: typing.Optional[types.Meta] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "InvoiceIn":
        instance = cls()
        instance.account_id = dict_data.get("accountId", None)
        instance.agent = helpers.get_meta(dict_data.get("agent", None))
        instance.agent_account = helpers.get_meta(dict_data.get("agentAccount", None))
        instance.applicable = dict_data.get("applicable", False)
        instance.attributes = dict_data.get("attributes", [])
        instance.code = dict_data.get("code", None)
        instance.contract = helpers.get_meta(dict_data.get("contract", None))
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description", None)
        instance.external_code = dict_data.get("externalCode", None)
        instance.files = dict_data.get("files", [])
        instance.group = helpers.get_meta(dict_data.get("group", None))
        instance.id = dict_data.get("id", None)
        instance.incoming_date = helpers.parse_date(dict_data.get("incomingDate"))
        instance.incoming_number = dict_data.get("incomingNumber", None)
        instance.meta = dict_data.get("meta", None)
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name", None)
        instance.organization = helpers.get_meta(dict_data.get("organization", None))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount", None)
        )
        instance.owner = helpers.get_meta(dict_data.get("owner", None))
        instance.payed_sum = dict_data.get("payedSum", None)
        instance.payment_planned_moment = helpers.parse_date(
            dict_data.get("paymentPlannedMoment")
        )
        instance.positions = dict_data.get("positions", [])
        instance.printed = dict_data.get("printed", False)
        instance.project = helpers.get_meta(dict_data.get("project", None))
        instance.published = dict_data.get("published", False)
        instance.rate = dict_data.get("rate", None)
        instance.shared = dict_data.get("shared", False)
        instance.shipped_sum = dict_data.get("shippedSum", None)
        instance.state = helpers.get_meta(dict_data.get("state", None))
        instance.store = helpers.get_meta(dict_data.get("store", None))
        instance.sum = dict_data.get("sum", None)
        instance.sync_id = dict_data.get("syncId", None)
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled", False)
        instance.vat_included = dict_data.get("vatIncluded", False)
        instance.vat_sum = dict_data.get("vatSum", None)
        instance.supplies = [
            helpers.get_meta(x, must=True) for x in dict_data.get("supplies", [])
        ]
        instance.purchase_order = helpers.get_meta(dict_data.get("purchaseOrder", None))
        return instance


class GetInvoicesInRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-poluchit-scheta-postawschikow

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
        search: typing.Optional[str] = None,
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
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.search is not None:
            params["search"] = self.search
        return {
            "method": "GET",
            "url": "https://api.moysklad.ru/api/remap/1.2/entity/invoicein",
            "params": params,
        }

    def from_response(self, result: dict) -> typing.List[InvoiceIn]:
        return [InvoiceIn.from_json(obj_json) for obj_json in result["rows"]]


class GetInvoiceInRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-poluchit-schet-postawschika-po-id

    Параметры
    Параметр 	Описание
    id 	string (required) Example: 3b7e6a5d-9e2c-11e7-7a34-8f550003f9a9 ID Счета поставщика
    """

    def __init__(self, invoice_id: str):
        """

        :param invoice_id: Invoice ID (ID Счета поставщика)
        """
        self.uuid = invoice_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/{self.uuid}",
        }

    def from_response(self, response: dict) -> InvoiceIn:
        return InvoiceIn.from_json(response)


class CreateInvoiceInRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-sozdat-schet-postawschika
    Обязательные поля
    name 	        номер Счета поставщика
    organization 	Ссылка на ваше юрлицо в формате Метаданных
    agent 	        Ссылка на контрагента (поставщика) в формате Метаданных

    Дополнительные поля
    Название 	            Тип 	 	    Описание
    agentAccount 	        Meta 		    Метаданные счета контрагента Expand Change-handler
    applicable 	            Boolean 	 	Отметка о проведении Обязательное при ответе Change-handler
    attributes 	            Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта Change-handler
    code 	                String(255) 	Код Счета поставщика
    contract 	            Meta 	 	    Метаданные договора Expand Change-handler
    description 	        String(4096) 	Комментарий Счета поставщика Change-handler
    externalCode 	        String(255) 	Внешний код Счета поставщика Обязательное при ответе Change-handler
    files 	                MetaArray 		Метаданные массива Файлов (Максимальное количество файлов - 100) Обязательное при ответе Expand
    group 	                Meta 	 	    Отдел сотрудника Обязательное при ответе Expand
    incomingDate 	        DateTime 	  	Входящая дата Change-handler
    incomingNumber 	        Float 	  	    Входящий номер Change-handler
    meta 	                Meta 		    Метаданные Счета поставщика Обязательное при ответе Change-handler
    moment 	                DateTime 	  	Дата документа Обязательное при ответе Change-handler
    organizationAccount 	Meta 		    Метаданные счета юрлица Expand Change-handler
    owner 	                Meta 	 	    Владелец (Сотрудник) Обязательное при ответе Expand
    payedSum 	            Float 		    Сумма входящих платежей по Счету поставщика Обязательное при ответе Только для чтения Change-handler
    paymentPlannedMoment 	DateTime 	  	Планируемая дата оплаты Change-handler
    positions 	            MetaArray 		Метаданные позиций Счета поставщика Обязательное при ответе Expand Change-handler
    project 	            Meta 	 	    Метаданные проекта Expand Change-handler
    rate 	                Object 		    Валюта. Подробнее тут Обязательное при ответе Change-handler
    shared 	                Boolean 	    Общий доступ Обязательное при ответе
    state 	                Meta 	 	    Метаданные статуса счета Expand Change-handler
    store 	                Meta 		    Метаданные склада Expand Change-handler
    syncId 	                UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    updated 	            DateTime 	  	Момент последнего обновления Счета поставщика Обязательное при ответе Только для чтения Change-handler
    vatEnabled 	            Boolean 		Учитывается ли НДС Обязательное при ответе Change-handler
    vatIncluded 	        Boolean 		Включен ли НДС в цену Change-handler
    """

    class CreateInvoiceInPosition(typing.TypedDict):
        """
        Позиции Оприходования - это список товаров/модификаций/серий. Объект позиции Оприходования содержит следующие поля:
        Название 	Тип 	        Описание
        assortment 	Meta 	        Метаданные товара/услуги/серии/модификации, которую представляет собой позиция     Обязательное при ответе Expand Change-handler Update-provider
        price 	    Float 	        Цена товара/услуги в копейках     Обязательное при ответе Change-handler Update-provider
        quantity 	Int 	        Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе.     Обязательное при ответе Change-handler Update-provider
        discount 	        Int 	        Процент скидки или наценки. Наценка указывается отрицательным числом, т.е. -10 создаст наценку в 10% Обязательное при ответе Change-handler Update-provider
        vat 	            Float 	        НДС в процентах. Обязательное при ответе Change-handler Update-provider
        """

        assortment: types.Meta
        price: typing.Optional[float]
        quantity: float
        discount: typing.Optional[float]
        vat: typing.Optional[float]

    def __init__(
        self,
        name: str,
        organization: types.Meta,
        agent: types.Meta,
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
        incoming_number: typing.Union[Unset, float] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payed_sum: typing.Union[Unset, float] = Unset,
        payment_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        positions: typing.Union[Unset, typing.List[CreateInvoiceInPosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        """
        Создание счета поставщика

        :param name: Invoice number (Номер счета)
        :param organization: Link to your organization in Metadata format (Ссылка на ваше юрлицо в формате Метаданных
        :param agent: Link to the counterparty (supplier) in Metadata format (Ссылка на контрагента (поставщика) в формате Метаданных)
        :param agent_account: Link to the counterparty's account in Metadata format (Ссылка на счет контрагента в формате Метаданных)
        :param applicable: Marking for the document (Отметка о проведении)
        :param attributes: Additional fields operators (Операторы доп. полей)
        :param code: Invoice code (Код счета)
        :param contract: Link to the contract in Metadata format (Ссылка на договор в формате Метаданных)
        :param description: Invoice comment (Комментарий счета)
        :param external_code: Invoice external code (Внешний код счета)
        :param files: File array metadata (Метаданные массива Файлов)
        :param group: Department of the employee (Отдел сотрудника)
        :param incoming_date: Incoming date (Входящая дата)
        :param incoming_number: Incoming number (Входящий номер)
        :param moment: Document date (Дата документа)
        :param organization_account: Link to the organization's account in Metadata format (Ссылка на счет юрлица в формате Метаданных)
        :param owner: Owner (Employee) (Владелец (Сотрудник))
        :param payed_sum: Amount of incoming payments on the invoice (Сумма входящих платежей по счету)
        :param payment_planned_moment: Planned payment date (Планируемая дата оплаты)
        :param positions: Invoice positions (Позиции счета)
        :param project: Link to the project in Metadata format (Ссылка на проект в формате Метаданных)
        :param rate: Currency (Валюта)
        :param shared: Common Access (Общий доступ)
        :param state: Link to the status of the account in Metadata format (Ссылка на статус счета в формате Метаданных)
        :param store: Link to the warehouse in Metadata format (Ссылка на склад в формате Метаданных)
        :param vat_enabled: Is VAT taken into account (Учитывается ли НДС)
        :param vat_included: Is VAT included in the price (Включен ли НДС в цену)
        """
        self.name = name
        self.organization = organization
        self.agent = agent

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
        self.organization_account = organization_account
        self.owner = owner
        self.payed_sum = payed_sum
        self.payment_planned_moment = payment_planned_moment
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.store = store
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> dict:
        json_data = {
            "name": self.name,
            "organization": {"meta": self.organization},
            "agent": {"meta": self.agent},
        }
        if self.agent_account != Unset:
            json_data["agentAccount"] = (
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
        if self.incoming_date != Unset:
            json_data["incomingDate"] = self.incoming_date.strftime("%Y-%m-%d %H:%M:%S")
        if self.incoming_number != Unset:
            json_data["incomingNumber"] = self.incoming_number
        if self.moment != Unset:
            json_data["moment"] = self.moment.strftime("%Y-%m-%d %H:%M:%S")
        if self.organization_account != Unset:
            json_data["organizationAccount"] = (
                {"meta": self.organization_account}
                if self.organization_account is not None
                else None
            )
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.payed_sum != Unset:
            json_data["payedSum"] = self.payed_sum
        if self.payment_planned_moment != Unset:
            json_data["paymentPlannedMoment"] = self.payment_planned_moment.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                pos = {}
                assortment = position.get("assortment")
                if assortment is not None:
                    pos["assortment"] = {"meta": assortment}
                else:
                    raise ValueError("Assortment is required for position")
                price = position.get("price")
                if price is not None:
                    pos["price"] = price
                quantity = position.get("quantity")
                if quantity is not None:
                    pos["quantity"] = quantity
                else:
                    raise ValueError("Quantity is required for position")
                if "discount" in position:
                    pos["discount"] = position["discount"]
                if "vat" in position:
                    pos["vat"] = position["vat"]
                json_data["positions"].append(pos)
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
        if self.store != Unset:
            json_data["store"] = (
                {"meta": self.store} if self.store is not None else None
            )
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included
        return {
            "method": "POST",
            "url": "https://api.moysklad.ru/api/remap/1.2/entity/invoicein",
            "json": json_data,
        }

    def from_response(self, response: dict) -> InvoiceIn:
        return InvoiceIn.from_json(response)


class InvoiceInPosition(types.MoySkladBaseClass):
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-poziciq-scheta-postawschika
    def __init__(self):
        self.meta: typing.Union[Unset, types.Meta] = Unset
        self.id: typing.Union[Unset, str] = Unset
        self.account_id: typing.Union[Unset, str] = Unset
        self.quantity: typing.Union[Unset, float] = Unset
        self.price: typing.Union[Unset, float] = Unset
        self.discount: typing.Union[Unset, float] = Unset
        self.vat: typing.Union[Unset, float] = Unset
        self.vat_enabled: typing.Union[Unset, bool] = Unset
        self.assortment: typing.Union[Unset, types.Meta] = Unset

    @classmethod
    def from_json(cls, data: dict) -> "InvoiceInPosition":
        position = cls()
        position.meta = data.get("meta")
        position.id = data.get("id")
        position.account_id = data.get("accountId")
        position.quantity = data.get("quantity")
        position.price = data.get("price")
        position.discount = data.get("discount")
        position.vat = data.get("vat")
        position.vat_enabled = data.get("vatEnabled")
        position.assortment = helpers.get_meta(data.get("assortment"))
        return position


class DeleteInvoiceInRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-udalit-schet-postawschika
    """

    def __init__(self, invoice_id: str):
        self.uuid = invoice_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/{self.uuid}",
            "allow_non_json": True,
        }

    def from_response(self, response):
        return None


class UpdateInvoiceInRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-izmenit-schet-postawschika

    name 	        номер Счета поставщика
    organization 	Ссылка на ваше юрлицо в формате Метаданных
    agent 	        Ссылка на контрагента (поставщика) в формате Метаданных

    Название 	            Тип 	 	    Описание
    agentAccount 	        Meta 		    Метаданные счета контрагента Expand Change-handler
    applicable 	            Boolean 	 	Отметка о проведении Обязательное при ответе Change-handler
    attributes 	            Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта Change-handler
    code 	                String(255) 	Код Счета поставщика
    contract 	            Meta 	 	    Метаданные договора Expand Change-handler
    description 	        String(4096) 	Комментарий Счета поставщика Change-handler
    externalCode 	        String(255) 	Внешний код Счета поставщика Обязательное при ответе Change-handler
    files 	                MetaArray 		Метаданные массива Файлов (Максимальное количество файлов - 100) Обязательное при ответе Expand
    group 	                Meta 	 	    Отдел сотрудника Обязательное при ответе Expand
    incomingDate 	        DateTime 	  	Входящая дата Change-handler
    incomingNumber 	        Float 	  	    Входящий номер Change-handler
    meta 	                Meta 		    Метаданные Счета поставщика Обязательное при ответе Change-handler
    moment 	                DateTime 	  	Дата документа Обязательное при ответе Change-handler
    organizationAccount 	Meta 		    Метаданные счета юрлица Expand Change-handler
    owner 	                Meta 	 	    Владелец (Сотрудник) Обязательное при ответе Expand
    payedSum 	            Float 		    Сумма входящих платежей по Счету поставщика Обязательное при ответе Только для чтения Change-handler
    paymentPlannedMoment 	DateTime 	  	Планируемая дата оплаты Change-handler
    positions 	            MetaArray 		Метаданные позиций Счета поставщика Обязательное при ответе Expand Change-handler
    project 	            Meta 	 	    Метаданные проекта Expand Change-handler
    rate 	                Object 		    Валюта. Подробнее тут Обязательное при ответе Change-handler
    shared 	                Boolean 	    Общий доступ Обязательное при ответе
    state 	                Meta 	 	    Метаданные статуса счета Expand Change-handler
    store 	                Meta 		    Метаданные склада Expand Change-handler
    syncId 	                UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    updated 	            DateTime 	  	Момент последнего обновления Счета поставщика Обязательное при ответе Только для чтения Change-handler
    vatEnabled 	            Boolean 		Учитывается ли НДС Обязательное при ответе Change-handler
    vatIncluded 	        Boolean 		Включен ли НДС в цену Change-handler
    """

    UpdateInvoiceInPosition = CreateInvoiceInRequest.CreateInvoiceInPosition

    def __init__(
        self,
        invoice_in_id: str,
        name: typing.Union[Unset, str] = Unset,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
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
        incoming_number: typing.Union[Unset, float] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        payed_sum: typing.Union[Unset, float] = Unset,
        payment_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        positions: typing.Union[Unset, typing.List[UpdateInvoiceInPosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        """
        Изменение счета поставщика

        :param name: Invoice number (Номер счета)
        :param organization: Link to your organization in Metadata format (Ссылка на ваше юрлицо в формате Метаданных
        :param agent: Link to the counterparty (supplier) in Metadata format (Ссылка на контрагента (поставщика) в формате Метаданных)
        :param agent_account: Link to the counterparty's account in Metadata format (Ссылка на счет контрагента в формате Метаданных)
        :param applicable: Marking for the document (Отметка о проведении)
        :param attributes: Additional fields operators (Операторы доп. полей)
        :param code: Invoice code (Код счета)
        :param contract: Link to the contract in Metadata format (Ссылка на договор в формате Метаданных)
        :param description: Invoice comment (Комментарий счета)
        :param external_code: Invoice external code (Внешний код счета)
        :param files: File array metadata (Метаданные массива Файлов)
        :param group: Department of the employee (Отдел сотрудника)
        :param incoming_date: Incoming date (Входящая дата)
        :param incoming_number: Incoming number (Входящий номер)
        :param moment: Document date (Дата документа)
        :param organization_account: Link to the organization's account in Metadata format (Ссылка на счет юрлица в формате Метаданных)
        :param owner: Owner (Employee) (Владелец (Сотрудник))
        :param payed_sum: Amount of incoming payments on the invoice (Сумма входящих платежей по счету)
        :param payment_planned_moment: Planned payment date (Планируемая дата оплаты)
        :param positions: Invoice positions (Позиции счета)
        :param project: Link to the project in Metadata format (Ссылка на проект в формате Метаданных)
        :param rate: Currency (Валюта)
        :param shared: Common Access (Общий доступ)
        :param state: Link to the status of the account in Metadata format (Ссылка на статус счета в формате Метаданных)
        :param store: Link to the warehouse in Metadata format (Ссылка на склад в формате Метаданных)
        :param vat_enabled: Is VAT taken into account (Учитывается ли НДС)
        :param vat_included: Is VAT included in the price (Включен ли НДС в цену)
        """
        self.invoice_in_id = invoice_in_id

        self.name = name
        self.organization = organization
        self.agent = agent
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
        self.organization_account = organization_account
        self.owner = owner
        self.payed_sum = payed_sum
        self.payment_planned_moment = payment_planned_moment
        self.positions = positions
        self.project = project
        self.rate = rate
        self.shared = shared
        self.state = state
        self.store = store
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> dict:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.organization != Unset:
            json_data["organization"] = (
                {"meta": self.organization} if self.organization is not None else None
            )
        if self.agent != Unset:
            json_data["agent"] = (
                {"meta": self.agent} if self.agent is not None else None
            )
        if self.agent_account != Unset:
            json_data["agentAccount"] = (
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
        if self.incoming_date != Unset:
            json_data["incomingDate"] = self.incoming_date.strftime("%Y-%m-%d %H:%M:%S")
        if self.incoming_number != Unset:
            json_data["incomingNumber"] = self.incoming_number
        if self.moment != Unset:
            json_data["moment"] = self.moment.strftime("%Y-%m-%d %H:%M:%S")
        if self.organization_account != Unset:
            json_data["organizationAccount"] = (
                {"meta": self.organization_account}
                if self.organization_account is not None
                else None
            )
        if self.owner != Unset:
            json_data["owner"] = (
                {"meta": self.owner} if self.owner is not None else None
            )
        if self.payed_sum != Unset:
            json_data["payedSum"] = self.payed_sum
        if self.payment_planned_moment != Unset:
            json_data["paymentPlannedMoment"] = self.payment_planned_moment.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        if self.positions != Unset:
            json_data["positions"] = []
            for position in self.positions:
                pos = {}
                assortment = position.get("assortment")
                if assortment is not None:
                    pos["assortment"] = {"meta": assortment}
                else:
                    raise ValueError("Assortment is required for position")
                price = position.get("price")
                if price is not None:
                    pos["price"] = price
                quantity = position.get("quantity")
                if quantity is not None:
                    pos["quantity"] = quantity
                else:
                    raise ValueError("Quantity is required for position")
                if "discount" in position:
                    pos["discount"] = position["discount"]
                if "vat" in position:
                    pos["vat"] = position["vat"]
                json_data["positions"].append(pos)
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
        if self.store != Unset:
            json_data["store"] = (
                {"meta": self.store} if self.store is not None else None
            )
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included

        if len(json_data) == 0:
            raise ValueError("No data to update")
        return {
            "method": "PUT",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/{self.invoice_in_id}",
            "json": json_data,
        }

    def from_response(self, response: dict) -> InvoiceIn:
        return InvoiceIn.from_json(response)


class GetInvoiceInPositionRequest(types.ApiRequest):
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-poluchit-poziciu
    def __init__(self, invoice_in_id: str, position_id: str):
        """
        Получить позицию счета поставщика по id

        :param invoice_in_id: ID счета поставщика
        :param position_id: ID позиции счета поставщика
        """
        self.invoice_in_id = invoice_in_id
        self.position_id = position_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/"
            f"{self.invoice_in_id}/positions/{self.position_id}",
        }

    def from_response(self, response: dict) -> InvoiceInPosition:
        return InvoiceInPosition.from_json(response)


class GetInvoiceInPositionsRequest(types.ApiRequest):
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-poluchit-pozicii-scheta-postawschika
    def __init__(self, invoice_in_id: str, limit: int = 1000, offset: int = 0):
        """
        Получить позиции счета поставщика

        :param invoice_in_id: ID счета поставщика
        :param limit: Количество элементов в списке
        :param offset: Смещение списка

        """
        self.invoice_in_id = invoice_in_id
        self.limit = limit
        self.offset = offset

    def to_request(self) -> dict:
        params = {"limit": self.limit, "offset": self.offset}
        return {
            "method": "GET",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/"
            f"{self.invoice_in_id}/positions",
            "params": params,
        }

    def from_response(self, response: dict) -> typing.List[InvoiceInPosition]:
        return [InvoiceInPosition.from_json(item) for item in response.get("rows", [])]


class CreateInvoiceInPositionRequest(types.ApiRequest):
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-sozdat-poziciu
    def __init__(
        self,
        invoice_in_id: str,
        quantity: float,
        assortment: types.Meta,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
    ):
        """
        Добавить позицию счета поставщика

        :param invoice_in_id: ID счета поставщика
        :param quantity: Количество товара
        :param assortment: Товар
        :param price: Цена товара
        :param discount: Скидка
        :param vat: НДС
        """
        self.invoice_in_id = invoice_in_id
        self.quantity = quantity
        self.assortment = assortment
        self.price = price
        self.discount = discount
        self.vat = vat

    def to_request(self) -> dict:
        json_data = {"quantity": self.quantity, "assortment": {"meta": self.assortment}}
        if self.price != Unset:
            json_data["price"] = self.price
        if self.discount != Unset:
            json_data["discount"] = self.discount
        if self.vat != Unset:
            json_data["vat"] = self.vat
        return {
            "method": "POST",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/"
            f"{self.invoice_in_id}/positions",
            "json": json_data,
        }

    def from_response(self, response: dict) -> InvoiceInPosition:
        return InvoiceInPosition.from_json(response[0])


class DeleteInvoiceInPositionRequest(types.ApiRequest):
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-udalit-poziciu
    def __init__(self, invoice_in_id: str, position_id: str):
        """
        Удалить позицию счета поставщика

        :param invoice_in_id: ID счета поставщика
        :param position_id: ID позиции счета поставщика
        """
        self.invoice_in_id = invoice_in_id
        self.position_id = position_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/"
            f"{self.invoice_in_id}/positions/{self.position_id}",
            "allow_non_json": True,
        }

    def from_response(self, response):
        return None


class UpdateInvoiceInPositionRequest(types.ApiRequest):
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-schet-postawschika-izmenit-poziciu
    def __init__(
        self,
        invoice_in_id: str,
        position_id: str,
        quantity: typing.Union[Unset, float] = Unset,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
    ):
        """
        Изменить позицию счета поставщика

        :param invoice_in_id: ID счета поставщика
        :param position_id: ID позиции счета поставщика
        :param quantity: Количество товара
        :param assortment: Товар
        :param price: Цена товара
        :param discount: Скидка
        :param vat: НДС
        """
        self.invoice_in_id = invoice_in_id
        self.position_id = position_id
        self.quantity = quantity
        self.assortment = assortment
        self.price = price
        self.discount = discount
        self.vat = vat

    def to_request(self) -> dict:
        json_data = {}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.assortment != Unset:
            json_data["assortment"] = (
                {"meta": self.assortment} if self.assortment is not None else None
            )
        if self.price != Unset:
            json_data["price"] = self.price
        if self.discount != Unset:
            json_data["discount"] = self.discount
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if len(json_data) == 0:
            raise ValueError("No data to update")
        return {
            "method": "PUT",
            "url": f"https://api.moysklad.ru/api/remap/1.2/entity/invoicein/"
            f"{self.invoice_in_id}/positions/{self.position_id}",
            "json": json_data,
        }

    def from_response(self, response: dict) -> InvoiceInPosition:
        return InvoiceInPosition.from_json(response)

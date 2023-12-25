import typing
import datetime
from moysklad_api import types, helpers
from moysklad_api.types import Unset, RequestData


class PurchaseOrder(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-zakazy-postawschikam

    Атрибуты сущности
    Название 	            Тип 	        Описание
    accountId 	            UUID 	 	    ID учетной записи Обязательное при ответе Только для чтения
    agent 	                Meta 	 	    Метаданные контрагента     Обязательное при ответе Необходимо при создании
    agentAccount 	        Meta 		    Метаданные счета контрагента
    applicable 	            Boolean 	 	Отметка о проведении     Обязательное при ответе
    attributes 	            Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта
    code 	                String(255) 	Код Заказа поставщику
    contract 	            Meta 	 	    Метаданные договора
    created 	            DateTime 	  	Дата создания Обязательное при ответе Только для чтения
    deleted 	            DateTime 	  	Момент последнего удаления Заказа поставщику Только для чтения
    deliveryPlannedMoment 	DateTime 	  	Планируемая дата отгрузки
    description 	        String(4096) 	Комментарий Заказа поставщику
    externalCode 	        String(255) 	Внешний код Заказа поставщику     Обязательное при ответе
    files 	                MetaArray 		Метаданные массива Файлов (Максимальное количество файлов - 100)     Обязательное при ответе
    group 	                Meta 	 	    Отдел сотрудника     Обязательное при ответе
    id 	                    UUID 	 	    ID Заказа поставщику Обязательное при ответе Только для чтения
    invoicedSum 	        Float 		    Сумма счетов поставщику     Только для чтения
    meta 	                Meta 		    Метаданные Заказа поставщику     Обязательное при ответе
    moment 	                DateTime 	  	Дата документа     Обязательное при ответе
    name 	                String(255) 	Наименование Заказа поставщику     Обязательное при ответе
    organization 	        Meta 	 	    Метаданные юрлица     Обязательное при ответе Необходимо при создании
    organizationAccount 	Meta 		    Метаданные счета юрлица
    owner 	                Meta 	 	    Владелец (Сотрудник)     Обязательное при ответе
    payedSum 	            Float 		    Сумма входящих платежей по Заказу     Только для чтения
    positions 	            MetaArray 		Метаданные позиций Заказа поставщику
    printed 	            Boolean 	 	Напечатан ли документ     Обязательное при ответе Только для чтения
    project 	            Meta 	 	    Метаданные проекта
    published 	            Boolean 	 	Опубликован ли документ     Обязательное при ответе Только для чтения
    rate 	                Object 		    Валюта. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-teh-operaciq-valuta-w-dokumentah)     Обязательное при ответе
    shared 	                Boolean 	 	Общий доступ     Обязательное при ответе
    shippedSum 	            Float 		    Сумма отгруженного     Только для чтения
    state 	                Meta 	 	    Метаданные статуса заказа
    store 	                Meta     	 	Метаданные склада
    sum 	                Int      	  	Сумма Заказа поставщику в установленной валюте     Только для чтения
    syncId 	                UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    updated 	            DateTime 	  	Момент последнего обновления Заказа поставщику     Обязательное при ответе Только для чтения
    vatEnabled 	            Boolean 		Учитывается ли НДС     Обязательное при ответе
    vatIncluded 	        Boolean 		Включен ли НДС в цену
    vatSum 	                Float 		    Сумма НДС     Только для чтения
    waitSum 	            Float 		    Сумма товаров в пути

    Связи с другими документами
    Название 	            Описание
    customerOrders      	Массив ссылок на связанные заказы покупателей в формате Метаданных
    invoicesIn 	            Массив ссылок на связанные счета поставщиков в формате Метаданных
    payments 	            Массив ссылок на связанные платежи в формате Метаданных
    supply 	            Массив ссылок на связанные приемки в формате Метаданных
    internalOrder 	        Внутренний заказ, связанный с заказом поставщику, в формате Метаданных
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
    delivery_planned_moment: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    external_code: str
    files: types.MetaArray
    group: types.Meta
    id: str
    invoiced_sum: float
    meta: types.Meta
    moment: datetime.datetime
    name: str
    organization: types.Meta
    organization_account: typing.Optional[types.Meta]
    owner: types.Meta
    payed_sum: typing.Optional[float]
    positions: typing.Optional[types.MetaArray]
    printed: bool
    project: typing.Optional[types.Meta]
    published: bool
    rate: types.Rate
    shared: bool
    shipped_sum: typing.Optional[float]
    state: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]
    sum: typing.Optional[int]
    sync_id: typing.Optional[str]
    updated: datetime.datetime
    vat_enabled: bool
    vat_included: typing.Optional[bool]
    vat_sum: typing.Optional[float]
    wait_sum: typing.Optional[float]
    custom_orders: typing.Optional[typing.List[types.Meta]]
    invoices_in: typing.Optional[typing.List[types.Meta]]
    payments: typing.Optional[typing.List[types.Meta]]
    supplies: typing.Optional[typing.List[types.Meta]]
    internal_order: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PurchaseOrder":
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
        instance.delivery_planned_moment = helpers.parse_date(
            dict_data.get("deliveryPlannedMoment")
        )
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.invoiced_sum = dict_data.get("invoicedSum")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.owner = dict_data.get("owner")
        instance.payed_sum = dict_data.get("payedSum")
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.shared = dict_data.get("shared")
        instance.shipped_sum = dict_data.get("shippedSum")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        instance.wait_sum = dict_data.get("waitSum")
        instance.custom_orders = [
            helpers.get_meta(x, must=True) for x in dict_data.get("customOrders", [])
        ]
        instance.invoices_in = [
            helpers.get_meta(x, must=True) for x in dict_data.get("invoicesIn", [])
        ]
        instance.payments = [
            helpers.get_meta(x, must=True) for x in dict_data.get("payments", [])
        ]
        instance.supplies = [
            helpers.get_meta(x, must=True) for x in dict_data.get("supply", [])
        ]
        instance.internal_order = helpers.get_meta(dict_data.get("internalOrder"))
        return instance


class PurchaseOrderPosition(types.MoySkladBaseClass):
    """
    Позиции Заказа поставщику

    Позиции Заказа - это список товаров/услуг/модификаций/серий. Объект позиции Заказа содержит следующие поля:
    Название 	        Тип 	Описание
    accountId 	        UUID 	ID учетной записи     Обязательное при ответе Только для чтения
    assortment 	        Meta 	Метаданные товара/услуги/серии/модификации, которую представляет собой позиция     Обязательное при ответе Expand
    discount 	        Int 	Процент скидки или наценки. Наценка указывается отрицательным числом, т.е. -10 создаст наценку в 10%     Обязательное при ответе
    id 	                UUID 	ID позиции     Обязательное при ответе Только для чтения
    pack 	            Object 	Упаковка Товара. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-towar-towary-atributy-wlozhennyh-suschnostej-upakowki-towara
    price 	            Float 	Цена товара/услуги в копейках     Обязательное при ответе
    quantity 	        Int 	Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе.     Обязательное при ответе
    shipped 	        Int 	Принято     Обязательное при ответе
    inTransit 	        Int 	Ожидание     Обязательное при ответе
    vat 	            Int 	НДС, которым облагается текущая позиция     Обязательное при ответе
    vatEnabled 	        Boolean Включен ли НДС для позиции. С помощью этого флага для позиции можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%.     Обязательное при ответе
    wait 	            Boolean 	Ожидается данной позиции
    """

    account_id: str
    assortment: types.Meta
    discount: int
    id: str
    pack: typing.Optional[dict]
    price: float
    quantity: float
    shipped: int
    in_transit: int
    vat: int
    vat_enabled: bool
    wait: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PurchaseOrderPosition":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.discount = dict_data.get("discount")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.shipped = dict_data.get("shipped")
        instance.in_transit = dict_data.get("inTransit")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.wait = dict_data.get("wait")
        return instance


class GetPurchaseOrderListRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-poluchit-spisok-zakazow-postawschikam

    Параметры
    Параметр 	Описание
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    search 	    string (optional) Example: 0001 Фильтр документов по указанной поисковой строке.
    """

    def __init__(
        self,
        limit: typing.Union[Unset, int] = 1000,
        offset: int = 0,
        search: typing.Optional[str] = Unset,
    ):
        """

        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        :param search: Filter documents by the specified search string. (Фильтр документов по указанной поисковой строке.)
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
            url=f"{helpers.BASE_URL}/entity/purchaseorder",
            params=params,
        )

    def from_response(self, result) -> typing.List[PurchaseOrder]:
        return [PurchaseOrder.from_json(item) for item in result["rows"]]


class CreatePurchaseOrderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-sozdat-zakaz-postawschiku

    Название 	            Тип 	        Описание
    organization 	        Meta            Ссылка на ваше юрлицо в формате Метаданных
    agent 	                Meta            Ссылка на контрагента (поставщику) в формате Метаданных

    необязательные параметры:
    agentAccount 	        Meta 		    Метаданные счета контрагента
    applicable 	            Boolean 	 	Отметка о проведении     Обязательное при ответе
    attributes 	            Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта
    code 	                String(255) 	Код Заказа поставщику
    contract 	            Meta 	 	    Метаданные договора
    deliveryPlannedMoment 	DateTime 	  	Планируемая дата отгрузки
    description 	        String(4096) 	Комментарий Заказа поставщику
    externalCode 	        String(255) 	Внешний код Заказа поставщику     Обязательное при ответе
    files 	                Array 		    Метаданные массива Файлов (Максимальное количество файлов - 100)     Обязательное при ответе
    group 	                Meta 	 	    Отдел сотрудника     Обязательное при ответе
    meta 	                Meta 		    Метаданные Заказа поставщику     Обязательное при ответе
    moment 	                DateTime 	  	Дата документа     Обязательное при ответе
    name 	                String(255) 	Наименование Заказа поставщику     Обязательное при ответе
    organization 	        Meta 	 	    Метаданные юрлица     Обязательное при ответе Необходимо при создании
    organizationAccount 	Meta 		    Метаданные счета юрлица
    owner 	                Meta 	 	    Владелец (Сотрудник)     Обязательное при ответе
    positions 	            Array(Position) Метаданные позиций Заказа поставщику
    project 	            Meta 	 	    Метаданные проекта
    rate 	                Object 		    Валюта. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-teh-operaciq-valuta-w-dokumentah)     Обязательное при ответе
    shared 	                Boolean 	 	Общий доступ     Обязательное при ответе
    state 	                Meta 	 	    Метаданные статуса заказа
    store 	                Meta     	 	Метаданные склада
    syncId 	                UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    vatEnabled 	            Boolean 		Учитывается ли НДС     Обязательное при ответе
    vatIncluded 	        Boolean 		Включен ли НДС в цену
    waitSum 	            Float 		    Сумма товаров в пути

    Связи с другими документами
    Название 	            Описание
    customerOrders      	Массив ссылок на связанные заказы покупателей в формате Метаданных
    invoicesIn 	            Массив ссылок на связанные счета поставщиков в формате Метаданных
    payments 	            Массив ссылок на связанные платежи в формате Метаданных
    supply 	            Массив ссылок на связанные приемки в формате Метаданных
    internalOrder 	        Внутренний заказ, связанный с заказом поставщику, в формате Метаданных
    """

    class CreatePosition(typing.TypedDict):
        """
        Обязательные параметры:
        assortment 	        Meta 	 	Метаданные товара
        quantity 	        Int 	 	Количество

        price 		        Float 	 	Цена поставки
        vat 	            Float 	 	Ставка НДС
        inTransit 	        Int 	 	Количество товаров в пути
        discount 	        Float 	 	Скидка
        """

        assortment: types.Meta
        quantity: float

        price: typing.NotRequired[float]
        vat: typing.NotRequired[float]
        inTransit: typing.NotRequired[int]
        discount: typing.NotRequired[float]

    def __init__(
        self,
        organization: types.Meta,
        agent: types.Meta,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
        wait_sum: typing.Union[Unset, float] = Unset,
        customer_orders: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        invoices_in: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        payments: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        supplies: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param organization: Organization meta (Метаданные юрлица)
        :param agent: Agent meta (Метаданные контрагента)
        :param agent_account: Agent account meta (Метаданные счета контрагента)
        :param applicable: Applicable (Действует)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract meta (Метаданные договора)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group meta (Метаданные группы)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param organization_account: Organization account meta (Метаданные счета организации)
        :param owner: Owner meta (Метаданные владельца)
        :param positions: Positions (Позиции)
        :param project: Project meta (Метаданные проекта)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State meta (Метаданные статуса заказа)
        :param store: Store meta (Метаданные склада)
        :param sync_id: Sync ID (ID синхронизации. После заполнения недоступен для изменения)
        :param vat_enabled: Vat enabled (Учитывается ли НДС)
        :param vat_included: Vat included (Включен ли НДС в цену)
        :param wait_sum: Wait sum (Сумма товаров в пути)
        :param customer_orders: Customer orders (Заказы покупателей)
        :param invoices_in: Invoices in (Входящие счета)
        :param payments: Payments (Платежи)
        :param supplies: Supplies (Поставки)
        :param internal_order: Internal order meta (Метаданные внутреннего заказа)
        """
        self.organization: types.Meta = organization
        self.agent: types.Meta = agent
        self.agent_account: typing.Optional[types.Meta] = agent_account
        self.applicable: typing.Optional[bool] = applicable
        self.attributes: typing.Optional[typing.List[dict]] = attributes
        self.code: typing.Optional[str] = code
        self.contract: typing.Optional[types.Meta] = contract
        self.delivery_planned_moment: typing.Optional[
            datetime.datetime
        ] = delivery_planned_moment
        self.description: typing.Optional[str] = description
        self.external_code: typing.Optional[str] = external_code
        self.files: typing.Optional[types.MetaArray] = files
        self.group: typing.Optional[types.Meta] = group
        self.meta: typing.Optional[types.Meta] = meta
        self.moment: typing.Optional[datetime.datetime] = moment
        self.name: typing.Optional[str] = name
        self.organization_account: typing.Optional[types.Meta] = organization_account
        self.owner: typing.Optional[types.Meta] = owner
        self.positions: typing.Optional[
            typing.List[CreatePurchaseOrderRequest.CreatePosition]
        ] = positions
        self.project: typing.Optional[types.Meta] = project
        self.rate: typing.Optional[types.Rate] = rate
        self.shared: typing.Optional[bool] = shared
        self.state: typing.Optional[types.Meta] = state
        self.store: typing.Optional[types.Meta] = store
        self.sync_id: typing.Optional[str] = sync_id
        self.vat_enabled: typing.Optional[bool] = vat_enabled
        self.vat_included: typing.Optional[bool] = vat_included
        self.wait_sum: typing.Optional[float] = wait_sum
        self.customer_orders: typing.Optional[typing.List[types.Meta]] = customer_orders
        self.invoices_in: typing.Optional[typing.List[types.Meta]] = invoices_in
        self.payments: typing.Optional[typing.List[types.Meta]] = payments
        self.supplies: typing.Optional[typing.List[types.Meta]] = supplies
        self.internal_order: typing.Optional[types.Meta] = internal_order

    def to_request(self) -> RequestData:
        json_data = {
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
        if self.delivery_planned_moment != Unset:
            json_data["deliveryPlannedMoment"] = helpers.date_to_str(
                self.delivery_planned_moment
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
        if self.meta != Unset:
            json_data["meta"] = self.meta
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
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
        if self.positions != Unset:
            json_data["positions"] = []
            for item in self.positions:
                pos = {
                    "assortment": {"meta": item["assortment"]},
                    "quantity": item["quantity"],
                }
                if "price" in item:
                    pos["price"] = item["price"]
                if "vat" in item:
                    pos["vat"] = item["vat"]
                if "inTransit" in item:
                    pos["inTransit"] = item["inTransit"]
                if "discount" in item:
                    pos["discount"] = item["discount"]
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
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included
        if self.wait_sum != Unset:
            json_data["waitSum"] = self.wait_sum
        if self.customer_orders != Unset:
            json_data["customerOrders"] = [
                {"meta": item} for item in self.customer_orders
            ]
        if self.invoices_in != Unset:
            json_data["invoicesIn"] = [{"meta": item} for item in self.invoices_in]
        if self.payments != Unset:
            json_data["payments"] = [{"meta": item} for item in self.payments]
        if self.supplies != Unset:
            json_data["supply"] = [{"meta": item} for item in self.supplies]
        if self.internal_order != Unset:
            json_data["internalOrder"] = (
                {"meta": self.internal_order}
                if self.internal_order is not None
                else None
            )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/purchaseorder",
            json=json_data,
        )

    def from_response(self, result) -> PurchaseOrder:
        return PurchaseOrder.from_json(result)


class DeletePurchaseOrderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-udalit-zakaz-postawschiku

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    """

    def __init__(self, order_id: str):
        """

        :param order_id: Order id to delete (ID Заказа поставщику для удаления)
        """
        self.order_id = order_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}",
            allow_non_json=True,
        )

    def from_response(self, result) -> None:
        return None


class GetPurchaseOrderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-zakaz-postawschiku

    Получить Заказ поставщику

    Параметры
    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    """

    def __init__(self, order_id: str):
        """

        :param order_id: Order id to get (ID Заказа поставщику для получения)
        """
        self.order_id = order_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}",
        )

    def from_response(self, result) -> PurchaseOrder:
        return PurchaseOrder.from_json(result)


class UpdatePurchaseOrderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-izmenit-zakaz-postawschiku

    Параметры
    Параметр 	Описание
    id 	string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.

    Необязательные параметры
    Название 	            Тип 	        Описание
    organization 	        Meta            Ссылка на ваше юрлицо в формате Метаданных
    agent 	                Meta            Ссылка на контрагента (поставщику) в формате Метаданных
    agentAccount 	        Meta 		    Метаданные счета контрагента
    applicable 	            Boolean 	 	Отметка о проведении     Обязательное при ответе
    attributes 	            Array(Object) 	Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта
    code 	                String(255) 	Код Заказа поставщику
    contract 	            Meta 	 	    Метаданные договора
    deliveryPlannedMoment 	DateTime 	  	Планируемая дата отгрузки
    description 	        String(4096) 	Комментарий Заказа поставщику
    externalCode 	        String(255) 	Внешний код Заказа поставщику     Обязательное при ответе
    files 	                Array 		    Метаданные массива Файлов (Максимальное количество файлов - 100)     Обязательное при ответе
    group 	                Meta 	 	    Отдел сотрудника     Обязательное при ответе
    meta 	                Meta 		    Метаданные Заказа поставщику     Обязательное при ответе
    moment 	                DateTime 	  	Дата документа     Обязательное при ответе
    name 	                String(255) 	Наименование Заказа поставщику     Обязательное при ответе
    organization 	        Meta 	 	    Метаданные юрлица     Обязательное при ответе Необходимо при создании
    organizationAccount 	Meta 		    Метаданные счета юрлица
    owner 	                Meta 	 	    Владелец (Сотрудник)     Обязательное при ответе
    positions 	            Array(Position) Метаданные позиций Заказа поставщику
    project 	            Meta 	 	    Метаданные проекта
    rate 	                Object 		    Валюта. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-teh-operaciq-valuta-w-dokumentah)     Обязательное при ответе
    shared 	                Boolean 	 	Общий доступ     Обязательное при ответе
    state 	                Meta 	 	    Метаданные статуса заказа
    store 	                Meta     	 	Метаданные склада
    syncId 	                UUID 	 	    ID синхронизации. После заполнения недоступен для изменения
    vatEnabled 	            Boolean 		Учитывается ли НДС     Обязательное при ответе
    vatIncluded 	        Boolean 		Включен ли НДС в цену
    waitSum 	            Float 		    Сумма товаров в пути

    Связи с другими документами
    Название 	            Описание
    customerOrders      	Массив ссылок на связанные заказы покупателей в формате Метаданных
    invoicesIn 	            Массив ссылок на связанные счета поставщиков в формате Метаданных
    payments 	            Массив ссылок на связанные платежи в формате Метаданных
    supply 	            Массив ссылок на связанные приемки в формате Метаданных
    internalOrder 	        Внутренний заказ, связанный с заказом поставщику, в формате Метаданных
    """

    UpdatePosition = CreatePurchaseOrderRequest.CreatePosition

    def __init__(
        self,
        order_id: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        agent_account: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        contract: typing.Union[Unset, types.Meta] = Unset,
        delivery_planned_moment: typing.Union[Unset, datetime.datetime] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        meta: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, types.Rate] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
        wait_sum: typing.Union[Unset, float] = Unset,
        customer_orders: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        invoices_in: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        payments: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        supplies: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        internal_order: typing.Union[Unset, types.Meta] = Unset,
    ):
        """

        :param order_id: ID Заказа поставщику
        :param organization: Organization meta (Метаданные юрлица)
        :param agent: Agent meta (Метаданные контрагента)
        :param agent_account: Agent account meta (Метаданные счета контрагента)
        :param applicable: Applicable (Действует)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param contract: Contract meta (Метаданные договора)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param files: Files (Файлы)
        :param group: Group meta (Метаданные группы)
        :param meta: Meta (Метаданные)
        :param moment: Moment (Дата)
        :param name: Name (Название)
        :param organization_account: Organization account meta (Метаданные счета организации)
        :param owner: Owner meta (Метаданные владельца)
        :param positions: Positions (Позиции)
        :param project: Project meta (Метаданные проекта)
        :param rate: Rate (Курс)
        :param shared: Shared (Общий доступ)
        :param state: State meta (Метаданные статуса заказа)
        :param store: Store meta (Метаданные склада)
        :param sync_id: Sync ID (ID синхронизации. После заполнения недоступен для изменения)
        :param vat_enabled: Vat enabled (Учитывается ли НДС)
        :param vat_included: Vat included (Включен ли НДС в цену)
        :param wait_sum: Wait sum (Сумма товаров в пути)
        :param customer_orders: Customer orders (Заказы покупателей)
        :param invoices_in: Invoices in (Входящие счета)
        :param payments: Payments (Платежи)
        :param supplies: Supplies (Поставки)
        :param internal_order: Internal order meta (Метаданные внутреннего заказа)
        """
        self.order_id: str = order_id
        self.organization: typing.Optional[types.Meta] = organization
        self.agent: typing.Optional[types.Meta] = agent
        self.agent_account: typing.Optional[types.Meta] = agent_account
        self.applicable: typing.Optional[bool] = applicable
        self.attributes: typing.Optional[typing.List[dict]] = attributes
        self.code: typing.Optional[str] = code
        self.contract: typing.Optional[types.Meta] = contract
        self.delivery_planned_moment: typing.Optional[
            datetime.datetime
        ] = delivery_planned_moment
        self.description: typing.Optional[str] = description
        self.external_code: typing.Optional[str] = external_code
        self.files: typing.Optional[types.MetaArray] = files
        self.group: typing.Optional[types.Meta] = group
        self.meta: typing.Optional[types.Meta] = meta
        self.moment: typing.Optional[datetime.datetime] = moment
        self.name: typing.Optional[str] = name
        self.organization_account: typing.Optional[types.Meta] = organization_account
        self.owner: typing.Optional[types.Meta] = owner
        self.positions: typing.Optional[
            typing.List[UpdatePurchaseOrderRequest.UpdatePosition]
        ] = positions
        self.project: typing.Optional[types.Meta] = project
        self.rate: typing.Optional[types.Rate] = rate
        self.shared: typing.Optional[bool] = shared
        self.state: typing.Optional[types.Meta] = state
        self.store: typing.Optional[types.Meta] = store
        self.sync_id: typing.Optional[str] = sync_id
        self.vat_enabled: typing.Optional[bool] = vat_enabled
        self.vat_included: typing.Optional[bool] = vat_included
        self.wait_sum: typing.Optional[float] = wait_sum
        self.customer_orders: typing.Optional[typing.List[types.Meta]] = customer_orders
        self.invoices_in: typing.Optional[typing.List[types.Meta]] = invoices_in
        self.payments: typing.Optional[typing.List[types.Meta]] = payments
        self.supplies: typing.Optional[typing.List[types.Meta]] = supplies
        self.internal_order: typing.Optional[types.Meta] = internal_order

    def to_request(self) -> RequestData:
        json_data = {}
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
        if self.delivery_planned_moment != Unset:
            json_data["deliveryPlannedMoment"] = helpers.date_to_str(
                self.delivery_planned_moment
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
        if self.meta != Unset:
            json_data["meta"] = self.meta
        if self.moment != Unset:
            json_data["moment"] = helpers.date_to_str(self.moment)
        if self.name != Unset:
            json_data["name"] = self.name
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
        if self.positions != Unset:
            json_data["positions"] = []
            for item in self.positions:
                pos = {
                    "assortment": {"meta": item["assortment"]},
                    "quantity": item["quantity"],
                }
                if "price" in item:
                    pos["price"] = item["price"]
                if "vat" in item:
                    pos["vat"] = item["vat"]
                if "inTransit" in item:
                    pos["inTransit"] = item["inTransit"]
                if "discount" in item:
                    pos["discount"] = item["discount"]
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
        if self.sync_id != Unset:
            json_data["syncId"] = self.sync_id
        if self.vat_enabled != Unset:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included != Unset:
            json_data["vatIncluded"] = self.vat_included
        if self.wait_sum != Unset:
            json_data["waitSum"] = self.wait_sum
        if self.customer_orders != Unset:
            json_data["customerOrders"] = [
                {"meta": item} for item in self.customer_orders
            ]
        if self.invoices_in != Unset:
            json_data["invoicesIn"] = [{"meta": item} for item in self.invoices_in]
        if self.payments != Unset:
            json_data["payments"] = [{"meta": item} for item in self.payments]
        if self.supplies != Unset:
            json_data["supply"] = [{"meta": item} for item in self.supplies]
        if self.internal_order != Unset:
            json_data["internalOrder"] = (
                {"meta": self.internal_order}
                if self.internal_order is not None
                else None
            )

        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}",
            json=json_data,
        )

    def from_response(self, result) -> PurchaseOrder:
        return PurchaseOrder.from_json(result)


class GetPurchaseOrderPositionsRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-poluchit-pozicii-zakaza-postawschiku

    Параметры
    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    limit 	    number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	    number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(self, order_id: str, limit: int = 1000, offset: int = 0):
        """

        :param order_id: Id of the order (ID заказа)
        :param limit: Max number of entities to extract (Максимальное количество сущностей для извлечения)
        :param offset: Offset in the list of entities (Отступ в выдаваемом списке сущностей)
        """
        self.order_id = order_id
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
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}/positions",
            params=params,
        )

    def from_response(self, result) -> typing.List[PurchaseOrderPosition]:
        return [PurchaseOrderPosition.from_json(item) for item in result["rows"]]


class CreatePurchaseOrderPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-sozdat-poziciu-zakaza-postawschiku

    Параметр 	        Описание
    id 	                string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    Assortment 	        Meta   (required) Ссылка на товар/услугу/серию/модификацию, которую представляет собой позиция. Также можно указать поле с именем service, consignment, variant в соответствии с тем, чем является указанная позиция. Подробнее об этом поле можно прочитать в описании позиции Заказа (https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-zakazy-postawschikam-pozicii-zakaza-postawschiku)
    Quantity 	        number (required) Example: 1 Количество товара/услуги/серии/модификации в позиции.
    price 		        Float 	 	Цена поставки
    vat 	            Float 	 	Ставка НДС
    inTransit 	        Int 	 	Количество товаров в пути
    discount 	        Float 	 	Скидка
    """

    def __init__(
        self,
        order_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
        in_transit: typing.Union[Unset, int] = Unset,
        discount: typing.Union[Unset, float] = Unset,
    ):
        """

        :param order_id: Id of the order (ID заказа)
        :param assortment: Meta of the product/service/series/modification (Ссылка на товар/услугу/серию/модификацию)
        :param quantity: Quantity of the product/service/series/modification (Количество товара/услуги/серии/модификации)
        :param price: Price (Цена поставки)
        :param vat: VAT rate (Ставка НДС)
        :param in_transit: Number of product in transit (Количество товаров в пути)
        :param discount: Discount (Скидка)
        """
        self.order_id = order_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.vat = vat
        self.in_transit = in_transit
        self.discount = discount

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.price != Unset:
            json_data["price"] = self.price
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.in_transit != Unset:
            json_data["inTransit"] = self.in_transit
        if self.discount != Unset:
            json_data["discount"] = self.discount
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}/positions",
            json=json_data,
        )

    def from_response(self, result) -> PurchaseOrderPosition:
        # I have no idea why they decided to return a list of one element
        return PurchaseOrderPosition.from_json(result[0])


class GetPurchaseOrderPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-poziciq-zakaza

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    positionID 	string (required) Example: 34f6344f-015e-11e6-9464-e4de0000006c id позиции Заказа поставщику.
    """

    def __init__(self, order_id: str, position_id: str):
        """

        :param order_id: Id of the order (ID заказа)
        :param position_id: Id of the position (ID позиции)
        """
        self.order_id = order_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}/positions/{self.position_id}",
        )

    def from_response(self, result) -> PurchaseOrderPosition:
        return PurchaseOrderPosition.from_json(result)


class UpdatePurchaseOrderPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-izmenit-poziciu-zakaza

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    positionID 	string (required) Example: 34f6344f-015e-11e6-9464-e4de0000006c id позиции Заказа поставщику.

    Assortment 	        Meta   Ссылка на товар/услугу/серию/модификацию, которую представляет собой позиция. Также можно указать поле с именем service, consignment, variant в соответствии с тем, чем является указанная позиция. Подробнее об этом поле можно прочитать в описании позиции Заказа (https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-zakazy-postawschikam-pozicii-zakaza-postawschiku)
    Quantity 	        number Example: 1 Количество товара/услуги/серии/модификации в позиции.
    price 		        Float 	 	Цена поставки
    vat 	            Float 	 	Ставка НДС
    inTransit 	        Int 	 	Количество товаров в пути
    discount 	        Float 	 	Скидка
    """

    def __init__(
        self,
        order_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        price: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, float] = Unset,
        in_transit: typing.Union[Unset, int] = Unset,
        discount: typing.Union[Unset, float] = Unset,
    ):
        """

        :param order_id: Id of the order (ID заказа)
        :param position_id: Id of the position (ID позиции)
        :param assortment: Meta of the product/service/series/modification (Ссылка на товар/услугу/серию/модификацию)
        :param quantity: Quantity of the product/service/series/modification (Количество товара/услуги/серии/модификации)
        :param price: Price (Цена поставки)
        :param vat: VAT (Ставка НДС)
        :param in_transit: Quantity in transit (Количество товаров в пути)
        :param discount: Discount (Скидка)
        """
        self.order_id = order_id
        self.position_id = position_id

        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.vat = vat
        self.in_transit = in_transit
        self.discount = discount

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
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.in_transit != Unset:
            json_data["inTransit"] = self.in_transit
        if self.discount != Unset:
            json_data["discount"] = self.discount

        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result) -> PurchaseOrderPosition:
        return PurchaseOrderPosition.from_json(result)


class DeletePurchaseOrderPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-postawschiku-udalit-poziciu

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Заказа поставщику.
    positionID 	string (required) Example: 34f6344f-015e-11e6-9464-e4de0000006c id позиции Заказа поставщику.
    """

    def __init__(self, order_id: str, position_id: str):
        """

        :param order_id: Id of the order (ID заказа)
        :param position_id: Id of the position (ID позиции)
        """
        self.order_id = order_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/purchaseorder/{self.order_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result) -> None:
        return None

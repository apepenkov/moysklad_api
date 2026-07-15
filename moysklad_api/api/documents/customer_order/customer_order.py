import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class CustomerOrder(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-zakaz-pokupatelq

    accountId              | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    agent                  | Meta        | Метаданные контрагента. Обязательное при ответе, Необходимо при создании, Expand
    agentAccount            | Meta        | Метаданные счета контрагента. Expand
    applicable               | Boolean     | Отметка о проведении. Обязательное при ответе
    attributes                | Array(Object)| Доп. поля
    code                        | String(255) | Код Заказа покупателя
    contract                     | Meta        | Метаданные договора. Expand
    created                        | DateTime    | Дата создания. Обязательное при ответе, Только для чтения
    deleted                          | DateTime    | Момент последнего удаления. Только для чтения
    deliveryPlannedMoment              | DateTime    | Планируемая дата приёмки
    description                          | String(4096)| Комментарий
    externalCode                           | String(255) | Внешний код. Обязательное при ответе
    files                                    | MetaArray   | Файлы. Обязательное при ответе, Expand
    group                                      | Meta        | Отдел сотрудника. Обязательное при ответе, Expand
    id                                           | UUID        | ID Заказа покупателя. Обязательное при ответе, Только для чтения
    invoicedSum                                    | Float       | Сумма счетов покупателю. Обязательное при ответе, Только для чтения
    meta                                              | Meta        | Метаданные Заказа покупателя. Обязательное при ответе
    moment                                              | DateTime    | Дата документа. Обязательное при ответе
    name                                                  | String(255) | Наименование. Обязательное при ответе
    organization                                            | Meta        | Метаданные юрлица. Обязательное при ответе, Необходимо при создании, Expand
    organizationAccount                                       | Meta        | Метаданные счета юрлица. Expand
    owner                                                       | Meta        | Владелец. Expand
    payedSum                                                      | Float       | Сумма входящих платежей. Обязательное при ответе, Только для чтения
    positions                                                      | MetaArray   | Позиции. Обязательное при ответе, Expand
    printed                                                          | Boolean     | Напечатан ли документ. Обязательное при ответе, Только для чтения
    project                                                            | Meta        | Метаданные проекта. Expand
    published                                                            | Boolean     | Опубликован ли документ. Обязательное при ответе, Только для чтения
    rate                                                                   | Object      | Валюта. Обязательное при ответе
    reservedSum                                                              | Float       | Сумма товаров в резерве. Обязательное при ответе, Только для чтения
    salesChannel                                                               | Meta        | Метаданные канала продаж. Expand
    shared                                                                       | Boolean     | Общий доступ. Обязательное при ответе
    shipmentAddress                                                                | String(255) | Адрес доставки
    shipmentAddressFull                                                              | Object      | Адрес доставки (детализированный)
    shippedSum                                                                         | Float       | Сумма отгруженного. Обязательное при ответе, Только для чтения
    state                                                                                | Meta        | Метаданные статуса заказа. Expand
    store                                                                                  | Meta        | Метаданные склада. Expand
    sum                                                                                      | Float       | Сумма Заказа. Обязательное при ответе, Только для чтения
    syncId                                                                                     | UUID        | ID синхронизации
    taxSystem                                                                                    | Enum        | Код системы налогообложения
    updated                                                                                        | DateTime    | Момент последнего обновления. Обязательное при ответе, Только для чтения
    vatEnabled                                                                                       | Boolean     | Учитывается ли НДС. Обязательное при ответе
    vatIncluded                                                                                        | Boolean     | Включен ли НДС в цену
    vatSum                                                                                               | Float       | Сумма НДС. Обязательное при ответе, Только для чтения
    purchaseOrders                                                                                         | Array(Meta) | Связанные заказы поставщикам
    demands                                                                                                  | Array(Meta) | Связанные отгрузки
    payments                                                                                                   | Array(Meta) | Связанные платежи
    productionTasks                                                                                              | Array(Meta) | Связанные производственные задания
    invoicesOut                                                                                                    | Array(Meta) | Связанные счета покупателям
    moves                                                                                                            | Array(Meta) | Связанные перемещения
    prepayments                                                                                                         | Array(Meta) | Связанные предоплаты
    """

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    agent_account: typing.Optional[types.Meta]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    contract: typing.Optional[types.Meta]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    delivery_planned_moment: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    invoiced_sum: typing.Optional[float]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    organization_account: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    payed_sum: typing.Optional[float]
    positions: typing.Optional[dict]
    printed: typing.Optional[bool]
    project: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    rate: typing.Optional[dict]
    reserved_sum: typing.Optional[float]
    sales_channel: typing.Optional[types.Meta]
    shared: typing.Optional[bool]
    shipment_address: typing.Optional[str]
    shipment_address_full: typing.Optional[dict]
    shipped_sum: typing.Optional[float]
    state: typing.Optional[types.Meta]
    store: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    tax_system: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    vat_enabled: typing.Optional[bool]
    vat_included: typing.Optional[bool]
    vat_sum: typing.Optional[float]
    purchase_orders: typing.Optional[typing.List[types.Meta]]
    demands: typing.Optional[typing.List[types.Meta]]
    payments: typing.Optional[typing.List[types.Meta]]
    production_tasks: typing.Optional[typing.List[types.Meta]]
    invoices_out: typing.Optional[typing.List[types.Meta]]
    moves: typing.Optional[typing.List[types.Meta]]
    prepayments: typing.Optional[typing.List[types.Meta]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "CustomerOrder":
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
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.payed_sum = dict_data.get("payedSum")
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.rate = dict_data.get("rate")
        instance.reserved_sum = dict_data.get("reservedSum")
        instance.sales_channel = helpers.get_meta(dict_data.get("salesChannel"))
        instance.shared = dict_data.get("shared")
        instance.shipment_address = dict_data.get("shipmentAddress")
        instance.shipment_address_full = dict_data.get("shipmentAddressFull")
        instance.shipped_sum = dict_data.get("shippedSum")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.tax_system = dict_data.get("taxSystem")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.vat_enabled = dict_data.get("vatEnabled")
        instance.vat_included = dict_data.get("vatIncluded")
        instance.vat_sum = dict_data.get("vatSum")
        instance.purchase_orders = [
            helpers.get_meta(x, must=True) for x in dict_data.get("purchaseOrders", [])
        ]
        instance.demands = [
            helpers.get_meta(x, must=True) for x in dict_data.get("demands", [])
        ]
        instance.payments = [
            helpers.get_meta(x, must=True) for x in dict_data.get("payments", [])
        ]
        instance.production_tasks = [
            helpers.get_meta(x, must=True)
            for x in dict_data.get("productionTasks", [])
        ]
        instance.invoices_out = [
            helpers.get_meta(x, must=True) for x in dict_data.get("invoicesOut", [])
        ]
        instance.moves = [
            helpers.get_meta(x, must=True) for x in dict_data.get("moves", [])
        ]
        instance.prepayments = [
            helpers.get_meta(x, must=True) for x in dict_data.get("prepayments", [])
        ]
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("customerorder",)


class Position(types.MoySkladBaseClass):
    """
    accountId  | UUID  | ID учетной записи. Обязательное при ответе, Только для чтения
    assortment  | Meta  | Метаданные позиции. Обязательное при ответе, Expand
    discount     | Float | Процент скидки/наценки. Обязательное при ответе
    id            | UUID  | ID позиции. Обязательное при ответе, Только для чтения
    pack           | Object| Упаковка товара
    price           | Float | Цена в копейках. Обязательное при ответе
    quantity         | Float | Количество. Обязательное при ответе
    reserve           | Float | Резерв данной позиции
    shipped            | Float | Доставлено. Обязательное при ответе, Только для чтения
    taxSystem           | Enum  | Код системы налогообложения
    vat                   | Int   | НДС. Обязательное при ответе
    vatEnabled              | Boolean| Включен ли НДС. Обязательное при ответе
    """

    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    discount: typing.Optional[float]
    id: typing.Optional[str]
    pack: typing.Optional[dict]
    price: typing.Optional[float]
    quantity: typing.Optional[float]
    reserve: typing.Optional[float]
    shipped: typing.Optional[float]
    tax_system: typing.Optional[str]
    vat: typing.Optional[int]
    vat_enabled: typing.Optional[bool]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.discount = dict_data.get("discount")
        instance.id = dict_data.get("id")
        instance.pack = dict_data.get("pack")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.reserve = dict_data.get("reserve")
        instance.shipped = dict_data.get("shipped")
        instance.tax_system = dict_data.get("taxSystem")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "customerorder", "positions"


def _build_customerorder_json(
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
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    organization_account: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    rate: typing.Union[Unset, dict] = Unset,
    sales_channel: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    shipment_address: typing.Union[Unset, str] = Unset,
    shipment_address_full: typing.Union[Unset, dict] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    store: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
    tax_system: typing.Union[Unset, str] = Unset,
    vat_enabled: typing.Union[Unset, bool] = Unset,
    vat_included: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if agent != Unset:
        json_data["agent"] = {"meta": agent}
    if agent_account != Unset:
        json_data["agentAccount"] = {"meta": agent_account}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if code != Unset:
        json_data["code"] = code
    if contract != Unset:
        json_data["contract"] = {"meta": contract}
    if delivery_planned_moment != Unset:
        json_data["deliveryPlannedMoment"] = helpers.date_to_str(
            delivery_planned_moment
        )
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if group != Unset:
        json_data["group"] = {"meta": group}
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if organization_account != Unset:
        json_data["organizationAccount"] = {"meta": organization_account}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if positions != Unset:
        json_data["positions"] = []
        for position in positions:
            new_position: dict = position.copy()
            new_position["assortment"] = {"meta": new_position["assortment"]}
            json_data["positions"].append(new_position)
    if project != Unset:
        json_data["project"] = {"meta": project}
    if rate != Unset:
        json_data["rate"] = rate
    if sales_channel != Unset:
        json_data["salesChannel"] = {"meta": sales_channel}
    if shared != Unset:
        json_data["shared"] = shared
    if shipment_address != Unset:
        json_data["shipmentAddress"] = shipment_address
    if shipment_address_full != Unset:
        json_data["shipmentAddressFull"] = shipment_address_full
    if state != Unset:
        json_data["state"] = {"meta": state}
    if store != Unset:
        json_data["store"] = {"meta": store}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    if tax_system != Unset:
        json_data["taxSystem"] = tax_system
    if vat_enabled != Unset:
        json_data["vatEnabled"] = vat_enabled
    if vat_included != Unset:
        json_data["vatIncluded"] = vat_included
    return json_data


class GetCustomerOrdersRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ):
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
            url=f"{helpers.BASE_URL}/entity/customerorder",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[CustomerOrder]:
        return [CustomerOrder.from_json(x) for x in result["rows"]]


class CreateCustomerOrderRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        price: typing.NotRequired[float]
        discount: typing.NotRequired[float]
        vat: typing.NotRequired[int]
        reserve: typing.NotRequired[float]

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
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        shipment_address: typing.Union[Unset, str] = Unset,
        shipment_address_full: typing.Union[Unset, dict] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.organization = organization
        self.agent = agent
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.delivery_planned_moment = delivery_planned_moment
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.sales_channel = sales_channel
        self.shared = shared
        self.shipment_address = shipment_address
        self.shipment_address_full = shipment_address_full
        self.state = state
        self.store = store
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_customerorder_json(
            organization=self.organization,
            agent=self.agent,
            agent_account=self.agent_account,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            contract=self.contract,
            delivery_planned_moment=self.delivery_planned_moment,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            positions=self.positions,
            project=self.project,
            rate=self.rate,
            sales_channel=self.sales_channel,
            shared=self.shared,
            shipment_address=self.shipment_address,
            shipment_address_full=self.shipment_address_full,
            state=self.state,
            store=self.store,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/customerorder",
            json=json_data,
        )

    def from_response(self, result: dict) -> CustomerOrder:
        return CustomerOrder.from_json(result)


class DeleteCustomerOrderRequest(types.ApiRequest):
    def __init__(self, order_id: str):
        self.order_id = order_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetCustomerOrderRequest(types.ApiRequest):
    def __init__(self, order_id: str):
        self.order_id = order_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}",
        )

    def from_response(self, result: dict) -> CustomerOrder:
        return CustomerOrder.from_json(result)


class UpdateCustomerOrderRequest(types.ApiRequest):
    UpdatePosition = CreateCustomerOrderRequest.CreatePosition

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
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        rate: typing.Union[Unset, dict] = Unset,
        sales_channel: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        shipment_address: typing.Union[Unset, str] = Unset,
        shipment_address_full: typing.Union[Unset, dict] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        store: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
        tax_system: typing.Union[Unset, str] = Unset,
        vat_enabled: typing.Union[Unset, bool] = Unset,
        vat_included: typing.Union[Unset, bool] = Unset,
    ):
        self.order_id = order_id
        self.organization = organization
        self.agent = agent
        self.agent_account = agent_account
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.contract = contract
        self.delivery_planned_moment = delivery_planned_moment
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.positions = positions
        self.project = project
        self.rate = rate
        self.sales_channel = sales_channel
        self.shared = shared
        self.shipment_address = shipment_address
        self.shipment_address_full = shipment_address_full
        self.state = state
        self.store = store
        self.sync_id = sync_id
        self.tax_system = tax_system
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included

    def to_request(self) -> RequestData:
        json_data = _build_customerorder_json(
            organization=self.organization,
            agent=self.agent,
            agent_account=self.agent_account,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            contract=self.contract,
            delivery_planned_moment=self.delivery_planned_moment,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            positions=self.positions,
            project=self.project,
            rate=self.rate,
            sales_channel=self.sales_channel,
            shared=self.shared,
            shipment_address=self.shipment_address,
            shipment_address_full=self.shipment_address_full,
            state=self.state,
            store=self.store,
            sync_id=self.sync_id,
            tax_system=self.tax_system,
            vat_enabled=self.vat_enabled,
            vat_included=self.vat_included,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> CustomerOrder:
        return CustomerOrder.from_json(result)


class GetCustomerOrderPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        order_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
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
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class CreateCustomerOrderPositionRequest(types.ApiRequest):
    def __init__(
        self,
        order_id: str,
        assortment: types.Meta,
        quantity: float,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        reserve: typing.Union[Unset, float] = Unset,
    ):
        self.order_id = order_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.vat = vat
        self.reserve = reserve

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
        if self.reserve != Unset:
            json_data["reserve"] = self.reserve
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}/positions",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class GetCustomerOrderPositionRequest(types.ApiRequest):
    def __init__(self, order_id: str, position_id: str):
        self.order_id = order_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class UpdateCustomerOrderPositionRequest(types.ApiRequest):
    def __init__(
        self,
        order_id: str,
        position_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        price: typing.Union[Unset, float] = Unset,
        discount: typing.Union[Unset, float] = Unset,
        vat: typing.Union[Unset, int] = Unset,
        reserve: typing.Union[Unset, float] = Unset,
    ):
        self.order_id = order_id
        self.position_id = position_id
        self.assortment = assortment
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.vat = vat
        self.reserve = reserve

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.price != Unset:
            json_data["price"] = self.price
        if self.discount != Unset:
            json_data["discount"] = self.discount
        if self.vat != Unset:
            json_data["vat"] = self.vat
        if self.reserve != Unset:
            json_data["reserve"] = self.reserve
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeleteCustomerOrderPositionRequest(types.ApiRequest):
    def __init__(self, order_id: str, position_id: str):
        self.order_id = order_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/customerorder/{self.order_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

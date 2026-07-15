import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData

# Общий список полей Точки продаж - см. документацию (много Enum-ов и вложенных
# объектов, представленных как raw dict, т.к. это скорее конфигурация, чем
# самостоятельные сущности).


class RetailStore(types.MoySkladBaseClass):
    """
    Точка продаж (retailstore). Полный список полей и их описания - см.
    W:\\stuff\\api-remap-1.2-doc\\md\\dictionaries\\_retailstore.md
    Здесь перечислены основные поля; сложные вложенные объекты (environment,
    state, addressFull, priceType, software, chequePrinter и т.п.) переданы как dict.
    """

    account_id: typing.Optional[str]
    acquire: typing.Optional[types.Meta]
    active: typing.Optional[bool]
    address: typing.Optional[str]
    address_full: typing.Optional[dict]
    allow_create_products: typing.Optional[bool]
    allow_custom_price: typing.Optional[bool]
    allow_delete_receipt_positions: typing.Optional[bool]
    allow_sell_tobacco_without_mrc: typing.Optional[bool]
    archived: typing.Optional[bool]
    auth_token_attached: typing.Optional[bool]
    bank_percent: typing.Optional[float]
    cashiers: typing.Optional[types.Meta]
    control_cashier_choice: typing.Optional[bool]
    control_shipping_stock: typing.Optional[bool]
    create_agents_tags: typing.Optional[typing.List[dict]]
    create_cash_in_on_retail_shift_closing: typing.Optional[bool]
    create_order_with_state: typing.Optional[types.Meta]
    create_payment_in_on_retail_shift_closing: typing.Optional[bool]
    customer_order_states: typing.Optional[typing.List[dict]]
    default_tax_system: typing.Optional[str]
    demand_prefix: typing.Optional[str]
    description: typing.Optional[str]
    discount_enable: typing.Optional[bool]
    discount_max_percent: typing.Optional[int]
    enable_returns_with_no_reason: typing.Optional[bool]
    environment: typing.Optional[dict]
    external_code: typing.Optional[str]
    filter_agents_tags: typing.Optional[typing.List[str]]
    fiscal_type: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    id_qr: typing.Optional[str]
    issue_orders: typing.Optional[bool]
    last_operation_names: typing.Optional[typing.List[dict]]
    marking_selling_mode: typing.Optional[str]
    marks_check_mode: typing.Optional[str]
    master_retail_stores: typing.Optional[dict]
    meta: typing.Optional[types.Meta]
    minion_to_master_type: typing.Optional[str]
    name: typing.Optional[str]
    ofd_enabled: typing.Optional[bool]
    only_in_stock: typing.Optional[bool]
    order_tax_system: typing.Optional[str]
    order_to_state: typing.Optional[types.Meta]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    price_type: typing.Optional[dict]
    print_always: typing.Optional[bool]
    priority_ofd_send: typing.Optional[str]
    product_folders: typing.Optional[dict]
    qr_acquire: typing.Optional[types.Meta]
    qr_bank_percent: typing.Optional[float]
    qr_pay_enabled: typing.Optional[bool]
    qr_terminal_id: typing.Optional[str]
    receipt_template: typing.Optional[types.Meta]
    required_fio: typing.Optional[bool]
    required_phone: typing.Optional[bool]
    required_email: typing.Optional[bool]
    required_birthdate: typing.Optional[bool]
    required_sex: typing.Optional[bool]
    required_discount_card_number: typing.Optional[bool]
    reserve_prepaid_goods: typing.Optional[bool]
    return_from_closed_shift_enabled: typing.Optional[bool]
    sell_reserves: typing.Optional[bool]
    send_marks_for_check: typing.Optional[bool]
    send_marks_to_chestny_znak_on_cloud: typing.Optional[bool]
    sync_agents: typing.Optional[bool]
    shared: typing.Optional[bool]
    show_beer_on_tap: typing.Optional[bool]
    state: typing.Optional[dict]
    store: typing.Optional[types.Meta]
    tobacco_mrc_control_type: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "RetailStore":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.acquire = helpers.get_meta(dict_data.get("acquire"))
        instance.active = dict_data.get("active")
        instance.address = dict_data.get("address")
        instance.address_full = dict_data.get("addressFull")
        instance.allow_create_products = dict_data.get("allowCreateProducts")
        instance.allow_custom_price = dict_data.get("allowCustomPrice")
        instance.allow_delete_receipt_positions = dict_data.get(
            "allowDeleteReceiptPositions"
        )
        instance.allow_sell_tobacco_without_mrc = dict_data.get(
            "allowSellTobaccoWithoutMRC"
        )
        instance.archived = dict_data.get("archived")
        instance.auth_token_attached = dict_data.get("authTokenAttached")
        instance.bank_percent = dict_data.get("bankPercent")
        instance.cashiers = helpers.get_meta(dict_data.get("cashiers"))
        instance.control_cashier_choice = dict_data.get("controlCashierChoice")
        instance.control_shipping_stock = dict_data.get("controlShippingStock")
        instance.create_agents_tags = dict_data.get("createAgentsTags")
        instance.create_cash_in_on_retail_shift_closing = dict_data.get(
            "createCashInOnRetailShiftClosing"
        )
        instance.create_order_with_state = helpers.get_meta(
            dict_data.get("createOrderWithState")
        )
        instance.create_payment_in_on_retail_shift_closing = dict_data.get(
            "createPaymentInOnRetailShiftClosing"
        )
        instance.customer_order_states = dict_data.get("customerOrderStates")
        instance.default_tax_system = dict_data.get("defaultTaxSystem")
        instance.demand_prefix = dict_data.get("demandPrefix")
        instance.description = dict_data.get("description")
        instance.discount_enable = dict_data.get("discountEnable")
        instance.discount_max_percent = dict_data.get("discountMaxPercent")
        instance.enable_returns_with_no_reason = dict_data.get(
            "enableReturnsWithNoReason"
        )
        instance.environment = dict_data.get("environment")
        instance.external_code = dict_data.get("externalCode")
        instance.filter_agents_tags = dict_data.get("filterAgentsTags")
        instance.fiscal_type = dict_data.get("fiscalType")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.id_qr = dict_data.get("idQR")
        instance.issue_orders = dict_data.get("issueOrders")
        instance.last_operation_names = dict_data.get("lastOperationNames")
        instance.marking_selling_mode = dict_data.get("markingSellingMode")
        instance.marks_check_mode = dict_data.get("marksCheckMode")
        instance.master_retail_stores = dict_data.get("masterRetailStores")
        instance.meta = dict_data.get("meta")
        instance.minion_to_master_type = dict_data.get("minionToMasterType")
        instance.name = dict_data.get("name")
        instance.ofd_enabled = dict_data.get("ofdEnabled")
        instance.only_in_stock = dict_data.get("onlyInStock")
        instance.order_tax_system = dict_data.get("orderTaxSystem")
        instance.order_to_state = helpers.get_meta(dict_data.get("orderToState"))
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.price_type = dict_data.get("priceType")
        instance.print_always = dict_data.get("printAlways")
        instance.priority_ofd_send = dict_data.get("priorityOfdSend")
        instance.product_folders = dict_data.get("productFolders")
        instance.qr_acquire = helpers.get_meta(dict_data.get("qrAcquire"))
        instance.qr_bank_percent = dict_data.get("qrBankPercent")
        instance.qr_pay_enabled = dict_data.get("qrPayEnabled")
        instance.qr_terminal_id = dict_data.get("qrTerminalId")
        instance.receipt_template = helpers.get_meta(dict_data.get("receiptTemplate"))
        instance.required_fio = dict_data.get("requiredFio")
        instance.required_phone = dict_data.get("requiredPhone")
        instance.required_email = dict_data.get("requiredEmail")
        instance.required_birthdate = dict_data.get("requiredBirthdate")
        instance.required_sex = dict_data.get("requiredSex")
        instance.required_discount_card_number = dict_data.get(
            "requiredDiscountCardNumber"
        )
        instance.reserve_prepaid_goods = dict_data.get("reservePrepaidGoods")
        instance.return_from_closed_shift_enabled = dict_data.get(
            "returnFromClosedShiftEnabled"
        )
        instance.sell_reserves = dict_data.get("sellReserves")
        instance.send_marks_for_check = dict_data.get("sendMarksForCheck")
        instance.send_marks_to_chestny_znak_on_cloud = dict_data.get(
            "sendMarksToChestnyZnakOnCloud"
        )
        instance.sync_agents = dict_data.get("syncAgents")
        instance.shared = dict_data.get("shared")
        instance.show_beer_on_tap = dict_data.get("showBeerOnTap")
        instance.state = dict_data.get("state")
        instance.store = helpers.get_meta(dict_data.get("store"))
        instance.tobacco_mrc_control_type = dict_data.get("tobaccoMrcControlType")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("retailstore",)


def _build_retailstore_json(**fields) -> dict:
    name_map = {
        "acquire": "acquire",
        "active": "active",
        "address": "address",
        "address_full": "addressFull",
        "allow_create_products": "allowCreateProducts",
        "allow_delete_receipt_positions": "allowDeleteReceiptPositions",
        "allow_sell_tobacco_without_mrc": "allowSellTobaccoWithoutMRC",
        "archived": "archived",
        "bank_percent": "bankPercent",
        "control_cashier_choice": "controlCashierChoice",
        "control_shipping_stock": "controlShippingStock",
        "create_agents_tags": "createAgentsTags",
        "create_cash_in_on_retail_shift_closing": "createCashInOnRetailShiftClosing",
        "create_order_with_state": "createOrderWithState",
        "create_payment_in_on_retail_shift_closing": "createPaymentInOnRetailShiftClosing",
        "customer_order_states": "customerOrderStates",
        "default_tax_system": "defaultTaxSystem",
        "demand_prefix": "demandPrefix",
        "description": "description",
        "discount_enable": "discountEnable",
        "discount_max_percent": "discountMaxPercent",
        "enable_returns_with_no_reason": "enableReturnsWithNoReason",
        "filter_agents_tags": "filterAgentsTags",
        "fiscal_type": "fiscalType",
        "group": "group",
        "id_qr": "idQR",
        "issue_orders": "issueOrders",
        "marking_selling_mode": "markingSellingMode",
        "marks_check_mode": "marksCheckMode",
        "master_retail_stores": "masterRetailStores",
        "minion_to_master_type": "minionToMasterType",
        "name": "name",
        "only_in_stock": "onlyInStock",
        "order_tax_system": "orderTaxSystem",
        "order_to_state": "orderToState",
        "organization": "organization",
        "owner": "owner",
        "price_type": "priceType",
        "print_always": "printAlways",
        "priority_ofd_send": "priorityOfdSend",
        "product_folders": "productFolders",
        "qr_acquire": "qrAcquire",
        "qr_bank_percent": "qrBankPercent",
        "qr_pay_enabled": "qrPayEnabled",
        "qr_terminal_id": "qrTerminalId",
        "receipt_template": "receiptTemplate",
        "required_fio": "requiredFio",
        "required_phone": "requiredPhone",
        "required_email": "requiredEmail",
        "required_birthdate": "requiredBirthdate",
        "required_sex": "requiredSex",
        "required_discount_card_number": "requiredDiscountCardNumber",
        "reserve_prepaid_goods": "reservePrepaidGoods",
        "return_from_closed_shift_enabled": "returnFromClosedShiftEnabled",
        "sell_reserves": "sellReserves",
        "send_marks_for_check": "sendMarksForCheck",
        "send_marks_to_chestny_znak_on_cloud": "sendMarksToChestnyZnakOnCloud",
        "sync_agents": "syncAgents",
        "shared": "shared",
        "show_beer_on_tap": "showBeerOnTap",
        "store": "store",
        "tobacco_mrc_control_type": "tobaccoMrcControlType",
    }
    meta_fields = {
        "acquire",
        "create_order_with_state",
        "group",
        "order_to_state",
        "organization",
        "owner",
        "qr_acquire",
        "receipt_template",
        "store",
    }
    json_data = {}
    for key, value in fields.items():
        if value is Unset:
            continue
        json_key = name_map[key]
        if key in meta_fields:
            json_data[json_key] = {"meta": value}
        else:
            json_data[json_key] = value
    return json_data


class GetRetailStoresRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/retailstore",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[RetailStore]:
        return [RetailStore.from_json(x) for x in result["rows"]]


class CreateRetailStoreRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        organization: types.Meta,
        store: types.Meta,
        price_type: dict,
        **kwargs,
    ):
        """
        :param name: Наименование Точки продаж
        :param organization: Метаданные Юрлица
        :param store: Метаданные Склада
        :param price_type: Тип цен, с которыми будут продаваться товары
        :param kwargs: Остальные необязательные поля Точки продаж (snake_case),
            см. RetailStore/_build_retailstore_json для полного списка ключей.
        """
        self.name = name
        self.organization = organization
        self.store = store
        self.price_type = price_type
        self.kwargs = kwargs

    def to_request(self) -> RequestData:
        json_data = _build_retailstore_json(
            name=self.name,
            organization=self.organization,
            store=self.store,
            price_type=self.price_type,
            **self.kwargs,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/retailstore",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetailStore:
        return RetailStore.from_json(result)


class DeleteRetailStoreRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/retailstore/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetRetailStoreRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/retailstore/{self.id}",
        )

    def from_response(self, result: dict) -> RetailStore:
        return RetailStore.from_json(result)


class UpdateRetailStoreRequest(types.ApiRequest):
    def __init__(self, id_: str, **kwargs):
        """
        :param id_: ID Точки продаж
        :param kwargs: Поля Точки продаж для обновления (snake_case), см.
            RetailStore/_build_retailstore_json для полного списка ключей.
        """
        self.id = id_
        self.kwargs = kwargs

    def to_request(self) -> RequestData:
        json_data = _build_retailstore_json(**self.kwargs)
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/retailstore/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> RetailStore:
        return RetailStore.from_json(result)

import typing
import datetime
from .... import types


class InternalOrder(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-vnutrennie-zakazy

    accountId 	UUID 	                    ID учетной записи       Обязательное при ответе     Только для чтения
    applicable 	Boolean 	                Отметка о проведении    Обязательное при ответе
    attributes 	Array(Object) 	            Операторы доп. полей 	Коллекция метаданных доп. полей. Поля объекта Только для чтения
    code 	String(255) 	 	            Код Внутреннего заказа
    created 	DateTime 	 	            Дата создания           Обязательное при ответе Только для чтения
    deleted 	DateTime 	 	            Момент последнего удаления Внутреннего заказа Обязательное при ответе Только для чтения
    deliveryPlannedMoment 	DateTime 		Планируемая дата приемки
    description 	String(4096) 	 	    Комментарий Внутреннего заказа
    externalCode 	String(255) 	 	    Внешний код Внутреннего заказа     Обязательное при ответе
    files 	MetaArray 		                Метаданные массива Файлов (Максимальное количество файлов - 100)    Обязательное при ответе Expand
    group 	Meta 	 	                    Отдел сотрудника    Обязательное при ответе Expand
    id 	UUID 	 	                        ID Внутреннего заказа  Обязательное при ответе Только для чтения
    meta 	Meta 		                    Метаданные Внутреннего заказа    Обязательное при ответе Только для чтения
    moment 	DateTime 	 	                Дата документа     Обязательное при ответе
    moves 	Array(Object) 		            Коллекция метаданных на связанные заказы перемещения    Обязательное при ответе
    name 	String(255) 	 	            Наименование Внутреннего заказа    Обязательное при ответе Необходимо при создании
    organization 	Meta 	 	            Метаданные юрлица    Обязательное при ответе Expand Необходимо при создании
    owner 	Meta 	 	                    Владелец (Сотрудник)    Обязательное при ответе Expand
    positions 	MetaArray 		            Метаданные позиций Внутреннего заказа Обязательное при ответе Только для чтения Expand
    printed 	Boolean 	 	            Напечатан ли документ    Обязательное при ответе Только для чтения
    project 	Meta 	 	                Метаданные проекта    Expand
    published 	Boolean 	 	            Опубликован ли документ     Обязательное при ответе Только для чтения
    purchaseOrders 	Array(Object) 		    Коллекция метаданных на связанные заказы поставщику     Обязательное при ответе
    rate 	Object 		                    Валюта. Обязательное при ответе
    shared 	Boolean 	 	                Общий доступ Обязательное при ответе Только для чтения
    state 	Meta 	 	                    Метаданные статуса Внутреннего заказа     Expand
    store 	                                Метаданные склада     Expand
    sum 	Int 	                        Сумма Внутреннего заказа в копейках   Обязательное при ответе Только для чтения
    syncId 	UUID 	 	                    ID синхронизации. После заполнения недоступен для изменения     Только для чтения
    updated 	DateTime 	                Момент последнего обновления Внутреннего заказа     Обязательное при ответе Только для чтения
    vatEnabled 	Boolean 		            Учитывается ли НДС     Обязательное при ответе
    vatIncluded 	Boolean 		        Включен ли НДС в цену
    vatSum 	Float 		                    Сумма НДС   Обязательное при ответе Только для чтения
    """

    def __init__(self):
        self.account_id: str = None
        self.applicable: bool = None
        self.attributes: typing.Optional[list] = None
        self.code: typing.Optional[str] = None
        self.created: datetime.datetime = None
        self.deleted: datetime.datetime = None
        self.delivery_planned_moment: typing.Optional[datetime.datetime] = None
        self.description: typing.Optional[str] = None
        self.external_code: str = None
        self.files: types.MetaArray = None
        self.group: types.Meta = None
        self.id: str = None
        self.meta: types.Meta = None
        self.moment: datetime.datetime = None
        self.moves: list = None
        self.name: str = None
        self.organization: types.Meta = None
        self.owner: types.Meta = None
        self.positions: types.MetaArray = None
        self.project: typing.Optional[types.Meta] = None
        self.printed: bool = None
        self.published: bool = None
        self.purchase_orders: list = None
        self.rate: types.Rate = None
        self.shared: bool = None
        self.state: typing.Optional[types.Meta] = None
        self.store: typing.Optional[types.Meta] = None
        self.sum: int = None
        self.sync_id: typing.Optional[str] = None
        self.updated: datetime.datetime = None
        self.vat_enabled: bool = None
        self.vat_included: typing.Optional[bool] = None
        self.vat_sum: float = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "InternalOrder":
        result = cls()
        result.account_id = dict_data.get("accountId")
        result.applicable = dict_data.get("applicable")
        result.attributes = dict_data.get("attributes")
        result.code = dict_data.get("code")
        created = dict_data.get("created")
        if created:
            result.created = datetime.datetime.fromisoformat(created)
        deleted = dict_data.get("deleted")
        if deleted:
            result.deleted = datetime.datetime.fromisoformat(deleted)
        delivery_planned_moment = dict_data.get("deliveryPlannedMoment")
        if delivery_planned_moment:
            result.delivery_planned_moment = datetime.datetime.fromisoformat(
                delivery_planned_moment
            )
        result.description = dict_data.get("description")
        result.external_code = dict_data.get("externalCode")
        result.files = dict_data.get("files")
        group = dict_data.get("group")
        if group:
            result.group = group["meta"]
        result.id = dict_data.get("id")
        result.meta = dict_data.get("meta")
        moment = dict_data.get("moment")
        if moment:
            result.moment = datetime.datetime.fromisoformat(moment)
        result.moves = dict_data.get("moves")
        result.name = dict_data.get("name")
        organization = dict_data.get("organization")
        if organization:
            result.organization = organization["meta"]
        owner = dict_data.get("owner")
        if owner:
            result.owner = owner["meta"]
        result.positions = dict_data.get("positions")
        project = dict_data.get("project")
        if project:
            result.project = project["meta"]
        result.printed = dict_data.get("printed")
        result.published = dict_data.get("published")
        result.purchase_orders = dict_data.get("purchaseOrders")
        result.rate = dict_data.get("rate")
        result.shared = dict_data.get("shared")
        state = dict_data.get("state")
        if state:
            result.state = state["meta"]
        store = dict_data.get("store")
        if store:
            result.store = store["meta"]
        result.sum = dict_data.get("sum")
        result.sync_id = dict_data.get("syncId")
        updated = dict_data.get("updated")
        if updated:
            result.updated = datetime.datetime.fromisoformat(updated)
        result.vat_enabled = dict_data.get("vatEnabled")
        result.vat_included = dict_data.get("vatIncluded")
        result.vat_sum = dict_data.get("vatSum")
        return result


class Position(types.MoySkladBaseClass):
    """

    accountId 	UUID        ID учетной записи Обязательное при ответе Только для чтения
    assortment 	Meta 	    Метаданные товара/услуги/серии/модификации, которую представляет собой позиция Обязательное при ответе Expand
    id 	        UUID 	    ID позиции Обязательное при ответе Только для чтения
    pack 	    Object      Упаковка Товара.
    price 	    Float       Цена товара/услуги в копейках Обязательное при ответе
    quantity 	Int 	    Количество товаров/услуг данного вида в позиции. Если позиция - товар, у которого включен учет по серийным номерам, то значение в этом поле всегда будет равно количеству серийных номеров для данной позиции в документе. Обязательное при ответе
    vat 	    Int	        НДС, которым облагается текущая позиция Обязательное при ответе
    vatEnabled 	Boolean 	Включен ли НДС для позиции. С помощью этого флага для позиции можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%. Обязательное при ответе
    """

    def __init__(
        self,
        account_id: typing.Optional[str] = None,
        assortment: typing.Optional[dict] = None,
        id_: typing.Optional[str] = None,
        pack: typing.Optional[dict] = None,
        price: typing.Optional[int] = None,
        quantity: typing.Optional[int] = None,
        vat: typing.Optional[int] = None,
        vat_enabled: typing.Optional[bool] = None,
    ):
        self.account_id: typing.Optional[str] = account_id
        self.assortment: typing.Optional[types.Meta] = assortment
        self.id: typing.Optional[str] = id_
        self.pack: typing.Optional[dict] = pack
        self.price: float = price
        self.quantity: float = quantity
        self.vat: int = vat
        self.vat_enabled: typing.Optional[bool] = vat_enabled

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        result = cls()
        result.account_id = dict_data.get("accountId")
        result.assortment = dict_data.get("assortment", {}).get("meta")
        result.id = dict_data.get("id")
        result.pack = dict_data.get("pack")
        result.price = dict_data.get("price")
        result.quantity = dict_data.get("quantity")
        result.vat = dict_data.get("vat")
        result.vat_enabled = dict_data.get("vatEnabled")
        return result


class GetInternalOrdersRequest(types.ApiRequest):
    """
    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennie-zakazy
    Получить Внутренние заказы

    Параметры
    Параметр 	Описание
    limit 	number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    search 	string (optional) Example: 0001 Фильтр документов по указанной поисковой строке.
    """

    def __init__(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ):
        """
        :param limit: Limit the number of results (Ограничить количество результатов)
        :param offset:  Offset the results (Сместить результаты)
        :param search:  Search query (Поисковый запрос)
        """
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(
        self,
    ) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.search is not None:
            params["search"] = self.search
        return {
            "method": "GET",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/internalorder",
            "params": params,
        }

    def from_response(self, response: dict) -> typing.List[InternalOrder]:
        return [InternalOrder.from_json(i) for i in response["rows"]]


class CreateInternalOrderRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        """
        `Position`, returned by GetInternalOrders and `Position`, used in CreateInternalOrder, are different.
        So, I created this class to avoid confusion.

        `Позиция` внутреннего заказа, возвращаемая методом GetInternalOrders и `Позиция` внутреннего заказа, используемая в CreateInternalOrder, отличаются друг от друга.
        Поэтому я создал этот класс, чтобы избежать путаницы.
        """

        quantity: float
        price: int
        discount: int
        vat: int
        assortment: types.Meta

    """
    Создать Внутренний заказ

    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-sozdat-vnutrennij-zakaz
    """

    def __init__(
        self,
        organization: types.Meta,
        owner: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        group: typing.Optional[types.Meta] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        moment: typing.Optional[typing.Union[str, datetime.datetime]] = None,
        applicable: typing.Optional[bool] = None,
        rate: typing.Optional[types.Rate] = None,
        sum_: typing.Optional[int] = None,
        store: typing.Optional[types.Meta] = None,
        project: typing.Optional[types.Meta] = None,
        state: typing.Optional[types.Meta] = None,
        positions: typing.Optional[typing.List[CreatePosition]] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        delivery_planned_moment: typing.Optional[datetime.datetime] = None,
        files: typing.Optional[list] = None,
        moves: typing.Optional[list] = None,
        purchase_orders: typing.Optional[list] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
    ):
        """
        :param organization: Organization (Организация)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий)
        :param group: Group (Группа)
        :param name: Name (Название)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param moment: Date (Дата)
        :param applicable: Applicable (Применимый)
        :param rate: Rate (Ставка)
        :param sum_: Sum (Сумма)
        :param store: Store (Склад)
        :param project: Project (Проект)
        :param state: State (Состояние)
        :param positions: Positions (Позиции)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param files: Files (Файлы)
        :param moves: Moves (Движения)
        :param purchase_orders: Purchase orders (Заказы на закупку)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)
        """
        self.organization = organization
        self.owner = owner
        self.shared = shared
        self.group = group
        self.name = name
        self.description = description
        self.external_code = external_code
        self.moment = moment
        self.applicable = applicable
        self.rate = rate
        self.sum = sum_
        self.store = store
        self.project = project
        self.state = state
        self.positions = positions
        self.attributes = attributes
        self.code = code
        self.delivery_planned_moment = delivery_planned_moment
        self.files = files
        self.moves = moves
        self.purchase_orders = purchase_orders
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included
        if positions:
            """
            Additional check for `positions` field.
            (Дополнительная проверка для поля `positions`)
            """
            if not isinstance(positions, list):
                raise ValueError("positions must be list")
            for position in positions:
                if not isinstance(position, dict):
                    raise ValueError("positions must be list of dict")
                for x in ["quantity", "price", "discount", "vat", "assortment"]:
                    if x not in position:
                        raise ValueError(f"Positions must contain {x}")

    def to_request(
        self,
    ) -> dict:
        if not self.organization:
            raise ValueError("organization is required")
        json_data = {"organization": {"meta": self.organization}}
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.shared is not None:
            json_data["shared"] = self.shared
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.name is not None:
            json_data["name"] = self.name
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.moment is not None:
            json_data["moment"] = self.moment
        if self.applicable is not None:
            json_data["applicable"] = self.applicable
        if self.rate is not None:
            json_data["rate"] = self.rate
        if self.sum is not None:
            json_data["sum"] = self.sum
        if self.store is not None:
            json_data["store"] = {"meta": self.store}
        if self.project is not None:
            json_data["project"] = {"meta": self.project}
        if self.state is not None:
            json_data["state"] = {"meta": self.state}
        if self.positions is not None:
            json_data["positions"] = []
            for i in self.positions:
                json_data["positions"].append(
                    {
                        "quantity": i["quantity"],
                        "price": i["price"],
                        "discount": i["discount"],
                        "vat": i["vat"],
                        "assortment": {"meta": i["assortment"]},
                    }
                )
        if self.attributes is not None:
            json_data["attributes"] = self.attributes
        if self.code is not None:
            json_data["code"] = self.code
        if self.delivery_planned_moment is not None:
            json_data["deliveryPlannedMoment"] = self.delivery_planned_moment
        if self.files is not None:
            json_data["files"] = self.files
        if self.moves is not None:
            json_data["moves"] = self.moves
        if self.purchase_orders is not None:
            json_data["purchaseOrders"] = self.purchase_orders
        if self.vat_enabled is not None:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included is not None:
            json_data["vatIncluded"] = self.vat_included
        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/internalorder",
            "json": json_data,
        }

    def from_response(self, response: dict) -> InternalOrder:
        return InternalOrder.from_json(response)


class GetInternalOrderRequest(types.ApiRequest):
    """
    Get Internal Order by its id
    Получить Внутренний заказ по его id

    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-vnutrennij-zakaz
    """

    def __init__(self, id_: str):
        """
        :param id_: Internal order ID (ID внутреннего заказа)
        """
        self.id = id_

    def to_request(
        self,
    ) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.id}",
        }

    def from_response(self, response: dict) -> InternalOrder:
        return InternalOrder.from_json(response)


class UpdateInternalOrderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-izmenit-vnutrennij-zakaz

    Update Internal Order by its id. Params are the same as for CreateInternalOrder, but add 'id' param.
    Обновить Внутренний заказ по его id. Параметры такие же, как у CreateInternalOrder, но добавляется параметр 'id'.
    """

    UpdatePosition = CreateInternalOrderRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: types.Meta = None,
        owner: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        group: typing.Optional[types.Meta] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        moment: typing.Optional[typing.Union[str, datetime.datetime]] = None,
        applicable: typing.Optional[bool] = None,
        rate: typing.Optional[types.Rate] = None,
        sum_: typing.Optional[int] = None,
        store: typing.Optional[types.Meta] = None,
        project: typing.Optional[types.Meta] = None,
        state: typing.Optional[types.Meta] = None,
        positions: typing.Optional[typing.List[UpdatePosition]] = None,
        attributes: typing.Optional[typing.List[dict]] = None,
        code: typing.Optional[str] = None,
        delivery_planned_moment: typing.Optional[datetime.datetime] = None,
        files: typing.Optional[list] = None,
        moves: typing.Optional[list] = None,
        purchase_orders: typing.Optional[list] = None,
        vat_enabled: typing.Optional[bool] = None,
        vat_included: typing.Optional[bool] = None,
    ):
        """
        :param id_: Internal order ID (ID внутреннего заказа)
        :param organization: Organization (Организация)
        :param owner: Owner (Владелец)
        :param shared: Shared (Общий)
        :param group: Group (Группа)
        :param name: Name (Название)
        :param description: Description (Описание)
        :param external_code: External code (Внешний код)
        :param moment: Date (Дата)
        :param applicable: Applicable (Применимый)
        :param rate: Rate (Ставка)
        :param sum_: Sum (Сумма)
        :param store: Store (Склад)
        :param project: Project (Проект)
        :param state: State (Состояние)
        :param positions: Positions (Позиции)
        :param attributes: Attributes (Атрибуты)
        :param code: Code (Код)
        :param delivery_planned_moment: Delivery planned moment (Планируемая дата доставки)
        :param files: Files (Файлы)
        :param moves: Moves (Движения)
        :param purchase_orders: Purchase orders (Заказы на закупку)
        :param vat_enabled: Vat enabled (НДС включен)
        :param vat_included: Vat included (НДС включен в цену)
        """
        self.id = id_
        self.organization = organization
        self.owner = owner
        self.shared = shared
        self.group = group
        self.name = name
        self.description = description
        self.external_code = external_code
        self.moment = moment
        self.applicable = applicable
        self.rate = rate
        self.sum = sum_
        self.store = store
        self.project = project
        self.state = state
        self.positions = positions
        self.attributes = attributes
        self.code = code
        self.delivery_planned_moment = delivery_planned_moment
        self.files = files
        self.moves = moves
        self.purchase_orders = purchase_orders
        self.vat_enabled = vat_enabled
        self.vat_included = vat_included
        if positions:
            """
            Additional check for `positions` field.
            (Дополнительная проверка для поля `positions`)
            """
            if not isinstance(positions, list):
                raise ValueError("positions must be list")
            for position in positions:
                if not isinstance(position, dict):
                    raise ValueError("positions must be list of dict")
                for x in ["quantity", "price", "discount", "vat", "assortment"]:
                    if x not in position:
                        raise ValueError(f"Positions must contain {x}")

    def to_request(
        self,
    ) -> dict:
        json_data = {}
        if self.organization is not None:
            json_data["organization"] = {"meta": self.organization}
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.shared is not None:
            json_data["shared"] = self.shared
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.name is not None:
            json_data["name"] = self.name
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.moment is not None:
            json_data["moment"] = self.moment
        if self.applicable is not None:
            json_data["applicable"] = self.applicable
        if self.rate is not None:
            json_data["rate"] = self.rate
        if self.sum is not None:
            json_data["sum"] = self.sum
        if self.store is not None:
            json_data["store"] = {"meta": self.store}
        if self.project is not None:
            json_data["project"] = {"meta": self.project}
        if self.state is not None:
            json_data["state"] = {"meta": self.state}
        if self.positions is not None:
            json_data["positions"] = []
            for i in self.positions:
                json_data["positions"].append(
                    {
                        "quantity": i["quantity"],
                        "price": i["price"],
                        "discount": i["discount"],
                        "vat": i["vat"],
                        "assortment": {"meta": i["assortment"]},
                    }
                )
        if self.attributes is not None:
            json_data["attributes"] = self.attributes
        if self.code is not None:
            json_data["code"] = self.code
        if self.delivery_planned_moment is not None:
            json_data["deliveryPlannedMoment"] = self.delivery_planned_moment
        if self.files is not None:
            json_data["files"] = self.files
        if self.moves is not None:
            json_data["moves"] = self.moves
        if self.purchase_orders is not None:
            json_data["purchaseOrders"] = self.purchase_orders
        if self.vat_enabled is not None:
            json_data["vatEnabled"] = self.vat_enabled
        if self.vat_included is not None:
            json_data["vatIncluded"] = self.vat_included
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.id}",
            "json": json_data,
        }

    def from_response(self, response: dict) -> InternalOrder:
        return InternalOrder.from_json(response)


class GetOrderPositionsRequest(types.ApiRequest):
    """
    Get all positions of the order by its id
    Получить все позиции заказа по его id

    # https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-pozicii-vnutrennego-zakaza
    """

    def __init__(
        self,
        id_: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
    ):
        """
        :param id_: Internal order ID (ID внутреннего заказа)
        :param limit: Limit (Ограничение)
        :param offset: Offset (Смещение)
        :param search: Search (Поиск)
        """
        self.id = id_
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(
        self,
    ) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        if self.search is not None:
            params["search"] = self.search

        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.id}/positions",
            "params": params,
        }

    def from_response(self, response: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in response["rows"]]


class AddOrderPositionsRequest(types.ApiRequest):
    AddPosition = CreateInternalOrderRequest.CreatePosition
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-pozicii-vnutrennego-zakaza

    Add positions to order by its id and positions list
    Добавить позиции в заказ по его id и списку позиций
    """

    def __init__(
        self,
        id_: str,
        positions: typing.List[AddPosition],
    ):
        """

        :param id_: Internal order ID (ID внутреннего заказа)
        :param positions: Positions (Позиции, которые нужно добавить)
        """
        self.id = id_
        self.positions = positions
        if not isinstance(positions, list) or len(positions) == 0:
            raise ValueError("positions must be list with at least one element")
        for position in positions:
            if not isinstance(position, dict):
                raise ValueError("positions must be list of dict")
            for x in ["quantity", "price", "discount", "vat", "assortment"]:
                if x not in position:
                    raise ValueError(f"Positions must contain {x}")

    def to_request(
        self,
    ) -> dict:
        json_data = []
        for i in self.positions:
            json_data.append(
                {
                    "quantity": i["quantity"],
                    "price": i["price"],
                    "discount": i["discount"],
                    "vat": i["vat"],
                    "assortment": {"meta": i["assortment"]},
                }
            )
        return {
            "method": "POST",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.id}/positions",
            "json": json_data,
        }

    def from_response(self, response: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in response]


class DeleteOrderPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-udalit-poziciu-vnutrennego-zakaza

    Delete position by its id from order by order and positions id
    Удалить позицию по ее id из заказа по id заказа и позиции
    """

    def __init__(
        self,
        order_id: str,
        position_id: str,
    ):
        """
        :param order_id: Internal order ID (ID внутреннего заказа)
        :param position_id: Position ID (ID позиции)
        """
        self.order_id = order_id
        self.position_id = position_id

    def to_request(
        self,
    ) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.order_id}/positions/{self.position_id}",
            "allow_non_json": True,  # this endpoint returns empty body (octet-stream)
            "json": {},
        }

    def from_response(self, response: dict) -> None:
        # This API request returns nothing (Этот запрос ничего не возвращает)
        return None


class GetOrderPositionRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-poziciu

    Get position by its id from order by order and positions id
    Получить позицию по ее id из заказа по id заказа и позиции
    """

    def __init__(
        self,
        order_id: str,
        position_id: str,
    ):
        """

        :param order_id: order id (id заказа)
        :param position_id: position id (id позиции)
        """
        self.order_id = order_id
        self.position_id = position_id

    def to_request(
        self,
    ) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.order_id}/positions/{self.position_id}",
        }

    def from_response(self, response: dict) -> Position:
        return Position.from_json(response)

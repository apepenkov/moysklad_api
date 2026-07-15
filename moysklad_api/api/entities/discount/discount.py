# Скидки (discount) - неоднородная сущность из 3 подтипов: накопительная скидка
# (accumulationdiscount), персональная скидка (personaldiscount) и специальная
# цена (specialpricediscount). Также сюда относится "округление копеек" -
# системная сущность с типом discount, доступная только для чтения/изменения.
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Discount(types.MoySkladBaseClass):
    """
    Обобщенное представление скидки, как она приходит в общем списке
    "Получить все скидки" (может быть любым из 3 подтипов, либо
    системным округлением копеек).

    accountId      | UUID          | ID учетной записи. Обязательное при ответе, Только для чтения
    active         | Boolean       | Индикатор, является ли скидка активной. Обязательное при ответе
    agentTags      | Array(String) | Тэги контрагентов, к которым применяется скидка
    allAgents      | Boolean       | Индикатор, действует ли скидка на всех контрагентов
    allProducts    | Boolean       | Индикатор, действует ли скидка на все товары
    assortment     | Array(Object) | Товары и услуги, к которым применяется скидка
    productFolders | Array(Object) | Группы товаров, к которым применяется скидка
    discount       | Float         | Процент скидки (специальная цена, фиксированный процент)
    specialPrice   | Object        | Спец. цена: {"value": Int, "priceType": Meta}
    levels         | Array(Object) | Проценты скидок при определенной сумме продаж (накопительная скидка)
    usePriceType   | Boolean       | Использовать ли тип цен вместо процента (специальная цена)
    id             | UUID          | ID Скидки. Обязательное при ответе, Только для чтения
    meta           | Meta          | Метаданные Скидки. Обязательное при ответе
    name           | String(255)   | Наименование Скидки. Обязательное при ответе
    """

    account_id: typing.Optional[str]
    active: typing.Optional[bool]
    agent_tags: typing.Optional[typing.List[str]]
    all_agents: typing.Optional[bool]
    all_products: typing.Optional[bool]
    assortment: typing.Optional[typing.List[dict]]
    product_folders: typing.Optional[typing.List[dict]]
    discount: typing.Optional[float]
    special_price: typing.Optional[dict]
    levels: typing.Optional[typing.List[dict]]
    use_price_type: typing.Optional[bool]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Discount":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.active = dict_data.get("active")
        instance.agent_tags = dict_data.get("agentTags")
        instance.all_agents = dict_data.get("allAgents")
        instance.all_products = dict_data.get("allProducts")
        instance.assortment = dict_data.get("assortment")
        instance.product_folders = dict_data.get("productFolders")
        instance.discount = dict_data.get("discount")
        instance.special_price = dict_data.get("specialPrice")
        instance.levels = dict_data.get("levels")
        instance.use_price_type = dict_data.get("usePriceType")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("discount",)


class GetDiscountsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
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
            url=f"{helpers.BASE_URL}/entity/discount",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Discount]:
        return [Discount.from_json(x) for x in result["rows"]]


class UpdateRoundingDiscountRequest(types.ApiRequest):
    """Изменить округление копеек (системная скидка типа discount)."""

    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        active: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.name = name
        self.active = active

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.active != Unset:
            json_data["active"] = self.active
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/discount/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Discount:
        return Discount.from_json(result)


class AccumulationDiscount(types.MoySkladBaseClass):
    """
    Накопительная скидка. entity/accumulationdiscount
    id, meta, accountId, name, active, allProducts, allAgents, agentTags,
    assortment, productFolders, levels (Array({"amount": Int, "discount": Float}))
    """

    account_id: typing.Optional[str]
    active: typing.Optional[bool]
    agent_tags: typing.Optional[typing.List[str]]
    all_agents: typing.Optional[bool]
    all_products: typing.Optional[bool]
    assortment: typing.Optional[typing.List[dict]]
    product_folders: typing.Optional[typing.List[dict]]
    levels: typing.Optional[typing.List[dict]]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "AccumulationDiscount":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.active = dict_data.get("active")
        instance.agent_tags = dict_data.get("agentTags")
        instance.all_agents = dict_data.get("allAgents")
        instance.all_products = dict_data.get("allProducts")
        instance.assortment = dict_data.get("assortment")
        instance.product_folders = dict_data.get("productFolders")
        instance.levels = dict_data.get("levels")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("accumulationdiscount",)


class CreateAccumulationDiscountRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        active: bool,
        all_products: bool,
        all_agents: bool,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        assortment: typing.Union[Unset, typing.List[dict]] = Unset,
        product_folders: typing.Union[Unset, typing.List[dict]] = Unset,
        levels: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.name = name
        self.active = active
        self.all_products = all_products
        self.all_agents = all_agents
        self.agent_tags = agent_tags
        self.assortment = assortment
        self.product_folders = product_folders
        self.levels = levels

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
            "active": self.active,
            "allProducts": self.all_products,
            "allAgents": self.all_agents,
        }
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.assortment != Unset:
            json_data["assortment"] = self.assortment
        if self.product_folders != Unset:
            json_data["productFolders"] = self.product_folders
        if self.levels != Unset:
            json_data["levels"] = self.levels
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/accumulationdiscount",
            json=json_data,
        )

    def from_response(self, result: dict) -> AccumulationDiscount:
        return AccumulationDiscount.from_json(result)


class GetAccumulationDiscountRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/accumulationdiscount/{self.id}",
        )

    def from_response(self, result: dict) -> AccumulationDiscount:
        return AccumulationDiscount.from_json(result)


class UpdateAccumulationDiscountRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        active: typing.Union[Unset, bool] = Unset,
        all_products: typing.Union[Unset, bool] = Unset,
        all_agents: typing.Union[Unset, bool] = Unset,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        assortment: typing.Union[Unset, typing.List[dict]] = Unset,
        product_folders: typing.Union[Unset, typing.List[dict]] = Unset,
        levels: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.id = id_
        self.name = name
        self.active = active
        self.all_products = all_products
        self.all_agents = all_agents
        self.agent_tags = agent_tags
        self.assortment = assortment
        self.product_folders = product_folders
        self.levels = levels

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.active != Unset:
            json_data["active"] = self.active
        if self.all_products != Unset:
            json_data["allProducts"] = self.all_products
        if self.all_agents != Unset:
            json_data["allAgents"] = self.all_agents
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.assortment != Unset:
            json_data["assortment"] = self.assortment
        if self.product_folders != Unset:
            json_data["productFolders"] = self.product_folders
        if self.levels != Unset:
            json_data["levels"] = self.levels
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/accumulationdiscount/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> AccumulationDiscount:
        return AccumulationDiscount.from_json(result)


class DeleteAccumulationDiscountRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/accumulationdiscount/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class PersonalDiscount(types.MoySkladBaseClass):
    """
    Персональная скидка. entity/personaldiscount
    id, meta, accountId, name, active, allProducts, allAgents, agentTags,
    assortment, productFolders, discount (Float, процент скидки)
    """

    account_id: typing.Optional[str]
    active: typing.Optional[bool]
    agent_tags: typing.Optional[typing.List[str]]
    all_agents: typing.Optional[bool]
    all_products: typing.Optional[bool]
    assortment: typing.Optional[typing.List[dict]]
    product_folders: typing.Optional[typing.List[dict]]
    discount: typing.Optional[float]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "PersonalDiscount":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.active = dict_data.get("active")
        instance.agent_tags = dict_data.get("agentTags")
        instance.all_agents = dict_data.get("allAgents")
        instance.all_products = dict_data.get("allProducts")
        instance.assortment = dict_data.get("assortment")
        instance.product_folders = dict_data.get("productFolders")
        instance.discount = dict_data.get("discount")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("personaldiscount",)


class CreatePersonalDiscountRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        active: bool,
        all_products: bool,
        all_agents: bool,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        assortment: typing.Union[Unset, typing.List[dict]] = Unset,
        product_folders: typing.Union[Unset, typing.List[dict]] = Unset,
        discount: typing.Union[Unset, float] = Unset,
    ):
        self.name = name
        self.active = active
        self.all_products = all_products
        self.all_agents = all_agents
        self.agent_tags = agent_tags
        self.assortment = assortment
        self.product_folders = product_folders
        self.discount = discount

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
            "active": self.active,
            "allProducts": self.all_products,
            "allAgents": self.all_agents,
        }
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.assortment != Unset:
            json_data["assortment"] = self.assortment
        if self.product_folders != Unset:
            json_data["productFolders"] = self.product_folders
        if self.discount != Unset:
            json_data["discount"] = self.discount
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/personaldiscount",
            json=json_data,
        )

    def from_response(self, result: dict) -> PersonalDiscount:
        return PersonalDiscount.from_json(result)


class GetPersonalDiscountRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/personaldiscount/{self.id}",
        )

    def from_response(self, result: dict) -> PersonalDiscount:
        return PersonalDiscount.from_json(result)


class UpdatePersonalDiscountRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        active: typing.Union[Unset, bool] = Unset,
        all_products: typing.Union[Unset, bool] = Unset,
        all_agents: typing.Union[Unset, bool] = Unset,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        assortment: typing.Union[Unset, typing.List[dict]] = Unset,
        product_folders: typing.Union[Unset, typing.List[dict]] = Unset,
        discount: typing.Union[Unset, float] = Unset,
    ):
        self.id = id_
        self.name = name
        self.active = active
        self.all_products = all_products
        self.all_agents = all_agents
        self.agent_tags = agent_tags
        self.assortment = assortment
        self.product_folders = product_folders
        self.discount = discount

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.active != Unset:
            json_data["active"] = self.active
        if self.all_products != Unset:
            json_data["allProducts"] = self.all_products
        if self.all_agents != Unset:
            json_data["allAgents"] = self.all_agents
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.assortment != Unset:
            json_data["assortment"] = self.assortment
        if self.product_folders != Unset:
            json_data["productFolders"] = self.product_folders
        if self.discount != Unset:
            json_data["discount"] = self.discount
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/personaldiscount/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> PersonalDiscount:
        return PersonalDiscount.from_json(result)


class DeletePersonalDiscountRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/personaldiscount/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class SpecialPriceDiscount(types.MoySkladBaseClass):
    """
    Специальная цена. entity/specialpricediscount
    id, meta, accountId, name, active, allProducts, allAgents, agentTags,
    assortment, productFolders, usePriceType (Boolean),
    specialPrice (Object: {"value": Int, "priceType": Meta})
    """

    account_id: typing.Optional[str]
    active: typing.Optional[bool]
    agent_tags: typing.Optional[typing.List[str]]
    all_agents: typing.Optional[bool]
    all_products: typing.Optional[bool]
    assortment: typing.Optional[typing.List[dict]]
    product_folders: typing.Optional[typing.List[dict]]
    use_price_type: typing.Optional[bool]
    special_price: typing.Optional[dict]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]

    @classmethod
    def from_json(cls, dict_data: dict) -> "SpecialPriceDiscount":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.active = dict_data.get("active")
        instance.agent_tags = dict_data.get("agentTags")
        instance.all_agents = dict_data.get("allAgents")
        instance.all_products = dict_data.get("allProducts")
        instance.assortment = dict_data.get("assortment")
        instance.product_folders = dict_data.get("productFolders")
        instance.use_price_type = dict_data.get("usePriceType")
        instance.special_price = dict_data.get("specialPrice")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("specialpricediscount",)


class CreateSpecialPriceDiscountRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        active: bool,
        all_products: bool,
        all_agents: bool,
        use_price_type: bool,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        assortment: typing.Union[Unset, typing.List[dict]] = Unset,
        product_folders: typing.Union[Unset, typing.List[dict]] = Unset,
        special_price: typing.Union[Unset, dict] = Unset,
    ):
        self.name = name
        self.active = active
        self.all_products = all_products
        self.all_agents = all_agents
        self.use_price_type = use_price_type
        self.agent_tags = agent_tags
        self.assortment = assortment
        self.product_folders = product_folders
        self.special_price = special_price

    def to_request(self) -> RequestData:
        json_data = {
            "name": self.name,
            "active": self.active,
            "allProducts": self.all_products,
            "allAgents": self.all_agents,
            "usePriceType": self.use_price_type,
        }
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.assortment != Unset:
            json_data["assortment"] = self.assortment
        if self.product_folders != Unset:
            json_data["productFolders"] = self.product_folders
        if self.special_price != Unset:
            json_data["specialPrice"] = self.special_price
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/specialpricediscount",
            json=json_data,
        )

    def from_response(self, result: dict) -> SpecialPriceDiscount:
        return SpecialPriceDiscount.from_json(result)


class GetSpecialPriceDiscountRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/specialpricediscount/{self.id}",
        )

    def from_response(self, result: dict) -> SpecialPriceDiscount:
        return SpecialPriceDiscount.from_json(result)


class UpdateSpecialPriceDiscountRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        active: typing.Union[Unset, bool] = Unset,
        all_products: typing.Union[Unset, bool] = Unset,
        all_agents: typing.Union[Unset, bool] = Unset,
        use_price_type: typing.Union[Unset, bool] = Unset,
        agent_tags: typing.Union[Unset, typing.List[str]] = Unset,
        assortment: typing.Union[Unset, typing.List[dict]] = Unset,
        product_folders: typing.Union[Unset, typing.List[dict]] = Unset,
        special_price: typing.Union[Unset, dict] = Unset,
    ):
        self.id = id_
        self.name = name
        self.active = active
        self.all_products = all_products
        self.all_agents = all_agents
        self.use_price_type = use_price_type
        self.agent_tags = agent_tags
        self.assortment = assortment
        self.product_folders = product_folders
        self.special_price = special_price

    def to_request(self) -> RequestData:
        json_data = {}
        if self.name != Unset:
            json_data["name"] = self.name
        if self.active != Unset:
            json_data["active"] = self.active
        if self.all_products != Unset:
            json_data["allProducts"] = self.all_products
        if self.all_agents != Unset:
            json_data["allAgents"] = self.all_agents
        if self.use_price_type != Unset:
            json_data["usePriceType"] = self.use_price_type
        if self.agent_tags != Unset:
            json_data["agentTags"] = self.agent_tags
        if self.assortment != Unset:
            json_data["assortment"] = self.assortment
        if self.product_folders != Unset:
            json_data["productFolders"] = self.product_folders
        if self.special_price != Unset:
            json_data["specialPrice"] = self.special_price
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/specialpricediscount/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> SpecialPriceDiscount:
        return SpecialPriceDiscount.from_json(result)


class DeleteSpecialPriceDiscountRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/specialpricediscount/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

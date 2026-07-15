import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Variant(types.MoySkladBaseClass):
    """
    accountId          | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived           | Boolean     | Добавлен ли товар в архив. Обязательное при ответе
    article            | String(255) | Артикул модификации
    barcodes           | Array(Object)| Штрихкоды модификации
    buyPrice           | Object      | Закупочная цена
    characteristics    | Array(Object)| Характеристики Модификации. Обязательное при ответе, Необходимо при создании
    code               | String(255) | Код Модификации
    description        | String(4096)| Описание Модификации
    discountProhibited | Boolean     | Признак запрета скидок. Обязательное при ответе
    externalCode       | String(255) | Внешний код Модификации. Обязательное при ответе
    id                  | UUID        | ID Модификации. Обязательное при ответе, Только для чтения
    images              | MetaArray   | Изображения. Обязательное при ответе, Expand
    meta                | Meta        | Метаданные Модификации. Обязательное при ответе
    minPrice            | Object      | Минимальная цена
    minimumStock        | Object      | Неснижаемый остаток (по запросу fields=minimumStock)
    name                | String(255) | Наименование товара с Модификацией. Обязательное при ответе
    packs                | Array(Object)| Упаковки модификации
    product               | Meta        | Метаданные товара. Обязательное при ответе, Необходимо при создании, Expand
    salePrices            | Array(Object)| Цены продажи
    things                | Array(String)| Серийные номера. Только для чтения
    updated                | DateTime    | Момент последнего обновления. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    article: typing.Optional[str]
    barcodes: typing.Optional[typing.List[dict]]
    buy_price: typing.Optional[dict]
    characteristics: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    description: typing.Optional[str]
    discount_prohibited: typing.Optional[bool]
    external_code: typing.Optional[str]
    id: typing.Optional[str]
    images: typing.Optional[dict]
    meta: typing.Optional[types.Meta]
    min_price: typing.Optional[dict]
    minimum_stock: typing.Optional[dict]
    name: typing.Optional[str]
    packs: typing.Optional[typing.List[dict]]
    product: typing.Optional[types.Meta]
    sale_prices: typing.Optional[typing.List[dict]]
    things: typing.Optional[typing.List[str]]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Variant":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.article = dict_data.get("article")
        instance.barcodes = dict_data.get("barcodes")
        instance.buy_price = dict_data.get("buyPrice")
        instance.characteristics = dict_data.get("characteristics")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.discount_prohibited = dict_data.get("discountProhibited")
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.images = dict_data.get("images")
        instance.meta = dict_data.get("meta")
        instance.min_price = dict_data.get("minPrice")
        instance.minimum_stock = dict_data.get("minimumStock")
        instance.name = dict_data.get("name")
        instance.packs = dict_data.get("packs")
        instance.product = helpers.get_meta(dict_data.get("product"))
        instance.sale_prices = dict_data.get("salePrices")
        instance.things = dict_data.get("things")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("variant",)


def _build_variant_json(
    product: typing.Union[Unset, types.Meta] = Unset,
    characteristics: typing.Union[Unset, typing.List[dict]] = Unset,
    name: typing.Union[Unset, str] = Unset,
    archived: typing.Union[Unset, bool] = Unset,
    article: typing.Union[Unset, str] = Unset,
    barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
    buy_price: typing.Union[Unset, dict] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    discount_prohibited: typing.Union[Unset, bool] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    images: typing.Union[Unset, typing.List[dict]] = Unset,
    min_price: typing.Union[Unset, dict] = Unset,
    minimum_stock: typing.Union[Unset, dict] = Unset,
    packs: typing.Union[Unset, typing.List[dict]] = Unset,
    sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
) -> dict:
    json_data = {}
    if product != Unset:
        json_data["product"] = {"meta": product}
    if characteristics != Unset:
        json_data["characteristics"] = characteristics
    if name != Unset:
        json_data["name"] = name
    if archived != Unset:
        json_data["archived"] = archived
    if article != Unset:
        json_data["article"] = article
    if barcodes != Unset:
        json_data["barcodes"] = barcodes
    if buy_price != Unset:
        json_data["buyPrice"] = buy_price
    if code != Unset:
        json_data["code"] = code
    if description != Unset:
        json_data["description"] = description
    if discount_prohibited != Unset:
        json_data["discountProhibited"] = discount_prohibited
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if images != Unset:
        json_data["images"] = images
    if min_price != Unset:
        json_data["minPrice"] = min_price
    if minimum_stock != Unset:
        json_data["minimumStock"] = minimum_stock
    if packs != Unset:
        json_data["packs"] = packs
    if sale_prices != Unset:
        json_data["salePrices"] = sale_prices
    return json_data


class GetVariantsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/variant",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Variant]:
        return [Variant.from_json(x) for x in result["rows"]]


class CreateVariantRequest(types.ApiRequest):
    def __init__(
        self,
        product: types.Meta,
        characteristics: typing.List[dict],
        name: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        article: typing.Union[Unset, str] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        buy_price: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        images: typing.Union[Unset, typing.List[dict]] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        minimum_stock: typing.Union[Unset, dict] = Unset,
        packs: typing.Union[Unset, typing.List[dict]] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.product = product
        self.characteristics = characteristics
        self.name = name
        self.archived = archived
        self.article = article
        self.barcodes = barcodes
        self.buy_price = buy_price
        self.code = code
        self.description = description
        self.discount_prohibited = discount_prohibited
        self.external_code = external_code
        self.images = images
        self.min_price = min_price
        self.minimum_stock = minimum_stock
        self.packs = packs
        self.sale_prices = sale_prices

    def to_request(self) -> RequestData:
        json_data = _build_variant_json(
            product=self.product,
            characteristics=self.characteristics,
            name=self.name,
            archived=self.archived,
            article=self.article,
            barcodes=self.barcodes,
            buy_price=self.buy_price,
            code=self.code,
            description=self.description,
            discount_prohibited=self.discount_prohibited,
            external_code=self.external_code,
            images=self.images,
            min_price=self.min_price,
            minimum_stock=self.minimum_stock,
            packs=self.packs,
            sale_prices=self.sale_prices,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/variant",
            json=json_data,
        )

    def from_response(self, result: dict) -> Variant:
        return Variant.from_json(result)


class DeleteVariantRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/variant/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetVariantRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/variant/{self.id}",
        )

    def from_response(self, result: dict) -> Variant:
        return Variant.from_json(result)


class UpdateVariantRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        product: typing.Union[Unset, types.Meta] = Unset,
        characteristics: typing.Union[Unset, typing.List[dict]] = Unset,
        name: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        article: typing.Union[Unset, str] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        buy_price: typing.Union[Unset, dict] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        discount_prohibited: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        images: typing.Union[Unset, typing.List[dict]] = Unset,
        min_price: typing.Union[Unset, dict] = Unset,
        minimum_stock: typing.Union[Unset, dict] = Unset,
        packs: typing.Union[Unset, typing.List[dict]] = Unset,
        sale_prices: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.id = id_
        self.product = product
        self.characteristics = characteristics
        self.name = name
        self.archived = archived
        self.article = article
        self.barcodes = barcodes
        self.buy_price = buy_price
        self.code = code
        self.description = description
        self.discount_prohibited = discount_prohibited
        self.external_code = external_code
        self.images = images
        self.min_price = min_price
        self.minimum_stock = minimum_stock
        self.packs = packs
        self.sale_prices = sale_prices

    def to_request(self) -> RequestData:
        json_data = _build_variant_json(
            product=self.product,
            characteristics=self.characteristics,
            name=self.name,
            archived=self.archived,
            article=self.article,
            barcodes=self.barcodes,
            buy_price=self.buy_price,
            code=self.code,
            description=self.description,
            discount_prohibited=self.discount_prohibited,
            external_code=self.external_code,
            images=self.images,
            min_price=self.min_price,
            minimum_stock=self.minimum_stock,
            packs=self.packs,
            sale_prices=self.sale_prices,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/variant/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Variant:
        return Variant.from_json(result)

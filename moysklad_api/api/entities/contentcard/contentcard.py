import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ContentCard(types.MoySkladBaseClass):
    """
    accountId       | UUID          | ID учетной записи. Обязательное при ответе, Только для чтения
    assortment      | Meta          | Метаданные Ассортимента. Обязательное при ответе, Необходимо при создании, Expand, После создания недоступно для изменения
    cardContentName | String(255)   | Как карточка отображается в списке на UI. Обязательное при ответе, Необходимо при создании
    description     | String(10000) | Описание товара или услуги. Обязательное при ответе, Необходимо при создании
    id              | UUID          | ID Карточки контента. Обязательное при ответе, Только для чтения
    meta            | Meta          | Метаданные Карточки контента. Обязательное при ответе
    name            | String(255)   | Название товара или услуги. Обязательное при ответе, Необходимо при создании
    salePlatform    | Meta          | Метаданные Площадки для продаж. Обязательное при ответе, Необходимо при создании, Expand
    salesChannels   | Array(Object) | Ссылки на каналы продаж. Обязательное при ответе, Необходимо при создании, Expand
    images          | MetaArray     | Изображения. Expand
    """

    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    card_content_name: typing.Optional[str]
    description: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    sale_platform: typing.Optional[types.Meta]
    sales_channels: typing.Optional[typing.List[dict]]
    images: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ContentCard":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.card_content_name = dict_data.get("cardContentName")
        instance.description = dict_data.get("description")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.sale_platform = helpers.get_meta(dict_data.get("salePlatform"))
        instance.sales_channels = dict_data.get("salesChannels")
        instance.images = dict_data.get("images")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("contentcard",)


def _build_contentcard_json(
    assortment: typing.Union[Unset, types.Meta] = Unset,
    card_content_name: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    name: typing.Union[Unset, str] = Unset,
    sale_platform: typing.Union[Unset, types.Meta] = Unset,
    sales_channels: typing.Union[Unset, typing.List[types.Meta]] = Unset,
) -> dict:
    json_data = {}
    if assortment != Unset:
        json_data["assortment"] = {"meta": assortment}
    if card_content_name != Unset:
        json_data["cardContentName"] = card_content_name
    if description != Unset:
        json_data["description"] = description
    if name != Unset:
        json_data["name"] = name
    if sale_platform != Unset:
        json_data["salePlatform"] = {"meta": sale_platform}
    if sales_channels != Unset:
        json_data["salesChannels"] = [{"meta": m} for m in sales_channels]
    return json_data


class GetContentCardsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/contentcard",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ContentCard]:
        return [ContentCard.from_json(x) for x in result["rows"]]


class CreateContentCardRequest(types.ApiRequest):
    def __init__(
        self,
        assortment: types.Meta,
        card_content_name: str,
        description: str,
        name: str,
        sale_platform: types.Meta,
        sales_channels: typing.List[types.Meta],
    ):
        self.assortment = assortment
        self.card_content_name = card_content_name
        self.description = description
        self.name = name
        self.sale_platform = sale_platform
        self.sales_channels = sales_channels

    def to_request(self) -> RequestData:
        json_data = _build_contentcard_json(
            assortment=self.assortment,
            card_content_name=self.card_content_name,
            description=self.description,
            name=self.name,
            sale_platform=self.sale_platform,
            sales_channels=self.sales_channels,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/contentcard",
            json=json_data,
        )

    def from_response(self, result: dict) -> ContentCard:
        return ContentCard.from_json(result)


class DeleteContentCardRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/contentcard/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetContentCardRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/contentcard/{self.id}",
        )

    def from_response(self, result: dict) -> ContentCard:
        return ContentCard.from_json(result)


class UpdateContentCardRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        card_content_name: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        name: typing.Union[Unset, str] = Unset,
        sale_platform: typing.Union[Unset, types.Meta] = Unset,
        sales_channels: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    ):
        self.id = id_
        self.card_content_name = card_content_name
        self.description = description
        self.name = name
        self.sale_platform = sale_platform
        self.sales_channels = sales_channels

    def to_request(self) -> RequestData:
        json_data = _build_contentcard_json(
            card_content_name=self.card_content_name,
            description=self.description,
            name=self.name,
            sale_platform=self.sale_platform,
            sales_channels=self.sales_channels,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/contentcard/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ContentCard:
        return ContentCard.from_json(result)

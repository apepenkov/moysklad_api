import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Consignment(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived     | Boolean     | Добавлена ли партия в архив. Обязательное при ответе
    attributes   | Array(Object)| Коллекция доп. полей Партии
    assortment   | Meta        | Метаданные товара/услуги/комплекта. Обязательное при ответе, Необходимо при создании, Expand
    barcodes     | Array(Object)| Штрихкоды партии
    code         | String(255) | Код Партии
    description  | String(4096)| Описание Партии
    expiryDate   | DateTime    | Срок годности Партии. Необходимо при создании (или label)
    externalCode | String(255) | Внешний код Партии. Обязательное при ответе
    id           | UUID        | ID Партии. Обязательное при ответе, Только для чтения
    images       | MetaArray   | Изображения товара, к которому относится партия. Только для чтения
    label        | String(255) | Метка Партии. Необходимо при создании (или expiryDate)
    meta         | Meta        | Метаданные Партии. Обязательное при ответе
    name         | String(255) | Наименование Партии. Обязательное при ответе, Только для чтения
    updated      | DateTime    | Момент последнего обновления сущности. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    assortment: typing.Optional[types.Meta]
    barcodes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    description: typing.Optional[str]
    expiry_date: typing.Optional[datetime.datetime]
    external_code: typing.Optional[str]
    id: typing.Optional[str]
    images: typing.Optional[dict]
    label: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Consignment":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.attributes = dict_data.get("attributes")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.barcodes = dict_data.get("barcodes")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.expiry_date = helpers.parse_date(dict_data.get("expiryDate"))
        instance.external_code = dict_data.get("externalCode")
        instance.id = dict_data.get("id")
        instance.images = dict_data.get("images")
        instance.label = dict_data.get("label")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("consignment",)


class GetConsignmentsRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/consignment",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Consignment]:
        return [Consignment.from_json(x) for x in result["rows"]]


class CreateConsignmentRequest(types.ApiRequest):
    def __init__(
        self,
        assortment: types.Meta,
        label: typing.Union[Unset, str] = Unset,
        expiry_date: typing.Union[Unset, datetime.datetime] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.assortment = assortment
        self.label = label
        self.expiry_date = expiry_date
        self.barcodes = barcodes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.archived = archived
        self.attributes = attributes

    def to_request(self) -> RequestData:
        json_data = {"assortment": {"meta": self.assortment}}
        if self.label != Unset:
            json_data["label"] = self.label
        if self.expiry_date != Unset:
            json_data["expiryDate"] = helpers.date_to_str(self.expiry_date)
        if self.barcodes != Unset:
            json_data["barcodes"] = self.barcodes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/consignment",
            json=json_data,
        )

    def from_response(self, result: dict) -> Consignment:
        return Consignment.from_json(result)


class DeleteConsignmentRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/consignment/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetConsignmentRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/consignment/{self.id}",
        )

    def from_response(self, result: dict) -> Consignment:
        return Consignment.from_json(result)


class UpdateConsignmentRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        label: typing.Union[Unset, str] = Unset,
        expiry_date: typing.Union[Unset, datetime.datetime] = Unset,
        barcodes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    ):
        self.id = id_
        self.assortment = assortment
        self.label = label
        self.expiry_date = expiry_date
        self.barcodes = barcodes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.archived = archived
        self.attributes = attributes

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.label != Unset:
            json_data["label"] = self.label
        if self.expiry_date != Unset:
            json_data["expiryDate"] = helpers.date_to_str(self.expiry_date)
        if self.barcodes != Unset:
            json_data["barcodes"] = self.barcodes
        if self.code != Unset:
            json_data["code"] = self.code
        if self.description != Unset:
            json_data["description"] = self.description
        if self.external_code != Unset:
            json_data["externalCode"] = self.external_code
        if self.archived != Unset:
            json_data["archived"] = self.archived
        if self.attributes != Unset:
            json_data["attributes"] = self.attributes
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/consignment/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Consignment:
        return Consignment.from_json(result)

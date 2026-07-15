# Печать этикеток и ценников (labels) - action-запрос, а не CRUD-сущность.
# ВНИМАНИЕ: ответ сервера не содержит JSON тела - готовый файл (или статус
# готовности) отдается через заголовок `Location` (коды 303/202). Поэтому
# `from_response` этого запроса всегда возвращает None; чтобы получить
# реальный URL файла, нужно выполнить `client.raw_request(**request.to_request().to_kwargs())`
# и прочитать заголовок `Location` из ответа напрямую.
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class PrintLabelsRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        organization: types.Meta,
        count: int,
        price_type: types.Meta,
        template: types.Meta,
    ):
        """
        :param entity_type: Тип сущности (product, service, bundle, variant)
        :param entity_id: ID сущности, для которой запрашивается печать
        :param organization: Метаданные Юрлица
        :param count: Количество ценников/этикеток (макс. 1000)
        :param price_type: Метаданные типа цены (salePrice.priceType)
        :param template: Метаданные Шаблона печати
        """
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.organization = organization
        self.count = count
        self.price_type = price_type
        self.template = template

    def to_request(self) -> RequestData:
        json_data = {
            "organization": {"meta": self.organization},
            "count": self.count,
            "salePrice": {"priceType": {"meta": self.price_type}},
            "template": {"meta": self.template},
        }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/export",
            json=json_data,
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

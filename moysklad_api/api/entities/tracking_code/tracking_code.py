# Коды маркировки (trackingCodes) - вложенная сущность позиции документа.
# Общий путь: /entity/{entityType}/{entityId}/positions/{positionId}/trackingCodes
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class TrackingCode(types.MoySkladBaseClass):
    """
    id             | UUID          | ID кода маркировки. Только для чтения
    cis            | String        | Код маркировки в стандартном формате. Необходимо при создании
    cis_1162       | String        | Код маркировки в формате тега 1162. Только для чтения
    type           | String        | Тип кода маркировки. Необходимо при создании
    trackingCodes  | Array(Object) | Массив вложенных кодов маркировки
    """

    id: typing.Optional[str]
    cis: typing.Optional[str]
    cis_1162: typing.Optional[str]
    type: typing.Optional[str]
    tracking_codes: typing.Optional[typing.List[dict]]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TrackingCode":
        instance = cls()
        instance.id = dict_data.get("id")
        instance.cis = dict_data.get("cis")
        instance.cis_1162 = dict_data.get("cis_1162")
        instance.type = dict_data.get("type")
        instance.tracking_codes = dict_data.get("trackingCodes")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("trackingcode",)


class GetTrackingCodesRequest(types.ApiRequest):
    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        position_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        codetype: typing.Union[Unset, typing.Literal["gs1", "tag_1162", "all"]] = Unset,
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.position_id = position_id
        self.limit = limit
        self.offset = offset
        self.codetype = codetype

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.codetype != Unset:
            params["codetype"] = self.codetype
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/positions/{self.position_id}/trackingCodes",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[TrackingCode]:
        return [TrackingCode.from_json(x) for x in result["rows"]]


class SetTrackingCodesRequest(types.ApiRequest):
    """Массовое создание и обновление Кодов маркировки позиции."""

    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        position_id: str,
        tracking_codes: typing.List[dict],
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.position_id = position_id
        self.tracking_codes = tracking_codes

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/positions/{self.position_id}/trackingCodes",
            json=self.tracking_codes,
        )

    def from_response(self, result: list) -> typing.List[TrackingCode]:
        return [TrackingCode.from_json(x) for x in result]


class DeleteTrackingCodesRequest(types.ApiRequest):
    """Массовое удаление Кодов маркировки позиции (по meta или id)."""

    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        position_id: str,
        tracking_codes: typing.List[dict],
    ):
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.position_id = position_id
        self.tracking_codes = tracking_codes

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/{self.entity_type}/{self.entity_id}/positions/{self.position_id}/trackingCodes/delete",
            json=self.tracking_codes,
        )

    def from_response(self, result: list) -> list:
        return result

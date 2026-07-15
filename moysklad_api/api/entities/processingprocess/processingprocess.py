import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ProcessingProcess(types.MoySkladBaseClass):
    """
    accountId    | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    archived     | Boolean     | Добавлен ли Техпроцесс в архив. Обязательное при ответе
    description  | String(4096)| Комментарий Техпроцесса
    externalCode | String(255) | Внешний код Техпроцесса. Обязательное при ответе
    group        | Meta        | Отдел сотрудника. Обязательное при ответе, Expand
    id           | UUID        | ID Техпроцесса. Обязательное при ответе, Только для чтения
    meta         | Meta        | Метаданные Техпроцесса. Обязательное при ответе, Только для чтения
    name         | String(255) | Наименование Техпроцесса. Обязательное при ответе, Необходимо при создании
    owner        | Meta        | Владелец (Сотрудник). Expand
    positions    | MetaArray   | Метаданные позиций Техпроцесса. Обязательное при ответе, Необходимо при создании, Expand
    shared       | Boolean     | Общий доступ. Обязательное при ответе
    updated      | DateTime    | Момент последнего обновления сущности. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    archived: typing.Optional[bool]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    positions: typing.Optional[dict]
    shared: typing.Optional[bool]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingProcess":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.shared = dict_data.get("shared")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingprocess",)


class ProcessingProcessPosition(types.MoySkladBaseClass):
    """
    accountId       | UUID | ID учетной записи. Только для чтения
    id              | UUID | ID позиции. Только для чтения
    meta            | Meta | Метаданные позиции. Только для чтения
    processingstage | Meta | Метаданные этапа. Необходимо при создании, Expand
    nextPositions   | MetaArray | Метаданные следующих позиций
    """

    account_id: typing.Optional[str]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    processingstage: typing.Optional[types.Meta]
    next_positions: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingProcessPosition":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.processingstage = helpers.get_meta(dict_data.get("processingstage"))
        instance.next_positions = dict_data.get("nextPositions")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingprocess", "positions")


def _build_processingprocess_json(
    name: typing.Union[Unset, str] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    archived: typing.Union[Unset, bool] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
) -> dict:
    json_data = {}
    if name != Unset:
        json_data["name"] = name
    if positions != Unset:
        json_data["positions"] = positions
    if archived != Unset:
        json_data["archived"] = archived
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if group != Unset:
        json_data["group"] = {"meta": group}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if shared != Unset:
        json_data["shared"] = shared
    return json_data


class GetProcessingProcessesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/processingprocess",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingProcess]:
        return [ProcessingProcess.from_json(x) for x in result["rows"]]


class CreateProcessingProcessRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        positions: typing.List[dict],
        archived: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.name = name
        self.positions = positions
        self.archived = archived
        self.description = description
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = _build_processingprocess_json(
            name=self.name,
            positions=self.positions,
            archived=self.archived,
            description=self.description,
            external_code=self.external_code,
            group=self.group,
            owner=self.owner,
            shared=self.shared,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingprocess",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingProcess:
        return ProcessingProcess.from_json(result)


class DeleteProcessingProcessRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProcessingProcessRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.id}",
        )

    def from_response(self, result: dict) -> ProcessingProcess:
        return ProcessingProcess.from_json(result)


class UpdateProcessingProcessRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        positions: typing.Union[Unset, typing.List[dict]] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
    ):
        self.id = id_
        self.name = name
        self.positions = positions
        self.archived = archived
        self.description = description
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.shared = shared

    def to_request(self) -> RequestData:
        json_data = _build_processingprocess_json(
            name=self.name,
            positions=self.positions,
            archived=self.archived,
            description=self.description,
            external_code=self.external_code,
            group=self.group,
            owner=self.owner,
            shared=self.shared,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingProcess:
        return ProcessingProcess.from_json(result)


class GetProcessingProcessPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        processingprocess_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processingprocess_id = processingprocess_id
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
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.processingprocess_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingProcessPosition]:
        return [ProcessingProcessPosition.from_json(x) for x in result["rows"]]


class CreateProcessingProcessPositionsRequest(types.ApiRequest):
    def __init__(self, processingprocess_id: str, processingstages: typing.List[types.Meta]):
        self.processingprocess_id = processingprocess_id
        self.processingstages = processingstages

    def to_request(self) -> RequestData:
        json_data = [
            {"processingstage": {"meta": m}} for m in self.processingstages
        ]
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.processingprocess_id}/positions",
            json=json_data,
        )

    def from_response(self, result: list) -> typing.List[ProcessingProcessPosition]:
        return [ProcessingProcessPosition.from_json(x) for x in result]


class GetProcessingProcessPositionRequest(types.ApiRequest):
    def __init__(self, processingprocess_id: str, position_id: str):
        self.processingprocess_id = processingprocess_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.processingprocess_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> ProcessingProcessPosition:
        return ProcessingProcessPosition.from_json(result)


class UpdateProcessingProcessPositionRequest(types.ApiRequest):
    def __init__(
        self,
        processingprocess_id: str,
        position_id: str,
        processingstage: types.Meta,
    ):
        self.processingprocess_id = processingprocess_id
        self.position_id = position_id
        self.processingstage = processingstage

    def to_request(self) -> RequestData:
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.processingprocess_id}/positions/{self.position_id}",
            json={"processingstage": {"meta": self.processingstage}},
        )

    def from_response(self, result: dict) -> ProcessingProcessPosition:
        return ProcessingProcessPosition.from_json(result)


class DeleteProcessingProcessPositionRequest(types.ApiRequest):
    def __init__(self, processingprocess_id: str, position_id: str):
        self.processingprocess_id = processingprocess_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingprocess/{self.processingprocess_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

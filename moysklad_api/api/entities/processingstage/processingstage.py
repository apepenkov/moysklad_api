import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class ProcessingStage(types.MoySkladBaseClass):
    """
    accountId            | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    allPerformers         | Boolean     | Доступность назначения любого сотрудника. Обязательное при ответе
    archived              | Boolean     | Добавлен ли Этап в архив. Обязательное при ответе
    description           | String(4096)| Комментарий Этапа
    distributionRequired   | Boolean     | Видимость заданий для исполнителей. Обязательное при ответе
    externalCode           | String(255) | Внешний код Этапа. Обязательное при ответе
    group                   | Meta        | Отдел сотрудника. Обязательное при ответе, Expand
    id                       | UUID        | ID Этапа. Обязательное при ответе, Только для чтения
    materialStore            | Meta        | Метаданные склада материалов. Только для чтения
    meta                      | Meta        | Метаданные Этапа. Обязательное при ответе, Только для чтения
    name                      | String(255) | Наименование Этапа. Обязательное при ответе, Необходимо при создании
    owner                     | Meta        | Владелец (Сотрудник). Expand
    performers                | MetaArray   | Возможные исполнители. Обязательное при ответе
    shared                    | Boolean     | Общий доступ. Обязательное при ответе
    standardHourCost           | Double      | Стоимость нормо-часа. Обязательное при ответе
    updated                    | DateTime    | Момент последнего обновления Этапа. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    all_performers: typing.Optional[bool]
    archived: typing.Optional[bool]
    description: typing.Optional[str]
    distribution_required: typing.Optional[bool]
    external_code: typing.Optional[str]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    material_store: typing.Optional[types.Meta]
    meta: typing.Optional[types.Meta]
    name: typing.Optional[str]
    owner: typing.Optional[types.Meta]
    performers: typing.Optional[typing.List[dict]]
    shared: typing.Optional[bool]
    standard_hour_cost: typing.Optional[float]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProcessingStage":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.all_performers = dict_data.get("allPerformers")
        instance.archived = dict_data.get("archived")
        instance.description = dict_data.get("description")
        instance.distribution_required = dict_data.get("distributionRequired")
        instance.external_code = dict_data.get("externalCode")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.material_store = helpers.get_meta(dict_data.get("materialStore"))
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.performers = dict_data.get("performers")
        instance.shared = dict_data.get("shared")
        instance.standard_hour_cost = dict_data.get("standardHourCost")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processingstage",)


def _build_processingstage_json(
    name: typing.Union[Unset, str] = Unset,
    all_performers: typing.Union[Unset, bool] = Unset,
    archived: typing.Union[Unset, bool] = Unset,
    description: typing.Union[Unset, str] = Unset,
    distribution_required: typing.Union[Unset, bool] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    performers: typing.Union[Unset, typing.List[types.Meta]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    standard_hour_cost: typing.Union[Unset, float] = Unset,
) -> dict:
    json_data = {}
    if name != Unset:
        json_data["name"] = name
    if all_performers != Unset:
        json_data["allPerformers"] = all_performers
    if archived != Unset:
        json_data["archived"] = archived
    if description != Unset:
        json_data["description"] = description
    if distribution_required != Unset:
        json_data["distributionRequired"] = distribution_required
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if group != Unset:
        json_data["group"] = {"meta": group}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if performers != Unset:
        json_data["performers"] = [{"meta": m} for m in performers]
    if shared != Unset:
        json_data["shared"] = shared
    if standard_hour_cost != Unset:
        json_data["standardHourCost"] = standard_hour_cost
    return json_data


class GetProcessingStagesRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/processingstage",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[ProcessingStage]:
        return [ProcessingStage.from_json(x) for x in result["rows"]]


class CreateProcessingStageRequest(types.ApiRequest):
    def __init__(
        self,
        name: str,
        all_performers: typing.Union[Unset, bool] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        distribution_required: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        performers: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        standard_hour_cost: typing.Union[Unset, float] = Unset,
    ):
        self.name = name
        self.all_performers = all_performers
        self.archived = archived
        self.description = description
        self.distribution_required = distribution_required
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.performers = performers
        self.shared = shared
        self.standard_hour_cost = standard_hour_cost

    def to_request(self) -> RequestData:
        json_data = _build_processingstage_json(
            name=self.name,
            all_performers=self.all_performers,
            archived=self.archived,
            description=self.description,
            distribution_required=self.distribution_required,
            external_code=self.external_code,
            group=self.group,
            owner=self.owner,
            performers=self.performers,
            shared=self.shared,
            standard_hour_cost=self.standard_hour_cost,
        )
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processingstage",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingStage:
        return ProcessingStage.from_json(result)


class DeleteProcessingStageRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processingstage/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProcessingStageRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processingstage/{self.id}",
        )

    def from_response(self, result: dict) -> ProcessingStage:
        return ProcessingStage.from_json(result)


class UpdateProcessingStageRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        name: typing.Union[Unset, str] = Unset,
        all_performers: typing.Union[Unset, bool] = Unset,
        archived: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        distribution_required: typing.Union[Unset, bool] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        performers: typing.Union[Unset, typing.List[types.Meta]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        standard_hour_cost: typing.Union[Unset, float] = Unset,
    ):
        self.id = id_
        self.name = name
        self.all_performers = all_performers
        self.archived = archived
        self.description = description
        self.distribution_required = distribution_required
        self.external_code = external_code
        self.group = group
        self.owner = owner
        self.performers = performers
        self.shared = shared
        self.standard_hour_cost = standard_hour_cost

    def to_request(self) -> RequestData:
        json_data = _build_processingstage_json(
            name=self.name,
            all_performers=self.all_performers,
            archived=self.archived,
            description=self.description,
            distribution_required=self.distribution_required,
            external_code=self.external_code,
            group=self.group,
            owner=self.owner,
            performers=self.performers,
            shared=self.shared,
            standard_hour_cost=self.standard_hour_cost,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processingstage/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> ProcessingStage:
        return ProcessingStage.from_json(result)

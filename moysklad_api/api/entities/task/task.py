import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Task(types.MoySkladBaseClass):
    """
    accountId         | UUID        | ID учетной записи. Обязательное при ответе, Только для чтения
    agent             | Meta        | Контрагент или юрлицо, связанное с задачей. Expand
    assignee          | Meta        | Ответственный за выполнение задачи. Обязательное при ответе, Необходимо при создании, Expand
    author            | Meta        | Сотрудник, создавший задачу. Обязательное при ответе, Только для чтения, Expand
    authorApplication  | Meta        | Решение, создавшее задачу. Только для чтения, Expand
    completed         | DateTime    | Время выполнения задачи. Обязательное при ответе, Только для чтения
    created           | DateTime    | Момент создания. Обязательное при ответе, Только для чтения
    description       | String(4096)| Текст задачи. Обязательное при ответе, Необходимо при создании
    done              | Boolean     | Отметка о выполнении задачи. Обязательное при ответе
    dueToDate         | DateTime    | Срок задачи
    files             | MetaArray   | Метаданные массива Файлов. Обязательное при ответе, Expand
    id                | UUID        | ID Задачи. Обязательное при ответе, Только для чтения
    implementer       | Meta        | Сотрудник, выполнивший задачу. Только для чтения, Expand
    meta              | Meta        | Метаданные Задачи. Обязательное при ответе
    state             | Meta        | Метаданные Типа задачи. Expand
    notes             | Meta        | Метаданные комментариев к задаче. Обязательное при ответе, Expand
    operation         | Meta        | Метаданные Документа, связанного с задачей. Expand
    updated           | DateTime    | Момент последнего обновления Задачи. Обязательное при ответе, Только для чтения
    """

    account_id: typing.Optional[str]
    agent: typing.Optional[types.Meta]
    assignee: types.Meta
    author: typing.Optional[types.Meta]
    author_application: typing.Optional[types.Meta]
    completed: typing.Optional[datetime.datetime]
    created: typing.Optional[datetime.datetime]
    description: str
    done: typing.Optional[bool]
    due_to_date: typing.Optional[datetime.datetime]
    files: typing.Optional[dict]
    id: typing.Optional[str]
    implementer: typing.Optional[types.Meta]
    meta: typing.Optional[types.Meta]
    state: typing.Optional[types.Meta]
    notes: typing.Optional[dict]
    operation: typing.Optional[types.Meta]
    updated: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Task":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.agent = helpers.get_meta(dict_data.get("agent"))
        instance.assignee = helpers.get_meta(dict_data.get("assignee"))
        instance.author = helpers.get_meta(dict_data.get("author"))
        instance.author_application = helpers.get_meta(dict_data.get("authorApplication"))
        instance.completed = helpers.parse_date(dict_data.get("completed"))
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.description = dict_data.get("description")
        instance.done = dict_data.get("done")
        instance.due_to_date = helpers.parse_date(dict_data.get("dueToDate"))
        instance.files = dict_data.get("files")
        instance.id = dict_data.get("id")
        instance.implementer = helpers.get_meta(dict_data.get("implementer"))
        instance.meta = dict_data.get("meta")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.notes = dict_data.get("notes")
        instance.operation = helpers.get_meta(dict_data.get("operation"))
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("task",)


class TaskNote(types.MoySkladBaseClass):
    """
    author            | Meta        | Сотрудник, создавший комментарий. Обязательное при ответе, Только для чтения
    authorApplication  | Meta        | Решение, создавшее комментарий. Только для чтения
    id                | UUID        | ID комментария
    meta              | Meta        | Метаданные комментария
    moment            | DateTime    | Момент создания комментария. Обязательное при ответе, Только для чтения
    text              | String(4096)| Текст комментария. Обязательное при ответе, Необходимо при создании
    files             | MetaArray   | Метаданные массива Файлов комментария
    """

    author: typing.Optional[types.Meta]
    author_application: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    text: typing.Optional[str]
    files: typing.Optional[dict]

    @classmethod
    def from_json(cls, dict_data: dict) -> "TaskNote":
        instance = cls()
        instance.author = helpers.get_meta(dict_data.get("author"))
        instance.author_application = helpers.get_meta(dict_data.get("authorApplication"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.text = dict_data.get("text")
        instance.files = dict_data.get("files")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("task", "notes")


class GetTasksRequest(types.ApiRequest):
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
            url=f"{helpers.BASE_URL}/entity/task",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Task]:
        return [Task.from_json(x) for x in result["rows"]]


class CreateTaskRequest(types.ApiRequest):
    def __init__(
        self,
        description: str,
        assignee: types.Meta,
        agent: typing.Union[Unset, types.Meta] = Unset,
        done: typing.Union[Unset, bool] = Unset,
        due_to_date: typing.Union[Unset, datetime.datetime] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        operation: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.description = description
        self.assignee = assignee
        self.agent = agent
        self.done = done
        self.due_to_date = due_to_date
        self.state = state
        self.operation = operation

    def to_request(self) -> RequestData:
        json_data = {
            "description": self.description,
            "assignee": {"meta": self.assignee},
        }
        if self.agent != Unset:
            json_data["agent"] = {"meta": self.agent}
        if self.done != Unset:
            json_data["done"] = self.done
        if self.due_to_date != Unset:
            json_data["dueToDate"] = helpers.date_to_str(self.due_to_date)
        if self.state != Unset:
            json_data["state"] = {"meta": self.state}
        if self.operation != Unset:
            json_data["operation"] = {"meta": self.operation}
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/task",
            json=json_data,
        )

    def from_response(self, result: dict) -> Task:
        return Task.from_json(result)


class DeleteTaskRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/task/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetTaskRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/task/{self.id}",
        )

    def from_response(self, result: dict) -> Task:
        return Task.from_json(result)


class UpdateTaskRequest(types.ApiRequest):
    def __init__(
        self,
        id_: str,
        description: typing.Union[Unset, str] = Unset,
        assignee: typing.Union[Unset, types.Meta] = Unset,
        agent: typing.Union[Unset, types.Meta] = Unset,
        done: typing.Union[Unset, bool] = Unset,
        due_to_date: typing.Union[Unset, datetime.datetime] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        operation: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.id = id_
        self.description = description
        self.assignee = assignee
        self.agent = agent
        self.done = done
        self.due_to_date = due_to_date
        self.state = state
        self.operation = operation

    def to_request(self) -> RequestData:
        json_data = {}
        if self.description != Unset:
            json_data["description"] = self.description
        if self.assignee != Unset:
            json_data["assignee"] = {"meta": self.assignee}
        if self.agent != Unset:
            json_data["agent"] = {"meta": self.agent}
        if self.done != Unset:
            json_data["done"] = self.done
        if self.due_to_date != Unset:
            json_data["dueToDate"] = helpers.date_to_str(self.due_to_date)
        if self.state != Unset:
            json_data["state"] = {"meta": self.state}
        if self.operation != Unset:
            json_data["operation"] = {"meta": self.operation}
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/task/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Task:
        return Task.from_json(result)


class GetTaskNotesRequest(types.ApiRequest):
    def __init__(
        self,
        task_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.task_id = task_id
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
            url=f"{helpers.BASE_URL}/entity/task/{self.task_id}/notes",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[TaskNote]:
        return [TaskNote.from_json(x) for x in result["rows"]]


class CreateTaskNoteRequest(types.ApiRequest):
    def __init__(self, task_id: str, text: str):
        self.task_id = task_id
        self.text = text

    def to_request(self) -> RequestData:
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/task/{self.task_id}/notes",
            json={"text": self.text},
        )

    def from_response(self, result: list) -> TaskNote:
        return TaskNote.from_json(result[0])


class GetTaskNoteRequest(types.ApiRequest):
    def __init__(self, task_id: str, note_id: str):
        self.task_id = task_id
        self.note_id = note_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/task/{self.task_id}/notes/{self.note_id}",
        )

    def from_response(self, result: dict) -> TaskNote:
        return TaskNote.from_json(result)

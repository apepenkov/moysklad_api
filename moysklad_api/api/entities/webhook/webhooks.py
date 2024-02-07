import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Webhook(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-poluchit-spisok-webhukow


    Название 	        Тип 	        Описание
    meta                Meta 	        Метаданные
    authorApplication 	Meta 	        Приложение-владелец
    id 	                UUID 	        ID вебхука
    accountId 	        UUID 	        ID учетной записи
    entityType 	        String 	        Тип сущности
    url 	            String 	        URL вебхука
    method 	            String 	        HTTP метод
    enabled 	        Boolean 	    Включен ли вебхук
    action 	            String 	        Тип события
    """

    meta: types.Meta
    author_application: types.Meta
    id: str
    account_id: str
    entity_type: str
    url: str
    method: str
    enabled: bool
    action: str

    @classmethod
    def from_json(cls, dict_data: dict) -> "Webhook":
        instance = cls()
        instance.meta = dict_data.get("meta")
        instance.author_application = helpers.get_meta(
            dict_data.get("authorApplication")
        )
        instance.id = dict_data.get("id")
        instance.account_id = dict_data.get("accountId")
        instance.entity_type = dict_data.get("entityType")
        instance.url = dict_data.get("url")
        instance.method = dict_data.get("method")
        instance.enabled = dict_data.get("enabled")
        instance.action = dict_data.get("action")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return ("webhook",)


class GetWebhooksRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-poluchit-spisok-webhukow

    Получить список вебхуков
    """

    def __init__(self):
        pass

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/webhook",
        )

    def from_response(self, result: dict) -> typing.List[Webhook]:
        return [Webhook.from_json(item) for item in result["rows"]]


class CreateWebhookRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-sozdat-webhuk

    Создать вебхук
    Параметры запроса
    url 	    String 	URL вебхука
    entityType 	String 	Тип сущности
    action 	    String 	Тип события
    diffType 	String 	Тип изменений
    """

    def __init__(
        self,
        url: str,
        entity_type: str,
        action: str,
        diff_type: typing.Union[Unset, str] = Unset,
    ):
        """

        :param url: URL of webhook
        :param entity_type: type of entity
        :param action: type of action
        :param diff_type: diff type for update action
        """
        self.url = url
        self.entity_type = entity_type
        self.action = action
        self.diff_type = diff_type

    def to_request(self) -> RequestData:
        json_data = {
            "url": self.url,
            "entityType": self.entity_type,
            "action": self.action,
        }
        if self.diff_type != Unset:
            json_data["diffType"] = self.diff_type
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/webhook",
            json=json_data,
        )

    def from_response(self, result: dict) -> Webhook:
        return Webhook.from_json(result)


class GetWebhookRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-poluchit-otdel-nyj-webhuk

    Получить вебхук по id
    """

    def __init__(self, webhook_id: str):
        self.webhook_id = webhook_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/webhook/{self.webhook_id}",
        )

    def from_response(self, result: dict) -> Webhook:
        return Webhook.from_json(result)


class UpdateWebhookRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-izmenit-webhuk

    Изменить вебхук
    Параметры запроса
    url 	    String 	URL вебхука
    entityType 	String 	Тип сущности
    action 	    String 	Тип события
    diffType 	String 	Тип изменений
    """

    def __init__(
        self,
        webhook_id: str,
        url: typing.Union[Unset, str] = Unset,
        entity_type: typing.Union[Unset, str] = Unset,
        action: typing.Union[Unset, str] = Unset,
        diff_type: typing.Union[Unset, str] = Unset,
    ):
        """

        :param webhook_id: id of webhook
        :param url: URL of webhook
        :param entity_type: type of entity
        :param action: type of action
        :param diff_type: diff type for update action
        """
        self.webhook_id = webhook_id
        self.url = url
        self.entity_type = entity_type
        self.action = action
        self.diff_type = diff_type

    def to_request(self) -> RequestData:
        json_data = {}
        if self.url != Unset:
            json_data["url"] = self.url
        if self.entity_type != Unset:
            json_data["entityType"] = self.entity_type
        if self.action != Unset:
            json_data["action"] = self.action
        if self.diff_type != Unset:
            json_data["diffType"] = self.diff_type
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/webhook/{self.webhook_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Webhook:
        return Webhook.from_json(result)


class DeleteWebhookRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-udalit-webhuk

    Удалить вебхук
    """

    def __init__(self, webhook_id: str):
        self.webhook_id = webhook_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/webhook/{self.webhook_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

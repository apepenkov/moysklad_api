import datetime
import typing

from .... import types


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

    def __init__(self):
        self.meta: types.Meta = None
        self.author_application: types.Meta = None
        self.id: str = None
        self.account_id: str = None
        self.entity_type: str = None
        self.url: str = None
        self.method: str = None
        self.enabled: bool = None
        self.action: str = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "Webhook":
        instance = cls()
        instance.meta = dict_data.get("meta")
        author_application = dict_data.get("authorApplication")
        if author_application:
            instance.author_application = author_application["meta"]
        instance.id = dict_data.get("id")
        instance.account_id = dict_data.get("accountId")
        instance.entity_type = dict_data.get("entityType")
        instance.url = dict_data.get("url")
        instance.method = dict_data.get("method")
        instance.enabled = dict_data.get("enabled")
        instance.action = dict_data.get("action")
        return instance


class GetWebhooksRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-poluchit-spisok-webhukow

    Получить список вебхуков
    """

    def __init__(self):
        pass

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/webhook",
        }

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
        diff_type: typing.Optional[str] = None,
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

    def to_request(self) -> dict:
        json_data = {
            "url": self.url,
            "entityType": self.entity_type,
            "action": self.action,
        }
        if self.diff_type:
            json_data["diffType"] = self.diff_type

        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/webhook",
            "json": json_data,
        }

    def from_response(self, result: dict) -> Webhook:
        return Webhook.from_json(result)


class GetWebhookRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-poluchit-otdel-nyj-webhuk

    Получить вебхук по id
    """

    def __init__(self, webhook_id: str):
        self.webhook_id = webhook_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/webhook/{self.webhook_id}",
        }

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
        url: typing.Optional[str] = None,
        entity_type: typing.Optional[str] = None,
        action: typing.Optional[str] = None,
        diff_type: typing.Optional[str] = None,
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

    def to_request(self) -> dict:
        json_data = {}
        if self.url is not None:
            json_data["url"] = self.url
        if self.entity_type is not None:
            json_data["entityType"] = self.entity_type
        if self.action is not None:
            json_data["action"] = self.action
        if self.diff_type is not None:
            json_data["diffType"] = self.diff_type

        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/webhook/{self.webhook_id}",
            "json": json_data,
        }

    def from_response(self, result: dict) -> Webhook:
        return Webhook.from_json(result)


class DeleteWebhookRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-vebhuki-udalit-webhuk

    Удалить вебхук
    """

    def __init__(self, webhook_id: str):
        self.webhook_id = webhook_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/webhook/{self.webhook_id}",
            "allow_non_json": True,
        }

    def from_response(self, result: dict) -> None:
        return None

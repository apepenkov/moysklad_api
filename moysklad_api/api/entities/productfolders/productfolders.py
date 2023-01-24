import typing
import datetime
from .... import types


class ProductFolder(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-gruppy-towarow

    Атрибуты сущности
    Название 	            Тип 		    Описание
    accountId 	            UUID 	 	    ID учетной записи Обязательное при ответе Только для чтения
    archived 	            Boolean 	 	Добавлена ли Группа товаров в архив Обязательное при ответе Только для чтения
    code 	                String(255) 	Код Группы товаров
    description 	        String(4096) 	Описание Группы товаров
    effectiveVat 	        Int 		    Реальный НДС %     Только для чтения
    effectiveVatEnabled 	Boolean 		Дополнительный признак для определения разграничения реального НДС = 0 или "без НДС". (effectiveVat = 0, effectiveVatEnabled = false) -> "без НДС", (effectiveVat = 0, effectiveVatEnabled = true) -> 0%.     Только для чтения
    externalCode 	        String(255) 	Внешний код Группы товаров Обязательное при ответе
    group 	                Meta 	 	    Метаданные отдела сотрудника Обязательное при ответе Expand
    id 	                    UUID 	 	    ID Группы товаров Обязательное при ответе Только для чтения
    meta 	                Meta 		    Метаданные Группы товаров Обязательное при ответе
    name 	                String(255) 	Наименование Группы товаров Обязательное при ответе Необходимо при создании
    owner 	                Meta 	 	    Метаданные владельца (Сотрудника)     Expand
    pathName 	            String 	 	    Наименование Группы товаров, в которую входит данная Группа товаров Обязательное при ответе Только для чтения
    productFolder 	        Meta 		    Ссылка на Группу товаров, в которую входит данная Группа товаров, в формате Метаданных     Expand
    shared 	                Boolean 	 	Общий доступ Обязательное при ответе
    taxSystem 	            Enum 		    Код системы налогообложения. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-kod-sistemy-nalogooblozheniq
    updated 	            DateTime 	 	Момент последнего обновления сущности Обязательное при ответе Только для чтения
    useParentVat 	        Boolean 		Используется ли ставка НДС родительской группы. Если true для единицы ассортимента будет применена ставка, установленная для родительской группы. Обязательное при ответе
    vat 	                Int 		    НДС %
    vatEnabled 	            Boolean 		Включен ли НДС для группы. С помощью этого флага для группы можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%.

    Код системы налогообложения

    Значения поля taxSystem.
    Значение 	                            Описание
    GENERAL_TAX_SYSTEM 	                    ОСН
    PATENT_BASED 	                        Патент
    PRESUMPTIVE_TAX_SYSTEM 	                ЕНВД
    SIMPLIFIED_TAX_SYSTEM_INCOME 	        УСН. Доход
    SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME 	УСН. Доход-Расход
    TAX_SYSTEM_SAME_AS_GROUP 	            Совпадает с группой
    UNIFIED_AGRICULTURAL_TAX 	            ЕСХН
    """

    def __init__(self):
        self.account_id: str = None
        self.archived: bool = None
        self.code: typing.Optional[str] = None
        self.description: typing.Optional[str] = None
        self.effective_vat: typing.Optional[int] = None
        self.effective_vat_enabled: typing.Optional[bool] = None
        self.external_code: str = None
        self.group: types.Meta = None
        self.id: str = None
        self.meta: types.Meta = None
        self.name: str = None
        self.owner: types.Meta = None
        self.path_name: typing.Optional[str] = None
        self.shared: bool = None
        self.tax_system: typing.Optional[
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ]
        ] = None
        self.updated: datetime.datetime = None
        self.use_parent_vat: bool = None
        self.vat: typing.Optional[int] = None
        self.vat_enabled: typing.Optional[bool] = None

    @classmethod
    def from_json(cls, dict_data: dict) -> "ProductFolder":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.archived = dict_data.get("archived")
        instance.code = dict_data.get("code")
        instance.description = dict_data.get("description")
        instance.effective_vat = dict_data.get("effectiveVat")
        instance.effective_vat_enabled = dict_data.get("effectiveVatEnabled")
        instance.external_code = dict_data.get("externalCode")
        group = dict_data.get("group")
        if group:
            instance.group = group["meta"]
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        owner = dict_data.get("owner")
        if owner:
            instance.owner = owner["meta"]
        instance.path_name = dict_data.get("pathName")
        instance.shared = dict_data.get("shared")
        instance.tax_system = dict_data.get("taxSystem")
        updated = dict_data.get("updated")
        if updated:
            instance.updated = datetime.datetime.fromisoformat(updated)
        instance.use_parent_vat = dict_data.get("useParentVat")
        instance.vat = dict_data.get("vat")
        instance.vat_enabled = dict_data.get("vatEnabled")
        return instance


class GetProductFoldersRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-poluchit-spisok-grupp-towarow

    Параметры
    Параметр 	Описание
    limit 	number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.
    offset 	number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.
    """

    def __init__(self, limit=1000, offset=0):
        """

        :param limit: Limit of entities to extract. Allowed values 1 - 1000. (Лимит сущностей для извлечения. Допустимые значения 1 - 1000.)
        :param offset: Offset in the list of entities returned. (Отступ в выдаваемом списке сущностей.)
        """

        self.limit = limit
        self.offset = offset

    def to_request(self) -> dict:
        params = {}
        if self.limit is not None:
            params["limit"] = self.limit
        if self.offset is not None:
            params["offset"] = self.offset
        return {
            "method": "GET",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/productfolder",
            "params": params,
        }

    def from_response(self, response: dict) -> typing.List[ProductFolder]:
        return [ProductFolder.from_json(item) for item in response["rows"]]


class CreateProductFolderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-sozdat-nowuu-gruppu-towarow

    Название 	            Тип 		    Описание
    name 	                String(255) 	Наименование Группы товаров Обязательное при ответе Необходимо при создании
    code 	                String(255) 	[optional] Код Группы товаров
    description 	        String(4096) 	[optional] Описание Группы товаров
    externalCode 	        String(255) 	[optional] Внешний код Группы товаров Обязательное при ответе
    group 	                Meta 	 	    [optional] Метаданные отдела сотрудника Обязательное при ответе Expand
    meta 	                Meta 		    [optional] Метаданные Группы товаров Обязательное при ответе
    owner 	                Meta 	 	    [optional] Метаданные владельца (Сотрудника)     Expand
    productFolder 	        Meta 		    [optional] Ссылка на Группу товаров, в которую входит данная Группа товаров, в формате Метаданных     Expand
    shared 	                Boolean 	 	[optional] Общий доступ Обязательное при ответе
    taxSystem 	            Enum 		    [optional] Код системы налогообложения. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-kod-sistemy-nalogooblozheniq
    useParentVat 	        Boolean 		[optional] Используется ли ставка НДС родительской группы. Если true для единицы ассортимента будет применена ставка, установленная для родительской группы. Обязательное при ответе
    vat 	                Int 		    [optional] НДС %
    vatEnabled 	            Boolean 		[optional] Включен ли НДС для группы. С помощью этого флага для группы можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%.
    """

    def __init__(
        self,
        name: str,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        group: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        product_folder: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        tax_system: typing.Optional[
            typing.Literal[
                "GENERAL_TAX_SYSTEM",
                "PATENT_BASED",
                "PRESUMPTIVE_TAX_SYSTEM",
                "SIMPLIFIED_TAX_SYSTEM_INCOME",
                "SIMPLIFIED_TAX_SYSTEM_INCOME_OUTCOME",
                "TAX_SYSTEM_SAME_AS_GROUP",
                "UNIFIED_AGRICULTURAL_TAX",
            ]
        ] = None,
        use_parent_vat: typing.Optional[bool] = None,
        vat: typing.Optional[int] = None,
        vat_enabled: typing.Optional[bool] = None,
    ):
        """

        :param name: Name of the product folder (Имя группы товаров)
        :param code: Code of the product folder (Код группы товаров)
        :param description: Description of the product folder (Описание группы товаров)
        :param external_code: External code of the product folder (Внешний код группы товаров)
        :param group: Group of the product folder (Группа группы товаров)
        :param meta: Meta of the product folder (Метаданные группы товаров)
        :param owner: Owner of the product folder (Владелец группы товаров)
        :param product_folder: Product folder of the product folder (Группа товаров группы товаров)
        :param shared: Shared of the product folder (Общий доступ группы товаров)
        :param tax_system: Tax system of the product folder (Код системы налогообложения группы товаров)
        :param use_parent_vat: Use parent vat of the product folder (Используется ли ставка НДС родительской группы)
        :param vat: Vat of the product folder (НДС % группы товаров)
        :param vat_enabled: Vat enabled of the product folder (Включен ли НДС для группы товаров)
        """
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code
        self.group = group
        self.meta = meta
        self.owner = owner
        self.product_folder = product_folder
        self.shared = shared
        self.tax_system = tax_system
        self.use_parent_vat = use_parent_vat
        self.vat = vat
        self.vat_enabled = vat_enabled

    def to_request(self) -> dict:
        json_data = {
            "name": self.name,
        }
        if self.code is not None:
            json_data["code"] = self.code
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.meta is not None:
            json_data["meta"] = self.meta
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.product_folder is not None:
            json_data["productFolder"] = {"meta": self.product_folder}
        if self.shared is not None:
            json_data["shared"] = self.shared
        if self.tax_system is not None:
            json_data["taxSystem"] = self.tax_system
        if self.use_parent_vat is not None:
            json_data["useParentVat"] = self.use_parent_vat
        if self.vat is not None:
            json_data["vat"] = self.vat
        if self.vat_enabled is not None:
            json_data["vatEnabled"] = self.vat_enabled

        return {
            "method": "POST",
            "url": "https://online.moysklad.ru/api/remap/1.2/entity/productfolder",
            "json": json_data,
        }

    def from_response(self, result) -> "ProductFolder":
        return ProductFolder.from_json(result)


class DeleteProductFolderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-udalit-gruppu-towarow

    Delete product folder (Удалить группу товаров)

    folder_id: ID of the product folder (ID группы товаров)
    """

    def __init__(self, folder_id: str):
        """

        :param folder_id: Id of the product folder (Идентификатор группы товаров)
        """
        self.folder_id = folder_id

    def to_request(self) -> dict:
        return {
            "method": "DELETE",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/productfolder/{self.folder_id}",
            "allow_non_json": True,
        }

    def from_response(self, result) -> None:
        return None


class GetProductFolderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-poluchit-gruppu-towarow

    Параметр 	Описание
    id 	        string (required) Example: 7944ef04-f831-11e5-7a69-971500188b19 id Группы товаров.
    """

    def __init__(self, folder_id: str):
        """

        :param folder_id: Product folder id (ID папки товаров)
        """
        self.folder_id = folder_id

    def to_request(self) -> dict:
        return {
            "method": "GET",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/productfolder/{self.folder_id}",
        }

    def from_response(self, result) -> "ProductFolder":
        return ProductFolder.from_json(result)


class UpdateProductFolderRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-izmenit-gruppu-towarow


    Название 	            Тип 		    Описание
    id 	                    string          (required) 	Example: 7944ef04-f831-11e5-7a69-971500188b19 id Группы товаров.
    name 	                String(255) 	[optional] Наименование Группы товаров Обязательное при ответе Необходимо при создании
    code 	                String(255) 	[optional] Код Группы товаров
    description 	        String(4096) 	[optional] Описание Группы товаров
    externalCode 	        String(255) 	[optional] Внешний код Группы товаров Обязательное при ответе
    group 	                Meta 	 	    [optional] Метаданные отдела сотрудника Обязательное при ответе Expand
    meta 	                Meta 		    [optional] Метаданные Группы товаров Обязательное при ответе
    owner 	                Meta 	 	    [optional] Метаданные владельца (Сотрудника)     Expand
    productFolder 	        Meta 		    [optional] Ссылка на Группу товаров, в которую входит данная Группа товаров, в формате Метаданных     Expand
    shared 	                Boolean 	 	[optional] Общий доступ Обязательное при ответе
    taxSystem 	            Enum 		    [optional] Код системы налогообложения. Подробнее тут https://dev.moysklad.ru/doc/api/remap/1.2/dictionaries/#suschnosti-gruppa-towarow-kod-sistemy-nalogooblozheniq
    useParentVat 	        Boolean 		[optional] Используется ли ставка НДС родительской группы. Если true для единицы ассортимента будет применена ставка, установленная для родительской группы. Обязательное при ответе
    vat 	                Int 		    [optional] НДС %
    vatEnabled 	            Boolean 		[optional] Включен ли НДС для группы. С помощью этого флага для группы можно выставлять НДС = 0 или НДС = "без НДС". (vat = 0, vatEnabled = false) -> vat = "без НДС", (vat = 0, vatEnabled = true) -> vat = 0%.
    """

    def __init__(
        self,
        folder_id: str,
        name: typing.Optional[str] = None,
        code: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        external_code: typing.Optional[str] = None,
        group: typing.Optional[types.Meta] = None,
        meta: typing.Optional[types.Meta] = None,
        owner: typing.Optional[types.Meta] = None,
        product_folder: typing.Optional[types.Meta] = None,
        shared: typing.Optional[bool] = None,
        tax_system: typing.Optional[str] = None,
        use_parent_vat: typing.Optional[bool] = None,
        vat: typing.Optional[int] = None,
        vat_enabled: typing.Optional[bool] = None,
    ):
        """

        :param folder_id: Id of the folder to update (ID Группы товаров)
        :param name: Name of the folder (Наименование Группы товаров)
        :param code: Code of the product folder (Код группы товаров)
        :param description: Description of the product folder (Описание группы товаров)
        :param external_code: External code of the product folder (Внешний код группы товаров)
        :param group: Group of the product folder (Группа группы товаров)
        :param meta: Meta of the product folder (Метаданные группы товаров)
        :param owner: Owner of the product folder (Владелец группы товаров)
        :param product_folder: Product folder of the product folder (Группа товаров группы товаров)
        :param shared: Shared of the product folder (Общий доступ группы товаров)
        :param tax_system: Tax system of the product folder (Код системы налогообложения группы товаров)
        :param use_parent_vat: Use parent vat of the product folder (Используется ли ставка НДС родительской группы)
        :param vat: Vat of the product folder (НДС % группы товаров)
        :param vat_enabled: Vat enabled of the product folder (Включен ли НДС для группы товаров)
        """
        self.folder_id = folder_id
        self.name = name
        self.code = code
        self.description = description
        self.external_code = external_code
        self.group = group
        self.meta = meta
        self.owner = owner
        self.product_folder = product_folder
        self.shared = shared
        self.tax_system = tax_system
        self.use_parent_vat = use_parent_vat
        self.vat = vat
        self.vat_enabled = vat_enabled

    def to_request(self) -> dict:
        json_data = {}
        if self.name is not None:
            json_data["name"] = self.name
        if self.code is not None:
            json_data["code"] = self.code
        if self.description is not None:
            json_data["description"] = self.description
        if self.external_code is not None:
            json_data["externalCode"] = self.external_code
        if self.group is not None:
            json_data["group"] = {"meta": self.group}
        if self.meta is not None:
            json_data["meta"] = self.meta
        if self.owner is not None:
            json_data["owner"] = {"meta": self.owner}
        if self.product_folder is not None:
            json_data["productFolder"] = {"meta": self.product_folder}
        if self.shared is not None:
            json_data["shared"] = self.shared
        if self.tax_system is not None:
            json_data["taxSystem"] = self.tax_system
        if self.use_parent_vat is not None:
            json_data["useParentVat"] = self.use_parent_vat
        if self.vat is not None:
            json_data["vat"] = self.vat
        if self.vat_enabled is not None:
            json_data["vatEnabled"] = self.vat_enabled
        return {
            "method": "PUT",
            "url": f"https://online.moysklad.ru/api/remap/1.2/entity/productfolder/{self.folder_id}",
            "json": json_data,
        }

    def from_response(self, result) -> "ProductFolder":
        return ProductFolder.from_json(result)

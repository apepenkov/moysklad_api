import typing
import datetime
from .... import types, helpers
from ....types import Unset, RequestData


# https://dev.moysklad.ru/doc/api/remap/1.2/reports/#otchety-otchet-ostatki


class FullStockReport(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/reports/#otchety-otchet-ostatki-rasshirennyj-otchet-ob-ostatkah
    Атрибуты объекта отчета:
    Название 	        Тип 	        Описание
    article 	        String(255) 	Артикул
    code 	            String(255) 	Код     Обязательное при ответе
    externalCode 	    String(255) 	Внешний код сущности, по которой выводится остаток     Обязательное при ответе
    folder 	            Object 	        Группа Товара/Модификации/Cерии. Подробнее тут     Обязательное при ответе
    image 	            Meta 	        Метаданные изображения Товара/Модификации/Серии
    inTransit 	        Float 	        Ожидание     Обязательное при ответе
    meta 	            Meta 	        Метаданные Товара/Модификации/Серии по которой выдается остаток     Обязательное при ответе
    name 	            String(255) 	Наименование     Обязательное при ответе
    price 	            Float 	        Себестоимость
    quantity 	        Float 	        Доступно     Обязательное при ответе
    reserve 	        Float 	        Резерв     Обязательное при ответе
    salePrice 	        Float 	        Цена продажи
    stock 	            Float 	        Остаток     Обязательное при ответе
    stockDays 	        Int 	        Количество дней на складе     Обязательное при ответе
    uom 	            Object 	        Единица измерения. Подробнее тут (https://dev.moysklad.ru/doc/api/remap/1.2/reports/#otchety-otchet-ostatki-rasshirennyj-otchet-ob-ostatkah-edinica-izmereniq)    Обязательное при ответе
    """

    article: typing.Optional[str]
    code: str
    external_code: str
    folder: dict
    image: types.Meta
    in_transit: float
    meta: types.Meta
    name: str
    price: typing.Optional[float]
    quantity: float
    reserve: float
    sale_price: typing.Optional[float]
    stock: float
    stock_days: int
    uom: dict

    @classmethod
    def from_json(cls, dict_data: dict) -> "FullStockReport":
        """
        Создает объект из json
        :param dict_data:
        :return:
        """
        instance = cls()
        instance.article = dict_data.get("article")
        instance.code = dict_data.get("code")
        instance.external_code = dict_data.get("externalCode")
        instance.folder = dict_data.get("folder")
        instance.image = helpers.get_meta(dict_data.get("image"))
        instance.in_transit = dict_data.get("inTransit")
        instance.meta = dict_data.get("meta")
        instance.name = dict_data.get("name")
        instance.price = dict_data.get("price")
        instance.quantity = dict_data.get("quantity")
        instance.reserve = dict_data.get("reserve")
        instance.sale_price = dict_data.get("salePrice")
        instance.stock = dict_data.get("stock")
        instance.stock_days = dict_data.get("stockDays")
        instance.uom = dict_data.get("uom")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return "stock", "all"


class SmallStockReport(types.MoySkladBaseClass):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/reports/#otchety-otchet-ostatki-kratkij-otchet-ob-ostatkah
    """

    assortment_id: str
    store_id: typing.Optional[str]
    stock: int

    @classmethod
    def from_json(cls, dict_data: dict) -> "SmallStockReport":
        """
        Создает объект из json
        :param dict_data:
        :return:
        """
        instance = cls()
        instance.assortment_id = dict_data.get("assortmentId")
        instance.store_id = dict_data.get("storeId")
        instance.stock = dict_data.get("stock")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str, ...]]:
        return None


class GetFullStockReportRequest(types.ApiRequest):
    """
    https://dev.moysklad.ru/doc/api/remap/1.2/reports/#otchety-otchet-ostatki-poluchit-rasshirennyj-otchet-ob-ostatkah

    Параметры
    Параметр 	    Описание
    limit 	        number (optional) Default: 1000 Example: 1000 Максимальное количество сущностей для извлечения.Допустимые значения 1 - 1000.

    offset 	        number (optional) Default: 0 Example: 40 Отступ в выдаваемом списке сущностей.

    groupBy 	    string (optional) тип, по которому нужно сгруппировать выдачу.По умолчанию параметр groupBy имеет значение variant. Если вы хотите увидеть объекты типа consignment, или только объекты типа product, необходимо выставить соответствующее значение параметра.

    groupBy=product - выдает только товары
    groupBy=variant - выдает товары и модификации
    groupBy=consignment - выдает товары, модификации, серии

    includeRelated 	boolean (optional) Вывод остатков по модификациям и сериям товаров. Параметр позволяет включить в выборку остатки по модификациям и сериям для товаров. Необходимым условием для применения параметра является обязательное наличие фильтрации по товарам или модификациям или их комбинации. При выбранном значении includeRelated=true будут включены все остатки для товаров, модификаций и серий, указанных в параметрах фильтрации.
    При использовании параметра устанавливается параметр группировки groupBy=consignment, переданные значения для groupBy будут проигнорированы.


    Примеры использования параметра includeRelated:
    filter=variant!=&includeRelated=true выводит остатки товаров, модификаций, серий за исключением конкретной модификации указанной в URL.
    filter=product=&includeRelated=true выводит остатки конкретного товара указанного в URL, его модификации и серии.
    """

    def __init__(
        self,
        limit: typing.Union[Unset, int] = 1000,
        offset: typing.Union[Unset, int] = 0,
        group_by: typing.Union[
            Unset, typing.Literal["product", "variant", "consignment"]
        ] = Unset,
        include_related: typing.Union[Unset, bool] = Unset,
    ):
        """

        :param limit: Limit the number of entities to retrieve. (Ограничить количество сущностей для извлечения.)
        :param offset: Offset in the returned list of entities. (Отступ в выдаваемом списке сущностей.)
        :param group_by: Type to group by. (Тип, по которому нужно сгруппировать выдачу.)
        :param include_related: Include consignments for product and variants. (Вывод остатков по модификациям и сериям товаров.)
        """

        self.limit = limit
        self.offset = offset
        self.group_by = group_by
        self.include_related = include_related

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.group_by != Unset:
            params["groupBy"] = self.group_by
        if self.include_related != Unset:
            params["includeRelated"] = self.include_related
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/stock/all",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[FullStockReport]:
        return [FullStockReport.from_json(item) for item in result["rows"]]


class GetSmallStockReportCurrentRequest(types.ApiRequest):
    """
    /report/stock/all/current - Получить отчет о наличии товаров в магазинах

    Параметр include
    По умолчанию выводятся только результаты с ненулевым значением остатка. Для вывода нулевых остатков, необходимо добавить параметр include=zeroLines.

    Параметр changedSince
    По умолчанию выводятся остатки на текущий момент. Параметром changedSince можно получить остатки, которые изменились в интервале между временем указанным в параметре changedSince и текущим моментом. Остатки в ответах на эндпоинты /report/stock/all/current и /report/stock/bystore/current это фактический остаток на текущий момент времени на всех складах и с разбивкой по складам соответственно, не дельта за период, не остаток на момент времени changedSince, а фактический остаток по номенклатуре, у которой изменился остаток за интервал. Формат значения параметра - строка вида "гггг-мм-дд чч-мм-сс". Пример: changedSince=2016-08-23 15:21:09. Подробнее тут
    Ограничения и рекомендации, накладываемые на параметр:

    При использовании параметра changedSince всегда включен вывод нулевых остатков.
    Максимальное значение параметра changedSince в прошлое от текущего момента не должно превышать 24 часа.
    Минимальное значение параметра changedSince в прошлое от текущего момента не ограничено.
    Параметр changedSince не может превышать текущий момент.
    Небольшое перекрытие интервалов запросов поможет исключить потерю обновления остатков на границах интервалов (пример: запрос остатков каждые 30 минут за прошедшие 35 минут).
    Рекомендуется проводить полную синхронизацию остатков без параметра changedSince раз в сутки и чаще, в зависимости от частоты изменения остатков.

    Важно: если за запрашиваемый интервал был удален (не архивирован) товар или склад, то будет выведен остаток равный 0. Стоит учитывать, что по id запросить этот товар или склад уже не получится.
    Параметр stockType

    Параметром stockType выбирается тип остатка, который необходимо рассчитать. На данный момент возможно получить только один тип остатка. Значение по умолчанию - stock
    Значение 	Описание
    stock 	Физический остаток на складах, без учёта резерва и ожидания
    freeStock 	Остаток на складах за вычетом резерва
    quantity 	Доступно. Учитывает резерв и ожидания
    Доступные фильтры отчёта Текущие Остатки

    Можно ограничить отчёт несколькими товарами или складами. Указывается id сущности, а не url.
    Значение 	Тип 	Фильтрация 	Описание
    assortmentId 	UUID 	= 	Выдать в отчёте только указанные товары, модификации и серии
    storeId 	UUID 	= 	Выдать в отчёте только указанные склады

    Несколько значений можно указать через запятую или через несколько параметров:

    filter=assortmentId=00000000-0000-0000-0000-000000000001,00000000-0000-0000-0000-000000000002
    filter=assortmentId=00000000-0000-0000-0000-000000000001;assortmentId=00000000-0000-0000-0000-000000000002
    filter=assortmentId=00000000-0000-0000-0000-000000000001&filter=assortmentId=00000000-0000-0000-0000-000000000002

    """

    def __init__(
        self,
        include: typing.Union[Unset, str] = Unset,
        changed_since: typing.Union[Unset, datetime.datetime] = Unset,
        stock_type: typing.Union[
            Unset, typing.Literal["stock", "freeStock", "quantity"]
        ] = Unset,
        filter_assortment_id: typing.Union[Unset, typing.List[str]] = Unset,
        filter_store_id: typing.Union[Unset, typing.List[str]] = Unset,
    ):
        """

        :param include: Include related entities (Включить связанные сущности)
        :param changed_since: Changed since (Изменено с)
        :param stock_type: Stock type (Тип остатка)
        :param filter_assortment_id: Filter by assortment id (Фильтр по id товара)
        :param filter_store_id: Filter by store id (Фильтр по id склада)
        """
        self.include = include
        self.changed_since = changed_since
        self.stock_type = stock_type
        self.filter_assortment_id = filter_assortment_id
        self.filter_store_id = filter_store_id

    def to_request(self) -> RequestData:
        params = {}
        if self.include != Unset:
            params["include"] = self.include
        if self.changed_since != Unset:
            params["changedSince"] = helpers.date_to_str(self.changed_since)
        if self.stock_type != Unset:
            params["stockType"] = self.stock_type
        if self.filter_assortment_id != Unset:
            params["filter"] = []
            params["filter"].append(
                "assortmentId={}".format(",".join(self.filter_assortment_id))
            )
        if self.filter_store_id != Unset:
            if "filter" not in params:
                params["filter"] = []
            params["filter"].append("storeId={}".format(",".join(self.filter_store_id)))
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/report/stock/all/current",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[SmallStockReport]:
        return [SmallStockReport.from_json(item) for item in result]


# TODO: implement full reports

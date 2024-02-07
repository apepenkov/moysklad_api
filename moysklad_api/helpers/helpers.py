import datetime
import re
import typing

from moysklad_api.types import types


def parse_date(date_str: typing.Optional[str], must=False) -> typing.Optional[datetime]:
    if must:
        return datetime.datetime.fromisoformat(date_str)
    return datetime.datetime.fromisoformat(date_str) if date_str else None


def date_to_str(date: datetime.datetime) -> typing.Optional[str]:
    return date.strftime("%Y-%m-%d %H:%M:%S")


def get_meta(
    meta_data: typing.Optional[dict], must=False
) -> typing.Optional[types.Meta]:
    if must:
        return meta_data["meta"]
    return meta_data.get("meta") if meta_data else None


def guess_constructor_by_href(
    href: str,
) -> typing.Optional[typing.Type[types.MoySkladBaseClass]]:
    uuid_group = (
        r"(?:[a-z0-9-]{8}-[a-z0-9-]{4}-[a-z0-9-]{4}-[a-z0-9-]{4}-[a-z0-9-]{12})?"
    )
    found = re.findall(
        r"https://api\.moysklad\.ru/api/remap/\d+\.\d+/\w+/(\w+)/?"
        + uuid_group
        + "/?(\w+)?",
        href,
    )
    if not found:
        return None
    what_to_find = tuple()
    for elem in found[0]:
        if elem:
            what_to_find += (elem,)
    if not what_to_find:
        return None
    for subclass in types.MoySkladBaseClass.__subclasses__():
        if subclass.ms_name() == what_to_find:
            return subclass
    return None


def construct_or_meta(data: dict):
    if len(data) == 1 and "meta" in data:
        return types.Meta(**data["meta"])
    constructor = guess_constructor_by_href(data["meta"]["href"])
    if not constructor:
        return types.Meta(**data["meta"])
    return constructor.from_json(data)


BASE_URL = "https://api.moysklad.ru/api/remap/1.2"


if __name__ == "__main__":
    print(
        guess_constructor_by_href(
            "https://api.moysklad.ru/api/remap/1.2/entity/purchaseorder/7944ef04-f831-11e5-7a69-971500188b19/positions/34f6344f-015e-11e6-9464-e4de0000006c"
        )
    )
    print(
        guess_constructor_by_href(
            "https://api.moysklad.ru/api/remap/1.2/entity/purchaseorder/7944ef04-f831-11e5-7a69-971500188b19"
        )
    )
    print(
        guess_constructor_by_href(
            "https://api.moysklad.ru/api/remap/1.2/entity/purchaseorder"
        )
    )

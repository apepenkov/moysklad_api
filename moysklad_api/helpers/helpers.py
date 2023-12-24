import datetime
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

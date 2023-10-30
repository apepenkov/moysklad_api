import datetime
import typing


def parse_date(date_str: typing.Optional[str]) -> typing.Optional[datetime]:
    return datetime.datetime.fromisoformat(date_str) if date_str else None


def get_meta(meta_data: typing.Optional[dict]) -> typing.Optional[str]:
    return meta_data.get("meta") if meta_data else None

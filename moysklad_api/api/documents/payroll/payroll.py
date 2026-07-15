import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Payroll(types.MoySkladBaseClass):
    """Начисление зарплаты (entity/payroll)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    description: typing.Optional[str]
    attributes: typing.Optional[typing.List[dict]]
    created: typing.Optional[datetime.datetime]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    positions: typing.Optional[dict]
    printed: typing.Optional[bool]
    published: typing.Optional[bool]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sum: typing.Optional[float]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    start_payroll_period: typing.Optional[datetime.datetime]
    end_payroll_period: typing.Optional[datetime.datetime]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Payroll":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.description = dict_data.get("description")
        instance.attributes = dict_data.get("attributes")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.positions = dict_data.get("positions")
        instance.printed = dict_data.get("printed")
        instance.published = dict_data.get("published")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sum = dict_data.get("sum")
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.start_payroll_period = helpers.parse_date(
            dict_data.get("startPayrollPeriod")
        )
        instance.end_payroll_period = helpers.parse_date(
            dict_data.get("endPayrollPeriod")
        )
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("payroll",)


class Position(types.MoySkladBaseClass):
    meta: typing.Optional[types.Meta]
    account_id: typing.Optional[str]
    id: typing.Optional[str]
    employee: typing.Optional[types.Meta]
    base_salary: typing.Optional[float]
    piecework_salary: typing.Optional[float]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Position":
        instance = cls()
        instance.meta = dict_data.get("meta")
        instance.account_id = dict_data.get("accountId")
        instance.id = dict_data.get("id")
        instance.employee = helpers.get_meta(dict_data.get("employee"))
        instance.base_salary = dict_data.get("baseSalary")
        instance.piecework_salary = dict_data.get("pieceworkSalary")
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "payroll", "positions"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    start_payroll_period: typing.Union[Unset, datetime.datetime] = Unset,
    end_payroll_period: typing.Union[Unset, datetime.datetime] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    description: typing.Union[Unset, str] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    positions: typing.Union[Unset, typing.List[dict]] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if start_payroll_period != Unset:
        json_data["startPayrollPeriod"] = helpers.date_to_str(start_payroll_period)
    if end_payroll_period != Unset:
        json_data["endPayrollPeriod"] = helpers.date_to_str(end_payroll_period)
    if applicable != Unset:
        json_data["applicable"] = applicable
    if description != Unset:
        json_data["description"] = description
    if attributes != Unset:
        json_data["attributes"] = attributes
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if group != Unset:
        json_data["group"] = {"meta": group}
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if positions != Unset:
        json_data["positions"] = []
        for position in positions:
            new_position: dict = position.copy()
            new_position["employee"] = {"meta": new_position["employee"]}
            json_data["positions"].append(new_position)
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetPayrollsRequest(types.ApiRequest):
    def __init__(
        self,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
        search: typing.Union[Unset, str] = Unset,
    ):
        self.limit = limit
        self.offset = offset
        self.search = search

    def to_request(self) -> RequestData:
        params = {}
        if self.limit != Unset:
            params["limit"] = self.limit
        if self.offset != Unset:
            params["offset"] = self.offset
        if self.search != Unset:
            params["search"] = self.search
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/payroll", params=params
        )

    def from_response(self, result: dict) -> typing.List[Payroll]:
        return [Payroll.from_json(x) for x in result["rows"]]


class CreatePayrollRequest(types.ApiRequest):
    class CreatePosition(typing.TypedDict):
        employee: types.Meta
        base_salary: float
        piecework_salary: float

    def __init__(
        self,
        organization: types.Meta,
        start_payroll_period: datetime.datetime,
        end_payroll_period: datetime.datetime,
        applicable: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[CreatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.start_payroll_period = start_payroll_period
        self.end_payroll_period = end_payroll_period
        self.applicable = applicable
        self.description = description
        self.attributes = attributes
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            start_payroll_period=self.start_payroll_period,
            end_payroll_period=self.end_payroll_period,
            applicable=self.applicable,
            description=self.description,
            attributes=self.attributes,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/payroll", json=json_data
        )

    def from_response(self, result: dict) -> Payroll:
        return Payroll.from_json(result)


class DeletePayrollRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/payroll/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetPayrollRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/payroll/{self.id}"
        )

    def from_response(self, result: dict) -> Payroll:
        return Payroll.from_json(result)


class UpdatePayrollRequest(types.ApiRequest):
    UpdatePosition = CreatePayrollRequest.CreatePosition

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        start_payroll_period: typing.Union[Unset, datetime.datetime] = Unset,
        end_payroll_period: typing.Union[Unset, datetime.datetime] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        description: typing.Union[Unset, str] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        positions: typing.Union[Unset, typing.List[UpdatePosition]] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.start_payroll_period = start_payroll_period
        self.end_payroll_period = end_payroll_period
        self.applicable = applicable
        self.description = description
        self.attributes = attributes
        self.external_code = external_code
        self.files = files
        self.group = group
        self.moment = moment
        self.name = name
        self.owner = owner
        self.positions = positions
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            start_payroll_period=self.start_payroll_period,
            end_payroll_period=self.end_payroll_period,
            applicable=self.applicable,
            description=self.description,
            attributes=self.attributes,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            moment=self.moment,
            name=self.name,
            owner=self.owner,
            positions=self.positions,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/payroll/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Payroll:
        return Payroll.from_json(result)


class GetPayrollPositionsRequest(types.ApiRequest):
    def __init__(
        self,
        payroll_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.payroll_id = payroll_id
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
            url=f"{helpers.BASE_URL}/entity/payroll/{self.payroll_id}/positions",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Position]:
        return [Position.from_json(x) for x in result["rows"]]


class GetPayrollPositionRequest(types.ApiRequest):
    def __init__(self, payroll_id: str, position_id: str):
        self.payroll_id = payroll_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/payroll/{self.payroll_id}/positions/{self.position_id}",
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class CreatePayrollPositionRequest(types.ApiRequest):
    """Создать позицию. Ответ API - список позиций (в т.ч. созданная)."""

    def __init__(
        self,
        payroll_id: str,
        employee: types.Meta,
        base_salary: float,
        piecework_salary: float,
    ):
        self.payroll_id = payroll_id
        self.employee = employee
        self.base_salary = base_salary
        self.piecework_salary = piecework_salary

    def to_request(self) -> RequestData:
        json_data = {
            "employee": {"meta": self.employee},
            "baseSalary": self.base_salary,
            "pieceworkSalary": self.piecework_salary,
        }
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/payroll/{self.payroll_id}/positions",
            json=json_data,
        )

    def from_response(self, result: typing.List[dict]) -> typing.List[Position]:
        return [Position.from_json(x) for x in result]


class UpdatePayrollPositionRequest(types.ApiRequest):
    def __init__(
        self,
        payroll_id: str,
        position_id: str,
        employee: typing.Union[Unset, types.Meta] = Unset,
        base_salary: typing.Union[Unset, float] = Unset,
        piecework_salary: typing.Union[Unset, float] = Unset,
    ):
        self.payroll_id = payroll_id
        self.position_id = position_id
        self.employee = employee
        self.base_salary = base_salary
        self.piecework_salary = piecework_salary

    def to_request(self) -> RequestData:
        json_data = {}
        if self.employee != Unset:
            json_data["employee"] = {"meta": self.employee}
        if self.base_salary != Unset:
            json_data["baseSalary"] = self.base_salary
        if self.piecework_salary != Unset:
            json_data["pieceworkSalary"] = self.piecework_salary
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/payroll/{self.payroll_id}/positions/{self.position_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Position:
        return Position.from_json(result)


class DeletePayrollPositionRequest(types.ApiRequest):
    def __init__(self, payroll_id: str, position_id: str):
        self.payroll_id = payroll_id
        self.position_id = position_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/payroll/{self.payroll_id}/positions/{self.position_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

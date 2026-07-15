import argparse
import enum
import os.path
import re
import shutil
import sys
import typing

# noinspection PyPackageRequirements
import black

# noinspection PyPackageRequirements
import requests


class TableType(enum.Enum):
    name_type_filtering_description = 1
    name_type_description = 2
    param_description = 3
    name_description = 4
    attribute_description = 5
    field_description = 6


class KeywordsTableType(enum.StrEnum):
    name = "Название"
    type = "Тип"
    filtering = "Фильтрация"
    description = "Описание"
    param = "Параметр"
    attribute = "Атрибут"
    field = "Поле"


class DescriptionKeywords(enum.StrEnum):
    necessary_in_response = "Обязательное при ответе"
    read_only = "Только для чтения"
    expand = "Expand"
    necessary_in_creation = "Необходимо при создании"


DESCRIPTION_KEYWORDS_REGEXP = re.compile(r"`\+([\w ]+)`")
DESCRIPTION_KEYWORDS_REGEXP_SUB = re.compile(r"`\+[\w ]+`")

DESCRIPTION_DEFAULT_REGEXP = re.compile(r"\*\*Default: ([^*]+)\*\*")
DESCRIPTION_DEFAULT_REGEXP_SUB = re.compile(r"\*\*Default: [^*]+\*\*")


class PyType(enum.StrEnum):
    str = "str"
    bool = "bool"
    int = "int"
    float = "float"
    datetime = "datetime.datetime"
    list_dict = "typing.List[dict]"
    list_str = "typing.List[str]"
    list_int = "typing.List[int]"
    meta_array = "types.MetaArray"
    meta = "types.Meta"
    dict = "dict"
    none = "None"
    enum = "typing.Literal[]"

    def to_typehint(self) -> str:
        return self.value

    def to_def_typehint(self, optional: bool) -> str:
        if optional:
            return f"typing.Optional[{self.to_typehint()}]"
        return self.to_typehint()

    def to_param_typehint(self, required: bool) -> str:
        if required:
            return self.to_typehint()
        return f"typing.Union[Unset, {self.to_typehint()}] = Unset"

    def to_json_parse(self, snake_name: str, json_name: str):
        if snake_name == "meta":
            return f'instance.{snake_name} = dict_data.get("meta")'
        loaded = f'dict_data.get("{json_name}")'
        if self == PyType.meta:
            loaded = "helpers.get_meta(" + loaded + ")"
        elif self == PyType.datetime:
            loaded = "helpers.parse_date(" + loaded + ")"

        done = f"instance.{snake_name} = {loaded}"

        if self == PyType.list_dict and snake_name != "attributes":
            done += " # TODO: check if it's meta. If so: "
            done += (
                f"instance.{snake_name} = [helpers.get_meta(x) for x in {loaded} or []]"
            )
        return done

    def to_request_put_in_json(self, snake_name):
        if self == PyType.meta:
            load = f'{{"meta": self.{snake_name}}}'
        elif self == PyType.datetime:
            load = f"helpers.date_to_str(self.{snake_name})"
        else:
            load = f"self.{snake_name}"

        if self == PyType.list_dict and snake_name != "attributes":
            load += (
                "  # TODO: check if additional class is required, if param is complex"
            )

        return load


def type_to_python(type_: str):
    if type_ == "UUID" or type_ == "UID":
        return PyType.str
    if type_ == "Boolean":
        return PyType.bool
    if type_ == "Int":
        return PyType.int
    if type_ == "Float" or type_ == "Double":
        return PyType.float
    if type_ == "Array(Object)":
        return PyType.list_dict
    if type_ == "DateTime":
        return PyType.datetime
    if type_ == "MetaArray":
        return PyType.meta_array
    if type_ == "Object":
        return PyType.dict
    if type_ == "None":
        return PyType.none
    if type_ == "Meta" or "[Meta]" in type_:
        return PyType.meta
    if type_ == "String" or "String(" in type_:
        return PyType.str
    if type_ == "Array(String)":
        return PyType.list_str
    if type_ == "Array(Int)":
        return PyType.list_int
    if type_ == "Enum":
        return PyType.str
    raise ValueError(f"Unknown type: {type_}")


SNAKE_CASE_REGEXP_1 = re.compile(r"(.)([A-Z][a-z]+)")
SNAKE_CASE_REGEXP_2 = re.compile(r"([a-z0-9])([A-Z])")


def to_snake_case(name: str) -> str:
    return SNAKE_CASE_REGEXP_2.sub(
        r"\1_\2", SNAKE_CASE_REGEXP_1.sub(r"\1_\2", name)
    ).lower()


class TableField:
    name: typing.Optional[str]
    description: typing.Optional[str]
    filtering: typing.Optional[str]
    param: typing.Optional[str]
    tags: typing.List[DescriptionKeywords]
    default: typing.Optional[str]
    optional: typing.Optional[bool]  # used both for param and field
    table_type: TableType
    type: typing.Optional[PyType]
    orig_type: typing.Optional[str]

    def __init__(
        self,
        table_type: TableType,
        name: typing.Optional[str] = None,
        type_: typing.Optional[str] = None,
        filtering: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        tags=None,
        default: typing.Optional[str] = None,
        optional: typing.Optional[bool] = None,
        param: typing.Optional[str] = None,
    ):
        if tags is None:
            tags = []
        self.name = name
        if type_ and type_.startswith("[Meta]"):
            type_ = "Meta"
        self.type = type_to_python(type_) if type_ is not None else None
        self.orig_type = type_
        self.filtering = filtering
        if description:
            # description = description.replace("](..", "https://dev.moysklad.ru/doc/api/remap/1.2")
            description = re.sub(
                r"\[[\w \d.,]+\]\(\.\.([^)]+)\)",
                r"https://dev.moysklad.ru/doc/api/remap/1.2\1",
                description,
            )
        self.description = description
        self.tags = tags or []
        self.default = default
        self.optional = optional
        self.param = param
        self.table_type = table_type

    @classmethod
    def from_row(cls, row: str, table_type: TableType):
        row = row.strip()
        row = row.strip("|")
        row = row.strip()
        match table_type:
            case TableType.name_type_filtering_description:
                name, type_, filtering, description = row.split("|")
                name, type_, filtering, description = (
                    name.strip(),
                    type_.strip(),
                    filtering.strip(),
                    description.strip(),
                )
                name = name.strip("*")

                tags = re.findall(DESCRIPTION_KEYWORDS_REGEXP, description)
                description = DESCRIPTION_KEYWORDS_REGEXP_SUB.sub("", description)
                description = description.replace("<br>", " ")
                for i, tag in enumerate(tags):
                    tags[i] = DescriptionKeywords(tag)

                if type_ == "None":
                    breakpoint()

                return cls(
                    table_type,
                    name=name,
                    type_=type_,
                    filtering=filtering,
                    description=description,
                    tags=tags,
                )
            case TableType.name_type_description:
                name, type_, description = row.split("|")
                name, type_, description = (
                    name.strip(),
                    type_.strip(),
                    description.strip(),
                )
                name = name.strip("*")

                if type_ == "None":
                    breakpoint()

                tags = re.findall(DESCRIPTION_KEYWORDS_REGEXP, description)
                description = DESCRIPTION_KEYWORDS_REGEXP_SUB.sub("", description)
                description = description.replace("<br>", " ")
                for i, tag in enumerate(tags):
                    tags[i] = DescriptionKeywords(tag)
                return cls(
                    table_type,
                    name=name,
                    type_=type_,
                    description=description,
                )
            case TableType.param_description:
                param, description = row.split("|")
                param, description = param.strip(), description.strip()
                param = param.strip("*")

                # optional = "(optional)" in param
                # param = param.replace("(optional)", "").strip()

                optional = None
                if "(optional)" in description:
                    optional = True
                    description = description.replace("(optional)", "").strip()
                elif "(required)" in description:
                    optional = False
                    description = description.replace("(required)", "").strip()

                default = re.findall(DESCRIPTION_DEFAULT_REGEXP, description)
                description = DESCRIPTION_DEFAULT_REGEXP_SUB.sub("", description)
                description = description.replace("<br>", " ")
                if default:
                    default = default[0].strip()
                else:
                    default = None

                return cls(
                    table_type,
                    param=param,
                    description=description,
                    optional=optional,
                    default=default,
                )
            case TableType.name_description, TableType.attribute_description, TableType.field_description:
                name, description = row.split("|")
                name, description = name.strip(), description.strip()
                name = name.strip("*")

                tags = re.findall(DESCRIPTION_KEYWORDS_REGEXP, description)
                description = DESCRIPTION_KEYWORDS_REGEXP_SUB.sub("", description)
                description = description.replace("<br>", " ")
                for i, tag in enumerate(tags):
                    tags[i] = DescriptionKeywords(tag)
                return cls(
                    table_type,
                    name=name,
                    description=description,
                    tags=tags,
                )

    def __repr__(self):
        match self.table_type:
            case TableType.name_type_filtering_description:
                return (
                    f"<TableField name={self.name} type={self.type} filtering={self.filtering} "
                    f"description={self.description} tags={self.tags}>"
                )
            case TableType.name_type_description:
                return f"<TableField name={self.name} type={self.type} description={self.description} tags={self.tags}>"
            case TableType.param_description:
                return (
                    f"<TableField param={self.param} description={self.description} optional={self.optional} "
                    f"default={self.default}>"
                )

    @property
    def required_in_creation(self) -> bool:
        return DescriptionKeywords.necessary_in_creation in self.tags

    @property
    def required_in_response(self) -> bool:
        return DescriptionKeywords.necessary_in_response in self.tags

    @property
    def read_only(self) -> bool:
        return DescriptionKeywords.read_only in self.tags

    @property
    def snake_case_name(self) -> str:
        return to_snake_case(self.name)

    # as a response
    @property
    def class_def_str(self, prefix="\t"):
        return (
            prefix
            + f"{self.snake_case_name}: {self.type.to_def_typehint(self.required_in_response)}"
            # + f"\n{prefix}#" + self.description
        )

    @property
    def docstring(self, prefix="\t"):
        # return prefix + self.name + f" | {self.type} | "
        return f"{prefix}{self.name:25s} | {self.orig_type:20s} | {self.description}"

    @property
    def param_docstring(self, prefix="\t\t"):
        return f"{prefix}:param {self.snake_case_name}: {self.description}"

    def from_json_line(self, prefix="\t\t") -> str:
        return prefix + self.type.to_json_parse(self.snake_case_name, self.name)

    # as a request
    def create_param_str(self, prefix="\t\t\t"):
        if self.read_only:
            raise ValueError(f"Can't create param for read only field: {self.name}")
        if self.required_in_creation:
            return (
                prefix
                + f"{self.snake_case_name}: {self.type.to_param_typehint(not self.optional)}"
            )
        return (
            prefix
            + f"{self.snake_case_name}: typing.Union[Unset, {self.type.to_param_typehint(not self.optional)}] = Unset"
        )

    def init_str(self, prefix="\t\t"):
        if self.read_only:
            raise ValueError(f"Can't create param for read only field: {self.name}")

        return prefix + f"self.{self.snake_case_name} = {self.snake_case_name}"

    def create_to_json_str(self, prefix="\t\t", data_name="json_data"):
        if self.read_only:
            raise ValueError(f"Can't create param for read only field: {self.name}")

        load = self.type.to_request_put_in_json(self.snake_case_name)
        load = f'{data_name}["{self.name}"] = {load}'

        if not self.required_in_creation:
            return f"{prefix}if self.{self.snake_case_name} != Unset:\n{prefix}\t{load}"

        return prefix + load

    # update
    def update_param_str(self, prefix="\t\t\t"):
        if self.read_only:
            raise ValueError(f"Can't create param for read only field: {self.name}")
        return (
            prefix
            + f"{self.snake_case_name}: typing.Union[Unset, {self.type.to_param_typehint(not self.optional)}] = Unset"
        )

    def update_to_json_str(self, prefix="\t\t", data_name="json_data"):
        if self.read_only:
            raise ValueError(f"Can't create param for read only field: {self.name}")

        load = self.type.to_request_put_in_json(self.snake_case_name)
        load = f'{data_name}["{self.name}"] = {load}'

        return f"{prefix}if self.{self.snake_case_name} != Unset:\n{prefix}\t{load}"


class Table:
    rows: typing.List[TableField]
    type: TableType
    class_name = "ChangeMe"
    path = "REPLACEME"

    def __init__(self, header):
        self.rows = []
        if (
            KeywordsTableType.name in header
            and KeywordsTableType.type in header
            and KeywordsTableType.filtering in header
            and KeywordsTableType.description in header
        ):
            self.type = TableType.name_type_filtering_description
        elif (
            KeywordsTableType.name in header
            and KeywordsTableType.type in header
            and KeywordsTableType.description in header
        ):
            self.type = TableType.name_type_description
        elif (
            KeywordsTableType.param in header
            and KeywordsTableType.description in header
        ):
            self.type = TableType.param_description
        elif (
            KeywordsTableType.name in header and KeywordsTableType.description in header
        ):
            self.type = TableType.name_description
        elif (
            KeywordsTableType.attribute in header
            and KeywordsTableType.description in header
        ):
            self.type = TableType.attribute_description
        elif (
            KeywordsTableType.field in header
            and KeywordsTableType.description in header
        ):
            self.type = TableType.field_description
        else:
            raise ValueError(f"Unknown table type. Header: {header}")

        print(f"Entered table type: {self.type}")

    def parse_row(self, row: str):
        self.rows.append(TableField.from_row(row, self.type))

    def __repr__(self):
        return f"<Table type={self.type} rows={self.rows}>"

    @property
    def base_url(self):
        if self.path == "REPLACEME":
            return f"{{helpers.BASE_URL}}/REPLACEME_{self.class_name}"
        return f"{{helpers.BASE_URL}}/{self.path}"

    def to_class_def(self):
        class_name = self.class_name
        ret = f"class {self.class_name}(types.MoySkladBaseClass):\n"
        ret += '\t"""' + "\n"
        for row in self.rows:
            ret += f"{row.docstring}\n"
        ret += '\t"""' + "\n"
        for row in self.rows:
            ret += f"{row.class_def_str}\n"
        ret += "\n"

        prefix = "\t"
        ret += prefix + "@classmethod\n"
        ret += prefix + f'def from_json(cls, dict_data: dict) -> "{self.class_name}":\n'
        prefix += "\t"
        ret += prefix + "instance = cls()\n"
        for row in self.rows:
            ret += row.from_json_line(prefix)
            ret += "\n"
        ret += prefix + "return instance"
        return ret, class_name, None

    def to_create_class(self):
        class_name = f"Create{self.class_name}Request"
        ret = f"class {class_name}(types.ApiRequest):\n"
        prefix = "\t"
        ret += prefix + "def __init__(self,\n"
        prefix += "\t"

        required = []
        not_required = []

        rows = [row for row in self.rows if row.name != "meta" and not row.read_only]

        for row in rows:
            if row.required_in_creation:
                required.append(row.create_param_str(prefix))
            else:
                not_required.append(row.create_param_str(prefix))

        for row in required:
            ret += row + ",\n"

        for row in not_required:
            ret += row + ",\n"

        ret = ret[:-2] + "):\n"

        prefix += "\t"
        # init
        ret += prefix + '"""' + "\n"
        for row in rows:
            ret += row.param_docstring
            ret += "\n"
        ret += prefix + '"""' + "\n"

        for row in rows:
            ret += row.init_str(prefix)
            ret += "\n"
        # to_json
        prefix = prefix[:-2]
        ret += "\n"
        ret += prefix + "def to_request(self) -> RequestData:\n"
        prefix += "\t"
        data_name = "json_data"
        ret += prefix + f"{data_name} = {{}}\n"

        for row in rows:
            ret += row.create_to_json_str(prefix, data_name)
            ret += "\n"

        ret += prefix + "return RequestData(\n"
        prefix += "\t"
        ret += (
            prefix
            + f'method="POST", url=f"{self.base_url}", json={data_name} # TODO: check if URL is correct.\n'
        )
        prefix = prefix[:-1]
        ret += prefix + ")\n\n"

        # from_response

        prefix = prefix[:-1]
        ret += (
            prefix + f"def from_response(self, response: dict) -> {self.class_name}:\n"
        )
        prefix += "\t"
        ret += prefix + f"return {self.class_name}.from_json(response)\n"

        prefix = "\t"

        friendly_method = prefix + "# TODO\n"
        friendly_method += prefix + f"async def {to_snake_case(class_name)}(self, "
        # for row in rows:
        #     friendly_method += row.create_param_str(prefix) + ", "
        for row in required:
            friendly_method += row + ", "
        for row in not_required:
            friendly_method += row + ", "
        friendly_method = (
            friendly_method[:-2] + ") -> placeholder_api." + self.class_name + ":\n"
        )
        prefix += "\t"

        # docstring
        friendly_method += prefix + '"""' + "\n"
        for row in rows:
            friendly_method += row.param_docstring
            friendly_method += "\n"
        friendly_method += prefix + ":return: " + self.class_name + "\n"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + "return await self("
        friendly_method += "placeholder_api." + class_name + "("
        for row in rows:
            friendly_method += row.snake_case_name + "=" + row.snake_case_name + ", "
        friendly_method = friendly_method[:-2] + "))"
        return ret, class_name, friendly_method

    def to_delete_class(self):
        class_name = f"Delete{self.class_name}Request"
        ret = f"class {class_name}(types.ApiRequest):\n"
        prefix = "\t"
        ret += prefix + "def __init__(self, id_: str):\n"
        prefix += "\t"
        ret += prefix + "self.id = id_\n"
        prefix = prefix[:-1]
        ret += "\n"
        ret += prefix + "def to_request(self) -> RequestData:\n"
        prefix += "\t"
        ret += prefix + "return RequestData(\n"
        prefix += "\t"
        ret += (
            prefix
            + f'method="DELETE", url=f"{self.base_url}/{{self.id}}", allow_non_json=True # TODO: check if URL is correct.\n'
        )
        prefix = prefix[:-2]
        ret += prefix + ")\n\n"
        ret += prefix + "def from_response(self, response: dict) -> None:\n"
        prefix += "\t"
        ret += prefix + "return None\n"

        prefix = "\t"
        friendly_method = prefix + "# TODO\n"
        friendly_method += (
            prefix + f"async def {to_snake_case(class_name)}(self, id_: str) -> None:\n"
        )
        prefix += "\t"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + ":param id_: ID объекта для удаления\n"
        friendly_method += prefix + ":return: None\n"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + "return await self("
        friendly_method += "placeholder_api." + class_name + "(id_=id_))"
        return ret, class_name, friendly_method

    def to_update_class(self):
        class_name = f"Update{self.class_name}Request"
        ret = f"class {class_name}(types.ApiRequest):\n"
        prefix = "\t"
        ret += prefix + "def __init__(self, id_: str,\n"
        prefix += "\t"

        rows = [row for row in self.rows if row.name != "meta" and not row.read_only]

        for row in rows:
            ret += row.update_param_str() + ",\n"

        ret = ret[:-2] + "):\n"

        prefix += "\t"
        # init
        ret += prefix + '"""' + "\n"
        ret += prefix[:-1] + ":param id_: ID объекта для обновления\n"
        for row in rows:
            ret += row.param_docstring
            ret += "\n"
        ret += prefix + '"""' + "\n"

        ret += prefix + "self.id = id_\n"
        for row in rows:
            ret += row.init_str(prefix)
            ret += "\n"
        # to_json
        prefix = prefix[:-2]
        ret += "\n"
        ret += prefix + "def to_request(self) -> RequestData:\n"
        prefix += "\t"
        data_name = "json_data"
        ret += prefix + f"{data_name} = {{}}\n"

        for row in rows:
            ret += row.update_to_json_str(prefix, data_name)
            ret += "\n"

        ret += prefix + "return RequestData(\n"
        prefix += "\t"
        ret += (
            prefix
            + f'method="PUT", url=f"{self.base_url}/{{self.id}}", json={data_name} # TODO: check if URL is correct.\n'
        )
        prefix = prefix[:-1]
        ret += prefix + ")\n\n"

        # from_response

        prefix = prefix[:-1]
        ret += (
            prefix + f"def from_response(self, response: dict) -> {self.class_name}:\n"
        )
        prefix += "\t"
        ret += prefix + f"return {self.class_name}.from_json(response)\n"

        prefix = "\t"
        friendly_method = prefix + "# TODO\n"
        friendly_method += (
            prefix + f"async def {to_snake_case(class_name)}(self, id_: str,\n"
        )
        prefix += "\t"
        for row in rows:
            friendly_method += row.update_param_str(prefix) + ",\n"
        friendly_method += prefix + ") -> placeholder_api." + self.class_name + ":\n"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + ":param id_: ID объекта для обновления\n"
        for row in rows:
            friendly_method += row.param_docstring
            friendly_method += "\n"
        friendly_method += prefix + ":return: " + self.class_name + "\n"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + "return await self("
        friendly_method += "placeholder_api." + class_name + "(id_=id_, "
        for row in rows:
            friendly_method += row.snake_case_name + "=" + row.snake_case_name + ", "
        friendly_method = friendly_method[:-2] + "))"

        return ret, class_name, friendly_method

    def to_fetch_class(self):
        if self.class_name.endswith("y"):
            class_name = f"Get{self.class_name[:-1]}iesRequest"
        elif (
            self.class_name.endswith("s")
            or self.class_name.endswith("z")
            or self.class_name.endswith("x")
        ):
            class_name = f"Get{self.class_name}esRequest"
        else:
            class_name = f"Get{self.class_name}sRequest"
        ret = f"class {class_name}(types.ApiRequest):\n"
        prefix = "\t"
        ret += prefix + "def __init__(self,\n"
        prefix += "\t\t"
        ret += (
            prefix + "limit: int = 1000, # TODO: check if it's 1000 for this request\n"
        )
        ret += prefix + "offset: int = 0,\n"
        ret += prefix + "# TODO: check if group_by or filtering is present\n"
        ret += prefix + "):\n"
        prefix += "\t"
        ret += prefix + "self.limit = limit\n"
        ret += prefix + "self.offset = offset\n"

        prefix = prefix[:-3]
        ret += "\n"
        ret += prefix + "def to_request(self) -> RequestData:\n"
        prefix += "\t"
        ret += prefix + f'params = {{"limit": self.limit, "offset": self.offset}}\n'
        ret += prefix + "return RequestData(\n"
        prefix += "\t"
        ret += (
            prefix
            + f'method="GET", url=f"{self.base_url}", params=params # TODO: check if URL is correct.\n'
        )
        prefix = prefix[:-2]
        ret += prefix + ")\n\n"
        ret += (
            prefix
            + f"def from_response(self, response: dict) -> typing.List[{self.class_name}]:\n"
        )
        prefix += "\t"
        ret += (
            prefix
            + f'return [{self.class_name}.from_json(x) for x in response["rows"]]\n'
        )

        prefix = "\t"
        friendly_method = prefix + "# TODO\n"
        friendly_method += (
            prefix
            + f"async def {to_snake_case(class_name)}(self, limit: int = 1000, offset: int = 0) -> typing.List[placeholder_api.{self.class_name}]:\n"
        )
        prefix += "\t"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + ":param limit: Количество элементов в ответе\n"
        friendly_method += prefix + ":param offset: Смещение\n"
        friendly_method += prefix + ":return: typing.List[" + self.class_name + "]\n"
        friendly_method += prefix + '"""' + "\n"
        friendly_method += prefix + "return await self("
        friendly_method += (
            "placeholder_api." + class_name + "(limit=limit, offset=offset))"
        )

        return ret, class_name, friendly_method

    @staticmethod
    def _fmt(s):
        s = s.replace("\t", " " * 4)
        try:
            return black.format_str(s, mode=black.FileMode())
        except Exception as e:
            print(f"Failed to format: {e.__str__() }", file=sys.stderr)
            return s

    def generate(self):
        if (
            self.type == TableType.name_type_filtering_description
            or self.type == TableType.name_type_description
        ):
            fmts, class_names, friendly_methods = [], [], []

            def add(fmt, class_name, friendly_method):
                fmts.append(fmt)
                class_names.append(class_name)
                if friendly_method:
                    friendly_methods.append(friendly_method)

            add(*self.to_class_def())
            add(*self.to_create_class())
            add(*self.to_delete_class())
            add(*self.to_update_class())
            add(*self.to_fetch_class())

            text = "\n\n".join(fmts)
            text = self._fmt(text)

            friendly_methods = "\n\n".join(friendly_methods)
            friendly_methods = self._fmt(friendly_methods)

            return text, class_names, friendly_methods
        else:
            return None, [], None


def parse_doc(doc_url, name="ChangeMe", api_path="REPLACEME"):
    data = requests.get(doc_url).text

    in_table = False
    table: typing.Optional[Table] = None
    tables = []

    class_name = (name, 0)

    def increase_class_name():
        nonlocal class_name
        class_name = (class_name[0], class_name[1] + 1)

    def get_class_name():
        nonlocal class_name
        if class_name[1] == 0:
            return class_name[0]
        return f"{class_name[0]}{class_name[1]}"

    code_name = ""

    for line in data.splitlines():
        line = line.strip()
        if not code_name:
            found = re.findall(r"словом? \*\*(\w+)\*\*", line)
            if found:
                code_name = found[0]
                continue

        if line.startswith("|"):
            if not in_table:
                in_table = True
                table = Table(line)
                table.class_name = get_class_name()
                table.path = api_path
                increase_class_name()
                tables.append(table)
                continue
            if (
                line.startswith("| --")
                or line.startswith("|:--")
                or line == "|"
                or line.startswith("| :-")
            ):
                continue
            if ":--" in line:
                continue
            table.parse_row(line)
        else:
            if in_table:
                in_table = False
                # print("=" * 80)
                # print(f"Finished table: {table}")
                # print(table.generate())
                table = None
    if not code_name:
        raise ValueError("Failed to find code name")
    return tables, code_name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to parse", required=True)
    parser.add_argument(
        "--type",
        help="`documents` or `entities`",
        choices=["documents", "entities"],
        default=None,
    )
    parser.add_argument("--name", help="Class name", default="ChangeMe")
    args = parser.parse_args()
    name = args.name

    if name == "ChangeMe":
        name = args.url.split("/")[-1][1:].replace(".md", "").title()

    url = args.url

    type_ = args.type
    if not type_:
        if "includes/dictionaries" in url:
            type_ = "entities"
        elif "includes/documents" in url:
            type_ = "documents"
        else:
            raise ValueError(f"Failed to determine type for url: {url}")

    print(f"URL: {url}")
    print(f"Type: {type_}")
    print(f"Name: {name}")

    api_path = f"entity/{name.lower()}"

    output = rf"W:\work\projects\dad_of_kesh\moysklad_api\moysklad_api\api\{type_}"

    tables, code_name = parse_doc(args.url, name, api_path)
    tables = [table for table in tables if table.type != TableType.field_description]

    output = output + "/" + code_name

    if os.path.exists(output):
        shutil.rmtree(output)

    os.makedirs(output)
    to_add_to_init = []

    friendly_methods = []

    file_contents = f"""# Auto generated by docs_parser.py
# TODO: validate.
import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData
"""

    for table in tables:
        text, class_names, friendly_method_str = table.generate()
        if text is None:
            continue
        to_add_to_init.extend(class_names)
        file_contents += text
        file_contents += "\n\n"

        friendly_methods.append(friendly_method_str)

    try:
        file_contents = black.format_str(file_contents, mode=black.FileMode())
    except Exception as e:
        print(f"Failed to format: {e.__str__() }", file=sys.stderr)

    with open(output + f"/{code_name}.py", "w", encoding="UTF-8") as f:
        f.write(file_contents)

    init_contents = f"""# Auto generated by docs_parser.py
from .{code_name} import {", ".join(to_add_to_init)}

__all__ = [{", ".join([f'"{x}"' for x in to_add_to_init])}]
"""

    try:
        init_contents = black.format_str(init_contents, mode=black.FileMode())
    except Exception as e:
        print(f"Failed to format: {e.__str__() }", file=sys.stderr)

    with open(output + f"/__init__.py", "w", encoding="UTF-8") as f:
        f.write(init_contents)

    friendly_methods = "\n\n".join(friendly_methods)
    friendly_methods = "class DummyDeleteMe:\n" + friendly_methods
    friendly_methods = friendly_methods.replace("placeholder_api", f"{code_name}_api")

    import_ = f"from ..api.{type_} import {code_name} as {code_name}_api"

    try:
        friendly_methods = black.format_str(friendly_methods, mode=black.FileMode())
    except Exception as e:
        # for some reason it raises an error, but it works fine?..
        pass
    friendly_methods = "\n".join(friendly_methods.splitlines()[1:])
    print(import_)
    print()
    print(friendly_methods)


if __name__ == "__main__":
    main()

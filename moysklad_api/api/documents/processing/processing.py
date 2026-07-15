import datetime
import typing

from .... import types, helpers
from ....types import Unset, RequestData


class Processing(types.MoySkladBaseClass):
    """Техоперация (entity/processing)."""

    account_id: typing.Optional[str]
    applicable: typing.Optional[bool]
    attributes: typing.Optional[typing.List[dict]]
    code: typing.Optional[str]
    created: typing.Optional[datetime.datetime]
    deleted: typing.Optional[datetime.datetime]
    description: typing.Optional[str]
    external_code: typing.Optional[str]
    files: typing.Optional[dict]
    group: typing.Optional[types.Meta]
    id: typing.Optional[str]
    materials: typing.Optional[typing.List[dict]]
    materials_store: typing.Optional[types.Meta]
    meta: typing.Optional[types.Meta]
    moment: typing.Optional[datetime.datetime]
    name: typing.Optional[str]
    organization: typing.Optional[types.Meta]
    organization_account: typing.Optional[types.Meta]
    owner: typing.Optional[types.Meta]
    printed: typing.Optional[bool]
    processing_plan: typing.Optional[types.Meta]
    processing_sum: typing.Optional[int]
    products: typing.Optional[typing.List[dict]]
    products_store: typing.Optional[types.Meta]
    project: typing.Optional[types.Meta]
    published: typing.Optional[bool]
    quantity: typing.Optional[float]
    shared: typing.Optional[bool]
    state: typing.Optional[types.Meta]
    sync_id: typing.Optional[str]
    updated: typing.Optional[datetime.datetime]
    processing_order: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Processing":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.applicable = dict_data.get("applicable")
        instance.attributes = dict_data.get("attributes")
        instance.code = dict_data.get("code")
        instance.created = helpers.parse_date(dict_data.get("created"))
        instance.deleted = helpers.parse_date(dict_data.get("deleted"))
        instance.description = dict_data.get("description")
        instance.external_code = dict_data.get("externalCode")
        instance.files = dict_data.get("files")
        instance.group = helpers.get_meta(dict_data.get("group"))
        instance.id = dict_data.get("id")
        instance.materials = dict_data.get("materials")
        instance.materials_store = helpers.get_meta(dict_data.get("materialsStore"))
        instance.meta = dict_data.get("meta")
        instance.moment = helpers.parse_date(dict_data.get("moment"))
        instance.name = dict_data.get("name")
        instance.organization = helpers.get_meta(dict_data.get("organization"))
        instance.organization_account = helpers.get_meta(
            dict_data.get("organizationAccount")
        )
        instance.owner = helpers.get_meta(dict_data.get("owner"))
        instance.printed = dict_data.get("printed")
        instance.processing_plan = helpers.get_meta(dict_data.get("processingPlan"))
        instance.processing_sum = dict_data.get("processingSum")
        instance.products = dict_data.get("products")
        instance.products_store = helpers.get_meta(dict_data.get("productsStore"))
        instance.project = helpers.get_meta(dict_data.get("project"))
        instance.published = dict_data.get("published")
        instance.quantity = dict_data.get("quantity")
        instance.shared = dict_data.get("shared")
        instance.state = helpers.get_meta(dict_data.get("state"))
        instance.sync_id = dict_data.get("syncId")
        instance.updated = helpers.parse_date(dict_data.get("updated"))
        instance.processing_order = helpers.get_meta(dict_data.get("processingOrder"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return ("processing",)


class Material(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    quantity: typing.Optional[float]
    slot: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Material":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.quantity = dict_data.get("quantity")
        instance.slot = helpers.get_meta(dict_data.get("slot"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "processing", "materials"


class Product(types.MoySkladBaseClass):
    account_id: typing.Optional[str]
    assortment: typing.Optional[types.Meta]
    id: typing.Optional[str]
    quantity: typing.Optional[float]
    slot: typing.Optional[types.Meta]

    @classmethod
    def from_json(cls, dict_data: dict) -> "Product":
        instance = cls()
        instance.account_id = dict_data.get("accountId")
        instance.assortment = helpers.get_meta(dict_data.get("assortment"))
        instance.id = dict_data.get("id")
        instance.quantity = dict_data.get("quantity")
        instance.slot = helpers.get_meta(dict_data.get("slot"))
        return instance

    @staticmethod
    def ms_name() -> typing.Optional[typing.Tuple[str]]:
        return "processing", "products"


def _build_json(
    organization: typing.Union[Unset, types.Meta] = Unset,
    products_store: typing.Union[Unset, types.Meta] = Unset,
    materials_store: typing.Union[Unset, types.Meta] = Unset,
    processing_plan: typing.Union[Unset, types.Meta] = Unset,
    applicable: typing.Union[Unset, bool] = Unset,
    attributes: typing.Union[Unset, typing.List[dict]] = Unset,
    code: typing.Union[Unset, str] = Unset,
    description: typing.Union[Unset, str] = Unset,
    external_code: typing.Union[Unset, str] = Unset,
    files: typing.Union[Unset, types.MetaArray] = Unset,
    group: typing.Union[Unset, types.Meta] = Unset,
    materials: typing.Union[Unset, typing.List[dict]] = Unset,
    moment: typing.Union[Unset, datetime.datetime] = Unset,
    name: typing.Union[Unset, str] = Unset,
    organization_account: typing.Union[Unset, types.Meta] = Unset,
    owner: typing.Union[Unset, types.Meta] = Unset,
    processing_sum: typing.Union[Unset, int] = Unset,
    products: typing.Union[Unset, typing.List[dict]] = Unset,
    project: typing.Union[Unset, types.Meta] = Unset,
    quantity: typing.Union[Unset, float] = Unset,
    shared: typing.Union[Unset, bool] = Unset,
    state: typing.Union[Unset, types.Meta] = Unset,
    sync_id: typing.Union[Unset, str] = Unset,
) -> dict:
    json_data = {}
    if organization != Unset:
        json_data["organization"] = {"meta": organization}
    if products_store != Unset:
        json_data["productsStore"] = {"meta": products_store}
    if materials_store != Unset:
        json_data["materialsStore"] = {"meta": materials_store}
    if processing_plan != Unset:
        json_data["processingPlan"] = {"meta": processing_plan}
    if applicable != Unset:
        json_data["applicable"] = applicable
    if attributes != Unset:
        json_data["attributes"] = attributes
    if code != Unset:
        json_data["code"] = code
    if description != Unset:
        json_data["description"] = description
    if external_code != Unset:
        json_data["externalCode"] = external_code
    if files != Unset:
        json_data["files"] = files
    if group != Unset:
        json_data["group"] = {"meta": group}
    if materials != Unset:
        json_data["materials"] = []
        for material in materials:
            new_material: dict = material.copy()
            new_material["assortment"] = {"meta": new_material["assortment"]}
            if "slot" in new_material:
                new_material["slot"] = {"meta": new_material["slot"]}
            json_data["materials"].append(new_material)
    if moment != Unset:
        json_data["moment"] = helpers.date_to_str(moment)
    if name != Unset:
        json_data["name"] = name
    if organization_account != Unset:
        json_data["organizationAccount"] = {"meta": organization_account}
    if owner != Unset:
        json_data["owner"] = {"meta": owner}
    if processing_sum != Unset:
        json_data["processingSum"] = processing_sum
    if products != Unset:
        json_data["products"] = []
        for product in products:
            new_product: dict = product.copy()
            new_product["assortment"] = {"meta": new_product["assortment"]}
            if "slot" in new_product:
                new_product["slot"] = {"meta": new_product["slot"]}
            json_data["products"].append(new_product)
    if project != Unset:
        json_data["project"] = {"meta": project}
    if quantity != Unset:
        json_data["quantity"] = quantity
    if shared != Unset:
        json_data["shared"] = shared
    if state != Unset:
        json_data["state"] = {"meta": state}
    if sync_id != Unset:
        json_data["syncId"] = sync_id
    return json_data


class GetProcessingsRequest(types.ApiRequest):
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
            method="GET", url=f"{helpers.BASE_URL}/entity/processing", params=params
        )

    def from_response(self, result: dict) -> typing.List[Processing]:
        return [Processing.from_json(x) for x in result["rows"]]


class CreateProcessingRequest(types.ApiRequest):
    class MaterialOrProduct(typing.TypedDict):
        assortment: types.Meta
        quantity: float
        slot: typing.NotRequired[types.Meta]

    def __init__(
        self,
        organization: types.Meta,
        products_store: types.Meta,
        materials_store: types.Meta,
        processing_plan: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        materials: typing.Union[Unset, typing.List[MaterialOrProduct]] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        processing_sum: typing.Union[Unset, int] = Unset,
        products: typing.Union[Unset, typing.List[MaterialOrProduct]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.organization = organization
        self.products_store = products_store
        self.materials_store = materials_store
        self.processing_plan = processing_plan
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.materials = materials
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.processing_sum = processing_sum
        self.products = products
        self.project = project
        self.quantity = quantity
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            products_store=self.products_store,
            materials_store=self.materials_store,
            processing_plan=self.processing_plan,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            materials=self.materials,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            processing_sum=self.processing_sum,
            products=self.products,
            project=self.project,
            quantity=self.quantity,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="POST", url=f"{helpers.BASE_URL}/entity/processing", json=json_data
        )

    def from_response(self, result: dict) -> Processing:
        return Processing.from_json(result)


class DeleteProcessingRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processing/{self.id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProcessingRequest(types.ApiRequest):
    def __init__(self, id_: str):
        self.id = id_

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET", url=f"{helpers.BASE_URL}/entity/processing/{self.id}"
        )

    def from_response(self, result: dict) -> Processing:
        return Processing.from_json(result)


class UpdateProcessingRequest(types.ApiRequest):
    MaterialOrProduct = CreateProcessingRequest.MaterialOrProduct

    def __init__(
        self,
        id_: str,
        organization: typing.Union[Unset, types.Meta] = Unset,
        products_store: typing.Union[Unset, types.Meta] = Unset,
        materials_store: typing.Union[Unset, types.Meta] = Unset,
        processing_plan: typing.Union[Unset, types.Meta] = Unset,
        applicable: typing.Union[Unset, bool] = Unset,
        attributes: typing.Union[Unset, typing.List[dict]] = Unset,
        code: typing.Union[Unset, str] = Unset,
        description: typing.Union[Unset, str] = Unset,
        external_code: typing.Union[Unset, str] = Unset,
        files: typing.Union[Unset, types.MetaArray] = Unset,
        group: typing.Union[Unset, types.Meta] = Unset,
        materials: typing.Union[Unset, typing.List[MaterialOrProduct]] = Unset,
        moment: typing.Union[Unset, datetime.datetime] = Unset,
        name: typing.Union[Unset, str] = Unset,
        organization_account: typing.Union[Unset, types.Meta] = Unset,
        owner: typing.Union[Unset, types.Meta] = Unset,
        processing_sum: typing.Union[Unset, int] = Unset,
        products: typing.Union[Unset, typing.List[MaterialOrProduct]] = Unset,
        project: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        shared: typing.Union[Unset, bool] = Unset,
        state: typing.Union[Unset, types.Meta] = Unset,
        sync_id: typing.Union[Unset, str] = Unset,
    ):
        self.id = id_
        self.organization = organization
        self.products_store = products_store
        self.materials_store = materials_store
        self.processing_plan = processing_plan
        self.applicable = applicable
        self.attributes = attributes
        self.code = code
        self.description = description
        self.external_code = external_code
        self.files = files
        self.group = group
        self.materials = materials
        self.moment = moment
        self.name = name
        self.organization_account = organization_account
        self.owner = owner
        self.processing_sum = processing_sum
        self.products = products
        self.project = project
        self.quantity = quantity
        self.shared = shared
        self.state = state
        self.sync_id = sync_id

    def to_request(self) -> RequestData:
        json_data = _build_json(
            organization=self.organization,
            products_store=self.products_store,
            materials_store=self.materials_store,
            processing_plan=self.processing_plan,
            applicable=self.applicable,
            attributes=self.attributes,
            code=self.code,
            description=self.description,
            external_code=self.external_code,
            files=self.files,
            group=self.group,
            materials=self.materials,
            moment=self.moment,
            name=self.name,
            organization_account=self.organization_account,
            owner=self.owner,
            processing_sum=self.processing_sum,
            products=self.products,
            project=self.project,
            quantity=self.quantity,
            shared=self.shared,
            state=self.state,
            sync_id=self.sync_id,
        )
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processing/{self.id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Processing:
        return Processing.from_json(result)


class GetProcessingMaterialsRequest(types.ApiRequest):
    def __init__(
        self,
        processing_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processing_id = processing_id
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
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/materials",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Material]:
        return [Material.from_json(x) for x in result["rows"]]


class GetProcessingMaterialRequest(types.ApiRequest):
    def __init__(self, processing_id: str, material_id: str):
        self.processing_id = processing_id
        self.material_id = material_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/materials/{self.material_id}",
        )

    def from_response(self, result: dict) -> Material:
        return Material.from_json(result)


class CreateProcessingMaterialRequest(types.ApiRequest):
    """Добавить материал. Ответ API - список материалов (в т.ч. добавленный)."""

    def __init__(
        self,
        processing_id: str,
        assortment: types.Meta,
        quantity: float,
        slot: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.processing_id = processing_id
        self.assortment = assortment
        self.quantity = quantity
        self.slot = slot

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.slot != Unset:
            json_data["slot"] = {"meta": self.slot}
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/materials",
            json=json_data,
        )

    def from_response(self, result: typing.List[dict]) -> typing.List[Material]:
        return [Material.from_json(x) for x in result]


class UpdateProcessingMaterialRequest(types.ApiRequest):
    def __init__(
        self,
        processing_id: str,
        material_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        slot: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.processing_id = processing_id
        self.material_id = material_id
        self.assortment = assortment
        self.quantity = quantity
        self.slot = slot

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.slot != Unset:
            json_data["slot"] = {"meta": self.slot}
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/materials/{self.material_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Material:
        return Material.from_json(result)


class DeleteProcessingMaterialRequest(types.ApiRequest):
    def __init__(self, processing_id: str, material_id: str):
        self.processing_id = processing_id
        self.material_id = material_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/materials/{self.material_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None


class GetProcessingProductsRequest(types.ApiRequest):
    def __init__(
        self,
        processing_id: str,
        limit: typing.Union[Unset, int] = Unset,
        offset: typing.Union[Unset, int] = Unset,
    ):
        self.processing_id = processing_id
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
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/products",
            params=params,
        )

    def from_response(self, result: dict) -> typing.List[Product]:
        return [Product.from_json(x) for x in result["rows"]]


class GetProcessingProductRequest(types.ApiRequest):
    def __init__(self, processing_id: str, product_id: str):
        self.processing_id = processing_id
        self.product_id = product_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="GET",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/products/{self.product_id}",
        )

    def from_response(self, result: dict) -> Product:
        return Product.from_json(result)


class CreateProcessingProductRequest(types.ApiRequest):
    """Добавить продукт. Ответ API - список продуктов (в т.ч. добавленный)."""

    def __init__(
        self,
        processing_id: str,
        assortment: types.Meta,
        quantity: float,
        slot: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.processing_id = processing_id
        self.assortment = assortment
        self.quantity = quantity
        self.slot = slot

    def to_request(self) -> RequestData:
        json_data = {
            "assortment": {"meta": self.assortment},
            "quantity": self.quantity,
        }
        if self.slot != Unset:
            json_data["slot"] = {"meta": self.slot}
        return RequestData(
            method="POST",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/products",
            json=json_data,
        )

    def from_response(self, result: typing.List[dict]) -> typing.List[Product]:
        return [Product.from_json(x) for x in result]


class UpdateProcessingProductRequest(types.ApiRequest):
    def __init__(
        self,
        processing_id: str,
        product_id: str,
        assortment: typing.Union[Unset, types.Meta] = Unset,
        quantity: typing.Union[Unset, float] = Unset,
        slot: typing.Union[Unset, types.Meta] = Unset,
    ):
        self.processing_id = processing_id
        self.product_id = product_id
        self.assortment = assortment
        self.quantity = quantity
        self.slot = slot

    def to_request(self) -> RequestData:
        json_data = {}
        if self.assortment != Unset:
            json_data["assortment"] = {"meta": self.assortment}
        if self.quantity != Unset:
            json_data["quantity"] = self.quantity
        if self.slot != Unset:
            json_data["slot"] = {"meta": self.slot}
        return RequestData(
            method="PUT",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/products/{self.product_id}",
            json=json_data,
        )

    def from_response(self, result: dict) -> Product:
        return Product.from_json(result)


class DeleteProcessingProductRequest(types.ApiRequest):
    def __init__(self, processing_id: str, product_id: str):
        self.processing_id = processing_id
        self.product_id = product_id

    def to_request(self) -> RequestData:
        return RequestData(
            method="DELETE",
            url=f"{helpers.BASE_URL}/entity/processing/{self.processing_id}/products/{self.product_id}",
            allow_non_json=True,
        )

    def from_response(self, result: dict) -> None:
        return None

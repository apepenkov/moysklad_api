> MoySklad API
> ==========
---
## This is an _async_ python3.6+ wrapper for the MoySklad API. It is a work in progress.


# Structure
The MoySklad API is structured as follows:

* `moysklad_api/api/*` - contains raw API calls, and classes.
* `moysklad_api/errors` - contains error class
* `moysklad_api/types` - contains some common classes, such as 
  * ApiRequest (base for all API requests)
  * MoySkladBaseClass (base for all MoySklad classes)
  * typehinted dicts. (for example, `Meta` is a dict with type hints for all keys: {href: str, type: str, mediaType: str, ...})
* `moysklad/client` - contains the main client class (wrapper for the API).

# Api calls
Each Api caller is an instance of
```python
class ApiRequest:
    # method: typing.Literal["GET", "POST", "PUT", "DELETE", "PATCH"], url: str, **kwargs
    def to_request(self) -> dict:
        raise NotImplementedError

    def from_response(self, result):
        raise NotImplementedError
```
Example of an ApiRequest:
```python
class GetOrderPositionRequest(types.ApiRequest):
  """
  https://dev.moysklad.ru/doc/api/remap/1.2/documents/#dokumenty-vnutrennij-zakaz-poluchit-poziciu

  Get position by its id from order by order and positions id
  Получить позицию по ее id из заказа по id заказа и позиции
  """

  def __init__(
          self,
          order_id: str,
          position_id: str,
  ):
    """

    :param order_id: order id (id заказа)
    :param position_id: position id (id позиции)
    """
    self.order_id = order_id
    self.position_id = position_id

  def to_request(
          self,
  ) -> dict:
    return {
      "method": "GET",
      "url": f"https://online.moysklad.ru/api/remap/1.2/entity/internalorder/{self.order_id}/positions/{self.position_id}",
    }

  def from_response(self, response: dict) -> Position:
    return Position.json_parse(response)
```
When you want to call API, you have to either use wrapped method from `client`, or
call it via 
```python
await client(GetOrderPositionRequest(order_id="...", position_id="..."))
```
It will:
1. Call `GetOrderPositionRequest.to_request()`
2. Use returned dict to make a request (populating api_key, etc)
3. Call `GetOrderPositionRequest.from_response()` with the result of the request as an argument, and return the result.

Alternatively, you can use: (preferred way, as it provides typehints)
```python
await client.get_order_position(order_id="...", position_id="...")
```

`ApiRequest`s may have such arguments, as:
* basic python types (int, str, list, bool, etc)
* `datetime.datetime` (will be converted according to specification)
* **type-hinted dicts** (aka `typing.TypedDict`) from `moysklad_api/types` (`Meta` included)
* classes. If class is required, it may be nested in ApiRequest itself, or used from some api file.


# Meta
Meta is used in a lot of requests, so I want to clarify its usage.
You can either use `types.Meta`, or just pass the dict.

Example: (creating `CreatePosition` class and then using it in `CreateInternalOrderRequest`)
```python
position = internalorder.CreateInternalOrder.CreatePosition(
  quantity=1,
  price=0,
  discount=0,
  vat=0,
  assortment=types.Meta( # Using types.Meta
      href=f"https://online.moysklad.ru/api/remap/1.2/entity/product/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      metadataHref="https://online.moysklad.ru/api/remap/1.2/entity/product/metadata",
      type="product",
      mediaType="application/json",
  ),
)
response = await moysklad_client.create_internal_order(
  name="No name",
  description="Some description",
  organization=types.Meta(
    href="https://online.moysklad.ru/api/remap/1.2/entity/organization/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    metadataHref="https://online.moysklad.ru/api/remap/1.2/entity/organization/metadata",
    type="organization",
    mediaType="application/json",
  ),
  store=types.Meta(
      href="https://online.moysklad.ru/api/remap/1.2/entity/store/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      metadataHref="https://online.moysklad.ru/api/remap/1.2/entity/store/metadata",
      type="store",
      mediaType="application/json",
  ),
  positions=[position],
  attributes=[
    {
      "meta": { # Using dict
        "href": "https://online.moysklad.ru/api/remap/1.2/entity/internalorder/metadata/attributes/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        "type": "attributemetadata",
        "mediaType": "application/json",
      },
      "id": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
      "name": "Custom parameter name",
      "value": {
        "meta": {
          "href": "https://online.moysklad.ru/api/remap/1.2/entity/store/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
          "metadataHref": "https://online.moysklad.ru/api/remap/1.2/entity/store/metadata",
          "type": "store",
          "mediaType": "application/json",
          "uuidHref": "https://online.moysklad.ru/app/#warehouse/edit?id=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        },
      },
    }
  ]
)
```
# Type hints

**All requests are type-hinted**, so you can use IDE's autocomplete to find out what arguments are required.

Also each request class includes a link to the documentation, and a description of the arguments.

Responses are only type-hinted, if you use wrapped methods from `client`, or if you use `from_response` method.

I would highly recommend looking at type hints, as they are very informative.



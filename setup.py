from setuptools import setup

setup(
    name="moysklad_api",
    version="",
    packages=[
        "moysklad_api",
        "moysklad_api.api",
        "moysklad_api.api.entities",
        "moysklad_api.api.entities.internalorders",
        "moysklad_api.api.entities.products",
        "moysklad_api.api.entities.moves",
        "moysklad_api.api.entities.purchaseorders",
        "moysklad_api.api.entities.productfolders",
        "moysklad_api.api.entities.enters",
        "moysklad_api.api.reports",
        "moysklad_api.api.reports.stocks",
        "moysklad_api.types",
        "moysklad_api.client",
        "moysklad_api.errors",
    ],
    url="",
    license="",
    author="apepenkov",
    author_email="",
    description="",
)

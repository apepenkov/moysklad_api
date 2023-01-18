from setuptools import setup
import shutil

setup(
    name="moysklad_api",
    version="",
    packages=[
        "moysklad_api",
        "moysklad_api.api",
        "moysklad_api.api.entities",
        "moysklad_api.api.entities.internalorder",
        "moysklad_api.api.entities.products",
        "moysklad_api.api.entities.move",
        "moysklad_api.api.entities.purchaseorder",
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

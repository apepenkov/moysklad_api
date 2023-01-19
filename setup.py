from setuptools import setup
import shutil

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

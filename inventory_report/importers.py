from abc import ABC, abstractmethod
import csv
from typing import Dict, Type

from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        raise NotImplementedError("Method not implemented")


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            return [Product(**product) for product in json.loads(file.read())]


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            return [
                Product(
                    id=product["id"],
                    product_name=product["product_name"],
                    company_name=product["company_name"],
                    manufacturing_date=product["manufacturing_date"],
                    expiration_date=product["expiration_date"],
                    serial_number=product["serial_number"],
                    storage_instructions=product["storage_instructions"],
                )
                for product in csv.DictReader(file)
            ]


IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

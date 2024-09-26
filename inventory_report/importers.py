from abc import ABC, abstractmethod
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


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
if __name__ == "__main__":
    json_importer = JsonImporter("tests/mocks/inventory.json")
    print(json_importer.import_data())

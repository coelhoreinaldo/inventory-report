from typing import Union

from inventory_report.importers import IMPORTERS
from inventory_report.inventory import Inventory
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

REPORT_TYPES = {"simple": SimpleReport, "complete": CompleteReport}


def create_inventory(file_paths: list[str]) -> Inventory:
    inventory = Inventory()

    for path in file_paths:
        extension = path.split(".")[-1]

        if extension not in IMPORTERS:
            continue

        products = IMPORTERS[extension](path).import_data()
        inventory.add_data(products)

    return inventory


def create_report(
    inventory: Inventory,
    report_type: str,
) -> Union[SimpleReport, CompleteReport]:
    if report_type not in REPORT_TYPES:
        raise ValueError("Report type is invalid.")

    REPORT = REPORT_TYPES[report_type]()
    REPORT.add_inventory(inventory)
    return REPORT


def process_report_request(file_paths: list[str], report_type: str) -> str:
    report_type = report_type.lower()
    inventory = create_inventory(file_paths)
    report = create_report(inventory, report_type)

    return report.generate()

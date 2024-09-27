from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self):
        simple_report = super().generate()
        all_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
        ]
        company_counter = Counter(
            [product.company_name for product in all_products]
        )
        stocked_products_by_company = [
            f"- {company}: {count}\n"
            for company, count in company_counter.items()
        ]
        return (
            simple_report
            + "\nStocked products by company:\n"
            + "".join(stocked_products_by_company)
        )

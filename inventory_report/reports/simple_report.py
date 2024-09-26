from collections import Counter
from datetime import datetime, date

from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self):
        self.inventories = []

    def add_inventory(self, inventory):
        self.inventories.append(inventory)

    def generate(self):
        oldest_manufacturing_date = date.max
        closest_expiration_date = date.max
        company_counter = Counter()

        for inventory in self.inventories:
            for product in inventory.data:
                manufacturing_date = date.fromisoformat(
                    product.manufacturing_date
                )
                expiration_date = date.fromisoformat(product.expiration_date)

                if manufacturing_date < oldest_manufacturing_date:
                    oldest_manufacturing_date = manufacturing_date

                if (
                    expiration_date > datetime.now().date()
                    and expiration_date < closest_expiration_date
                ):
                    closest_expiration_date = expiration_date

                company_counter[product.company_name] += 1

        company_with_largest_inventory = company_counter.most_common(1)[0][0]

        return (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {company_with_largest_inventory}"
        )

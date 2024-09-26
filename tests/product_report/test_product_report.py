from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "1",
        "Product Name",
        "Company Name",
        "01/01/2023",
        "01/01/2024",
        "123456",
        "Storage instructions",
    )

    assert product.__str__() == (
        "The product 1 - Product Name with serial number 123456 "
        "manufactured on 01/01/2023 by the company Company Name "
        "valid until 01/01/2024 must be stored according to the "
        "following instructions: Storage instructions."
    )

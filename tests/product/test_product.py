from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "Product Name",
        "Company Name",
        "01/01/2023",
        "01/01/2024",
        "123456",
        "Storage instructions",
    )

    assert product.id == "1"
    assert product.product_name == "Product Name"
    assert product.company_name == "Company Name"
    assert product.manufacturing_date == "01/01/2023"
    assert product.expiration_date == "01/01/2024"
    assert product.serial_number == "123456"
    assert product.storage_instructions == "Storage instructions"

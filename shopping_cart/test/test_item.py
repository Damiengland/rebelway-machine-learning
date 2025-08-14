from shopping_cart.item import Item

def test_item_price() -> None:
    item = Item("Car", "Vehicle", 20000.99)
    assert item.price >= 0.0 or item.price == 20000.99

def test_item_name() -> None:
    item = Item("A", "B", 10.99)
    assert len(item.name) > 0
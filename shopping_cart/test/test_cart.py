import pytest
from shopping_cart.item import Item
from shopping_cart.cart import Cart

@pytest.fixture
def cart() -> Cart:
    cart = Cart(database_path="./test/test_database.json")
    cart.empty_cart()
    return cart

def test_total_price_of_cart(cart):
    item1 = Item("car", "vehicle", 20000.00)
    item2 = Item("bike", "vehicle", 1500.00)
    cart.add_item_to_cart(item1)
    cart.add_item_to_cart(item2)
    assert cart.get_total_price_of_items() == 21500.00

def test_empty_cart(cart):
    item1 = Item("a", "b", 1.2)
    cart.add_item_to_cart(item1)
    cart.empty_cart()
    assert len(cart.get_all_items()["Items"].items()) == 0

def test_search_item(cart):
    item = Item("laptop", "electronics", 999.99)
    cart.add_item_to_cart(item)
    items_list = cart.search_items("laptop")
    assert items_list[0].name == "laptop"

def test_get_all_items(cart):
    item1 = Item("laptop", "electronics", 999.99)
    item2 = Item("phone", "electronics", 499.99)
    cart.add_item_to_cart(item1)
    cart.add_item_to_cart(item2)
    all_items = cart.get_all_items()
    names_to_compare = [item1.name, item2.name]
    results = [item_data['name'] for item_id, item_data in all_items["Items"].items()]
    assert names_to_compare == results

def test_get_total_item_count(cart):
    item1 = Item("laptop", "electronics", 999.99)
    item2 = Item("phone", "electronics", 499.99)
    cart.add_item_to_cart(item1)
    cart.add_item_to_cart(item2)
    assert cart.get_total_item_count() == 2
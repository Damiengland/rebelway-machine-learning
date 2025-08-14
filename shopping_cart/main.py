from shopping_cart.item import Item
from shopping_cart.cart import Cart
from pathlib import Path

if __name__ == "__main__":

    # the main database for the cart to pass to the class
        # Get the directory where this script file is located
    script_dir = Path(__file__).parent
    database = f"{script_dir}/database.json"
    my_cart = Cart(database_path=database)

    #search for an item
    print("Searching for an item...")
    result = my_cart.search_items("apple")
    print("------------------------")

    # get the total amount of items in the cart
    print("Total items in cart:")
    total_items = my_cart.get_total_item_count()
    print(f"Total items count: {total_items}")
    print("------------------------")

    # Create an Item object
    print("Adding items to cart...")
    new_item = Item(name="milk", _price=0.99, type="dairy")
    my_cart.add_item_to_cart(new_item)
    print("------------------------")

    # get all the items in the cart
    print("Current items in cart:")
    my_cart.get_all_items(verbose=1)
    print("------------------------")

    # remove all items by name
    print("Removing items by name...")
    my_cart.remove_items_from_cart_by_query('milk')
    print("------------------------")

    # get all the items in the cart
    print("Current items in cart:")
    my_cart.get_all_items(verbose=1)
    print("------------------------")

    # get total price
    print("Total price:")
    total_price = my_cart.get_total_price_of_items()
    print(f"${round(total_price, 2)}")
    print("------------------------")

    # clear cart
    # print("Clearing cart...")
    # my_cart.empty_cart()
    
    
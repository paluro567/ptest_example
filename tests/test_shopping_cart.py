from shopping_cart.shopping_cart import ShoppingCart
import pytest
'''
using pytest, from the terminal in the directory of the project, 
simply run "$pytest" and all files  with the name "test_%" 
or "%_test%" will be tested and all functions with the same 
naming will be executed
'''


def test_can_add_item_to_cart():
    cart= ShoppingCart(5)
    cart.add("apple")
    assert cart.size()==1

def test_when_item_added_then_cart_contains_item():
    cart=ShoppingCart(5)
    cart.add("apple")
    assert ["apple"] ==cart.get_items()


# pass the test when an error is thrown
def test_when_add_past_max_size():
    cart=ShoppingCart(5)
    for _ in range(5):  # add m "max size" of items in the cart
            cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")  # adds one more to trigger overflow


def test_get_total_price():
    cart=ShoppingCart(5)
    cart.add("apple")
    cart.add("orange")
    prices={
        "apple":1.0,
        "orange":2.0
    }
    assert cart.get_total_price(prices)==3

    

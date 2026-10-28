from cart import new_cart



def test_new_cart():
    cart1 = new_cart("bob")
    cart2 = new_cart("ann")

    assert not cart2["items"] is cart1["items"]

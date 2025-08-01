from Salad import Salad
from CustomSalad import CustomSalad
from SpecialtySalad import SpecialtySalad
from SaladOrder import SaladOrder
from OrderQueue import OrderQueue

def test_salad_class():
    s = Salad("S", 8.75)
    assert s.get_price() == 8.75
    assert s.get_size() == "S"
    s.set_price(9.55)
    assert s.get_price() == 9.55
    s.set_size("M")
    assert s.get_size() == "M"

def test_custom_salad():
    cs1 = CustomSalad("L")
    cs1.add_topping("chicken")
    cs1.add_topping("cucumbers")

    assert cs1.get_salad_details() == \
"""\
CUSTOM SALAD
Size: L
Toppings:
\t+ chicken
\t+ cucumbers
Price: $18.75
"""
    cs2 = CustomSalad("S")
    cs2.add_topping("chicken")
    assert cs2.get_salad_details() == \
"""\
CUSTOM SALAD
Size: S
Toppings:
\t+ chicken
Price: $10.50
"""
    cs3 = CustomSalad("M")
    assert cs3.get_salad_details() == \
"""\
CUSTOM SALAD
Size: M
Toppings:
Price: $10.75
"""
    cs3.add_topping("chicken")
    assert cs3.get_salad_details() == \
"""\
CUSTOM SALAD
Size: M
Toppings:
\t+ chicken
Price: $13.25
"""

def test_specialty_and_salad_order():
    cs1 = CustomSalad("S")
    cs1.add_topping("chicken")
    cs1.add_topping("cucumber")
    ss1 = SpecialtySalad("S", "Cobb")
    order = SaladOrder(123000) #12:30:00PM
    order.add_salad(cs1)
    order.add_salad(ss1)
    assert order.get_time() == 123000
    order2 = SaladOrder(133000)
    assert order2.__lt__(order) == False
    assert order.info() == \
"""\
***
Order Time: 123000
CUSTOM SALAD
Size: S
Toppings:
\t+ chicken
\t+ cucumber
Price: $12.25

----
SPECIALTY SALAD
Size: S
Name: Cobb
Price: $12.50

----
TOTAL ORDER PRICE: $24.75
***
"""

def test_order_queue():
    oq = OrderQueue()
    assert oq.process_next_order() == ""

    o1 = SaladOrder(123000)  # 12:30:00PM
    oq1 = OrderQueue()
    oq1.add_order(o1)
    assert oq1.process_next_order() == \
"""\
***
Order Time: 123000
TOTAL ORDER PRICE: $0.00
***
"""

    o2 = SaladOrder(123000)  # 12:30:00PM
    oq2 = OrderQueue()
    oq2.add_order(o2)
    assert oq2.process_next_order() == \
"""\
***
Order Time: 123000
TOTAL ORDER PRICE: $0.00
***
"""

    o1 = SaladOrder(123000)  # 12:30:00PM
    o2 = SaladOrder(130000)  # 01:00:00PM
    o3 = SaladOrder(115000)  # 11:30:00AM
    order_queue = OrderQueue()
    order_queue.add_order(o1)
    order_queue.add_order(o2)
    order_queue.add_order(o3)
    assert order_queue.process_next_order() == \
"""\
***
Order Time: 115000
TOTAL ORDER PRICE: $0.00
***
"""
    assert order_queue.process_next_order() == \
"""\
***
Order Time: 123000
TOTAL ORDER PRICE: $0.00
***
"""
    assert order_queue.process_next_order() == \
"""\
***
Order Time: 130000
TOTAL ORDER PRICE: $0.00
***
"""
    o1 = SaladOrder(123000)  # 12:30:00PM
    o2 = SaladOrder(130000)  # 01:00:00PM
    o3 = SaladOrder(115000)  # 11:30:00AM
    order_queue = OrderQueue()
    order_queue.add_order(o1)
    order_queue.add_order(o2)
    order_queue.add_order(o3)

    assert order_queue.process_next_order() == \
"""\
***
Order Time: 115000
TOTAL ORDER PRICE: $0.00
***
"""
    assert order_queue.process_next_order() == \
"""\
***
Order Time: 123000
TOTAL ORDER PRICE: $0.00
***
"""
  #  assert order_queue.minChild(1) == 2

    o4 = SaladOrder(110000)  # 11:00:00AM
    order_queue.add_order(o4)
    assert order_queue.process_next_order() == \
"""\
***
Order Time: 110000
TOTAL ORDER PRICE: $0.00
***
"""
    assert order_queue.process_next_order() == \
"""\
***
Order Time: 130000
TOTAL ORDER PRICE: $0.00
***
"""

def test_percDown():
    order_queue = OrderQueue()
    order1 = SaladOrder(100000)  
    order2 = SaladOrder(120000)  
    order3 = SaladOrder(110000)  
    order_queue.add_order(order1)
    order_queue.add_order(order2)
    order_queue.add_order(order3)
    order_queue.heap[1], order_queue.heap[3] = order_queue.heap[3], order_queue.heap[1]
    order_queue.size = 3
    order_queue.percDown(1)
    assert order_queue.heap == [None, order1, order2, order3]

def test_minchild():
    order_queue = OrderQueue()
    order1 = SaladOrder(100000)  
    order2 = SaladOrder(120000)  
    order3 = SaladOrder(110000)  
    order_queue.add_order(order1)
    order_queue.add_order(order2)
    order_queue.add_order(order3)
    assert order_queue.minChild(1) == 3
    order_queue.heap[2], order_queue.heap[3] = order_queue.heap[3], order_queue.heap[2]
    assert order_queue.minChild(1) == 2





from Salad import Salad
from CustomSalad import CustomSalad 

class SaladOrder:
    def __init__(self, time):
        self.time = time
        self.salads = []

    def get_time(self):
        return self.time

    def add_salad(self, salad):
        self.salads.append(salad)

    def info(self):
        order_info = f"***\nOrder Time: {self.time}\n"
        total_price = 0.0

        for salad in self.salads:
            order_info += f"{salad.get_salad_details()}\n----\n"
            total_price += salad.get_price()
    
        order_info += f"TOTAL ORDER PRICE: ${total_price:.2f}\n***\n"
        return order_info

    def __lt__(self, other):
        return self.time < other.time
    
    
 
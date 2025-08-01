from Salad import Salad

class SpecialtySalad(Salad):
    prices = {"S": 12.50, "M": 14.50, "L": 16.50}

    def __init__(self, size, name):
        super().__init__(size)
        self.name = name
        self.set_price(self.prices[size])
    
    def get_salad_details(self):
        formatted = f"""\
SPECIALTY SALAD
Size: {self.size}
Name: {self.name}
Price: ${self.price:.2f}
"""
        return formatted
        


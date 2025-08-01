from Salad import Salad

class CustomSalad(Salad):
    prices = {"S": 8.75, "M": 10.75, "L": 12.75}

    def __init__(self, size):
        super().__init__(size)
        self.toppings = []
        self.set_price(self.prices[size])

    def add_topping(self, topping):
        self.toppings.append(topping)
        if self.size == "S":
            self.price += 1.75
        elif self.size == "M":
            self.price += 2.50 
        elif self.size == "L":
            self.price += 3.00 
            
    def get_salad_details(self):
        toppings_all = '\n'.join(f"\t+ {topping}" for topping in self.toppings)
        if self.toppings == []:
            return f"CUSTOM SALAD\nSize: {self.size}\nToppings:{toppings_all}\nPrice: ${self.price:.2f}\n"
        else:
            return f"CUSTOM SALAD\nSize: {self.size}\nToppings:\n{toppings_all}\nPrice: ${self.price:.2f}\n"
 
 
 
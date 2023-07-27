#!/usr/bin/env python3
import ipdb
class CashRegister:

    def __init__(self, discount = 0):
        # self.total = total
        self.discount = discount
        self.items =[]
        self.total = 0

    def add_item(self, title, price, quantity=1):
        self.current_tot = price*quantity 
        self.total += self.current_tot
        i = 1
        while i <= quantity:
            self.items.append(title)
            i += 1
        return self.items
        pass

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = self.total- self.total*(self.discount/100)
            print(f"After the discount, the total comes to ${round(self.total)}.")

    def void_last_transaction(self,):
        self.total -= self.current_tot
        pass
    # def reset_register_totals(self):
    #     self.items = []
    #     self.total = 0
    #     return (self.total, self.items)
# ipdb.set_trace()
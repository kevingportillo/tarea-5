class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Fondos Insuficientes.")
#cambios
            pass
        if(len(self.items_list())<=0):
            print("La tarjetar está sin fondos")
            pass
        print("La compra ha sido completada")
        return self.owner.wallet.withdraw(self.total_amount())

#cambios
        #else:
            #for item in self.items:
                #item.owner.wallet.balance += item.price  
                #self.owner.wallet.balance -= item.price
                #item.owner = self.owner  
            #self.items = []
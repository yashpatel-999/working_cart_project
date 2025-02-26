class product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_save=price-deal_price
    def display_details(self):
        print("Name: {}".format(self.name))
        print("price: {}".format(self.price))
        print("deal_price: {}".format(self.deal_price))
        print("ratings: {}".format(self.ratings))
        print("you_save: {}".format(self.you_save))
    def get_deal_price(self):
        return self.deal_price
class Electronicitem(product):
    def __init__(self,name,price,deal_price,ratings,warranty_in_months):
        super().__init__(name,price,deal_price,ratings)
        self.warranty_in_months=warranty_in_months
    def display_details(self):
        super().display_details()
        print("warranty_in_months: {}".format(self.warranty_in_months))
class groceryitems(product):
    def __init__(self,name,price,deal_price,ratings,expiry_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date=expiry_date
    def display_details(self):
        super().display_details()
        print("expiry_date:{}".format(self.expiry_date))
class Laptop(Electronicitem):
    def __init__(self,name,price,deal_price,ratings,warranty_in_months,ram,storage):
        super().__init__(name,price,deal_price,ratings,warranty_in_months)
        self.ram=ram
        self.storage=storage
    def display_details(self):
        super().display_details()
        print(f"Ram: {self.ram}")
        print(f"Storage: {self.storage}")
        
class Order:
    delivery_charges={
        "Normal":0,
        "Prime Delivery":100
    }
    def __init__(self, delivery_method,delivery_address):
        self.items_in_cart=[]
        self.delivery_method=delivery_method
        self.delivery_address=delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        print(f"Delivery Method: {self.delivery_method}")
        print(f"Delivery Address: {self.delivery_address}")
        print("----------------------------------------")
        for product,quantity in self.items_in_cart:
            product.display_details()
            print(f"Qunatity: {quantity}")
            print("")
        print("-----------------------------------------")    
        total_bill=self.display_total_bill()
        print(f"Total Bill: {total_bill}")
    def display_total_bill(self):
        total=0
        for product,quantity in self.items_in_cart:
            total= total+(product.get_deal_price())*quantity
        order_delivery_charges=Order.delivery_charges[self.delivery_method]
        total=total+order_delivery_charges
        return total
    @classmethod
    def update_delivery_charges(cls,delivery_method,charges):
        cls.delivery_charges[delivery_method]=charges
p=Electronicitem("laptop",50000,45000,5.0,34)
g=groceryitems("sugar",60,50,5,"25/12/2025")
o=Order("Normal", "Hyderabad")
o.add_item(p,2)
o.add_item(g,3)
Order.update_delivery_charges("Normal",50)
len_lap=Laptop("Lenovo 123",45000,30000,4.5,24,"16 GB","1 TB")
len_lap.display_details()
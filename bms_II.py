from datetime import datetime

class Bakery:
    def __init__(self):
        self.customers = {}
        self.orders_counter = 1

    def add_customer_details(self, name, order, quantity):
        order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        customer_id = self.orders_counter
        self.customers[customer_id] = {
            "name": name,
            "order": order,
            "quantity": quantity,
            "order_date": order_date,

        }
        print("customer added successfully")

    def display_customer_details(self):
        if not self.customers:
            print("no customer record")
            return 
        
        print("Customer details")

        for customer_id, data in self.customers.items():
            print(f"customer_id: {customer_id}")
            print(f"name {data['name']}")
            print(f"order {data['order']}")
            print(f"quantity {data['quantity']}")
            print(f"order_date {data['order_date']}")



    

bakery_system = Bakery()
bakery_system.add_customer_details("Asish", "Bread", 2)
bakery_system.display_customer_details()


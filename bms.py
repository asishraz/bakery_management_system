from datetime import datetime

class Bakery:
    def __init__(self):
        self.customers = {}
        self.orders_counter = 1

    def add_customer_details(self, name, order, quantity):
        order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        customer_id = self.orders_counter 
        self.orders_counter += 1

        self.customers[customer_id] = {
            "name": name,
            "order": order,
            "order_date": order_date,
            "quantity": quantity,
        }
        print("customer added successfully")


    def display_customer_details(self):
        if not self.customers:
            print("no customer record")
            return
        print("Customer Data ")
        for customer_id, data in self.customers.items():
            print(f"Customer ID: {customer_id}")
            print(f"Name: {data['name']}")
            print(f"Order: {data['order']}")
            print(f"Quantity: {data['quantity']}")
            print(f"Ordered Date: {data['order_date']}")


bakery_system = Bakery()
bakery_system.add_customer_details("asish", "bread", 2)
bakery_system.display_customer_details()

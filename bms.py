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

    def show_order_details(self, order_id):
        if order_id in self.customers:
            customer_data = self.customers[order_id]
            print(f"Order ID: {order_id}")
            print(f"Name: {customer_data['name']}")
            print(f"Order: {customer_data['order']}")
            print(f"Quantity: {customer_data['quantity']}")
            print(f"Date of Order: {customer_data['order_date']}")

            

        else:
            print("order id not found")

    def update_order(self, order_id, new_order, new_quantity):
        if order_id in self.customers:
            customer_data = self.customers[order_id]
            customer_data['order'] = new_order
            customer_data['quantity'] = new_quantity
            print("order updated successfully")


        else:
            print("Order ID not found.")

    



bakery_system = Bakery()
bakery_system.add_customer_details("asish", "bread", 2)
bakery_system.add_customer_details("raz", "pancake", 4)
bakery_system.add_customer_details("john", "cupcake", 5)
bakery_system.add_customer_details("peter", "vanilla_cake", 3)

bakery_system.display_customer_details()
bakery_system.show_order_details(2)
bakery_system.update_order(1, "CupCake", 3)
bakery_system.display_customer_details()



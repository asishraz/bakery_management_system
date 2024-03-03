class Bakery:
    def __init__(self):
        self.customers = {}
        self.orders_counter = 1

    def add_customer_details(self, name, order, quantity, date):
        order_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        customer_id = self.orders_counter 
        self.orders_counter += 1

        self.customers[customer_id] = {
            "name: ": name,
            "order: ": order,
            "date of order: ": date,
            "quantity: ": quantity,

        }
        print("customer added successfully")




bakery_system = Bakery()

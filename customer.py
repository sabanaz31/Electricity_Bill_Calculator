class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def display_customer(self):
        print("Customer Name :", self.name)
        print("Customer ID   :", self.customer_id)
class Bill:
    def __init__(self, customer, units, energy_charge, fixed_charge):
        self.customer = customer
        self.units = units
        self.energy_charge = energy_charge
        self.fixed_charge = fixed_charge

    def calculate_total(self):
        return self.energy_charge + self.fixed_charge

    def display_bill(self):
        total = self.calculate_total()

        print("\n========================================")
        print("          ELECTRICITY BILL")
        print("========================================")
        print("Customer Name  :", self.customer.name)
        print("Customer ID    :", self.customer.customer_id)
        print("Units Consumed :", self.units)
        print("----------------------------------------")
        print("Energy Charge  : ₹", format(self.energy_charge, ".2f"))
        print("Fixed Charge   : ₹", format(self.fixed_charge, ".2f"))
        print("----------------------------------------")
        print("Total Bill     : ₹", format(total, ".2f"))
        print("========================================")
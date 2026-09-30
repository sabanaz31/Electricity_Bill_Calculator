from customer import Customer
from units import Units
from energy_charge import EnergyCharge
from fixed_charge import FixedCharge
from bill import Bill


print("========================================")
print("       ELECTRICITY BILL CALCULATOR")
print("========================================")

# Taking input
name = input("Enter Customer Name : ")
customer_id = input("Enter Customer ID   : ")
units_consumed = float(input("Enter Units Consumed: "))

# Creating objects
customer = Customer(name, customer_id)
units = Units(units_consumed)

# Calculating energy charge
energy = EnergyCharge()
energy_charge = energy.calculate(units.get_units())

# Calculating fixed charge
fixed = FixedCharge()
fixed_charge = fixed.calculate()

# Creating and displaying bill
bill = Bill(
    customer,
    units.get_units(),
    energy_charge,
    fixed_charge
)

bill.display_bill()
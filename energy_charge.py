class EnergyCharge:
    def calculate(self, units):
        if units <= 100:
            charge = units * 3

        elif units <= 200:
            charge = (100 * 3) + ((units - 100) * 5)

        else:
            charge = (100 * 3) + (100 * 5) + ((units - 200) * 7)

        return charge
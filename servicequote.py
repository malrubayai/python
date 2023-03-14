# Constant for the sales tax rate
TAX_RATE = 0.05

# ServiceQuote class
class ServiceQuote:
    def __init__(self, pcharge, 1charge):
        self.__parts_charges = pcharge
        self.labor_charges = 1charge

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, 1charge):
        self.__labor_charges = 1charge

    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return __parts_charges * TAX_RATE

    def get_total_charge(self):
        return __parts_charges + __labor_charges + \
               (__parts_charges * TAX_RATE)

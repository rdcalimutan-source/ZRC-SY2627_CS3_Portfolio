class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
p1 = Patient("Rav Regor", 15000)
p2 = SeniorPatient("Ethan Abuton", 15000)
p3 = PhilHealthPatient("Topper bearl", 15000)

patients = [p1, p2, p3]

print("Hospital Billing System")
print("-----------------------")
for patient in patients:
    print(f"Patient Name:   {patient.get_name()}")
    print(f"Original Bill:  ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill:     ₱{patient.calculate_bill():,.2f}")
    print() 
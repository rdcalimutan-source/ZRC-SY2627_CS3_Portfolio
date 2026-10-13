class CD:
    def __init__(self, name="Campus Director", campus="ZRC Campus"):
        self.name = name
        self.campus = campus

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def campus(self):
        return self.__campus

    @campus.setter
    def campus(self, value):
        self.__campus = value

    def info(self):
        return f"{self.name} | {self.campus}"

class CID(CD):
    def __init__(self, budget=1000, staff=5, office="Room 10", code="CID-100"):
        super().__init__("CID Head", "ZRC Campus")
        self.budget = budget
        self.staff = staff
        self.office = office
        self.code = code

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def staff(self):
        return self.__staff

    @staff.setter
    def staff(self, value):
        self.__staff = value

    @property
    def office(self):
        return self.__office

    @office.setter
    def office(self, value):
        self.__office = value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    def hire_staff(self):
        self.staff += 1
        return f"Staff: {self.staff}"

    def spend_budget(self, amount):
        if 0 < amount <= self.budget:
            self.budget -= amount
        return f"Budget left: {self.budget}"

class SSD(CD):
    def __init__(self, budget=800, counselors=3):
        super().__init__("SSD Head", "ZRC Campus")
        self.budget = budget
        self.counselors = counselors

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def counselors(self):
        return self.__counselors

    @counselors.setter
    def counselors(self, value):
        self.__counselors = value

    def hire_counselor(self):
        self.counselors += 1
        return f"Counselors: {self.counselors}"

    def fund_program(self, amount):
        if 0 < amount <= self.budget:
            self.budget -= amount
        return f"Budget left: {self.budget}"

class Reading(CID):
    def __init__(self, books=10):
        super().__init__()
        self.books = books

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        self.__books = value

    def show_books(self):
        return f"Books: {self.books}"

class Math(CID):
    def __init__(self, kits=5):
        super().__init__()
        self.kits = kits

    @property
    def kits(self):
        return self.__kits

    @kits.setter
    def kits(self, value):
        self.__kits = value

    def show_kits(self):
        return f"Math kits: {self.kits}"

class Science(CID):
    def __init__(self, labs=2):
        super().__init__()
        self.labs = labs

    @property
    def labs(self):
        return self.__labs

    @labs.setter
    def labs(self, value):
        self.__labs = value

    def show_labs(self):
        return f"Science labs: {self.labs}"

class OnlineReading(Reading):
    def __init__(self, licenses=5):
        super().__init__()
        self.licenses = licenses

    @property
    def licenses(self):
        return self.__licenses

    @licenses.setter
    def licenses(self, value):
        self.__licenses = value

    def show_licenses(self):
        return f"Online licenses: {self.licenses}"

class Wellness(SSD):
    def __init__(self, program="Health Week"):
        super().__init__()
        self.program = program

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        self.__program = value

    def start_program(self):
        return f"{self.program} started"
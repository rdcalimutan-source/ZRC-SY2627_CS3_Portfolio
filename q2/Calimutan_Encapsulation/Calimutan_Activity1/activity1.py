
#Encapsulation
#Activity 1: Public, protected, and private attributes

class GameCharacter:
    def __init__(self, username):
        self.username = username  # Public attribute


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute


class Vehicle:
    def __init__(self, engine_code):
        self._engineCode = engine_code  # Protected attribute


class Student:
    def __init__(self, school_name):
        self.schoolName = school_name  # Public attribute


class VotingSystem:
    def __init__(self, voter_id):
        self.__voterID = voter_id  # Private attribute


# Create objects
character = GameCharacter("PlayerOne")
account = BankAccount(1500)
vehicle = Vehicle("ENG-204")
student = Student("Sample High School")
voting = VotingSystem("VOTER-001")

# Display accessible attributes
print("GameCharacter username:", character.username)
print("Vehicle engine code:", vehicle._engineCode)
print("Student school name:", student.schoolName)

print("Activity 1 examples created successfully.")

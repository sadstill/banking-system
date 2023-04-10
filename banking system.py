# Parent class: User
# Holds details about an user
# Has a function to show user details
# Child class: Bank
# Stores details about the account balance
# Stores details about the amount
# Allows ofr deposits, withdraw, view_balance

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)


# Parent class: User
# Holds details about an user
# Has a function to show user details
# Child class: Bank
# Stores details about the account balance
# Stores details about the amount
# Allows ofr deposits, withdraw, view_balance

# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details")
        print("................")
        print("Имя", self.name)
        print("Возраст", self.age)
        print("Пол", self.gender)


# Child class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.amount = None
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + amount
        print(f'Баланс аккаунта обновлен! | Доступно на балансе: {self.balance}')

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f'Недостаточный баланс! | Доступно на балансе: {self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'Вы успешно сняли деньги со счета! | Доступно на балансе: {self.balance}')

    def view_balance(self):
        self.show_details()
        print(f'Ваш баланс: {self.balance}')


'''
    Use property to protect some attributes

    Followed by a full example with a bank account
'''
class  Game:

    def  __init__(self, level=None):
        self.level = level if level else 0

    @property
    def level(self):
        return self._level

    @level.setter           # property must be defined over level to set it
    def level(self, value):
        if   not  isinstance(value,  int):
            raise TypeError('The value of level must be of type int.')
        if  value  <  0:
            self._level = 0
        elif  value  >  100:
            self._level = 100
        else:
            self._level = value

game = Game(200)
print(game.level)
game.level = 500
print(game.level)

### COMPLETE EXAMPLE WITH A BANK ACCOUNT
#*

class AccountException(Exception):

    def __init__(self, msg):
        super().__init__(f"Account Exception : {msg}")


class BankAccount:

    def __init__(self, number, balance):
        self.__number = number
        self.__balance = balance

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        raise AccountException("You can not change the account number")

    @number.deleter
    def number(self):
        if self.__balance > 0:
            raise AccountException("You only can delete an empty account")
        else:
            del self.__number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise AccountException("You can not set a negative balance")
        else:
            self.__balance = balance

    @balance.deleter
    def balance(self):
        self.__balance = 0

    def __str__(self):
        if hasattr(self,'number'):
            return f"bank account number : {self.__number} / Balance : {self.__balance:_}"
        else:
            return f"bank account number : None"

    def deposit(self, value):
        if value > 100_000:
            print("Warning : deposit > 100.000")
        self.__balance += value

    def withdraw(self, value):
        if value > 100_000:
            print("Warning : withdraw > 100.000")
        if self.__balance > value:
            self.__balance -= value
        else:
            print(f"Error : you only can withdraw {self.__balance:_}")


print("\nCreation of an account number with 1000 on balance")
b_account = BankAccount("123456", 1000)
print(b_account)

print("\nTry to set the balance to -200")
try:
    b_account.balance = -200
except AccountException as e:
    print(e)
print(b_account)

print("\ntrying to set a new value for the account number")
try:
    b_account.number = "456789"
except AccountException as e:
    print(e)
print(b_account)

print("\ntrying to deposit 1.000.000")
try:
    b_account.deposit(1_000_000)
except AccountException as e:
    print(e)
print(b_account)

print("\ntrying to withdraw 1.000.000")
try:
    b_account.withdraw(1_000_000)
except AccountException as e:
    print(e)
print(b_account)

print("\ntrying to delete the account attribute containing a non-zero balance")
try:
    del b_account.number
except AccountException as e:
    print(e)
print(b_account)

print("\ntrying to delete the balance")
try:
    del b_account.balance
except AccountException as e:
    print(e)
print(b_account)

print("\ntrying to delete the account attribute containing a non-zero balance")
try:
    del b_account.number
except AccountException as e:
    print(e)
print(b_account)


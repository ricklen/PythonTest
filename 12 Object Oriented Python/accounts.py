import datetime
import pytz


class Account:
    """Simple account class with balance"""

    # Static class is a class that you can call withouth having to create an
    # instance of the class itself.
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("Account created for {}".format(self.name))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("Amount must be greater than zero and more than your account balance") 
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "withdrawal"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)

    tim.deposit(1000)
    
    tim.withdraw(500)
    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()

    
    



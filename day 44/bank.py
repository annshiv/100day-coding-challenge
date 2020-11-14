class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self,acct_nbr,opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit
    
    # Define a __str__ mehthod to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance:.2f}'
    
    # Define a universal method to accept deposits
    def deposit(self,dep_amt):
        self.balance += dep_amt

    # Define a universal method to handle withdrawals
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
        else:
            return 'Funds Unavailable'

class Checking(Account):
    def __init__(self,acct_nbr,opening_deposit):
        # Run the base class __init__
        super().__init__(acct_nbr,opening_deposit)

    # Define a __str__ method that returns a string specific to Checking accounts
    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'
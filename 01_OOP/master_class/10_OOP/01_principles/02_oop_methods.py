# -*- coding: utf-8 -*-
"""

@author: anil_
"""
import datetime
import pytz

class Account:
    '''Simple Account class with Balance'''
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print(f'Account created for {self._name} where {self.get_balance()}')
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(self.get_balance())
            self._transaction_list.append((Account._current_time(), amount))
            
    def withdraw(self, amount):
        if 0<amount <= self.__balance:
            self.__balance -= amount
            print(self.get_balance())
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print('Insafficient balance')
    
    def get_balance(self):
        return f"Balance is {self.__balance}"
    
    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount >= 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print(f'{amount:6} {tran_type} on {date} (local time was {date.astimezone()})')
        

if __name__ == '__main__':
    ravi = Account('Ravi', 0)
    ravi.get_balance()
    
    ravi.deposit(2000)
    ravi.withdraw(200)
    
    ravi.withdraw(50000)
    ravi.show_transactions()
    ravi._current_time()

    raj = Account('Raj', 800)
    raj.__balance = 100
    raj.deposit(100)
    raj.withdraw(200)
    raj.show_transactions()

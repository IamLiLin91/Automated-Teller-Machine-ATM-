from datetime import datetime
from abc import ABC, abstractmethod 

class ATM_Transaction(ABC):
    transaction_id = 0#static variable
    def __init__(self, datetime, trans_type, amt_input=0):#external factor
        self.date = datetime
        self._trans_type = trans_type
        self._amt_input = amt_input #$$ used for the transaction.
        ATM_Transaction.transaction_id += 1
    
    def update(self, cust_acct, amt_input, transfer_account = None):#using abstract method
        pass

    
class Withdrawal(ATM_Transaction):
    def __init__(self, amt_input):#amt_input is external factor
        # calling Parent(ATM_Transaction) method
        super().__init__(datetime.now(), 'withdrawal', amt_input)#need to define variables from parent class
    
    def withdraw(self, cust_acct):
        return self.update(cust_acct)#go back to update function
    
    def update(self, cust_acct):
        cust_acct.debit(self._amt_input)#debit(-) off the balance
        return True
        

        
class Transfer(ATM_Transaction):
    def __init__(self, amt_input):
         #calling Parent(ATM_Transaction) method
        super().__init__(datetime.now(), 'transfer', amt_input)
    
    def update(self, cust_acct, input_acct_num):
        cust_acct.debit(self._amt_input)
        input_acct_num.credit(self._amt_input)#credit(+) the $$$ to the account link to this input_acct_num
        return True
        
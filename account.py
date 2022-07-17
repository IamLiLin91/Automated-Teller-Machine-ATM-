from additional_exceptions import InsufficientFunds

class Account():
    def __init__(self, acct_type, owner):#external factor
        self._acct_type = acct_type
        self.__owner = owner
        self.__balance = 0#already in Account class
    
    def check_balance(self):#get_balance(self)
        return self.__balance
    
    def set_balance(self, balance):#setter for balance
        self.__balance = balance
    
    def get_owner(self):#getter for owner
        return self.__owner
    
    def get_acct_type(self):#getter for account type
        return self._acct_type
    
    def debit(self, amt_input):
        if self.__validate_amt(amt_input) == True:#__validate_amt is embeded in so that this will check the amt_input first before debit
            amt_input = float(amt_input)
            if self.__balance >= amt_input: 
                self.__balance -= amt_input
            else:
                raise InsufficientFunds
    
    def credit(self, amt_input):
        if self.__validate_amt(amt_input) == True:
            amt_input = float(amt_input)
            self.__balance += amt_input
            
    
    def __validate_amt(self, amt_input):#amt_input is the input
        amt_input1 = float(amt_input)#first check whether the amt_input is less than 0
        if amt_input1 <= 0:
            raise ValueError#error will raise when the input is less than 0
        elif amt_input1 < 0.01:
            raise ValueError#for input such as "0.0000000001" as after float will be in scientific notation
        else:
            amt_str = str(amt_input1).split('.')#then check whether the amt_input's decimal place is it more than 2
            amt_integer = amt_str[0]#belong to whole number
            amt_decimal = amt_str[1]#belong to the decimal
            if len(amt_decimal) > 2:
                raise ValueError#error will raise when the input is less than 0
            else:
                return True

class Savings_Account(Account):#child class 
    def __init__(self, acct_num, owner, acct_type = 'savings'):
        # calling Parent(Account) method
        super().__init__(owner, acct_type)
        self.__acct_num = acct_num
        self._acct_type = acct_type
        
    def get_acct_num(self):#getter for account number 
        return self.__acct_num
        

class Current_Account(Account):#child class
    def __init__(self, acct_num, owner, acct_type = 'current'):
        # calling Parent(Account) method
        super().__init__(owner, acct_type)
        self.__acct_num = acct_num
        self._acct_type = acct_type
    
    def get_acct_num(self):#getter for account number
        return self.__acct_num
    
    
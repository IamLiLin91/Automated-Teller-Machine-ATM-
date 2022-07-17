from datetime import datetime

class Customer():
    
    def __init__(self, name, address, date_of_birth):#only outside of Customer class(database) then need to put, otherwise just do self.""
        self.__name = name
        self.__address = address
        self.__date_of_birth = datetime.strptime(date_of_birth, '%d-%b-%Y').strftime('%d-%b-%Y')#to match the database's DOB format
        self.__lst_of_accts = []#does not appear in _init_() due to this has already exits in database
    
    def get_name(self):#getter for name
        return self.__name
    
    def get_lst_of_accts(self):#getter for list of accounts
        return self.__lst_of_accts
    
    def owns(self, acct):# to check whether the customer has more than 1 account
        if len(self.__lst_of_accts) <= 2:
            self.__lst_of_accts.append(acct)
    
    def __str__(self): #to print out the detail according to the format below
        return "{}\n{}\n{}".format(self.__name, self.__address, self.__date_of_birth)
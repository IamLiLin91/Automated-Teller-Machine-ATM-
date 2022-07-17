from atm_transaction import  Withdrawal, Transfer #only in IDE(unless all scripts done in 1 single file), juypter notebook no need
from additional_exceptions import InvalidAccount, InvalidATMCard

class ATM():
    def __init__(self, location, managed_by):
        self.location = location
        self.managed_by = managed_by#access to Bank class
        self.__current_card = None
    
    def get_currentcard(self):#access to ATM_Card class
        return self.__current_card
    
    
    def transactions(self, trans_type, amt_input, acct_type, input_acct_num):#to check whether the withdraw or transfer is successful or not and this will be used in main_app
        cust_acct = self.__current_card.access(acct_type)#get customer object based on current card
        cust_acct_num = cust_acct.get_acct_num()#used this customer object to get account number
        if cust_acct_num == input_acct_num:#checking the input_acct_num
            raise InvalidAccount
            
        if trans_type == 'withdrawal':
            input_acct_num = None
            withdraw_class = Withdrawal(amt_input)#using the Withdrawal class to do the checking and debit process
            if withdraw_class.withdraw(cust_acct) == True:
                return f"Transaction successful."#when the transaction is completed
            
        else:
            transfer_acct = self.managed_by.get_acct(input_acct_num)#get account object based on input account number
            transfer_class = Transfer(amt_input)#using the Transfer class to do the checking plus debit and credit processes
            if transfer_class.update(cust_acct, transfer_acct) == True:
                return f"Transaction successful."#when the transaction is completed
    
    
    def check_accts(self):#to check whether the atm_card links to more than 2 accounts
        y = self.__current_card.get_acct_types()
        return len(y) == 2#=True
            
    def check_pin(self, pin_input):#this is checking pin function which will be used in main_app
        customer = self.__current_card.get_owned_by()
        return self.managed_by.authorize_pin(customer, pin_input)

    
    def check_card(self,card_input):
        x = self.managed_by.list_of_atm_cards
        for card in x:#checking aginst the list of atm cards
            if card_input == card.get_card_num():
                self.__current_card = card
                return True
        raise InvalidATMCard
    #raise error when the all card information is screened, only the first card_num will be read using "if else" statement
    
    def show_balance(self, acct_type):#for balance statement print out
        r = self.__current_card.access(acct_type)
        print(f"Your {acct_type} account has a balance of ${r.check_balance():.2f}.")
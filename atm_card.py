class ATM_Card():
    def __init__(self, card_num, owned_by):#external factor
        self.__card_num = card_num
        self.__owned_by = owned_by
    
    def get_acct_types(self):#getter for account types
        return self.__owned_by.get_lst_of_accts()
    
    def access(self, acct_type):#checking the accounts based on account type then return as account's object
        lst_of_acc = self.__owned_by.get_lst_of_accts()
        for acc in lst_of_acc:
            if acc.get_acct_type()==acct_type:
                return acc
    
    def get_card_num(self):#getter for card number
        return self.__card_num
    
    def get_owned_by(self):#getter for card's owner
        return self.__owned_by
    
    def __str__(self):#return card information in the formart below 
        return "{}\n{}".format(self.__card_num, self.__owned_by.get_name())
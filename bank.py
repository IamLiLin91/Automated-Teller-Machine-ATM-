import random
from additional_exceptions import InvalidPinNumber, AccountNotFound

class Bank():
    def __init__(self, bank_code, bank_address):#only outside of Bank class(database) then need to put, otherwise just do self.""
        self.__bank_code = bank_code
        self.__bank_address = bank_address
        self.list_of_atm = []#does not appear in _init_() due to this has already exits in database
        self.list_of_customers = []#does not appear in _init_() due to this has already exits in database
        self.list_of_atm_cards = []#does not appear in _init_() due to this has already exits in database
    
    def add_customer(self, customer, customer_pin):
        customer_id_num = format(random.randint(0000,9999), '04d')# to get id_num in random number in this format:"1234" (example)
        customer_id = customer.get_name() + customer_id_num # use the get_name() function to access to customer class to retrive 
        self.list_of_customers.append({'obj': customer, 'id':customer_id, 'pin':customer_pin})# will get the information in dict form into the list:e.g.[{'obj':customer's data(which is the customer's object), 'id':customer's id, 'pin':customer's pin}]
                                                                                              # 'obj', 'id' ,'pin' are the keys while cusomter, customer_id, customer_pin are the values correspond to the keys respectively
    def manages(self, atm_card):
        return self.list_of_atm_cards.append(atm_card)#get the atm_card into the list
    
    def maintains(self, atm):
        return self.list_of_atm.append(atm)#get the atm into the list
    
    def authorize_pin(self, customer, pin_input):
        for customer_dic in self.list_of_customers:#to access all the customer's information which is in the dict form in the customer list
            if customer_dic['obj'] == customer:
                if pin_input == customer_dic['pin']:
                    return True#when the pin input is matched to the customer's information found in the list
                else:
                    raise InvalidPinNumber# will raise this error when the pin_input does not match any customer from the database's list
    
    def get_acct(self, input_acct_num):
        for customer_dic in self.list_of_customers:
            lst_of_acc = customer_dic['obj'].get_lst_of_accts()
            for acc in lst_of_acc:
                if input_acct_num == acc.get_acct_num():
                    return acc
        raise AccountNotFound
        #the raise error need to be under the first "for" loop so that this error will raise when the entire database is checked
        # if the raise error is under the inner "for" loop, then only within the customer's database is checked
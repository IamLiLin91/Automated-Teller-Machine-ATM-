class InvalidAccount(Exception):
    pass

class AccountNotFound(Exception):
    pass

class InsufficientFunds(Exception):
    pass

class InvalidATMCard(Exception):
    pass

class InvalidPinNumber(Exception):
    pass

#all these exceptional errors above are customised for this atm_app
# customised error messages will be stated in main_app.py
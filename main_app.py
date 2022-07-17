from additional_exceptions import InvalidPinNumber, InvalidATMCard, InsufficientFunds, AccountNotFound, InvalidAccount

def atm_app(atm):#"atm" act as a placement for object to pass through
    while (1):#same as while True
        Options_input = input("\nAvaliable options:\n1. Insert ATM card\n2. Quit Simulation\nEnter an option:  ")#\n is for formatting purpose.
        if(Options_input == '2'): #the whole prgram will stop when '2' is keyed
            Options_input = int(Options_input)
            break
        elif(Options_input == '1'):#will lead to entering the atm card number
            Options_input = int(Options_input)
            card_input=input("Enter a ATM card number:")
            try:
                atm.check_card(card_input)#checking the card number whether is in the bank database, the whole program will stop when incorrect card number is input and 'invalid card' message will pop up
            except InvalidATMCard:
                print("Invalid Card. Please take your card.\n")#when the card number input is invalid
                continue#will return to option selection when invalid card number is keyed in
            if True:
                count = 0
                limit = 3
                while count < limit:#the number of attempts to key in the pin limits to 3 tries
                    count +=1
                    try:
                        pin_input=input("Enter a Pin Number: ")
                        atm.check_pin(pin_input)
                        atm_menu_sys(atm)#will enter to atm_menu when the input pin is ok
                        break#this is needed other when 'withdrawal'or "transfer" is done, it will prompt the user to key in the pin number instead of menu option
                    except InvalidPinNumber:#when the pin input is invalid
                        print("Invalid Pin!")
                else:
                    count = limit
                    print("You have hit the maximum limit. Please take your card.\n")#will return back when the wrong pin input max out 3 tries
           

def atm_menu_sys(atm):
    while (1):#same as while True
        menu_input = input("\nAvaliable options:\n1. Check balance\n2. Withdraw Funds\n3. Transfer Funds\n4. Return Card\nEnter a transaction option: ")#\n formatting purpose
        if (menu_input == '1'):#check balance
            menu_input = int(menu_input)
            if atm.check_accts()==True:#will enter to the sub-menu when there are more than 1 account link to this atm card
                sub_input = input("\nChoose Account:\n1. Current Account\n2. Savings Account\nEnter an account option: ")
                if (sub_input == '1'):
                    sub_input = int(sub_input)
                    acct_type = 'current'
                    atm.show_balance(acct_type)#show the account balance under current account
                elif (sub_input == '2'):
                    sub_input = int(sub_input)
                    acct_type = 'savings'#show the account balance under current account
                    atm.show_balance(acct_type)
            else:
                acct_type = 'savings'
                atm.show_balance(acct_type)#show the default account's balance
                
        elif (menu_input == '2'):#withdrawal
            menu_input = int(menu_input)
            trans_type='withdrawal'
            input_acct_num=None#default value when the "withdrawal" option is selected
            if atm.check_accts()==True:
                sub_input = input("\nChoose Account:\n1. Current Account\n2. Savings Account\nEnter an account option: ")
                if (sub_input == '1'):
                    sub_input = int(sub_input)
                    acct_type = 'current'
                    count = 0
                    limit = 3
                    while count < limit:#the number of attempts to key in the amount limits to 3 tries
                        count +=1
                        try:
                            amt_input = input("Enter an amount to withdraw: ")
                            atm.transactions(trans_type, amt_input, acct_type, input_acct_num)#checking the inputs
                            print("Card Returned")
                            atm.show_balance(acct_type)#will show the account balance when the input_amt is keyed correctly
                            return #will go back to the atm_app(atm) and the balance statement is printed out
                            break#will exit the loop and return to atm_menu_sys when the maximum tries is reached
                        except ValueError:
                            print("The amount entered is incorrect.")#when the input_amt is less than 0 or has more than 2 decimal points
                        except InsufficientFunds:
                            print("Insufficient funds in your account!")#when the input_amt is more than the account's balance
                    else:
                        count = limit
                        print("You have hit the maximum limit. Please select the option again.")
                    
                elif (sub_input == '2'):
                    sub_input = int(sub_input)
                    acct_type = 'savings'
                    count = 0
                    limit = 3
                    while count < limit:#the number of attempts to key in the amount limits to 3 tries
                        count += 1
                        try:
                            amt_input = input("Enter an amount to withdraw: ")
                            atm.transactions(trans_type, amt_input, acct_type, input_acct_num)#checking the inputs
                            print("Card Returned")
                            atm.show_balance(acct_type)#will show the account balance when the input_amt is keyed correctly
                            return#will go back to the atm_app(atm) and the balance statement is printed out
                            break#will exit the loop
                        except ValueError:
                            print("The amount entered is incorrect.")
                        except InsufficientFunds:
                            print("Insufficient funds in your account!")
                    else:
                        count = limit
                        print("You have hit the maximum limit. Please select the option again.")
                    
            else:
                acct_type = 'savings'#default account
                count = 0
                limit = 3
                while count < limit:#the number of attempts to key in the amount limits to 3 tries
                    count += 1
                    try:
                        amt_input = input("Enter an amount to withdraw: ")
                        atm.transactions(trans_type, amt_input, acct_type, input_acct_num)#checking the inputs
                        print("Card Returned")
                        atm.show_balance(acct_type)#will show the account balance when the input_amt is keyed correctly
                        return#will go back to the atm_app(atm) and the balance statement is printed out
                        break#will exit the loop
                    except ValueError:
                        print("The amount entered is incorrect.")
                    except InsufficientFunds:
                        print("Insufficient funds in your account!")
                else:
                    count = limit
                    print("You have hit the maximum limit. Please select the option again.")
                
        
        elif (menu_input == '3'):#Transfer funds
            menu_input = int(menu_input)
            trans_type='transfer'
            if atm.check_accts()==True:
                sub_input = input("\nChoose Account:\n1. Current Account\n2. Savings Account\nEnter an account option: ")
                if (sub_input == '1'):
                    sub_input = int(sub_input)
                    acct_type = 'current'
                    count = 0
                    limit = 3
                    while count < limit:#the number of attempts to key into the system limits to 3 tries
                        count += 1
                        try:
                            input_acct_num = input("Enter the account number to transfer funds to: ")
                            amt_input = input("Enter an amount to withdraw: ")
                            atm.transactions(trans_type, amt_input, acct_type, input_acct_num)
                            print("Card Returned")
                            atm.show_balance(acct_type)
                            return#will go back to the atm_app(atm) the balance statement is printed out
                            break#will exit the loop
                        except ValueError:
                            print("The amount entered is incorrect.")#when amount is incorrect
                        except InsufficientFunds:
                            print("Insufficient funds in your account!")# $$$ inside the account is not enough
                        except InvalidAccount:
                            print("Invalid Account!")#when the receiver's account number is the same as the sender
                        except AccountNotFound:
                            print("Account not found!")#not found in database
                    else:
                        count = limit
                        print("You have hit the maximum limit. Please select the option again.")
            
                
                elif (sub_input == '2'):
                    sub_input = int(sub_input)
                    acct_type = 'savings'
                    count = 0
                    limit = 3
                    while count < limit:
                        count += 1
                        try:
                            input_acct_num = input("Enter the account number to transfer funds to: ")
                            amt_input = input("Enter an amount to withdraw: ")
                            atm.transactions(trans_type, amt_input, acct_type, input_acct_num)
                            print("Card Returned")
                            atm.show_balance(acct_type)
                            return#will go back to the atm_app(atm) the balance statement is printed out
                            break#will exit the loop
                        except ValueError:
                            print("The amount entered is incorrect.")
                        except InsufficientFunds:
                            print("Insufficient funds in your account!")
                        except InvalidAccount:
                            print("Invalid Account!")
                        except AccountNotFound:
                            print("Account not found!")
                    else:
                        count = limit
                        print("You have hit the maximum limit. Please select the option again.")
                    
            else:
                acct_type = 'savings'#default account
                count = 0
                limit = 3
                while count < limit: #limit to 3 attempts
                    count += 1
                    try:
                        input_acct_num = input("Enter the account number to transfer funds to: ")
                        amt_input = input("Enter an amount to withdraw: ")
                        atm.transactions(trans_type, amt_input, acct_type, input_acct_num)
                        print("Card Returned")
                        atm.show_balance(acct_type)
                        return#will go back to the atm_app(atm) the balance statement is printed out
                        break#will exit the loop
                    except ValueError:
                        print("The amount entered is incorrect.")
                    except InsufficientFunds:
                        print("Insufficient funds in your account!")
                    except InvalidAccount:
                        print("Invalid Account!")
                    except AccountNotFound:
                        print("Account not found!")
                else:
                    count = limit
                    print("You have hit the maximum limit. Please select the option again.")
                
                
        if (menu_input == '4'):
            menu_input = int(menu_input)
            print("Card Returned")
            return
            break
 #int after the input is to ensure that any wrong input does not cause errors, the menu will still "stays on" until the "correct option" is keyed
 #no break, continue or return is used under menu_input ='1' as when the checking balance is done, it will return back to the list of option menu
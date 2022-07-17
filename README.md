# Automated Teller Machine(ATM)
## Overview
This project will be simulating of a scaled down version of an Automated Teller Machine (ATM) implemented using Object Orientation Principles. Python programming is used for this project via VScode IDE.
![image](https://user-images.githubusercontent.com/109471364/179403812-01c928e7-7b55-4a4d-be0b-70def7bcf55a.png)
### To scale down the complexities of a real world ATM, this project will be limited to this scenario:
* Bank XYZ maintains many ATMs. Each ATM can only perform 4 operations: Check balance, Withdrawals, Transfers and Quit.
* ATM transactions can only start when the user's PIN is entered correctly. If the PIN is invalid, the card is returned.
* Each bank can has only 1 type of ATM card and each ATM card has access to both a customer's Savings and Current account (if any).
* Each customer of the bank by default has a savings account.
* Customers of Bank XYZ are allowed to own only 1 ATM card.
* Withdrawals operations are done either from the customer's Savings or Current account.
* Transfers operations are done either from Savings to Current account and vice versa from the same customer or from an account of Customer A to an account of Customer B (both customers must be account holders of Bank XYZ).
* Transfer transactions must not go through if the transfer account number is not existent or transferee has insufficient funds for transfer.
## Assumptions For Testing
1. Each customer object has either a Savings or Current account or both from when they personally opened the accounts at the physical bank therefore do not create any  customer objects with more than 2 account types.
2. There is only 1 bank and 1 Automated Teller Machine for testing to keep the scale small. All other objects such as customer, ATM cards and accounts are allowed to have multiples.
3. Each customer can only own 1 ATM card.
## Scripts used in this project
- account
- additional_exceptions
- atm
- atm_card
- atm_transaction
- bank
- customer
- main_app
- test

import sys

#account balance variable 
account_balance = float(500.25)

#function for printing account balance
def printbalance():
  print("Your current balance:\n" + str(account_balance))

#function for performing deposit action, increase account balance
def deposit(account_balance):
  #get deposit amount from user
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  #increase balance by deposit amount
  if(deposit_amount <= 0):
     print("That's not a valid amount.")
  else:
    account_balance += deposit_amount
    #print summary of account balance and deposit amount
    print("Deposit was $%.2f, current balance is $%.2f" %(deposit_amount, account_balance))
    return(account_balance)

#function for performing withdraw action, if amount doesn't exceed total, decrease account balance
def withdrawal(account_balance):
  #get withdrawal amount from user
  withdrawal_amount = float(input("How much would you like to withdraw today?\n"))
  #check if withdrawal amount is larger then total account balance
  if(withdrawal_amount > account_balance):
    #print account balance is smaller then requested amount
    print("$%.2f is greater than your account balance of $%.2f" %(withdrawal_amount, account_balance))
  #check if withdrawal amount is less then or equal to total account balance
  elif(withdrawal_amount <= account_balance):
    #calculate account balance by subtracting withdrawal amount
    account_balance -= withdrawal_amount
    #print results from account balance and withdrawal amount
    print("Withdrawal amount was $%.2f, current balance is $%.2f" %(withdrawal_amount, account_balance))
    return(account_balance)

#user input request for bank/ATM actions
#if input does not equal Q(quit)
userchoice = 's'
while(userchoice != 'Q'):
  userchoice = input ("What would you like to do?\n")
  #if input equals D(deposit) action
  if (userchoice == 'D'):
    #run deposit function
    account_balance = deposit(account_balance)
  #if input equals B(balance) action
  elif(userchoice == 'B'):
    #run request for balance function
    printbalance()
  #if input equals W(withdrawal) action
  elif(userchoice == 'W'):
    #run withdrawal function
    account_balance = withdrawal(account_balance)
  #if input is other, print error message, request for input again
  elif(userchoice != 'Q' and userchoise != 'D' and userchoice != 'B' and userchoice != 'W'):
    print("Invalid entry - Please try again\n")
    userchoice = input("what would you like to do?\n")
#exit program print statement
print("Thank you for banking with us.\n")

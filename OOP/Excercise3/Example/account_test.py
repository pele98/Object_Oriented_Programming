#File name: account_test
#Author: Pekka Lehtola
#Description: Example code from Anne

from bank_account import *

def main():

    owner = str(input("Enter the owners name: "))
    start_bal = float(input("Enter the startin balance: "))

    savings = Bank_account(start_bal, owner)

    print(savings)
    #print("Balance is: ", format(savings.get_ballance(), ",.2f"), sep="")

    ammount = float(input("Enter the ammount to be deposited: "))
    savings.deposit(ammount)

    print(savings)
    #print("Balance is: ", format(savings.get_ballance(), ",.2f"), sep="")

    ammount = float(input("Enter the ammount for withdraw: "))
    savings.withdraw(ammount)

    print(savings)
    #print("Balance is: ", format(savings.get_ballance(), ",.2f"), sep="")

main()
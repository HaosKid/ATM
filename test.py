
#ATM
Money = 100000
BankMoney = 0
CardCode = 0000
while True:
    if CardCode == 0000:
        print("""
                            =========================================
                                                ATM
                            =========================================



        =================================================
        Good morning! Do you want to activate your card?
        =================================================
            /////                   ////
            /YES/                   /NO/
            /////                   ////
            
        """)

        Answear1 = input()
        if Answear1.lower() == "yes":
            CardCode = int(input("Please insert a code of 4 digits:"))
            if len(str(CardCode)) != 4:
                print("You have to insert only 4 digits!")
                CardCode = 0000
                continue
        elif Answear1.lower() == "no":
            print("Thank you! Have a nice day!")
            break
        else:
            print("404")
            break
    # type 1, 2, 3 or 4
    Answear2 = int(input("""
1. Deposit
2. Withdraw
3. Ballance
4. Change your code
5. Exit
"""))
    if Answear2 == 1:
        Deposit = int(input("How much money would you like to deposit?\n"))
        if Deposit <= Money:
            Money -= Deposit
            BankMoney += Deposit
            print(f"You deposited {Deposit}$ and now your ballance is: {BankMoney}$")
        elif Deposit <= 0:
            print("You cant deposit 0 or a negative number.")
            continue
        else:
            print("You dont have enought money!")
            continue
    if Answear2 == 2:
        if BankMoney == 0 :
            print("you dont have anought money!")
            continue
        withdraw = int(input("How much money would you like to take?\n"))
        if withdraw <= BankMoney:
            BankMoney -= withdraw
            Money += withdraw
            print(f"You took {withdraw}$ and now you have: {BankMoney}$")
            continue
        elif withdraw > BankMoney:
            print("You dont have enought money.")
            continue
        else:
            print("How did that end up here? >.>")
            break
    if Answear2 == 3:
        print(f"Your ballance is {BankMoney}$\nAnd {Money}$ cash.")
        continue
    if Answear2 == 4:
        CardCode = int(input("Please insert a code of 4 digits:"))
        if len(str(CardCode)) != 4:
            print("You have to insert only 4 digits!")
            CardCode = 0000
            continue
    if Answear2 == 5:
        print("have a nice day!")
        break
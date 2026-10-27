# pyhotn project on mini finance app

expenses = [] #creating a list soo that later wee can add all the expens.. dictionary.. to list 
print("wlcm to expenses tracker")

while True: # using while loop for options
    print("1. Add Expenses")
    print("2. View all expense")
    print("3. view total expens")
    print("4. Exit")

    choice= int(input("enter your choice"))

#add expense
    if(choice == 1):
        date= input("enter the date on which you spent money :")
        category= input("in what you spent ? (travel,food,grocories,bolls,shooping... :)")
        description = input("add more details you :")
        amount = float(input("enter the amount (how much you spent :)"))

        expense = { #add all the key and therer value inthe dictonairiiii
        
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense) #now we will aadd thisall the dictonarii 
        #key and there value to the list which we created in starting using .append() methdo

        print("Every thiing added congrats..")

    #2 view all the expenses

    elif(choice==2):
        if len(expenses) == 0:         #check length:
            print("plz enter any expenses first :")
        else:
            count = 1  #we will incres the count by 1 for every option
            for pay in expenses:
                print(f"expense number {count} {pay['date']}, {pay['category']} , {pay['description']}, {pay['amount']}" ) 
                count = count +1

#3 view all total expensesss
    elif(choice == 3):
        
        total = 0
        for pay in expenses:
            total = total + pay["amount"]
        print("ttotal =" , total)


#exit

    elif(choice == 4):
        print("thankyou wo using our service")
    
        break

    else:
        print("invalod choice try again ")

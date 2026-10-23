#Iterate through a given list of numbers and print only those numbers which are divisible by 5.

#num_list = [10, 20, 33, 46, 55]

#for nun in num_list:
 #   if nun % 5 == 0:
  #      print(nun)

#Write a program to find how many times the substring “Emma” appears in a given string.


#str_x = "Emma is good developer. Emma is a writer" # aa line ma string che je ma apde check karvana che ke "Emma" ketli vaar aave che.
                                                     #vaae ave che 
#text = str_x.count("Emma")  #.count check kare ans full srin my count kares ke emma ketli vaar ayu che 
#print("The substring 'Emma' appears", text, "times in the given string.")


# Print the following pattern where each row contains a number repeated a specific number of times based on its value.


#for i in range(1, 6):

    #simplly pela apde number ne strin ma convert kriye ane pachi ene print kariye che. 
    #and * ahiy string sthe differernt behave kare exmaple 

    #Number × Number = multiplication → 3 * 3 = 9

#String × Number = repetition → "3" * 3 = "333"

   #print(str(i)*i)# aa line 

#Write a program to check if a given number is a palindrome (reads the same forwards and backwards


#number = 121,125

#for num in number:
   #str_num =str(num)  # Convert the number to a string


    #if str_num == str_num[::-1]:  # ahiyaa apde simple real number ne for exmaple apde 121 ne pel string ma convet kri 

 #didho and then apde slice [::-1] use kari ne string ne imsple revers kri  and real
 #num sathe akhi string ne compare kari bev same ave to palin doem and na to pachi not

       # print(num,"is palindrome")
   # else:
      #  print(num,"is not palindrome")


#Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.



#list1 = [10, 20, 25, 30, 35]
#list2 = [40, 45, 60, 75, 90]

#new1 = [n for n in list1 if n % 2 != 0]

#new2 = [n for n in list2 if n%2==0]

#result = new1 + new2

#print(result)

#Write a program to extract each digit from an integer in the reverse order.

#number = 7536
#for num in str(number)[::-1]:
    #simple conver the intger number to string and then revers it using slice negitve indexig ana apce print kryi
  #  print(num , end="   ")


#Calculate income tax for a given income based on these rules:

#First $10,000: 0% tax
#Next $10,000: 10% tax
#Remaining income: 20% tax

#income = 45000

#if income <= 10000:
 #tax =0

#elif income <= 50000:

 #tax = income * 0.10

#else:
 #tax = income* 0.20

 #print(f"tax: {tax:.2f}")



#encapsulation

#Create BankAccount with private __balance and public owner. Print owner (works),
#  try __balance (fails), and add get_balance() to access it safely.


#class Bankaccount():
    #def __init__(self ,balance,owner):
      #  self.__balance = balance
     #   self.owner = owner

    #def get_balance(self):     #getter
 #       return self.__balance

#acc = Bankaccount(10000 , "dev")   #setter

#print(acc.get_balance())

#print(acc.__balance) # this will throw error beczz the attrbit is private



        
#Create Person with _name (protected) and Student(Person) 
# with show() returning _name. Test show() and direct access from outside.

#class Person():
  #  def __init__(self , name):
 #       self._name = name

#class Student(Person):
  #  def show(self):
 #       return self._name

#p = Person("darshit")

#print(p._name)
#s = Student("darshit rana")
#print(s.show())
#print(s._name)


#Create Secret with __password = "1234". 
#Try obj.__password (fails) and obj._Secret__password (works). Explain name mangling.

#class secret():
  #  def __init__(self , password = "1234"):
 #       self.__password = password

#s = secret()

#print(s._secret__password) #this is working because of name mangling

#print(s.__password) #giving error


#Create Temperature with private __celsius, get_celsius(), 
# and set_celsius(value) — only set if value >= -273.15.#


#class temp():
   # def __init__(self , celsius):
     #   self.__celsius = celsius

    #def get_celsius(self):
     #   return self.__celsius

    #def set_celsius(self ,value):
       # self.value = value
    #    if value >= -273.15:
   #           self.__celsius += value
  #      else:
 #          print("innvalis")

#t = temp(-.02343)
#print(t.get_celsius())

#Create Animal with _species = "Unknown", Mammal(Animal) with _warm_blooded = True,
#  Dog(Mammal) with show() printing both protected attributes.


class Animal():
    def __init__(self ,species= "Unknown"):
         self._species = species

class mammal(Animal):
     ##continuingg soon 

        

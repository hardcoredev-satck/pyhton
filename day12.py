#abstraction in pyhton

#Create BankAccount with public owner and private __balance. 
# Try printing both — __balance should fail. Add get_balance() to access it safely.

#class bankaccount:
    #def __init__(self,owner, balance):
    #    self.owner=owner #publicc
   #     self.__balance = balance #privatee

  #  def get_balance(self): #give the output  for publiccc
 #       return self.__balance #getterr ke throug yee value ko show karega 
        
#b = bankaccount("dev" , 20000)
#print(b.owner)
#try:
 #   print(b.__balance)  # works ad public
#except AttributeError as e:
 #   print(f"attribut eroro : {e}")
#print(b.get_balance())


#Create Person with _name (protected) and Student(Person) with show() returning _name. 
# Test show() and direct access from outside.

#class person:
  #  def __init__(self ,name):
 #       self._name = name

#class student(person):
  #  def show(self):
 #       return self._name

#s = student("dev")
#print(s.show())

#direct acces from outside pr
#print(s.show())


#Create Secret with __password = "1234".
# Try obj.__password (fails) and obj._Secret__password (works). Explain name mangling.


#class Secret :
  #  def __init__(self , password = "1234"):
 #       self.__password= password

#s =Secret() # object banuu
#try:
 #   print(s.__password) # errro
#except AttributeError as e:
 #   print("error : {e}")
#print(s._Secret__password) #print thase



#Create Temperature with private __celsius, get_celsius(), and set_celsius(value)
#  — only set if value >= -273.15.

#class Temp:
    #def __init__(self ,celsius):
     #   self.__celsius = celsius

    #def get_celsius(self):
     #   return self.__celsius

    #def set_celsius(self ,value):
    #    if value >= -273.15: #checl valid hai ky
   #         self.__celsius = value
  #      else:
 #           print("nothisnf")

#t= Temp(-300)
#print(t.get_celsius())


#Create Animal with _species = "Unknown", Mammal(Animal) with _warm_blooded = True, 
# Dog(Mammal) with show() printing both protected attributes.

#class Animal:
   # def __init__(self , species= "unknown"):
  #      self._species = species # if idahr mammel mai super( parent class ka agar nhi hota
        #to animal ne species set in nhi hote)

#class mammal(Animal):
  #  def __init__(self,species="unknown"):
 #       super().__init__(species)
 #       self._warm_blooded =True

#class dog(mammal):
   # def show(self):
  #       print(f"Species: {self._species}")
 #        print(f"Warm-blooded: {self._warm_blooded}")

         #if agar ahiya retunuse karvu hot to tupel sate thathu syntax
        # return self._species, self._warm_blooded    

#d =dog()
#d.show()


#Create Parent with __secret and reveal() method.
#  Create Child(Parent) that tries self.__secret directly — should fail. Explain why.

#answer: Child mein self.__secret directly access karna should fail —
# # kyunki Python private attributes ko name-mangle karta hai."


#class parent:
    #def __init__(self , secret ):
   #     self.__secret = secret

  #  def reveal(self):
 #       return self.__secret

#class child(parent):
  #  def get_secret(self  ):
 #       return self.reveal()

#c =child("dev")

#print(c.get_secret())



#Rewrite Q4's Temperature using @property for getter and @celsius.setter for setter with validation.


#class temp:
    #def __init__(self):
     #   self.__celsius = 0

    #@property
    #def celsius(self):
     #   return self.__celsius

    #@celsius.setter# pela value check karese pachi set karsw

    #def celsius(self, value):
    #    if value >= -273.15:
   #         self.__celsius = value
  #      else:
 #           print("Invalid temperature! Below absolute zero.")\


#t = temp()

#t.celsius = 25
#print(t.celsius)              # 25 

#t.celsius = -100
#print(t.celsius)              # -100 

#t.celsius = -300
#print(t.celsius)



#Create Student with private __grade, @property grade getter, 
# and @grade.setter that accepts only "A", "B", "C", "D", "F" — else ValueError.

#class student:
    #def __init__(self ,grade):
     #   self.__grade=grade

    #@property

    #def grade(self):
     #   return self.__grade

    #@grade.setter

    #def grade(self ,value):
    #    if value in ("A", "B", "C", "D", "F")   :
   #         self.__grade = value
  #      else:
 #           print("errror")


#s= student("A")
#print(s.grade)

#s.grade = "Z"                           # invalid setter
#print(s.grade)    






## LAST 2 QUE PENDING

#Create abstract Shape(ABC) with private __name, @property name getter, and @abstractmethod area(). 
# Create Rectangle and Circle implementing area(). Loop and print name + area().

#Create BankAccount with private __balance, __owner, @property balance (read-only), deposit(amount), withdraw(amount), and protected _log(message). Create SavingsAccount(BankAccount) with interest_rate and override deposit() to call super().deposit() and self._log(...). Test with deposits and withdrawals.

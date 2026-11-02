#que3
#Create Shape with area() returning 0.
#  Create Circle(Shape) overriding area()
#  to return 3.14 * radius ** 2. Test with Circle(5).


#class shape:
  #  def area(self):  #parent class
 #       return 0  
#class circle(shape):
    #def __init__(self ,radius): #child
   #     self.radius=radius

  #  def area(self):
 #           return 3.14 * self.radius ** 2 # overriding area method of shape class

#c=circle(5)
#print(f"Area of circle with radius {c.radius} is {c.area()}")


#Create Vehicle with __init__(self, brand) and info() printing "Brand: <brand>". 
# Create Car(Vehicle) overriding info() to call super().info() then print "Type: Car".
#  Test with Car("Toyota").

#class Vehicle:
    #def __init__(self ,brand):
   #     self.brand=brand
  #  def info(self):
 #       print(f"Brand: {self.brand}")

#class car(Vehicle):
   # def info(self):
  #      super().info() #super() is used to call the parent class constructor
 #       print("Type: Car")

#c=car("Toyota")
#c.brand = "Toyota"
#c.info()


 #Create Animal with eat(), Mammal(Animal) with walk(), Dog(Mammal) with bark().
 #  Create a Dog and call all three methods.


#class Animal:
 #   def eat(self):
  #      print("Eating...")

#class Mammal(Animal):
 #   def walk(self):
  #      print("Walking...")

#class Dog(Mammal):
 #   def bark(self):
  #       print("Woof!")

#d=Dog()
#d.eat()
#d.walk()
#d.bark()

#6. Using classes from Q5, print results of:

#class Animal:
 #   def eat(self):
  #      print("Eating...")

#class Mammal(Animal):
 #   def walk(self):
  #      print("Walking...")

#class Dog(Mammal):
 #   def bark(self):
  #       print("Woof!")

#dog=Dog()

#isinstance(dog, Animal) #true 
#isinstance(dog, Mammal) #true
#isinstance(dog, Dog) #true
#issubclass(Dog, Animal) #true
#issubclass(Animal, Dog) #false


#Q7. Create Flyer with fly(), Swimmer with swim(),
#  and Duck(Flyer, Swimmer). Create a Duck and call both methods.

#class Flyer:
  #  def fly(self):
 #       print("Flying...")

#class Swimmer:
  #  def swim(self):
 #       print("Swimming...")

#class Duck(Flyer, Swimmer):
 #   pass

#duck = Duck()
#duck.fly()
#duck.swim()

#Create custom exception InsufficientFundsError(Exception). 
# Create BankAccount with withdraw(amount) that raises this error if amount > balance.
#  Test with try/except.


#class InsufficientFundsError(Exception):
 #   pass
#class bankaccount:
    #def __init__(self ,balance):
     #   self.balance=balance
    #def withdraw(self,amount):
         #   if amount > self.balance:
    #            raise InsufficientFundsError("Insufficient funds for withdrawal")
   #         else:
  #              self.balance -= amount#Is account ke balance mein se amount minus karo —
                #aur naya balance wapas store karo.
 #               print(f"Withdrawal successful. New balance: {self.balance}")

#b=bankaccount(1000) # 1000 varu account che ahiya try ma erroro check thse if hase to print thse 
#try:
 #   b.withdraw(1500)
#except InsufficientFundsError as e:
    #print(e) # ahiya print thse "Insufficient funds for withdrawal" if amount > balance


# Create abstract class Shape(ABC) with @abstractmethod area(). 
# Create Rectangle(Shape) and Circle(Shape) implementing area(). 
# Try to instantiate Shape() directly (should fail), 
# then instantiate both subclasses and call area()

#from abc import ABC, abstractmethod      # ← abstractmethod import karo!


#class shape(ABC):
   # @abstractmethod                       # ← abstract method
  #  def area(self):
 #       pass


#class rectangle(shape):
   # def __init__(self, length, width):
    #    self.length = length
   #     self.width = width

  #  def area(self):                       # ← MUST implement
 #       return self.length * self.width


#class circle(shape):
    #def __init__(self, radius):
   #     self.radius = radius

  #  def area(self):                       # ← MUST implement
 #       return 3.14 * self.radius ** 2


# Try to instantiate Shape directly (should fail)
#try:
 #   s = shape()
#except TypeError as e:
 #   print(f"Cannot instantiate Shape: {e}")


# Instantiate both subclasses
#r = rectangle(5, 10)
#c = circle(5)

#print(f"Area of rectangle with length {r.length} and width {r.width} is {r.area()}")
#print(f"Area of circle with radius {c.radius} is {c.area()}")

#polymorphism operation overloading

#class vector:
    #def __init__(self, x, y):
      #  self.x = x
     #   self.y = y

    #def __add__(self, other):
   #     return vector(self.x + other.x, self.y + other.y) #overloading + operator

  #  def __str__(self):
 #       return f"Vector({self.x}, {self.y})"  #print

#v1 = vector(2, 3)
#v2 = vector(4, 5)

#v3 = v1 + v2  #using overloaded + operator
#print(v3)  #prints Vector(6, 8)


#Create Dog, Cat, Cow — each with speak() returning "Woof!", "Meow!", "Moo!"
# . Create one object of each and call speak().

#class Dog:
  #  def speak(self):
 #       return "woof!!"

#class Cat:
  #  def speak(self):
 #       return "meow!!"
#class cow:
  #  def speak(self):
 #       return "moo!!"

#dog = Dog()
#cat = Cat()
#cow = cow()
#print(f"dogsay: {dog.speak()}," f"cat speak: {cat.speak()}, " f"cow speak: {cow.speak()}")


#Using the same classes, put all three objects
#  in a list and loop through them — calling speak() on each.

#class Dog:
  #  def speak(self):
 #       return "woof!!"

#class Cat:
  #  def speak(self):
 #      return "meow!!"
#class cow:
  #  def speak(self):
 #      return "moo!!"

#animals = [Dog() , Cat(), cow()] # ahiya list ma dog,cat,cow ni object store kariye che
#for animal in animals:
    #print(animal.speak()) #ahiya loop ma animal ni object call kariye che and speak method call kariye che



#Write a function make_speak(animal) that takes any object and calls its speak() method.
# Test with Dog, Cat, Cow.


#class Dog:
  #  def speak(self):
 #      return "woof!!"
#class Cat:
  #  def speak(self):
 #      return "meow!!"
#class cow:
  # def speak(self):
 #     return "moo!!"
#def animal_speak(animal):
 #   return animal.speak() #ahiya animal ni object call kariye che and speak method call kariye che

#dog = Dog()
#cat = Cat()
#cow = cow()
#print(animal_speak(dog)) #prints woof!!


#Create Shape with area() returning 0. Create Rectangle(Shape) and Circle(Shape)
#  overriding area(). Loop through both objects and print each area().

#class shape:
 #   def area(self):
       # return 0

#class rectangle(shape):
 #   def __init__(self, width, height):
  #      self.width = width
   #     self.height = height

    #def area(self): #overringin area method of shape class
    #    return self.width * self.height

#class circle(shape):
 #   def __init__(self,radius):
   #     self.radius = radius
  #  def area(self): #overringin area method of shape class
    #    return 3.14 * self.radius ** 2

#shapes = [rectangle(4, 5), circle(3)]
#for shape in shapes:
 #   print(f"Area: {shape.area()}")


#Create Animal with info() printing "I am an animal". Create Dog(Animal) overriding info() — 
# call super() 
# .info() then print "I am a dog". Call info() on a Dog object.

#class Animal:
  #  def info(self):
 #       print("I am an animal")

#class Dog(Animal):
   # def info(self):
  #      super().info() #super() is used to call the parent class constructor
 #       print("I am a dog")


#d = Dog()
#d.info()


#Create two unrelated classes — Robot with speak() → "Beep!" and Ghost with speak() → 
# "Boo!". Write a function make_speak(obj) that calls obj.speak(). Test with both.

#class Robot:
  #  def speak(self):
 #       return "Beep!"

#class Ghost:
    #def speak(self):
   #     return "Boo!"

  #  def make_speak(obj):
 #       return obj.speak()

#robot = Robot()
#ghost = Ghost()
#rint(f"Robot says: {robot.speak() }, Ghost says: {ghost.speak()}")


#Create abstract class Shape(ABC) with @abstractmethod area().
#  Create Rectangle(Shape) and Triangle(Shape) implementing area().
#  Loop through both and print area().


#from abc import ABC, abstractmethod

#class Shape(ABC):
  #  @abstractmethod
  #  def area(self):
 #       pass
#class Rectangle(Shape):
    #def __init__(self ,width, height):
      #  self.width = width
   #     self.height = height

  #  def area(self):
 #        return self.width * self.height

    
#class Triangle(Shape):
    #def __init__(self, base, height):
      #  self.base = base
   #     self.height = height

  #  def area(self):
 #       return 0.5 * self.base * self.height
    
#shapes =[Rectangle(2,3) , Triangle(3,4)]


#for shape in shapes:
    # print(f"Area: {shape.area()}")



#Create Vector class with __init__(x, y). Add __add__ to overload + and __str__ for printing.
#  Test v1 + v2 → (6, 8).

#class vector:
    #def __init__(self,x,y):
      #  self.x=x
     #   self.y=y
    #def __add__(self,others):
     #   return vector(self.x + self.y , others.x + others.y)

    #def __str__(self):
        #return f"vector({self.x}, {self.y})"  #print
            
#v1 = vector(2, 3)
#v2 = vector(4, 5)

#v3 =v1 +v2

#print(v3)


#Create CreditCard, UPI, Cash — each with pay(amount) method printing a message.
#  Write process_payment(payment_method, amount) that calls .pay(amount).
#  Test with all three.

#class Creditcard:
  #  def pay(self,amount):
 #      print(f"Paid ₹{amount} via Credit Card")

#class upi:
  #  def pay(self , amount):
 #       print(f"Paid ₹{amount} via Credit Card")

#class Cash:
  #  def pay(self ,amount):
 #       print(f"Paid ₹{amount} via Credit Card")

#def process_payment(payment_method , amount):
 #   payment_method.pay(amount)


#process_payment(Creditcard(), 500)
#process_payment(upi(), 500)
#process_payment(Cash(), 500)



#Create Animal with speak() → "Some sound", Dog(Animal) with speak() → "Woof!",
#  Puppy(Dog) with speak() → "Yip!". Loop through all three objects, print each speak(), 
# and print isinstance(obj, Animal) and isinstance(obj, Dog) for each.

#class Animal:
  #  def speak(self):
 #       return "some sounf"

#class Dog(Animal):
  #  def speak(self):
 #       return "woof"

#class puppy(Dog):
  #  def speak(self):
 #       return "piiii"

#animals = [Animal() ,Dog() ,puppy()]

#for obj in animals:
    #print(obj.speak())
    #print(isinstance(obj, Animal))
   # print(isinstance(obj, Dog))

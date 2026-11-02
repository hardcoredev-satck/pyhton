#inhertance practice quetions

#Create Animal with eat() → prints "Eating...".
#  Create Dog(Animal) with bark() → prints "Woof!". Create a Dog and call both methods.

#class animal:
  #  def eat(self):
 #       print("Eating...")

#class dog(animal):#ahiay do class animal calss ni qualties inherit kare che and pota ni new add pn kare che 
  #  def bark(self):
 #       print("Woof!")  

#d = dog() #altlejj ahia animal ne call kraya vagr eating adn wofff bev ayuu
#d.eat()
#d.bark()


#Create Person with __init__(self, name, age).
#  Create Student(Person) with __init__(self, name, age, grade) using super(). 
# Create a Student and print all three attributes.

#class person:
    #def __init__(self,name,age):
   #     self.name=name #ahiya name object ni value apde store kariye che and slef.name ane name field che
  #                          #slef is a reference to current object
 #       self.age=age

#class student(person):
   # def __init__(self,name,age,grade):
  #      super().__init__(name,age) #super() is used to call the parent class constructor
 #       self.grade=grade

#s=student("dev",20,"A") #ahiya student class ni object create kariye che and name,age,grade pass kariye che
#print(f"Name: {s.name}, Age: {s.age}, Grade: {s.grade}") #ahiya print kariye che name,age,grade


    


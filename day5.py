day5.py
#Flexible Sum Calculator — Write summarize(*args, **kwargs) that returns the sum of 
# all positional args and the count of keyword args as a tuple.

#def summitall(*args, **kwargs):
    #ahiya *args postion argumnets collect karse
    #*kwargs kewors na argument ne collect karesr dictionar.. ma
 
  #total = sum(args)
 # count = len(kwargs)
  #return total , count

#print(summitall(1,2,3,4,a=34,b=45))


# Flexible Average Calculator
#def avg(*args , **kwargs):

    #total = sum(args)
    #count = len(args)
   # if count == 0:
  
  #      return 0
    #digits = kwargs.get("roun_too", 2) # ahiya get  dictory meths no use karyo che 
       # if niche fucntion call / print ma agar key hase to ee follow htde and iff nia hoi to defaul 2 jse 

 #   return round(total/count ,digits)

#print(avg(10,10,1055,roun_too = 5))


#Returns the largest number from all positional arguments passed via *args

#def largest(*args ,**kwargs):

   # if len(args) ==0:
     #   return kwargs.get("default" , 0)


    #use_abs = kwargs.get("absolute" ,False)

    #if use_abs:
    #    return max(args, key =abs)
   # else:
  #      return max(args)

 #   print(max_finder(10, 25, 7))                          # 25
#print(largest(-50, 20, 30, absolute=True))         # -50
#print(largest(-50, 20, 30, absolute=False))        # 30
#print(largest()) 
 

#Uses **kwargs to accept an optional keyword default (default value 0) — if no numbers are passed, return this default instead of crashing


#def max_finder(*args, **kwargs):
   # if len(args) == 0:
  #      return kwargs.get("default", 0)
 #   return max(args)


#print(max_finder(102, 123, 23, a=354))     # 123
#print(max_finder())                         # 0
#print(max_finder(default=99))               # 99  ← now works!
#print(max_finder(10, 20, 5))                # 20


#multipiy the args


      
#def multiply(*args):
    #result = 1
   # for num in args:
  #      result = result * num
 #   return result

#print(multiply(10,23))        


#Write a function show_info(**kwargs) that prints each key and value on its own line.

#def show_info(**kwargs):
  #  for key , value in kwargs.items():
 #       print(f"{key}: {value}")

#print(show_info(name="darshit"))


#Write a function describe(*args, **kwargs) that prints:

#def both_of(*args , **kwargs):
   # postion = len(args)
  #  options = len(kwargs)

 #   return postion , options

#print(both_of(1,2,3,4, e=20 , b=34))


#Safe .get() Print the value of "a", then "z", then "z" with a default of "missing" — using .get() only.

#def key_value(*args , **kwargs):
    
    #print(kwargs.get("a"))              # value of "a" (None if missing)
   # print(kwargs.get("z"))   
  #  print(kwargs.get("z", "missing")) 

 #   return kwargs.get("e", 0)    
#print(key_value(a= 1, b= 2 ))


#Write a function safe_max(*args) that returns None if no numbers are passed
#  (instead of crashing), and returns the largest number otherwise.

#def safe_max(*args , **kwargs):

   # if len(args) ==0:
     
  #   return kwargs.get("default" , None)

 #   return max(args)
    

#print(safe_max(3, 5, 2))     # 5
#print(safe_max(10))          # 10
#print(safe_max())            # None
#print(safe_max(-1, -5, -3))  # -1


#def analyze(*args, **kwargs):
    #if len(args) == 0:
     #   return kwargs.get("empty_msg", "No data")

    #total = sum(args)
    #count = len(args)
    #digits = kwargs.get("round_to", 2)
    #avg = round(total / count, digits)

    #use_abs = kwargs.get("absolute", False)
    #if use_abs:
   # else:
  #      max_val = max(args)

 #   return count, total, avg, max_val


#print(analyze(10, 20, 30))
# (3, 60, 20.0, 30)

#print(analyze(10, 20, 30, round_to=1))
# (3, 60, 20.0, 30)

#print(analyze(-50, 20, 30, absolute=True))
# (3, 0, 0.0, -50)

#print(analyze(-50, 20, 30, absolute=False))
# (3, 0, 0.0, 30)

#print(analyze())
# No data

#print(analyze(empty_msg="Nothing here"))
# Nothing here

#print(analyze(1, 2, 3, 4, round_to=3, absolute=True))
# (4, 10, 2.5, 4)


#DECORATORS

#def my_decorator(func):
   # def wrapper():
  #      return func()
 #   return wrapper
    
#@my_decorator

#def say_hello():
 #   return "hello darshit"

#print(say_hello())


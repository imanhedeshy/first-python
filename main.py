# # # This is the main file of the project
# # # First Python Project - just started learning Python
# # print("Hello World!")

# # x = 18
# # y = "Hello World!"

# # print(x, y)

# # # example of all variable types in Python
# # x = 5 # int
# # print(x, "is of type", type(x))
# # y = 5.5 # float
# # print(y, "is of type", type(y))
# # z = "Hello World!" # string
# # print(z, "is of type", type(z))
# # a = True # bool
# # print(a, "is of type", type(a))
# # b = ["apple", "banana", "cherry"] # list
# # print(b, "is of type", type(b))
# # c = ("apple", "banana", "cherry") # tuple
# # print(c, "is of type", type(c))
# # d = range(6) # range
# # print(d, "is of type", type(d))
# # e = {"name" : "John", "age" : 36} # dict
# # print(e, "is of type", type(e))
# # f = {"apple", "banana", "cherry"} # set
# # print(f, "is of type", type(f))
# # g = frozenset({"apple", "banana", "cherry"}) # frozenset
# # print(g, "is of type", type(g))
# # h = b"Hello" # bytes
# # print(h, "is of type", type(h))
# # i = bytearray(5) # bytearray
# # print(i, "is of type", type(i))
# # j = memoryview(bytes(5)) # memoryview
# # print(j, "is of type", type(j))


# # # Operators
# # # Arithmetic Operators
# # x = 5
# # y = 3
# # print(x + y) # addition
# # print(x - y) # subtraction
# # print(x * y) # multiplication
# # print(x / y) # division
# # print(x % y) # modulus
# # print(x ** y) # exponentiation
# # print(x // y) # floor division

# # # Assignment Operators
# # x = 5
# # print(x)
# # x += 3
# # print(x)
# # x -= 3
# # print(x)
# # x *= 3
# # print(x)
# # x /= 3
# # print(x)
# # x %= 3
# # print(x)
# # x //= 3
# # print(x)
# # x **= 3
# # print(x)
# # x &= 3
# # print(x)
# # x |= 3
# # print(x)
# # x ^= 3
# # print(x)
# # x >>= 3
# # print(x)
# # x <<= 3
# # print(x)

# # # Comparison Operators
# # x = 5
# # y = 3
# # print(x == y) # equal
# # print(x != y) # not equal
# # print(x > y) # greater than
# # print(x < y) # less than
# # print(x >= y) # greater than or equal
# # print(x <= y) # less than or equal

# # # Logical Operators
# # x = 5
# # print(x > 3 and x < 10) # and
# # print(x > 3 or x < 4) # or
# # print(not(x > 3 and x < 10)) # not

# # # Identity Operators
# # x = ["apple", "banana"]
# # y = ["apple", "banana"]
# # z = x
# # print(x is z) # is
# # print(x is y) # is not
# # print(x == y) # equal
# # print(x is not z) # is not
# # print(x is not y) # is not
# # print(x != y) # not equal

# # # Membership Operators
# # x = ["apple", "banana"]
# # print("banana" in x) # in
# # print("pineapple" not in x) # not in

# # # Bitwise Operators
# # x = 5
# # y = 3
# # print(x & y) # and
# # print(x | y) # or
# # print(x ^ y) # xor
# # print(~x) # not
# # print(x << y) # zero fill left shift
# # print(x >> y) # signed right shift

# # # Lists
# # thislist = ["apple", "banana", "cherry"]
# # print(thislist) # print list
# # print(thislist[1]) # print second item
# # print(thislist[-1]) # print last item
# # print(thislist[1:3]) # print second and third item
# # print(thislist[:2]) # print first two items
# # print(thislist[1:]) # print all items except first
# # print(thislist[-3:-1]) # print last two items
# # thislist[1] = "blackcurrant" # change second item
# # print(thislist) # print list
# # for x in thislist: # loop through list
# #     print(x) # print item
# # if "apple" in thislist: # check if item exists
# #     print("Yes, 'apple' is in the fruits list") # print message
# # print(len(thislist)) # print number of items
# # thislist.append("orange") # add item to end of list
# # print(thislist) # print list
# # thislist.insert(1, "orange") # add item at specified index
# # print(thislist) # print list
# # thislist.remove("banana") # remove specified item
# # print(thislist) # print list
# # thislist.pop() # remove last item
# # print(thislist) # print list
# # del thislist[0] # remove specified index
# # print(thislist) # print list
# # del thislist # delete list
# # thislist = list(("apple", "banana", "cherry")) # create list using constructor
# # print(thislist) # print list
# # thislist.clear() # empty list
# # print(thislist) # print list
# # thislist = list(("apple", "banana", "cherry")) # create list using constructor
# # mylist = thislist.copy() # copy list
# # print(mylist) # print list
# # mylist = list(thislist) # copy list
# # print(mylist) # print list
# # mylist = thislist # copy list
# # print(mylist) # print list
# # mylist = thislist[:] # copy list
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist.sort() # sort list
# # print(mylist) # print list
# # mylist.sort(reverse = True) # sort list descending
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist.reverse() # reverse list
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist3 = mylist + mylist2 # join lists
# # print(mylist3) # print list
# # for x in mylist: # loop through list
# #     mylist2.append(x) # add item to list
# # print(mylist2) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # for x in mylist2: # loop through list
# #     mylist.append(x) # add item to list
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist.extend(mylist2) # add list to list
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist3 = mylist + mylist2 # join lists
# # print(mylist3) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist.extend(mylist2) # add list to list
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist3 = mylist.copy() # copy list
# # mylist3.extend(mylist2) # add list to list
# # print(mylist3) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist3 = mylist.copy() # copy list
# # mylist3.append(mylist2) # add list to list
# # print(mylist3) # print list
# # mylist = [3, 2, 1] # create list
# # mylist2 = [4, 5, 6] # create list
# # mylist3 = mylist.copy() # copy list
# # mylist3.insert(1, mylist2) # add list at specified index
# # print(mylist3) # print list
# # mylist = [3, 2, 1] # create list
# # print(mylist.count(3)) # count number of items
# # mylist = [3, 2, 1] # create list
# # print(mylist.index(3)) # find index of item
# # mylist = [3, 2, 1] # create list
# # mylist.remove(3) # remove specified item
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist.pop(1) # remove specified index
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # del mylist[1] # remove specified index
# # print(mylist) # print list
# # mylist = [3, 2, 1] # create list
# # mylist.clear() # empty list
# # print(mylist) # print list

# # # Tuples
# # thistuple = ("apple", "banana", "cherry")
# # print(thistuple) # print tuple
# # print(thistuple[1]) # print second item
# # print(thistuple[-1]) # print last item
# # print(thistuple[1:3]) # print second and third item
# # print(thistuple[:2]) # print first two items

# # # Sets
# # thisset = {"apple", "banana", "cherry"}
# # print(thisset) # print set
# # for x in thisset: # loop through set
# #     print(x) # print item
# # print("banana" in thisset) # check if item exists
# # thisset.add("orange") # add item
# # print(thisset) # print set

# # # Dictionaries
# # thisdict = {
# #     "brand": "Ford",
# #     "model": "Mustang",
# #     "year": 1964
# # }
# # print(thisdict) # print dictionary
# # print(thisdict["model"]) # print value of specified key
# # print(thisdict.get("model")) # print value of specified key
# # thisdict["year"] = 2018 # change value of specified key
# # print(thisdict) # print dictionary
# # for x in thisdict: # loop through dictionary
# #     print(x) # print key
# # for x in thisdict: # loop through dictionary
# #     print(thisdict[x]) # print value
# # for x in thisdict.values(): # loop through dictionary
# #     print(x) # print value
# # for x, y in thisdict.items(): # loop through dictionary
# #     print(x, y) # print key and value
# # if "model" in thisdict: # check if key exists
# #     print("Yes, 'model' is one of the keys in the thisdict dictionary") # print message
# # print(len(thisdict)) # print number of items
# # thisdict["color"] = "red" # add item
# # print(thisdict) # print dictionary
# # thisdict.pop("model") # remove specified key
# # print(thisdict) # print dictionary
# # thisdict.popitem() # remove last inserted key
# # print(thisdict) # print dictionary
# # del thisdict["model"] # remove specified key
# # print(thisdict) # print dictionary
# # del thisdict # delete dictionary
# # thisdict = dict(brand="Ford", model="Mustang", year=1964) # create dictionary using constructor
# # print(thisdict) # print dictionary
# # thisdict.clear() # empty dictionary

# # # If...Else
# # a = 33
# # b = 200
# # if b > a: # if
# #     print("b is greater than a") # print message
# # a = 33
# # b = 33
# # if b > a: # if
# #     print("b is greater than a") # print message
# # elif a == b:
# #     print("a and b are equal")
# # a = 200
# # b = 33
# # if b > a: # if
# #     print("b is greater than a") # print message
# # elif a == b:
# #     print("a and b are equal")
# # else:
# #     print("a is greater than b")
# # a = 200
# # b = 33
# # if b > a: # if
# #     print("b is greater than a") # print message
# # else:
# #     print("b is not greater than a")
# # a = 2
# # b = 330
# # print("A") if a > b else print("B") # if short hand
# # a = 330
# # b = 330
# # print("A") if a > b else print("=") if a == b else print("B") # if short hand
# # a = 200
# # b = 33
# # c = 500
# # if a > b and c > a: # if
# #     print("Both conditions are True") # print message
# # a = 200
# # b = 33
# # c = 500
# # if a > b or a > c: # if
# #     print("At least one of the conditions is True") # print message
# # x = 41
# # if x > 10: # if
# #     print("Above ten,") # print message
# #     if x > 20: # if
# #         print("and also above 20!") # print message
# #     else:
# #         print("but not above 20.")
# # a = 33
# # b = 200
# # if b > a: # if
# #     pass # do nothing

# # # While Loops
# # i = 1
# # while i < 6: # while
# #     print(i) # print number
# #     i += 1 # increment number
# # i = 1
# # while i < 6: # while
# #     print(i) # print number
# #     if i == 3: # if
# #         break # stop loop
# #     i += 1 # increment number
# # i = 0
# # while i < 6: # while
# #     i += 1 # increment number
# #     if i == 3: # if
# #         continue # skip number
# #     print(i) # print number
# # i = 1

# # # For Loops
# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits: # for
# #     print(x) # print item
# # for x in "banana": # for
# #     print(x) # print letter
# # fruits = ["apple", "banana", "cherry"]
# # for x in fruits: # for
# #     print(x) # print item
# #     if x == "banana": # if
# #         break # stop loop
# # for x in fruits: # for
# #     if x == "banana": # if
# #         break # stop loop
# #     print(x) # print item
# # for x in fruits: # for
# #     if x == "banana": # if
# #         continue # skip item
# #     print(x) # print item
# # for x in range(6): # for
# #     print(x) # print number
# # for x in range(2, 6): # for
# #     print(x) # print number
# # for x in range(2, 30, 3): # for
# #     print(x) # print number

# # # Functions
# # def my_function(): # function
# #     print("Hello from a function") # print message
# # my_function() # call function
# # def my_function(fname): # function
# #     print(fname + " Refsnes") # print name
# # my_function("Emil") # call function
# # my_function("Tobias") # call function
# # my_function("Linus") # call function
# # def my_function(fname, lname): # function
# #     print(fname + " " + lname) # print name
# # my_function("Emil", "Refsnes") # call function
# # def my_function(*kids): # function
# #     print("The youngest child is " + kids[2]) # print message
# # my_function("Emil", "Tobias", "Linus") # call function
# # def my_function(child3, child2, child1): # function
# #     print("The youngest child is " + child3) # print message
# # my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") # call function
# # def my_function(**kid): # function
# #     print("His last name is " + kid["lname"]) # print message
# # my_function(fname = "Tobias", lname = "Refsnes") # call function
# # def my_function(country = "Norway"): # function
# #     print("I am from " + country) # print message
# # my_function("Sweden") # call function
# # my_function("India") # call function
# # my_function() # call function
# # my_function("Brazil") # call function
# # def my_function(food): # function
# #     for x in food: # for
# #         print(x) # print item
# # fruits = ["apple", "banana", "cherry"]
# # my_function(fruits) # call function
# # def my_function(x): # function
# #     return 5 * x # return value
# # print(my_function(3)) # print value
# # print(my_function(5)) # print value
# # print(my_function(9)) # print value
# # def my_function(): # function
# #     pass # do nothing
# # def my_function(): # function
# #     print("Hello from a function") # print message
# # my_function() # call function

# # # Lambda
# # x = lambda a : a + 10 # lambda
# # print(x(5)) # print value
# # x = lambda a, b : a * b # lambda
# # print(x(5, 6)) # print value
# # x = lambda a, b, c : a + b + c # lambda
# # print(x(5, 6, 2)) # print value
# # def myfunc(n): # function
# #     return lambda a : a * n # return value
# # mydoubler = myfunc(2) # call function
# # print(mydoubler(11)) # print value
# # def myfunc(n): # function
# #     return lambda a : a * n # return value
# # mydoubler = myfunc(2) # call function
# # mytripler = myfunc(3) # call function
# # print(mydoubler(11)) # print value
# # print(mytripler(11)) # print value

# # # Arrays
# # cars = ["Ford", "Volvo", "BMW"]
# # print(cars) # print array
# # x = cars[0] # get first item
# # print(x) # print item
# # cars[0] = "Toyota" # change first item
# # print(cars) # print array
# # x = len(cars) # get number of items
# # print(x) # print number
# # for x in cars: # loop through array
# #     print(x) # print item
# # cars.append("Honda") # add item
# # print(cars) # print array
# # cars.pop(1) # remove specified index
# # print(cars) # print array
# # cars.remove("Volvo") # remove specified item
# # print(cars) # print array
# # cars.clear() # empty array
# # print(cars) # print array
# # cars = ["Ford", "Volvo", "BMW"]
# # cars.sort() # sort array
# # print(cars) # print array
# # cars.sort(reverse = True) # sort array descending
# # print(cars) # print array
# # cars = ["Ford", "Volvo", "BMW"]
# # cars.reverse() # reverse array
# # print(cars) # print array
# # cars = ["Ford", "Volvo", "BMW"]
# # cars2 = cars.copy() # copy array
# # print(cars2) # print array
# # cars = ["Ford", "Volvo", "BMW"]
# # cars2 = list(cars) # copy array
# # print(cars2) # print array
# # cars = ["Ford", "Volvo", "BMW"]
# # cars2 = cars # copy array
# # print(cars2) # print array
# # cars = ["Ford", "Volvo", "BMW"]
# # cars2 = cars[:] # copy array
# # print(cars2) # print array

# # # Classes and Objects
# # class MyClass: # class
# #     x = 5 # attribute
# # p1 = MyClass() # create object
# # print(p1.x) # print attribute
# # class Person: # class
# #     def __init__(self, name, age): # function
# #         self.name = name # attribute
# #         self.age = age # attribute
# # p1 = Person("John", 36) # create object
# # print(p1.name) # print attribute
# # print(p1.age) # print attribute
# # class Person: # class
# #     def __init__(self, name, age): # function
# #         self.name = name # attribute
# #         self.age = age # attribute
# #     def myfunc(self): # function
# #         print("Hello my name is " + self.name) # print message
# # p1 = Person("John", 36) # create object
# # p1.myfunc() # call function

# # # Inheritance
# # class Person: # class
# #     def __init__(self, fname, lname): # function
# #         self.firstname = fname # attribute
# #         self.lastname = lname # attribute
# #     def printname(self): # function
# #         print(self.firstname, self.lastname) # print name
# # class Student(Person): # class
# #     pass # do nothing
# # x = Student("Mike", "Olsen") # create object
# # x.printname() # call function
# # class Student(Person): # class
# #     def __init__(self, fname, lname): # function
# #         Person.__init__(self, fname, lname) # attribute
# # x = Student("Mike", "Olsen") # create object
# # x.printname() # call function
# # class Student(Person): # class
# #     def __init__(self, fname, lname): # function
# #         super().__init__(fname, lname) # attribute
# # x = Student("Mike", "Olsen") # create object
# # x.printname() # call function

# # # Iterators
# # mytuple = ("apple", "banana", "cherry")
# # myit = iter(mytuple) # create iterator
# # print(next(myit)) # print item
# # print(next(myit)) # print item
# # print(next(myit)) # print item
# # mystr = "banana"
# # myit = iter(mystr) # create iterator
# # print(next(myit)) # print letter
# # print(next(myit)) # print letter
# # print(next(myit)) # print letter
# # mytuple = ("apple", "banana", "cherry")
# # for x in mytuple: # loop through iterator
# #     print(x) # print item
# # mystr = "banana"
# # for x in mystr: # loop through iterator
# #     print(x) # print letter
# # class MyNumbers: # class
# #     def __iter__(self): # function
# #         self.a = 1 # attribute
# #         return self # return value
# #     def __next__(self): # function
# #         x = self.a # attribute
# #         self.a += 1 # attribute
# #         return x # return value
# # myclass = MyNumbers() # create object
# # myiter = iter(myclass) # create iterator
# # print(next(myiter)) # print number
# # print(next(myiter)) # print number
# # print(next(myiter)) # print number
# # print(next(myiter)) # print number
# # print(next(myiter)) # print number

# # # Scope
# # def myfunc(): # function
# #     x = 300 # local variable
# #     print(x) # print variable
# # myfunc() # call function
# # def myfunc(): # function
# #     x = 300 # local variable
# #     def myinnerfunc(): # function
# #         print(x) # print variable
# #     myinnerfunc() # call function
# # myfunc() # call function
# # x = 300 # global variable
# # def myfunc(): # function
# #     print(x) # print variable
# # myfunc() # call function
# # print(x) # print variable
# # def myfunc(): # function
# #     global x # global variable
# #     x = 300 # global variable
# # myfunc() # call function
# # print(x) # print variable
# # x = 300 # global variable

# # # Modules
# # import mymodule # import module
# # mymodule.greeting("Jonathan") # call function
# # import mymodule as mx # import module
# # a = mx.person1["age"] # get value
# # print(a) # print value
# # import platform # import module
# # x = platform.system() # get value
# # print(x) # print value
# # import platform # import module
# # x = dir(platform) # get value
# # print(x) # print value
# # from mymodule import person1 # import module
# # print(person1["age"]) # print value

# # # Dates
# # import datetime # import module
# # x = datetime.datetime.now() # get value
# # print(x) # print value
# # import datetime # import module
# # x = datetime.datetime.now() # get value

# # # JSON
# # import json # import module
# # x = '{ "name":"John", "age":30, "city":"New York" }' # create object
# # y = json.loads(x) # parse JSON
# # print(y["age"]) # print value
# # import json # import module
# # x = { # create object
# #     "name": "John",
# #     "age": 30,
# #     "city": "New York"
# # }
# # y = json.dumps(x) # convert to JSON
# # print(y) # print value
# # import json # import module
# # print(json.dumps({"name": "John", "age": 30})) # convert to JSON
# # print(json.dumps(["apple", "bananas"])) # convert to JSON
# # print(json.dumps(("apple", "bananas"))) # convert to JSON
# # print(json.dumps("hello")) # convert to JSON
# # print(json.dumps(42)) # convert to JSON
# # print(json.dumps(31.76)) # convert to JSON
# # print(json.dumps(True)) # convert to JSON
# # print(json.dumps(False)) # convert to JSON
# # print(json.dumps(None)) # convert to JSON

# # # RegEx
# # import re # import module
# # txt = "The rain in Spain" # create string
# # x = re.search("^The.*Spain$", txt) # search string
# # print(x) # print value
# # import re # import module
# # txt = "The rain in Spain" # create string
# # x = re.findall("ai", txt) # find all matches
# # print(x) # print value
# # import re # import module
# # txt = "The rain in Spain" # create string
# # x = re.search("\s", txt) # search string
# # print("The first white-space character is located in position:", x.start()) # print value
# # import re # import module
# # txt = "The rain in Spain" # create string
# # x = re.split("\s", txt) # split string
# # print(x) # print value
# # import re # import module
# # txt = "The rain in Spain" # create string
# # x = re.split("\s", txt, 1) # split string
# # print(x) # print value

# # # Try...Except
# # try: # try
# #     print(x) # print value
# # except:
# #     print("An exception occurred")
# # try: # try
# #     print(x) # print value
# # except NameError:
# #     print("Variable x is not defined")
# # except:
# #     print("Something else went wrong")
# # try: # try
# #     print("Hello") # print message
# # except:
# #     print("Something went wrong")
# # else:
# #     print("Nothing went wrong")
# # try: # try
# #     print(x) # print value
# # except:
# #     print("Something went wrong")
# # finally:
# #     print("The 'try except' is finished")

# # # User Input
# # username = input("Enter username:") # get input
# # print("Username is: " + username) # print input
# # age = input("Enter your age:") # get input
# # print("Your age is: " + age) # print input
# # x = int(1) # convert to integer
# # y = int(2.8) # convert to integer
# # z = int("3") # convert to integer
# # print(x) # print value
# # print(y) # print value
# # print(z) # print value
# # x = float(1) # convert to float
# # y = float(2.8) # convert to float
# # z = float("3") # convert to float
# # w = float("4.2") # convert to float
# # print(x) # print value
# # print(y) # print value
# # print(z) # print value
# # print(w) # print value
# # x = str("s1") # convert to string
# # y = str(2) # convert to string
# # z = str(3.0) # convert to string
# # print(x) # print value
# # print(y) # print value
# # print(z) # print value

# # # String Formatting
# # price = 49 # create variable
# # txt = "The price is {} dollars" # create string
# # print(txt.format(price)) # print value
# # txt = "The price is {:.2f} dollars" # create string
# # print(txt.format(price)) # print value
# # txt = "The price is {:.0f} dollars" # create string
# # print(txt.format(price)) # print value
# # quantity = 3 # create variable
# # itemno = 567 # create variable
# # price = 49 # create variable

# # # Escape Characters
# # txt = "We are the so-called \"Vikings\" from the north." # create string
# # print(txt) # print value
# # txt = "Hello\nWorld!" # create string
# # print(txt) # print value
# # txt = "Hello\rWorld!" # create string
# # print(txt) # print value
# # txt = "Hello\tWorld!" # create string
# # print(txt) # print value
# # txt = "Hello \bWorld!" # create string
# # print(txt) # print value
# # txt = "Hello \fWorld!" # create string
# # print(txt) # print value
# # txt = "\110\145\154\154\157" # create string
# # print(txt) # print value
# # txt = "\x48\x65\x6c\x6c\x6f" # create string
# # print(txt) # print value

# x = 10
# if x > 10:
#     print("x is greater than 10")
# elif x == 10:
#     print("x is 10")
# else:
#     print("x is less than 10")

# x = [1, 3, 5, 7, 9, 11]
# for i in x:
#     print(i)

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# # function
# def greet(name):
#     return "Hello " + name

# print(greet("Iman"))

print("Hello World!")

x = 10
y = "Python is fun"

print(x)
print(y)
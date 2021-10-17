#classes

# class Employee:
#     company = 'google'
#     salary = 100

# harry = Employee()
# rajni = Employee()

# #creating instance attributes salary for both the objects
# harry.salary= 300
# rajni.salary=400
# prem=Employee()

# print(harry.company)
# print(rajni.company)

# Employee.company='youtube'

# print(harry.company)
# print(rajni.company)
# print(harry.salary)
# print(rajni.salary)
# print(prem.salary)

# self

# class Employee:
#     company = 'google'

#     def getsalary(self):
#         print(f'Salary for this employee working in {self.company} is {self.salary}k per month')

#     @staticmethod
#     def greet():
#         print('Good morning, sir')


# harry = Employee()
# harry.salary = 10000
# harry.getsalary()  # is same as Employee.getsalary(harry)
# harry.greet()

# printing  the employee deatils
# class Employee():
#     def getdeatails(self):
#         print(f'The name of the employee is {self.name}')
#         print(f'The salary of the employee is {self.salary}')
#         print(f'The subunit of the employee is {self.subnit}')

#     def __init__(self, name, salary, subnit):
#         self.name = name
#         self.salary = salary
#         self.subnit = subnit


# harry = Employee('harry', 1000, 'Youtube')
# harry.getdeatails()


# print('1.to store info of microsoft programmers -- important')


# class Programmer:
#     company = 'Microsoft'

#     def __init__(self, name, product):
#         self.name = name
#         self.product = product

#     def getInfo(self):
#         print(
#             f'the name of the {self.company} programmer is {self.name} and is working on {self.product} product')


# harry = Programmer("Harry", "skype")
# rajni = Programmer("Rajni", "youtube")
# rajni.getInfo()


# print('2.class calculator')



# class Claculator:
#     @staticmethod
#     def greet():
#         print("Hello user")
#     def __init__(self, num):
#         self.num = num

#     def sqaure(self):
#         print(f'The value of {self.num} is {self.num **2}')

#     def squareroot(self):
#         print(f'The value of {self.num} is {self.num **0.5}')

#     def cube(self):
#         print(f'The value of {self.num} is {self.num **3}')
# a = Claculator(3)
# a.greet()
# a.sqaure()
# a.squareroot()
# a.cube()

# print('3.train book tickets')

# class Train:
#     def __init__(self , name , fare , seats):
#         self.name=name
#         self.fare=fare
#         self.seats=seats
    
#     def getStatus(self):
#         print(f"The name of the train is {self.name}")
#         print(f"The fare of the train is {self.fare}")
#         print(f"The seats of the train is {self.seats}")
    
#     def bookTickets(self):
#         if(self.seats>0):
#             print(f'ur ticket has been booked ur seat number is:{self.seats} ')
#             self.seats=self.seats - 1
#         else:
#             print('sorry the train is full!')

# intercity=Train("intercity blah 1405",300,2)
# intercity.getStatus()
# intercity.bookTickets()
# intercity.getStatus()
# intercity.bookTickets()
# intercity.getStatus()

class Point:
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')

class Dog(Point):
    def bark(self):
        print('bark')


point1=Point()
point1.draw()

d=Dog()
d.bark()
d.draw()







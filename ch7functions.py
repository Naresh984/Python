# #https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Functions
# #it allows us to code with specific purpose in a single location
# #they r reusable

# def hello_fun():
#     print('*using print in func--')
# pass#it used when we didn't give any print to avoid error n say to use it later
# hello_fun()
# hello_fun()

# def blah():
#     return 'using return'
# print(blah().upper())

# def hello(greeting,name='you'):## the name here is default if v don't specify any
#     return '{} function {}'.format(greeting,name)
# print(hello('hi','damon'))

# def students_info(*args,**kwargs):
#     print(args)
#     print(kwargs)
# courses=['maths','science']
# info={'name':'damon','age':23}
# students_info(*courses, **info)#*start unpacks the list and dictioaries


# #random leap year problem

# # Number of days per month. First value placeholder for indexing purposes.
# month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# def is_leap(year):
#     """Return True for leap years, False for non-leap years."""

#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# def days_in_month(year, month):
#     """Return number of days in that month in that year."""

#     if not 1 <= month <= 12:
#         return 'Invalid Month'

#     if month == 2 and is_leap(year):
#         return 29

#     return month_days[month]

# print(is_leap(2020))
# print(days_in_month(2020,3))

# print('1.Write a program to convert celsius to farheniet')

# # (0°C × 9/5) + 32 = 32°F

# cel = int(input('Enter the temp in celsius: '))
# def farh(cel):
#     return (cel * (9/5)) + 32

# print("the temrperature in farheiet is " + str(farh(cel)))

print('2.to print a multiplication table')
def table(num):
    for i in range(1,11):
        print(f'{num}*{i}={num*i}')
    
a=int(input('Enter the no.: '))
print(table(a))


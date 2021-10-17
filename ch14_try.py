try:
    age=int(input('Enter ur Age: '))
    income = 2000
    risk = income/age
    print(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print("Age can't be 0")

#type of error 
#https://www.tutorialsteacher.com/python/error-types-in-python
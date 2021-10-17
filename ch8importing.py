#method1
import my_module 

courses=['blah','science','maths','chem']
index=my_module.find_index(courses,'chem')

print(index)

#method2
from my_module import find_index as find,test   #as is used when v want to use short of that function 

courses=['blah','science','maths','chem']
index=find(courses,'maths') # if v use from import specific then v can use witout importname 

print(test)
print(index)

#method3
from my_module import * # to import everything, this astrik makes it harder to find any errors later
#new
import sys
print(sys.path)

#if v don't have that module in current directory v get error
#ModuleNotFoundError: No module named 'my_module'--like this
#so v have to add it in ur sys path manually using nano or manually adding path here only

#useful module
#random
import random
rando_course=random.choice(courses)
print(rando_course)

#using maths modules
import math
rads=math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
today=datetime.date.today()
print(today)

print(calendar.isleap(2017))#using calendar module

import os
print(os.getcwd())

print('location of module')
print(os.__file__)

#import antigravity -- this opens a webbrowser

message='hello world'                           
print(message) 

#quotes problem

message1="harry's world"
print(message1)

message3='harry\'s world' #giving backslash , python will know that it close the string
print(message3)

#mutiple lines
message4=''' harry's world was very famous in early 20's '''
print(message4)

# #
# print(len(message)) #prints the len of string
# #slicing
# print(message[10]) #prints the letter of the index u specified and if u specify index that doesn't exist u'll get error
# print(message[0:5])#print out from 1st index to 2nd index(excluding it)
# print(message[:5])#default start from first letter

#list
# my_list=[0,  1, 2, 3, 4, 5, 6, 7, 8, 9]
# #        0,  1, 2, 3, 4, 5, 6, 7, 8, 9
# #       -10,-9,-8,-7,-6,-5,-4,-3,-2,-1  v can also use -ve to access the string

# print(my_list[0])
# print(my_list[-1])
# # list[start:end:step]
# print(my_list[3:7])
# print(my_list[-7:-2])
# print(my_list[1:])# to print all the numbers
#  #step allows u to skip certain no.of values , 1 is the default 
# print(my_list[2:-1:2]) #it starts at 2 then goes till -1 ,then print every 2nd no.
# print(my_list[2:-1:3]) #prints eveyr 3rd no.
# print(my_list[-1:2:-1])
# #reverse the whole list
# print(my_list[::-1])# leave start begining and end empty to go there , n -ve 

# sample_url='http://coreyms.com'
# #get top level domain from url
# print(sample_url[-4:])
# #without http://
# print(sample_url[7:])      
# print(sample_url[7:-4])   


#string methods
# message='hello world'
# print(message.upper())
# print(message.count('hello'))#if v wanna find the no. of times a letter is repeating
# print(message.find('world'))#to find at what index is the word/letter first appears
# print(message.find('universe'))#it will return -1 bcz it is not present 

# #to replace a word
# message_new=message.replace('world','universe')#v have to declare it to make it work
# print(message_new)

#to add strings
# greeting='Hello'
# name='jughead'
# message=greeting + ', ' + name + '.Welcome!'
# print(message)

# message=f'{greeting}, {name.upper()}.Welcome!'#f strings , maybe i can upper myword from message itself 
# print(message)

# #string formatting-- using this bcz concatination is not always good 

# person={'name':'jughead','age':28}#dictionary--
# tag='h1'
# text='this is a headline in html'
# sentence='<{0}>{1}<{0}>'.format(tag,text)
# print(sentence)

# sentence='My name is {0[name]} and I am {0[age]} years old'.format(person,person)
# print(sentence)

# l=['jughead',28]#list
# sentence='My name is {0[0]} and I am {0[1]} years old'.format(l,l)
# print(sentence)

# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', '33')

# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

# print('using **')
# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

# pi = 3.14159265

# sentence = 'Pi is equal to {:.2f}'.format(pi)# to get upto two decimal places or .3f for three decimal places
# print(sentence)

# sentence='1 MB is equal to {:,.2f} bytes'.format(1000**2)# v added a comma to separte it and also giving two decimals places.
# print(sentence)

# import datetime

# my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
# sentence = '{:%B %d, %Y}'.format(my_date)
# print(sentence)

# # March 01, 2016 fell on a Tuesday and was the 061 day of the year.

# sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
# print(sentence)

# dir function

# greeting='Hello'
# name='jughead'
# #reference
# print(dir(name))
# # to get help 
# print(help(str))#to more what all v can use in string
# print(help(str.lower))




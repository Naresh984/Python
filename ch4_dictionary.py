# #Dictionaries - Working with Key-Value Pairs

# student = {'name':'john','age': 25 , 'courses':['maths','compsci']}
# print(student)
# print(student['name'])#we are asking for that key value 
# student['phone']= '55-555'
# print(student.get('phone', 'Not found'))#if v use get v won't get an error if key doesn't exist

# #update
# student.update({'name':'jane', 'age': 26 , 'phone':'55-555'})
# print(student)

# #delete
# del student['age']
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())#pairs

# for key, value in student.items():
#     print(key,value)

# #examples
# print('the notes \n')
# mydict={
#     "panka":'fan',
#     "daba":'box',
#     "hath":'hand' 
# }
# print('options are ', mydict.keys())
# a=input("enter the hindi words:\n")
# #print('the meaning of ur word is', mydict[a])

# #below line will not give an error if the key is not present in the dictionary.
# print('the meaning of the word is', mydict.get(a))

# #2 write a program to input eight number from the user and display the unique no.s
# #Dictionaries cannot contain duplicate values so a dictionary with only unique values is returned by dict.
# print('A program to input eight number from the user and display the unique no.s\n')


# num1 =int(input('ENTER number 1 \n')) #typecasting
# num2 =int(input('ENTER number 2 \n'))
# num3 =int(input('ENTER number 3 \n'))
# num4 =int(input('ENTER number 4 \n'))
# num5 =int(input('ENTER number 5 \n'))
# num6 =int(input('ENTER number 6 \n'))
# num7 =int(input('ENTER number 7 \n'))
# num8 =int(input('ENTER number 8 \n'))

# s ={num1,num2,num3,num4,num5,num6,num7,num8} 
# print(s)

# print('Can v have a set with 18(int) and 18(str) as value in it')

# s={18,"18"} #both r different so it will print both 
# print(s)

#to create an empty list .allwo 4 frnds to enter their favourite language as values and use keys as their names.
favlan={}
a = input('enter ur favourite lan subham\n')
b = input('enter ur favourite lan naresh\n')
c = input('enter ur favourite lan aniket\n')
d = input('enter ur favourite lan sonali\n')

favlan['subham']=a
favlan['naresh']=b
favlan['aniket']=c
favlan['sonali']=d

print(favlan)
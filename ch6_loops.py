
# #loop in a loop
# for num in nums:
#     for letter in 'abc':
#         print(num,letter)


# for i in range(2,11):
#     print(i)

# #random
# names = 'nani'
# name =input('what is ur name???')
# if name in names:
#     print('hey nani how are you doing today ')
# else:
#         print('ur a outsider...')


# while loops
# i=1
# while i<=50:
#     print(str(i))
#     i+=1
# print('loop completed')

# while loop

# to print the content of a list
# print('To print the content of the list')
# fruits=['mango','chikku','pineapple']
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i+=1

# for loop
# print('To print the content of the list using for loop')
# fruits=['mango','chikku','pineapple']

# for item in fruits:
#     print(item)

#print('range function and for loop with else')
# in this else part willbe executed after the successful termination of loop
# for range in range(1,10):
#     print(range)
# else:
#     print('this is inside else for a loop')

# break and continue
# nums =[1,2,3,4,5,6]
# for num in nums:
#     if num==3:
#         print('found!')
#         break
#     print(num)

# print('1.mulitplication table')
# num=int(input('Enter ur number:'))
# i=1
# for i in range(1,11):
#     print(str(num) + 'x' + str(i) + '=' + str(i*num))
#     i+=1

# print('2.write a program to greet the person whose letter startwith')
# l1=['sohan','sachin','rahul']
# for name in l1:
#     if name.startswith('s'):
#         print('hello ' + name)

# print('3.multiplication table in while loop')
# num=int(input('Enter ur number:'))
# i=1
# while i in range(1,11):
#     print(str(num) + 'x' + str(i) + '=' + str(i*num))
#     i+=1

# print('4.to check whether the no. is prime or not')
# num=int(input('Enter the number:'))
# prime=True
# for i in range(2, num):
#     if(num%i==0):
#         prime=False
#         break
# if prime:
#     print('The number is prime')
# else:
#     print('The number is not prime')

# print('5.factorial program')

# num = int(input('Enter the number:'))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
# print(f"the factorial of this number is {factorial}")

# print('6.pattern printing')

# num=int(input('Enter the no. of times to be printed:'))
# for i in range(num):
#     print("*"*i)

# print('7.start pattern')
# n=3
# for i in range(3):
#     print(" " * (n-i-1), end="")# end is used to avoid extra spaces after print and to print in the same line 
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1),)


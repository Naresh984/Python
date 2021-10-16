
##to check whether a given identifier is keyword or not

# import keyword

# s=keyword.iskeyword('int')
# print(s)

## type conversion

# a=2+4.5 #implicit conversion
# print(a)
# b=float(2)+4.5 #explicit conversion
# print(b)

# #1.wpg to convert the given temperature in Fahrenheit to Celsius

# f=float(input("Enter the temperature in Fahrenheit:"))
# c=(f-32)*5.0/9
# print("Celsius temperature =",c)

##2.read 3 numbers and print there sum

# num1=int(input("Enter the 1st number:"))
# num2=int(input("Enter the 2nd number:"))
# num3=int(input("Enter the 3rd number:"))

# sum=num1+num2+num3
# print("Sum =",sum)

##3.wap to find the area of it's triangle from it's sides

# import math

# a=int(input("Enter side 1:"))
# b=int(input("Enter side 2:"))
# c=int(input("Enter side 3:"))

# s=float(a+b+c)/2 #here s is the semi perimeter of the triangle
# area=math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("Area of the triangle =",area)

# #4.Read a four digit binary number one digit at a time from rightmostdigit to left

# ones=int(input('Enter the ones digit:'))
# sum=int(ones*(2**0))

# tens=int(input('Enter the tens digit:'))
# sum=int(sum + tens*(2**1))

# hunds=int(input('Enter the hundreds digit:'))
# sum=int(sum + hunds*(2**2))

# th=int(input('Enter the thousands digit:'))
# sum=int(sum + th*(2**3))

# print('sum =',sum)


# # 5.find the x to the power of y

# base=int(input('Enter the base:'))
# power=int(input('Enter the power:'))
# print(base**power)

# #6.roots of a quadratic equation ax**2 + bx + c = 0 given a,b and c

# import math

# a=float(input('Enter the value of a:'))
# b=float(input('Enter the value of b:'))
# c=float(input('Enter the value of c:'))

# di=(b**2)-(4*a*c) #discriminant

# root1=(-b+math.sqrt(di))/2*a
# root2=(-b-math.sqrt(di))/2*a

# print('root are:\nr1={0},\nr2={1}'.format(root1,root2))


# #7.wap to add to real no.s using format function

# n1=int(input('Enter number 1:'))
# n2=int(input('Enter number 2:'))
# sum=n1+n2
# print("The sum of two numbers {0} and {1} is {2}".format(n1,n2,sum))































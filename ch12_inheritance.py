class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    pass            #if we use pass it will not give any error in next line

                    #after each class we should have two lines
class Cat(Mammal):
    def lick(self):
        print('lick')

d1=Dog()  #creating a object
d1.walk() #walk method

c=Cat()
c.lick()

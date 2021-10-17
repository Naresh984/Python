# #use open function to read content of a file
# f = open("sample.txt","r")#by default the mode run is r
# data = f.read()
# print(data)
# f.close()        #this is compulsary

#use readline function

# f = open("sample.txt","r")
# data = f.readline() # reads one line at a time.
# print(data)
# f.close()

# #writing/overide a file
# f = open('sample.txt','w')
# f.write('please write this to the file')
# f.close()

# #appeding
# f =open('sample.txt','a')
# f.write(' i am appending this again')
# f.close()

# with no need to close in this it is automatic
# with open('sample.txt','r') as f:
#     a=f.read()
#     print(a)

# pratice
# print('1.find word twinkle in text file')

# f= open('sample.txt')
# t=f.read()
# if 'twinkle' in t:
#     print('twinkle is present')
# else:
#     print('twinkle is not present')
# f.close()

# print('2.Game scores getting saved like this in games')

# def game():
#     return 34352345

# score = game()

# with open('sample.txt','r') as f:
#     sample=f.read()
# '''if it's empty it will append then check for the condition'''
# if sample=='':
#     with open('sample.txt','w') as f:
#         f.write(str(score))
# elif int(sample)<score :
#     with open('sample.txt','w') as f:
#         f.write(str(score))


# print('3.censor the words which are in the list')
# from os import replace

# words=['donkey','monkey','mmmm']
# with open('sample.txt','r') as f:
#     sample=f.read()

# for word in words:
#     sample=sample.replace(word,"#@#$%^&!")
#     with open('sample.txt','w') as f:
#         f.write(sample)

# print('4.find case sensitve word in a log file***************VP')

# log = True
# i = 1
# with open('log9.txt','r') as f:
    
#     while log:
#         log = f.readline()
#         if 'python' in log.lower():
#             print(log)
#             print(f'Yes python is present in line number {i}',end='')
#             print(i)
#         i+=1

# print('5.write a program to make a copy of sample.txt')

# with open('sample.txt','r') as f:
#     sample =f.read()

# with open('copy.txt','w') as f:
#     copy=f.write(sample)
        

# print('6.to check two files r identical or not')

# file1='sample.txt'
# file2='copy.txt'
# with open(file1,'r') as f:
#     sample=f.read()
# with open(file2,'r') as f:
#     copy=f.read()
# if sample == copy:
#     print('They are identical')
# else:
#     print('They are not identical')

# print('6.to rename a file')

# import os 

# oldname='sample2.txt'
# newname='renamed_by_python.txt'

# with open(oldname,'r') as f:
#     old=f.read()

# with open(newname,'w') as f:
#     new=f.write(old)

# os.remove(oldname)




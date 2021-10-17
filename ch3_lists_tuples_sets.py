
#sets doesn't allow list.
#we get value error when the value which we specified does'nt exist

print(''' *****************************
            Lists                       
******************************''')
courses= ['History','Math','Physics','Compsci']
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[2])
print(courses[0:2])#is also equal to print(courses[:2])
print(courses[2:])
print(courses[::-1])#revrsing the list
print(courses[0:4:3])#prints every 3rd no.

print('appending lists')
courses.append('Art')
print(courses)

print('insert at a specific postition')
courses.insert(0,'chem')#here is inserted at position 0
print(courses)

print('adding another list in a list')
courses2=['Education','evs']
courses.insert(0, courses2)
print(courses)
print(courses[0])

courses.extend(courses2)
print(courses)

print('remove')
courses.remove('Math')
print(courses)

#or use pop
print('popping')

print(courses.pop())

popped=courses.pop()
print(popped)

courses.pop(0)
print(courses)

#sorting
print('sorting')
courses.sort()
print(courses)

num=[5,2,1,4,3]
num.sort()
print(num)#ascending order sorted

print('to sort it in descending')
num.sort(reverse=True)
print(num)
courses.sort(reverse=True)
print(courses)

print('without altering the orginal list')
sorted_new=sorted(courses)
print(sorted_new)

print(min(num))
print(max(num))
print(sum(num))

#
print(courses.index('History'))

print('History' in courses)

print('print in each line')
for item in courses:
    print(item)

print('to print with index in each line')

for index,course in enumerate(courses):
    print(index, course)

print('to make it the number we wanna start with ')

for index,course in enumerate(courses, start=101):
    print(index, course)

print('List to string - if v wanna join them')
courses_str=' , '.join(courses)
print(courses_str)

print('String to List')
new_list=courses_str.split(' , ')
print(new_list)

print('mutable- refer the code to understand')
#mutable--- v can modify our list
list_1=['Hisotry','Math','Physics','CompSci']
list_2=list_1
list_1[0]='Art'
print(list_1)
print(list_2)

print(''' *****************************
            Tuples                       
******************************''')
#tuples have paranthesis
print('immutable - it can\'t be modified like append or remove anything but can be used to access ')
'''
tuple_1=('Hisotry','Math','Physics','CompSci')
tuple_2=tuple_1
tuple_1[0]='sanskrit'
print(tuple_1)
print(tuple_2)'''

print('**************** Sets ******************')

cs_courses={'Hisotry','Math','Physics','CompSci'}
art_courses={'Hisotry','Math', 'art ','Desgin'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

print('******Empty Sets********')
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()






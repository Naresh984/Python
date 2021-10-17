#this is incomplete
import os  ## this lets us navigate the file system 

os.chdir('/home/kali/Doc/pr/python/') ## changing directory to where it contains the files

print(os.getcwd()) # prints the current working directory


for f in os.listdir():  # all the files in that directory
	print(f)  
	# print(os.path.splitext(f))   # making a tuple 
	file_name , file_ext = os.path.splitext(f)
	
	# print(file_name.split('_'))

	# f_title, f_course, f_num= file_name.split('_')
	# print(f_title)
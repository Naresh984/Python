import os 
from datetime import datetime
print(dir(os))  # show all the methods

print(os.getcwd())  #print current working directory

#changing directory
os.chdir('/home/kali/Doc/pr/')

print(os.getcwd())

#to see files 
print(os.listdir())

#create new folder
# os.mkdir('os-demo-2')          #creates single file
# os.makedirs('os-demo-1/nothing')  #creats multiple subdirec
# print(os.listdir())

#deleting directories
# os.rmdir('os-demo-2')
# os.removedirs('os-demo-1/nothing')

#rename a file
# os.rename('JAvascript', 'javascript')

#info about a file
statt=os.stat('javascript').st_mtime    # to read last date modified
print(datetime.fromtimestamp(statt))

#tree like structure to show all directories 
for dirpath, dirnames, filenames in os.walk('/home/kali/Doc/pr'):  #os.walk is main point
	print('currentpath:',dirpath)
	print('Dirnames:', dirnames)
	print('files:')

#Accessing env variables
print(os.environ.get('HOME'))  #captures the home direc

#Appending or adding a file
file_path=os.path.join(os.environ.get('HOME'), 'test.txt') #create the path correctly 
print(file_path)

with open(file_path, 'w') as f:
	f.write('test.txt')


#more commands
print(os.path.basename('/home/kali'))
print(os.path.dirname('/tmp/newfile.txt'))
print(os.path.split('/home/kali'))
print(os.path.exists('/home/kali/Doc/pr/dsaf'))
print(os.path.isdir('/home/kali'))
print(os.path.isfile('/home/kali/'))
print(os.path.splitext('/home/kali/Doc/pr/python/apikey.py'))  # seprates the extesion , gets the first value 
print(os.path.realpath('/home/kali'))
print(dir(os.path)) # shows the methods v can run 

print(os.listdir())
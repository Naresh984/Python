import hashlib

flag = 0

pass_hash = input('Enter md5 hash: ')


wordlist = input('FIle name: ')

# we are gonna open this file with read permission
try:
    pass_file = open(wordlist, "r")
except:
    print('no file found')
    quit()

# now we r gonna compare the hashes


for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print('Password Found')
        print('Password is ' + word)
        flag = 1
        break

if flag==0:
    print('password is not in the list')

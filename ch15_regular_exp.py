from os import confstr_names
import re

# re is case sensitive
# raw strings:-
# print('\ttab') #execute to know the difference
# print(r'\ttab')

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
bat
sat
gat
'''


pattern = re.compile(r'coreyms\.com')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

print(text_to_search[1:5])

# sinppets:-
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary          ex: (r'\bHa') here Ha is the word
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets      -- pattern3 = re.compile(r'[^bg]at')
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number                       -- pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# {3,4}   - Range of Numbers (Minimum, Maximum)


# #### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

# since d means only digits
pattern1 = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')
matchess = pattern1.finditer(text_to_search)

for match1 in matchess:
    print(match1)


# READING A EMAIL DATA.TXT FILE

# pattern2 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') #since d means only digits
# #                   [firstletter][restletter]
# with open('data.txt','r') as f:
#     content = f.read()

#     matches = pattern2.finditer(content)

#     for match2 in matches:
#         print(match2)

pattern3 = re.compile(r'[^bg]at')
matchess2 = pattern3.finditer(text_to_search)

for match3 in matchess2:
    print(match3)


print('#Groups. Match several different patterns:-')

pattern4 = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')   # | means or like v mr,ms,mrs and refer snippets
matchees4= pattern4.finditer(text_to_search)

for match4 in matchees4:
    print(match4)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
print('#emails -- practice:-')

pattern5=re.compile(r'()')
matchees5 = pattern5.finditer(text_to_search)

for match5 in matchees5:
    print(match5)
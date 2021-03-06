import re

# re is case sensitive
# raw strings:-
# print('\ttab') #execute to know the difference 
# print(r'\ttab')
#findall returns just the matches while finditer returns the groups
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
# ?       - 0 or One     --is like optional
# {3}     - Exact Number                       -- pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# {3,4}   - Range of Numbers (Minimum, Maximum)
#print(match.group(0)) -0 means full


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

# pattern5=re.compile(r'[a-zA-Z]+@[a-zA-Z]+[-.]com') or 
pattern5 = re.compile(r'[a-zA-Z0-9-.]+@[a-zA-Z-]+\.(com|edu|net)')
matchees5 = pattern5.finditer(emails)

for match5 in matchees5:
    print(match5.group(0))


print('#urls ')
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern6=re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # here v made groups using paranthesis
# matchees6=pattern6.finditer(urls) # first method
subbed_urls= pattern6.sub(r'\2\3', urls) # 2nd method
print(subbed_urls)
# for match6 in matchees6:
#     print(match6.group(3))   # using groups


#Search a word
#using flagS to igonre the capital or not

sentence='hello google how are you doing today'

pattern7=re.compile(r'HEllo', re.IGNORECASE)
matchees7=pattern7.search(sentence)

print(matchees7)


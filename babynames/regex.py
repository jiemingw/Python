__author__ = 'jiemingw'
import re
re.compile('<title>(.*)</title>')

str = 'jwei.aiesec.tju@gmail.com'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print match.group()
else:
    print 'not found'


str = 'abcdef, abe'
match = re.search(r'[^ab]+', str)
#match = re.findall(r'[^ab]+', str)
if match:
    print match.group()
else:
    print 'not found'


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print match.group()   ## 'alice-b@google.com' (the whole match)
    print match.group(1)  ## 'alice-b' (the username, group 1)
    print match.group(2)  ## 'google.com' (the host, group 2)
# A common workflow with regular expressions is that you write a pattern for the thing you are looking for,
# adding parenthesis groups to extract the parts you want.

s = "192.168.1.43,Marry,had ,a,alittle,lamb11"
text = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3},\w*", s)[0] #192.168.1.43,Marry
text1 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3},.*", s)[0]
text2 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3},(.*)", s)[0]
print text, "\n", text1, "\n", text2
#192.168.1.43,Marry
#192.168.1.43,Marry,had ,a,alittle,lamb11
#Marry,had ,a,alittle,lamb11

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print tuple[0]  ## username
    print tuple[1]

#non-greedy
str = '<b>foo</b> and <i>so on</i>'
match = re.search('<.*?>', str)
if match:
    print match.group()
else:
    print 'not found'

#replacement
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
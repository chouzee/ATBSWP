import re

# create a regex object
# () allow us to search by group
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# pass the string to search() method
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

areaCode, mainNumber = mo.groups()
print('The area code is:', areaCode)
print('The main number:', mainNumber)


# Matching multiple groups with the Pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex. search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1))


# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventure of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventure of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())


# Matching one or more with the Plus
# + means match one or more
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
# will return error 
#mo3 = batRegex.search('The Adventures of Batman')
#print(mo3.group())


# Matching specific repetitions with Braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHaHa')
print(mo1.group(0))
# will return error because of none 3
#mo2 = haRegex.search('Ha')
#print(mo2.group(0))


# Greedy/non-greedy regex
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())


# findall() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)


# Substituting strings
namesRegex = re.compile(r'Agent \w+')
m1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(m1)

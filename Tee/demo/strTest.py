import string, re

str = open('sourse/strTest.txt').read()

print filter(lambda x: x in string.letters, str)


print ','.join(['a', 'b', 'c'])

occ = {'a':5}

print occ.get('a', 2)
print occ.get('abc', 2)

print ('_'.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', str)))




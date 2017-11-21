# import linecache
#
# tString = linecache.getline('sourse/test.txt', 4)
# print tString
#
# strList = linecache.getlines('sourse/test.txt')
# print len(strList)
# for i in strList:
#     print i
#
# count = len(open('sourse/test.txt', 'rU').readlines())
# print count



import string
import collections

strList = ['1', '2', '1', 'a', 'c', 'a', 'd']

mRes = collections.Counter(strList)
print mRes
print mRes['1']

def clearnWord(x):
    return x.strip().strip(',.!')

goalFile = open('sourse/wordCount.txt', 'rw')

content = goalFile.read().replace('\n', ' ').lower().split(' ')
content = map(clearnWord, content)
print content
print collections.Counter(content)
print collections.Counter(content)['item']





























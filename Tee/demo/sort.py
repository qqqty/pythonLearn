#print "hello python"

# #str
# a = raw_input('input a : ')
# b = raw_input('input b : ')
# print a + b
# print int(a) + int(b)
# print a + str(3)

def mySort(L):
    for i in range(0, len(L)):
        min = L[i]
        pos = i
        for j in range(i+1, len(L)):
            if L[j] < min:
                min = L[j]
                pos = j

        if pos != i:
            L[i], L[pos] = L[pos], L[i]


# L = [8,2,50,3]
# mySort(L)
# print L

# #data
# a = complex(1, 2)
# print a
#
# b = 132
# print b
# print hex(b)
# print oct(b)





# for i in range(1, 10):
#     for j in range(1, i+1):
#         print "%d * %d = %2d   " % (j, i, i*j),
#
#     print "\n"

# #time
# import time
#
# a = time.time()
# print a
# print time.localtime(time.time())
#
# print time.asctime( time.localtime(time.time()) )



# ss = "yuizcv"
# print ss[::-1]
#
#
#
# L = [8,2,50,3]
# l=list()
# for i in range(len(L)):
#     l.append(min(L))
#     L.remove(min(L))
# L=l
# print(L)






# a={1:1,2:2,3:3}
# def tet(x):
#     return x*x
#
# print map(tet,a.keys())
#
# arr = [[3 for i in range(3)] for i in range(3)]
#
# print arr[2][2]
#
# ll = "{'name' : 'jim', 'sex' : 'male', 'age': 18}"
# b=eval(ll)
# print b
# print type(b)





# t = ('a', 'b', ['A', 'B'])
# print t
# t[2][1] = 3
#
# print t



# d = { 95,85,59 }
# for key in d:
#     print key
# for name in d:
#     print name

#
# import math
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y + step * math.sin(angle)
#     return nx, ny
# #print math.cos(math.pi / 6), math.sin(math.pi / 6)
# print move(0, 0, 4, math.pi / 6)
#
# x, y = move(0, 0, 4, math.pi / 6)
# print x, y
#
#
# dao = "adfoui"
# print dao[4: 0: -2]
#
#
# print dao[0:1].upper() + dao[1:].lower()






# tmpList = [2,5,6]
#
# def mySum (x, y):
#     return x + y
#
# print reduce(mySum, tmpList)
#
#
# def mySqrIsInt(x):
#     #return x % 2 == 0
#     num = math.sqrt(x)
#     return num == math.ceil(num)
#
# L = filter(mySqrIsInt, range(1,100))
#
# print L


# print filter(lambda s: s and (len(s.strip()) > 0), ['test', None, '', 'str', ' ', 'END'])
#
#
#
# def f():
#     print 'call f()...'
#
#     def g():
#         print 'call g()...'
#
#     return g
#
# x = f()
#
# print x
# x()
#
#
#
#
#
# s='abcdefg'
# s=s.strip("asbdg")
# print s



class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        print '1231231'
        if(self.score<s.score):
            return 1
        if(self.score>s.score):
            return -1
        if(self.score==s.score):
            if(self.name>s.name):
                return 1;
            if(self.name<s.name):
                return -1
            return 0


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)


#
# vote_item = VoteItem()
#             vote_item.vote_id =
#             for i in range(1, 4):
#                 if



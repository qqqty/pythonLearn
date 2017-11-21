import numpy

arr = numpy.array([[n + m * 10 for n in range(2)] for m in range(2)])
a = range(2)

# print arr
# print a
#
# print arr * a
# print numpy.dot(arr, arr)
#
#
#
# arrTem = numpy.matrix(arr)
# aTem = numpy.matrix(a)
# print arr * arr
# print arrTem * arrTem
#
#
# print arrTem * (aTem.T)


# c = numpy.matrix([[1+1j, 2+2j], [3+3j, 4+4j]])
# print c
# # print numpy.conjugate(c)
# #
# # print c.T
# # print c.H
# print numpy.abs(c)
a = range(3)
print a
print numpy.mean(a)

print numpy.std(a), numpy.var(a)
print numpy.sum(a)


aTmp = numpy.matrix(a)
print aTmp
print aTmp.mean()
print aTmp.min(), aTmp.max()
print numpy.sum(aTmp)
print numpy.prod(aTmp + 1)
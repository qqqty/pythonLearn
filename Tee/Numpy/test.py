# import numpy
#
# a = numpy.linspace(0, 3, 5)
# b = numpy.linspace(0, 3, 5, endpoint=False)
#
# print a
# print b
#
#
#
# c = numpy.logspace(0, 4, 5, base=2)
#
# print c, c.shape, type(c)
#
#
# d = numpy.array([[1,2,3],[4, 5, 6]])
# print d, d.shape, type(d)
# td = numpy.array([[complex(1, 1), 3], [complex(2, 2), 4]], dtype=complex)
# print td
#
#
# e = d.T
# print e, e.shape, type(e)
#
# #print 2 ** 4 ** (1/4)
#
#
# aa = numpy.mat([[1,2,3], [4,5,6]])
# print aa, aa.shape, type(aa)
# bb = aa.T
# print bb, bb.shape, type(bb)



#mgrid ogrid

# import numpy
# import math
#
# print numpy.mgrid[0:20:5]
# print numpy.mgrid[0:20:4j]
#
# x, y = numpy.mgrid[0:5, 0:5]
# print x
# print y
# xx, yy = numpy.ogrid[0:5, 0:5]
# print xx
# print yy
#
# print x[2][2], xx[3][0], yy[0][1]
#
#
# print numpy.zeros((2, 3))
# print numpy.ones((4, 4))
#
#
# print math.radians(60)
# print math.degrees(1.047197)
#
#
# print numpy.random.rand(3, 3)
# print numpy.random.randn(2, 2)
#
#
# print numpy.diag([5,6,8])
# print numpy.diag([5,6,8], 1)
# print numpy.diag([5,6,8], -1)
#
# zz = numpy.array([
#     [1, 5, 8],
#     [4, 7, 10],
#     [2, 3, 6]
# ])
#
# print numpy.diag(zz)
# print numpy.diag(zz, 1)
# print numpy.diag(zz, -1)








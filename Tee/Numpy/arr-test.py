# import matplotlib.pyplot as plt
# import numpy
# data = numpy.genfromtxt('s/arr-test.dat')
#
# print data
# print data.shape



# import numpy
#
# m = numpy.array([[1, 10], [2, 20], [3, 30]])
#
# numpy.savetxt('s/m.csv', m, fmt='%.2f')
#
#
# numpy.save('s/m.csv', m)
# numpy.save('s/m', m)
#
# mm = numpy.load('s/m.npy')
# print mm



#
# import numpy
#
# arr = numpy.diag([1, 2, 3, 4.0])
# arr[0][3] = 0.3
# arr[3, 2] = 3.2
#
# print arr
#
# # print arr[1:3, 2]
# # print arr[1:3, 1:3]
#
# print arr[[1,2]]
# print arr[[1,2], [1, 2]]
#
#
# cc = arr[[1,2], [1, 2]]
#
# print cc[[True, False]]


import numpy

data = numpy.genfromtxt('s/arr-test.dat')

# mask_feb = data[:, 1] == 2
#
# print numpy.mean(data[mask_feb, 3])

months = range(1, 13)
monthly_mean = [numpy.mean(data[data[:, 1] == mon, 3]) for mon in months]

print monthly_mean



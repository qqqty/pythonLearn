import numpy
import pylab

x = numpy.linspace(0, 5, 10)

pic1 = pylab.subplot(211)
pic2 = pylab.subplot(212)

pylab.sca(pic2)

pylab.plot(x, x * x, 'r')

pylab.title("y = x * x")
pylab.xlabel('x')
pylab.ylabel('y')
pylab.xlim(0.0, 5.)
pylab.ylim(0., 30.0)


pylab.show()
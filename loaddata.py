import numpy

def load(fn):
	return numpy.loadtxt(fname=fn, delimiter=",")

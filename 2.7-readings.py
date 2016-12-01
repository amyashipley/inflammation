import numpy
import loaddata

def main():
    filename=sys.argv[1] # a new change!!
	data = loaddata.load(filename)
	print filename
	print data.mean(axis=1)

main()

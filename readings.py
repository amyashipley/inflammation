import numpy
import loaddata

def main():
	filename='data/inflammation-01.csv'
	data = loaddata.load(filename)
	print(filename)
	print(data.mean(axis=1))

main()

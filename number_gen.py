#!/usr/bin/env python

#Standard Lib
import sys
from random import randint

#Open Source
import sounddevice as sd
import numpy


def main(argv):
	values = [None] * 256
	dur = int(argv[0])
	fs = 48000
	myrecording = sd.rec(dur * fs, blocking=True, channels=2)
	sd.wait()
	
	for i in range(256):
		values[i] = randint(0, len(myrecording))

	values = [str(myrecording[_val][0]) for _val in range(len(values))]
	values = [binary_format(str(values[_row])) for _row in range(len(values))]
	values = [bin(int(_val))[2:] for _val in values]

	for _row in range(len(values)):
		curr = _row
		if len(str(values[_row])) < 8:
			_row = str(values[_row])
			padding = 8 - len(values[curr])
			padding = [str(randint(0,1)) for pad in range(padding)]
			for pad in padding:
				values[curr] = values[curr] + pad

		else:
			values[_row] = (str(values[_row])[:8])
		
	for _row in values:
		print(_row)



def binary_format(val):
	temp = val.split("0")
	temp = "".join(temp)
	temp = temp.split(".")
	temp = "".join(temp)
	temp = temp.split("-")
	temp = "".join(temp)
	return temp

if __name__ == '__main__':
	main(sys.argv[1:])
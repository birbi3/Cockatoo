#!/usr/bin/env python

#Standard Lib
import sys
from random import randint
import binascii

#Open Source
import sounddevice as sd
import numpy


def main(argv, argv2):
	values = [None] * int(argv2)
	dur = int(argv[0])
	fs = 48000
	myrecording = sd.rec(dur * fs, blocking=True, channels=2)
	sd.wait()
	
	for i in range(int(argv2)):
		values[i] = randint(0, len(myrecording))

	values = [str(myrecording[_val][0]) for _val in range(len(values))]
	values = [binary_format(str(values[_row])) for _row in range(len(values))]
	values = [bin(int(_val))[2:] for _val in values]

	for _row in range(len(values)):
		if len(str(values[_row])) < 7:
			padding = 7 - len(values[_row])
			padding = [str(randint(0,1)) for pad in range(padding)]
			for pad in padding:
				values[_row] = values[_row] + pad

		else:
			values[_row] = (str(values[_row])[:7])
		
	values = [chr(int(_row, 2)) for _row in values]
	key = "".join(values)
	print(key)
		



def binary_format(val):
	temp = val.split("0")
	temp = "".join(temp)
	temp = temp.split(".")
	temp = "".join(temp)
	temp = temp.split("-")
	temp = "".join(temp)
	return temp

if __name__ == '__main__':
	print(sys.argv)
	main(sys.argv[1], sys.argv[2])

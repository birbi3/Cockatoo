#!/usr/bin/env python

#Standard Lib
import sys
from random import randint

#Open Source
import sounddevice as sd
import numpy


def main(argv):
	values = [None] * 10
	dur = int(argv[0])
	fs = 48000
	myrecording = sd.rec(dur * fs, blocking=True, channels=2)
	sd.wait()
	
	for i in range(10):
		values[i] = randint(0, len(myrecording))

	values = [str(myrecording[_val][0]) for _val in range(len(values))]
	values = [binary_format(str(values[_row])) for _row in range(len(values))]
	values = [bin(int(_val))[2:] for _val in values]
	
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
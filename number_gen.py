#!/usr/bin/env python

#Standard Lib
import sys
from random import randint

#Open Source
import sounddevice as sd
import numpy


def main(argv):
	values = [None] * 5
	dur = int(argv[0])
	fs = 48000
	myrecording = sd.rec(dur * fs, blocking=True, channels=2)
	sd.wait()
	
	for i in range(5):
		values[i] = randint(0, len(myrecording))

	for _val in range(len(values)):
		values[_val] = ((str(myrecording[_val][0])))

	for _row in values:
		temp = _row.split("0")
		temp = "".join(temp)
		temp = temp.split(".")
		temp = "".join(temp)
		temp = temp.split("-")
		temp = "".join(temp)
		print("{0:b}".format(int(temp)))

if __name__ == '__main__':
	main(sys.argv[1:])
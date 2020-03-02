#!/usr/bin/env python3

#Standard Lib
import sys
from random import randint
import binascii
import operator
from bitstring import BitArray
import csv

#Open Source
import sounddevice as sd
import numpy


def main():
	values = [None] * int(250)
	fs = 48000
	myrecording = sd.rec(5 * fs, blocking=True, channels=2)
	sd.wait()

	bin_data = list()
	final_format = list()
	data = [binary_format(str(_row[0])) for _row in myrecording]
	for _row in data:
		if "e" in _row:
			_row = _row.split("e")
			_row = "".join(_row)
		if not _row:
			pass
		bin_data.append(_row)
	for _row in bin_data:
		if not _row:
			pass
		else:
			_row = bin(int(_row))[2:]
			final_format.append(_row)
	final_format = "".join(final_format)
	for _row in final_format:
		print(_row)
	

def binary_format(val):
	temp = val.split("0")
	temp = "".join(temp)
	temp = temp.split(".")
	temp = "".join(temp)
	temp = temp.split("-")
	temp = "".join(temp)
	return temp

if __name__ == "__main__":
	main()
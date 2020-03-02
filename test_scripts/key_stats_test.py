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
	
	for i in range(250):
		values[i] = randint(0, len(myrecording))

	##Split frabs the data from the recording

	values = [str(myrecording[_val][0]) for _val in values]


	#formats the audio data for binary conversion
	values = [binary_format(str(values[_row])) for _row in range(len(values))]

	#removes format
	values = [bin(int(_val))[2:] for _val in values]
	values = "".join(values)
	n = 8
	values = [values[index : index + n] for index in range(0, len(values), n)]

	for _row in range(0,len(values)):
		for i in range(1000):
			values[_row] = check_values(values[_row], myrecording)

	#converts it to ascii 	
	values = [str(int(_row, 2)) for _row in values]
	return values

def check_values(current_value, recording):
	test_val = BitArray(bin=current_value)
	if int(test_val.uint) <= 64:
		new_value = (sub_recording_parse(recording))
		return check_values(new_value, recording)
	elif 127 <= int(test_val.uint):
		new_value = (sub_recording_parse(recording))
		return check_values(new_value, recording)
	else:
		return current_value

def sub_recording_parse(recording):
	place = randint(0, len(recording))
	value = recording[place][0]
	value = str(value)
	value = binary_format(value)
	if "e" not in value:
		if value:
			value = bin(int(value))[2:]
			if len(str(value)) == 8:
				return value
			else:
				value = str(value)
				value = value[:7]
				return value
		else:
			return 0
	else:
		return 0

def binary_format(val):
	temp = val.split("0")
	temp = "".join(temp)
	temp = temp.split(".")
	temp = "".join(temp)
	temp = temp.split("-")
	temp = "".join(temp)
	return temp

if __name__ == '__main__':
	values = list()
	for i in range(10):
		print(str(i))
		try:
			key = main()
			for _row in key:
				values.append(str(_row))
		except:
			pass

	with open('key_stats_output.txt', 'w') as output:
		for i in values:
			output.write(str(i) + '\n')

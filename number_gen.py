#!/usr/bin/env python

#Standard Lib
import sys
from random import randint
import binascii
import operator
from bitstring import BitArray

#Open Source
import sounddevice as sd
import numpy


def main(argv, argv2):
	values = [None] * int(argv2)
	dur = int(argv)
	fs = 48000
	myrecording = sd.rec(dur * fs, blocking=True, channels=2)
	sd.wait()
	
	for i in range(int(argv2)):
		values[i] = randint(0, len(myrecording))

	##Split frabs the data from the recording

	values = [str(myrecording[_val][0]) for _val in values]


	#formats the audio data for binary conversion
	values = [binary_format(str(values[_row])) for _row in range(len(values))]
	print("plain ints")
	print("="*50 + "\n\n")
	print(values)

	#removes format
	values = [bin(int(_val))[2:] for _val in values]
	values = "".join(values)
	n = 8
	values = [values[index : index + n] for index in range(0, len(values), n)]
	print("binary ints")
	print("="*50 + "\n\n")
	print(values)
	print("\n\n")

	for _row in range(0,len(values)):
		for i in range(100000):
			values[_row] = check_values(values[_row], myrecording)


	print("random values")
	print(values)
	print('\n\n')

	#splits the values into 8 bits and adds padding if there isn't enough bits
	for _row in range(len(values)):
		if len(str(values[_row])) < 7:
			padding = 7 - len(values[_row])
			padding = [str(randint(0,1)) for pad in range(padding)]
			for pad in padding:
				values[_row] = values[_row] + pad

		else:
			values[_row] = (str(values[_row])[:7])
	
	#converts it to ascii 	
	values = [chr(int(_row, 2)) for _row in values]
	key = "".join(values)
	print(key) 


def check_values(current_value, recording):
	test_val = BitArray(bin=current_value)
	if int(test_val.uint) <= 32:
		new_value = (sub_recording_parse(recording))
		return new_value
	elif 127 <= int(test_val.uint):
		new_value = (sub_recording_parse(recording))
		return new_value
	else:
		return current_value

def sub_recording_parse(recording):
	place = randint(0, len(recording))
	value = recording[place][0]
	value = str(value)
	value = binary_format(value)
	value = bin(int(value))[2:]
	if len(str(value)) == 8:
		return value
	else:
		value = str(value)
		value = value[:7]
		return value



def binary_format(val):
	temp = val.split("0")
	temp = "".join(temp)
	temp = temp.split(".")
	temp = "".join(temp)
	temp = temp.split("-")
	temp = "".join(temp)
	return temp

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])


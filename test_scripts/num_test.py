#!/usr/bin/env python3

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
	
	audio_data = [bin(int(myrecording[_val][0])) for _val in range(len(myrecording))]
	for _row in range(len(audio_data)):
		if "-" in str(audio_data[_row]):
			audio_data[_row] = str(_row).strip('-')
		if "b" in str(audio_data[_row]):
			audio_data[_row] = str(_row).strip('b')
		audio_data[_row] = bin(int(audio_data[_row]))[2:]
	audio_data = "".join(audio_data)
	audio_data = [audio_data[i:i+8] for i in range(0, len(audio_data), 8)]

	for i in range(int(argv2)):
		values[i] = randint(0, len(audio_data))

	##Split frabs the data from the recording

	#values = [str(myrecording[_val][0]) for _val in values]


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
	values = [chr(int(_row, 2)) for _row in values]
	key = "".join(values)
	print(key)

def check_values(current_value, recording):
	test_val = BitArray(bin=current_value)
	if int(test_val.uint) <= 32:
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


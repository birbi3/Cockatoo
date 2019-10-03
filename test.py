#!/usr/bin/env python

#Standard Lib
import sys
from random import randint
import binascii
import time
#Open Source
import sounddevice as sd
import numpy


def main(argv, argv2):
	values = [None] * int(argv2)
	dur = int(argv[0])
	fs = 48000
	myrecording = sd.rec(dur * fs, channels=1, blocking=True)
	sd.wait()
	with open('test123.txt', 'a+') as test123:
		for i in range(500):
			test123.write(str(myrecording[randint(0, len(myrecording))]) + '\n')
	test123.close()
	
	outputt = ''
	#for i in range(int(argv2[0])):
	while(len(outputt) != int(argv2[0])):
		def strippy(inny):
			return inny[1:-1].replace('.','').replace('e','').replace('-','')
		def randy():
			empty = True
			while empty:
				rindex = myrecording[randint(0, len(myrecording))]
				if(rindex != ''):
					empty = False
			return int(strippy(str(rindex)))
		
		c = randy()^randy()
		if(c < int(0x110000)):
			outputt += (chr(c))
	print(bin(outputt))
	quit()











	values = [str(myrecording[randint(0, len(myrecording))][0] ^ myrecording[randint(0, len(myrecording))]) for _val in range(len(values))]
	'''
	for a 32 bit random number
	len(values) == 32

	values = []
	for _val in range(len(values)):
		values.append(str(myrecording[_val][0]))
	'''
	print(str(values))
	print('\n\n\n')



	values = [binary_format(str(values[_row])) for _row in range(len(values))]
	'''
	values = []
	for _row in range(len(values)):
		values.append(binary_format(str(values[_row])))
	'''
	print(str(values))
	values = [bin(int(_val.replace('e', '')))[2:] for _val in values]
	



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
	if(val != '0'):
		temp = val.split("0")
		temp = "".join(temp)
		temp = temp.split(".")
		temp = "".join(temp)
		temp = temp.split("-")
		temp = "".join(temp)
		return temp
	else:
		return '0'

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
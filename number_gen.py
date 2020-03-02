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
    key = [None] * int(argv2)
    fs = 48000
    myrecording = sd.rec(int(argv) * fs, blocking=True, channels=2)
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
    values = "".join(final_format)
    n = 8
    values = [values[index : index + n] for index in range(0, len(values), n)]

    key = [values[i] for i in range(len(key))]

    for _row in range(0,len(key)):
        for i in range(1000):
            key[_row] = check_values(key[_row], myrecording)

    #converts it to ascii   
    key = [chr(int(_row, 2)) for _row in key]
    key = "".join(key)
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


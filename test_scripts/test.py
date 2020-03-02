import matplotlib.pyplot as plt
import sounddevice as sd
import pandas as pd
import numpy as np
import csv


def csv_data():
    with open('test_output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['value'])
        for i in range(5):
            fs = 48000
            myrecording = sd.rec(15 * fs, blocking=True, channels=2)
            sd.wait()
            print('test: {}'.format(i))
            values = [str(myrecording[_row][0]) for _row in range(len(myrecording))]
            for _row in values:
                writer.writerow([_row])

def plot_data_general():
    freq = pd.read_csv('test_output.csv')
    freq['value'].plot(kind='hist', bins=[-1.0, -0.95, -0.90, - 0.85, - 0.80, - 0.75, - 0.70, - 0.65, - 0.60, - 0.55, - 0.50, - 0.45, - 0.40, - 0.35, - 0.30, - 0.25, - 0.20, - 0.15, - 0.10, - 0.05, 0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.0])
    #freq['value'].value_counts().plot(kind='hist')
    plt.show()

def plot_data_twenty():
    freq = pd.read_csv('test_output.csv')
    freq['value'].plot(kind='hist', bins=[-0.90, - 0.85, - 0.80, - 0.75, - 0.70, - 0.65, - 0.60, - 0.55, - 0.50, - 0.45, - 0.40, - 0.35, - 0.30, - 0.25, - 0.20, - 0.15, - 0.10, - 0.05, 0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90])
    #freq['value'].value_counts().plot(kind='hist')
    plt.show()

def plot_stuff():
    freq  =  pd.read_csv('key_stats_output.csv')
    freq['value'].plot(kind='hist', bins=[i for i in range(128)])
    plt.show()

def plot_stuff_2():
    freq  =  pd.read_csv('bin_tests/test_one.csv')
    freq['value'].plot(kind='hist', bins=[-1, 0, 1, 2])
    plt.show()

plot_stuff()
#csv_data()
#plot_data_twenty()
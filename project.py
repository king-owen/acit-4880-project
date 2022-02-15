from ast import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import *
import operator
def input_csv():
    df = pd.read_csv("parking-meters.csv", sep = ';')

    #Takes aways the number sign in front, and turns the string into a float
    df["R_MF_9A_6P"]= [float(i[1:]) for i in df['R_MF_9A_6P']]
    df["R_MF_6P_10"]= [float(i[1:]) for i in df['R_MF_6P_10']]
    df["R_SA_9A_6P"]= [float(i[1:]) for i in df['R_SA_9A_6P']]
    df["R_SA_6P_10"]= [float(i[1:]) for i in df['R_SA_6P_10']]
    df["R_SU_6P_10"]= [float(i[1:]) for i in df['R_SU_6P_10']]
    df["R_SU_9A_6P"]= [float(i[1:]) for i in df['R_SU_9A_6P']]
    print(df)
    return df

def get_under_2():
    """ Will print out the amount of parking there is per region under 2 dollars/hr"""
 
    df = input_csv()
    #Finding where they have day time parking the is under 2.00
    df = df.drop(df[df["R_MF_9A_6P"] <= 2].index)

    parking_numbers = {}

    for parking in df['Geo Local Area']:
        if parking not in parking_numbers:
            parking_numbers[parking] = 1
        else:
            parking_numbers[parking] +=1

    parking_numbers = dict( sorted(parking_numbers.items(), key=operator.itemgetter(1),reverse=True))
    keys = parking_numbers.keys()
    vals = parking_numbers.values()
    print(vals)
    val_list = list(vals)
    key_list = list(keys)
    print(val_list)
    plt.bar(range(len(parking_numbers)),val_list, tick_label = key_list)
    plt.show()

def main():
    get_under_2()

main()
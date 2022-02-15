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
    return df

def get_geo_location():
    input=input_csv()
    geo_list = []
    for parking in input['Geo Local Area']:
        if parking not in geo_list:
            geo_list.append(parking)
    return geo_list

def get_num_of_spots_under_price(time, price):
    """ Will print out the amount of parking there is per region under 2 dollars/hr"""
 
    df = input_csv()
    #Finding where they have day time parking the is under 2.00
    df = df.drop(df[df[time] <= price].index)

    parking_numbers = {}

    for parking in df['Geo Local Area']:
        if parking not in parking_numbers:
            parking_numbers[parking] = 1
        else:
            parking_numbers[parking] +=1

    parking_numbers = dict( sorted(parking_numbers.items(), key=operator.itemgetter(1),reverse=True))
    keys = parking_numbers.keys()
    vals = parking_numbers.values()
    val_list = list(vals)
    key_list = list(keys)
    plt.bar(range(len(parking_numbers)),val_list, tick_label = key_list)
    plt.show()

def get_parking_info(time):
    '''get mean, median, min, max of parking '''
    
    geo_list = get_geo_location()
    mm_list = []
    for place in geo_list:
        input = input_csv()
        input = input.drop(input[input["Geo Local Area"] == place].index)
        mm_list.append([input[time].mean(),input[time].median(), input[time].min(), input[time].max()])
    data = pd.DataFrame(mm_list, index = geo_list, columns = ['Mean', 'Median', 'Min', 'Max'])
    print(data)

def main():
    time_day = ['R_MF_9A_6P','R_SA_9A_6P','R_SU_9A_6P']
    time_night = ['R_MF_6P_10','R_SA_6P_10','R_SU_6P_10']
    time = time_night[1]
    price = 2
    get_num_of_spots_under_price(time, price)
    get_parking_info(time)

main()
from ast import operator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from math import *
import operator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler

def input_csv():
    df = pd.read_csv("cars.csv", sep = ',')
   
    keys = {}
    convert_list = ['model_name', 'transmission', 'color','engine_fuel', 'engine_has_gas', 'engine_type','body_type', 'has_warranty', 'state', 'drivetrain','is_exchangeable']
   
    df = df.drop(df[df["manufacturer_name"] != 'Subaru'].index)
    df= df.drop(['manufacturer_name','feature_0','feature_1','feature_2','feature_3','feature_4','feature_5','feature_6','feature_7','feature_8','feature_9', "location_region", "number_of_photos", "up_counter"],axis=1)
    for item in convert_list:
        return_list = convert_to_dict(df,item)
#        check(df[item], return_list[0],return_list[1])
        df[item] = return_list[0]
        keys[item] = return_list[1]
       # keys[item]= return_dict
    
    print(df)
    return df

def convert_to_dict(file_input, column_name):
    type_dict ={}
    counter = 1
    car_list=[]
    for car_type in file_input[column_name]:
        if car_type not in type_dict:
            type_dict[car_type] = counter
            car_list.append(type_dict[car_type])
            counter += 1
        else:
            car_list.append(type_dict[car_type])
    #file_input[column_name] = car_list    
    return [car_list, type_dict]

def check(df,input,key):
    counter= 0
    for counter in range(len(df)):
        value = get_key(key,input[counter])
        if df[counter] != value:
            print(df[counter],'does not equal to', value)
            print('the counter is ', counter)
        counter+=1

def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def decision_tree_accuracy():
    dataset = input_csv()
    X = dataset.iloc[:, :-1].values
    print(X)
    y = dataset.iloc[:, -1].values
    sc = StandardScaler()
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print(score)

def decision_tree_predict():
    dataset=input_csv()
    X = dataset[['model_name', 'odometer_value', 'year_produced']].values
    y = dataset[['price_usd']].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 0)
    y_train=y_train.astype('int')
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, y_train)
    car_info = [[1, 19000,2012]]
    cost=classifier.predict(car_info)
    print(cost)
    
def main():
    decision_tree_predict()

main()
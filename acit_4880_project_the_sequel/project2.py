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
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
import warnings
from sklearn.exceptions import DataConversionWarning
from sklearn.metrics import plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from scipy import stats
import numpy as np
from math import *

def input_csv(for_algo):
    df = pd.read_csv("cars.csv", sep = ',')
   
    keys = {}
    convert_list = ['model_name', 'transmission', 'color','engine_fuel', 'engine_has_gas', 'engine_type','body_type', 'has_warranty', 'state', 'drivetrain','is_exchangeable']
   
    df = df.drop(df[df["manufacturer_name"] != 'Subaru'].index)
    df= df.drop(['manufacturer_name','feature_0','feature_1','feature_2','feature_3','feature_4','feature_5','feature_6','feature_7','feature_8','feature_9', "location_region", "number_of_photos", "up_counter"],axis=1)
    if for_algo == False:
        return df
    for item in convert_list:
        return_list = convert_to_dict(df,item)
        df[item] = return_list[0]
        keys[item] = return_list[1]
    price_list = []
    for item in df['price_usd']:
        if item > 10000:
            price_list.append(1)
        else:
            price_list.append(0)
    df['under_10k'] = price_list
    return df

def get_car_types():
    input = input_csv(False)
    car_list = []
    for car_type in input['model_name']:
        if car_type not in car_list:
            car_list.append(car_type)
    return car_list

def get_car_info():
    '''get mean, median, min, max of parking '''
    car_list = get_car_types()
    mm_list = []
    for car in car_list:
        input = input_csv(False)
        input = input.drop(input[input["model_name"] != car].index)
        mm_list.append([input['price_usd'].mean().round(2),input['price_usd'].median(), input['price_usd'].min().round(2), input['price_usd'].max(), input['price_usd'].std().round(2), len(input)])
    data = pd.DataFrame(mm_list, index = car_list, columns = ['Mean', 'Median', 'Min', 'Max', 'std', 'Amount in Stock'])
    print(data)

def get_inventory():
    input = input_csv(False)
    inventory={}
    for car in input['model_name']:
        if car not in inventory:
            inventory[car] = 1
        else: 
            inventory[car] +=1
    inventory_numbers = dict( sorted(inventory.items(), key=operator.itemgetter(1),reverse=True))
    keys = inventory.keys()
    vals = inventory.values()
    val_list = list(vals)
    key_list = list(keys)
    plt.bar(range(len(inventory_numbers)),val_list, tick_label = key_list)
    plt.show()

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
    dataset = input_csv(True)
    dataset = dataset[['model_name', 'odometer_value', 'year_produced','under_10k']]
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    sc = StandardScaler()
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    print("Decision Tree Accuracy", score)
    print("Precision:",precision_score(y_test, y_pred))
    print("Recall:",recall_score(y_test, y_pred))
    print("F1-Score:",f1_score(y_test, y_pred))
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)

def decision_tree_predict():
    dataset=input_csv(True)
    X = dataset[['model_name', 'odometer_value', 'year_produced']].values
    y = dataset[['price_usd']].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)
    y_train=y_train.astype('int')
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 10)
    classifier.fit(X_train, y_train)
    car_info = [[1, 132000,2012]]
    cost=classifier.predict(car_info)
    print('Decision Tree Prediction of cost with this info', car_info,'cost will be :', cost)

def knn_predict():
    dataset=input_csv(True)
    X = dataset[['model_name', 'odometer_value', 'year_produced']].values
    y = dataset[['price_usd']].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)
    y_train=y_train.astype('int')
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(X_train, y_train.ravel())
    car_info = [[1, 132000,2012]]
    cost=classifier.predict(car_info)
    print('KNN Prediction of cost with this info', car_info,'cost will be :', cost)

def knn_accuracy():
    dataset=input_csv(True)
    feature_set = ['model_name', 'odometer_value', 'year_produced']
    features = dataset[feature_set] 
    target = dataset.under_10k
    feature_train,feature_test, target_train, target_test = train_test_split(features, target, test_size=0.25, random_state=10)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(feature_train,target_train) 
    predictions = model.predict(feature_test)
    print("Accuracy:",accuracy_score(target_test, predictions))
    print("Precision:",precision_score(target_test, predictions))
    print("Recall:",recall_score(target_test, predictions))
    print("F1-Score:",f1_score(target_test, predictions))
    cm = confusion_matrix(target_test, predictions)
    print(cm)

def random_forest():
    dataset=input_csv(True)
    dataset = dataset[['model_name', 'odometer_value', 'year_produced','under_10k']]
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)
    y_train=y_train.astype('int')
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 10)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    accuracy = accuracy_score(y_test, y_pred)
    print("Random Forest Accuracy", accuracy)
    print("Precision:",precision_score(y_test, y_pred))
    print("Recall:",recall_score(y_test, y_pred))
    print("F1-Score:",f1_score(y_test, y_pred))

def random_forest_predict():
    dataset=input_csv(True)
    X = dataset[['model_name', 'odometer_value', 'year_produced']].values
    y = dataset[['price_usd']].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 10)
    y_train=y_train.astype('int')
    classifier = RandomForestClassifier(criterion = 'entropy', random_state = 10)
    classifier.fit(X_train, y_train.ravel())
    car_info = [[1, 132000,2012]]
    cost=classifier.predict(car_info)
    print('Random Forest Prediction of cost with this info', car_info,'cost will be :', cost)

def p_value():
    t_value = (8873.79 - 10000)/(6165.01/sqrt(67))
    p_value = stats.t.sf(np.abs(t_value), 67)
    print(p_value)

def main():
    #decision_tree_predict()
    #decision_tree_accuracy()
    knn_accuracy()
    knn_predict()
    #get_car_info()
    #get_inventory()
    #random_forest()
    #random_forest_predict()
    #p_value()
main()
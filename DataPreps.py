from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (classification_report, confusion_matrix)
import pandas as pd
import numpy as np
import random



def pre_process_BMI_category(bmi):
    if bmi < 15:
        return "VSUW"
    elif bmi < 16:
        return "SUW"
    elif bmi < 18.5:
        return "UW"
    elif bmi < 25:
        return "NORMAL"
    elif bmi <= 30:
        return "OW"
    else:
        return "OBESE"

def ModelGenerator():
    df_diabetes = pd.read_csv('../Diabetes-API/input/diabetes.csv')
    df_train = df_diabetes[df_diabetes.columns[:-1]]
    
    df_train['BMICat'] = df_train['BMI'].apply(pre_process_BMI_category)

    df_train = pd.concat([df_train, pd.get_dummies(df_train['BMICat'])], axis = 1)

            

    df_train = df_train.drop(columns=['BMICat'], axis = 1)
    # print(df_train.columns.values)
    # X,y
    data_in = df_train
    data_out = df_diabetes['Outcome']
    
    ourModel = GradientBoostingClassifier(learning_rate=0.001, n_estimators=1000)
    ourModel.fit(data_in, data_out)

    return ourModel

# Lets assume that data enters in JSON dict form
def PreProcess(InputDict):
    '''
    input format : {"Pregnancies" : 4 ,
                     "Glucose" : 148, 
                     "BloodPressure" : 55,
                     "SkinThickness" : 66,
                     "Insulin" : 1, 
                     "BMI" : ,
                     "Diabetes Pedigree Funtion :,
                     "Age": 
                     }

    '''

    print("\n Inserted Information : ", InputDict)

    df_train = pd.DataFrame(InputDict, index = range(1))
    df_train['BMICat'] = df_train['BMI'].apply(pre_process_BMI_category)
    #print(df_train.head())
    df_train = pd.concat([df_train, pd.get_dummies(df_train['BMICat'])], axis = 1)
    df_train = df_train.drop(columns=['BMICat'], axis = 1)

    #print(df_train.head())

    required = ["VSUW", "UW", "NORMAL", "OW", "OBESE"]
    for i in required:
        if i not in df_train.columns.values:
            df_train[i] = pd.Series(data = 0, index = df_train.index)
    
    #print ("Input Columns" , df_train.columns.values)

    toTrain = ModelGenerator()

    prediction = toTrain.predict(df_train)
    prediction_probs = toTrain.predict_proba(df_train)
    #print("\n", prediction_probs)
    #print("\n", prediction)
    return {"prediction" : prediction[0], "probablity_class_0" : prediction_probs[0][0], "probablity_class_1" : prediction_probs[0][1]}
    

#x = ModelGenerator()
#print(x.feature_importances_)

if __name__ == "__main__":
    print("\n\n***** Model Generation testing *****")
    print(ModelGenerator())
    
    print("\n\n***** Prediction Tests *****")

    print("\n Output:",PreProcess({"Pregnancies" : random.randint(0, 9) ,
                     "Glucose" : random.randint(100, 200), 
                     "BloodPressure" : random.randint(30, 70),
                     "SkinThickness" : random.randint(20, 30),
                     "Insulin" : random.choice([0, random.randint(65,85)]), 
                     "BMI" : random.randint(25, 50),
                     'DiabetesPedigreeFunction':random.random() * random.randint(1,3),
                     "Age":random.randint(25, 60) 
                     }))


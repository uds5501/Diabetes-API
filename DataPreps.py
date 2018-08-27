from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (classification_report, confusion_matrix)
import pandas as pd
import numpy as np




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
    df_train = pd.DataFrame(InputDict)
    df_train['BMICat'] = df_train['BMI'].apply(pre_process_BMI_category)
    df_train = pd.concat([df_train, pd.get_dummies(df_train['BMICat'])], axis = 1)
    df_train = df_train.drop(columns=['BMICat'], axis = 1)

    toTrain = ourModel()

    prediction = ourModel.predict(df_train)
    prediction_probs = ourModel.prediction_probs(df_train)
    return {"prediction" : prediction, "pred_0" : prediction_probs[0] * 100, "pred_1" : prediction_probs[1] * 100}
    

#x = ModelGenerator()
#print(x.feature_importances_)
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import (classification_report, confusion_matrix)
import pandas as pd
import numpy as np


def ModelGenerator(data_in, data_out):
    ourModel = GradientBoostingClassifier(learning_rate=0.001, n_estimators=1000)
    ourModel.fit(data_in, data_out)

    return ourModel

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

# Lets assume that data enters in JSON dict form
def PreProcess(InputDict):
    inputdf = 


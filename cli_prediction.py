import argparse
import numpy as np
from model.prediction import prediction
from conf.conf import logging, settings

parser = argparse.ArgumentParser(description='predicts car price')

parser.add_argument('-v','--list', nargs='+', type=int, required=True, help='Enter 3 values of features to predict')
parser.add_argument('-m', '--mod', metavar='',type=str , help='Enter model to predict with, lasso or ridge')
parser.add_argument('-g', '--grid', nargs='+', type=float, help='If needed, enter value of alpha to tune the model', required=False)

args = parser.parse_args()

def predictor(values: list, model: str, grid=None) -> float:
    values = [values]
    if model == 'lasso':
        return prediction(values, settings.MODELS.lasso, grid)

    if model == 'ridge':
        return prediction(values, settings.MODELS.ridge, grid)
    #in case of the incorrect model input
    else:
        return 'model you\'ve entered is not supported, try lasso or ridge' 
        
predict = predictor(args.list, args.mod, {'alpha' :args.grid})
logging.info(f'Prediction result {predict}')
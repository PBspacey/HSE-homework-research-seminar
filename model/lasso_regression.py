import pandas as pd
import numpy as np
from connector.connector import get_data
from conf.conf import logging
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Lasso
from util.util import save_model
from conf.conf import settings


def train_test_split_(df: pd.DataFrame) -> pd.DataFrame:
    
    #setting variables 
    X = df[['symboling', 'enginesize', 'horsepower']]
    y = df['price']
    logging.info('variables are set')

    # Split variables into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, #independent variables
                                                        y, #dependent variable
                                                        random_state = 3
                                                    )
    logging.info('data is split')
    return X_train, X_test, y_train, y_test


def training_lasso(X_train: pd.DataFrame, y_train: pd.DataFrame) -> None:
    # # Initialize the model

    reg = Lasso(alpha=2.0, max_iter = 10000)
   
    # Train the model
    reg.fit(X_train, y_train)
    logging.info('model is trained')

    save_model(settings.MODELS.lasso, reg)

    return reg



df = get_data(settings.DATA.data_set)
X_train, X_test, y_train, y_test = train_test_split_(df)
reg = training_lasso(X_train, y_train)

# reg = load_model(settings.MODELS.lasso)
# logging.info('accuracy of the model is {:.2}'.format(reg.score(X_test, y_test)))
# logging.info(f'prediction is: {reg.predict(X_test)}')


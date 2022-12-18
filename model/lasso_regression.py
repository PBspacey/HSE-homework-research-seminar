from connector.connector import get_data
from conf.conf import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso

logging.info('extrcting dataframe')
df = get_data('https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/cars.csv')
logging.info('dataframe is extracted')

def train_test_split_(df):
    
    #setting variables 
    X = df[['symboling', 'enginesize', 'horsepower']]
    y = df['price']

    # Split variables into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, #independent variables
                                                        y, #dependent variable
                                                        random_state = 3
                                                    )
    return X_train, X_test, y_train, y_test


def training_lasso(X_train, y_train):
    # Initialize the model
    reg = Lasso(alpha=2.0, max_iter = 10000)

    # Train the model
    reg.fit(X_train, y_train)

    return reg

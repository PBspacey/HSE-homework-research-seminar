from util.util import load_model
from conf.conf import logging
from sklearn.model_selection import GridSearchCV
from model.lasso_regression import X_train, y_train

#this .py file is made to predict both of the models that I made and tune hyperparameters if needed 

def grid_search(model:  str, grid_params: dict) -> None:
    model = load_model(model)
    gs = GridSearchCV(model, grid_params)
    gs.fit(X_train, y_train)
    logging.info(f'best parameters are found: {gs.best_params_}')
    return gs


def prediction(values: list, link_to_model: str, grid_params = None) -> float:
    if grid_params is None:
        reg = load_model(link_to_model)
        logging.info('model predicted')
        return reg.predict(values)
    else: 
        reg = grid_search(link_to_model, grid_params)
        logging.info('model predicted')
        return reg.predict(values)








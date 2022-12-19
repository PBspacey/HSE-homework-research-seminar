from util.util import load_model
from conf.conf import logging


#this .py file is made to predict both of the models that I made
def prediction(values, link_to_model: str) -> float:
    reg = load_model(link_to_model)
    logging.info('model predicted')
    return reg.predict(values)
    


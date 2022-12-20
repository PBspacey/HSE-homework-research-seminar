import pickle
from conf.conf import logging 

def save_model(directory: str, model) -> None:
    pickle.dump(model, open(directory, 'wb'))
    logging.info('model is saved')

def load_model(directory: str) -> None:
    logging.info('model is loaded')
    return pickle.load(open(directory, 'rb'))
    
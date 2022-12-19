from model.prediction import prediction
from conf.conf import logging
from conf.conf import settings


pred = prediction([[0, 180, 249]], settings.MODELS.las)
logging.info(f'predicted value is {pred}')




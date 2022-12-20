from model.prediction import prediction
from conf.conf import logging
from conf.conf import settings


# choose one of two models 
ridge = settings.MODELS.ridge
lasso = settings.MODELS.lasso

# set parameters for tuning if needed. It is possible to set needed alpha for the model
grid_params = {
    'alpha': [0, 0.5, 1, 1.5, 2, 2.5, 3]
}

# delete grid params from the argument, if it is needed to run models on default parameters 
pred = prediction([[0, 180, 249]],lasso , grid_params)
logging.info(f'predicted value is {pred}')




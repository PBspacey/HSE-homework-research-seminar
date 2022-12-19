from sklearn.model_selection import GridSearchCV
import numpy as np
from conf.conf import settings

def parameters_fitting(model, grid_parameters: dict) -> dict:
   
    mod = GridSearchCV(model, grid_parameters)
    return mod, mod.get_params

grid_params = {
    'alpha': np.arange(0.00, 1.0, 0.01)
}

print(parameters_fitting(settings.MODELS.lasso, grid_params))

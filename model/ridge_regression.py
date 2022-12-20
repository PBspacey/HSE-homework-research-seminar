import pandas as pd
from conf.conf import logging
from sklearn.linear_model import Ridge
from util.util import save_model
from conf.conf import settings
from model.lasso_regression import X_train, y_train


def training_ridge(X_train: pd.DataFrame, y_train: pd.DataFrame) -> None:
    # Initialize the model
    reg = Ridge(alpha=2.0, max_iter = 10000)

    # Train the model
    reg.fit(X_train, y_train)
    logging.info('model is trained')

    save_model(settings.MODELS.ridge, reg)


reg = training_ridge(X_train, y_train)

# reg = load_model(settings.MODELS.ridge)
# logging.info('accuracy of the model is {:.2}'.format(reg.score(X_test, y_test)))
# logging.info(f'prediction is: {reg.predict(X_test)}')
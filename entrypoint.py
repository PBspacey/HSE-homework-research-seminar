from model.prediction import prediction
from conf.conf import logging

pred = prediction([[0, 180, 249]], 'model/conf/lasso_regression.pkl')
logging.info(f'{pred}')




# df = get_data('https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/cars.csv')
# X_train, X_test, y_train, y_test = train_test_split_(df)
# reg = training_lasso(X_train, y_train)

# reg = load_model('model/conf/lasso_regression.pkl')
# logging.info('accuracy of the model is {:.2}'.format(reg.score(X_test, y_test)))
# logging.info(f'prediction is: {reg.predict(X_test)}')
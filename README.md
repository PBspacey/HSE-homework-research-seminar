# HSE-homework-research-seminar
This repository consists of two linear models: ridge and lasso.
Models and dataset are taken from git https://github.com/5x12/ml-cookbook/


To use models for prediction run entrypoint.py with needed parameters.
It is possible to tune hyperparameters for each model or run models without them.

To tune hyperparametes or set definite hyperparameter enter needed parameters into grid_params in entrypoint.py of set them right into function
To run model on default parameters, delete from entrypoint.params 'grid_params' argument 

It is possible to change dataset, just change the link on it in conf/settings.toml

To use prediction with cli enter to terminal needed values, model and parameters in terminal in this format:
"python3 cli_prediction.py -v *your 3 values for prediction with space between (example: 1 23 432)* -m *model name (example: lasso)* -g *it is optional, here is needed to enter alpha parameters with space between (example: 0 2 0.5)*
if help is needed enter to terminal python3 cli_prediction.py -h

example of the working prediction: python3 cli_prediction.py -v 1 132 243 -m lasso -g 1 2 3 
# HSE-homework-research-seminar
This repository consists of two linear models: ridge and lasso.
Models and dataset are taken from git https://github.com/5x12/ml-cookbook/


To use models for prediction run entrypoint.py with needed parameters.
It is possible to tune hyperparameters for each model or run models without them.

To tune hyperparametes enter needed parameters into grid_params in entrypoint.py of set them right into function
To run model on default parameters, delete from entrypoint.params 'grid_params' argument 

It is possible to change dataset, just change the link on it in conf/settings.toml

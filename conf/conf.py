import logging
import os 
from dynaconf import Dynaconf

logging.basicConfig(level=logging.INFO)

current_directory = os.path.dirname(os.path.realpath(__file__))
settings = Dynaconf(settings_file=f'{current_directory}/settings.toml')
   


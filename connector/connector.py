import pandas as pd
from conf.conf import logging 

def get_data(link: str) -> pd.DataFrame:
    """
    this function extracts data from...
    """
    logging.info('extrcting dataframe')
    df = pd.read_csv(link)
    logging.info('dataframe is extracted')
    return df 



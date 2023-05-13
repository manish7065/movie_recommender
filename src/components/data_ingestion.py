import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from dataclasses import dataclass



## Intitialize the Data Ingetion Configuration

@dataclass
class DataIngestionconfig:

    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    """
    Here, Movie dataset and credits data set will be combined and then stored to raw data. 
    
    """
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            movies=pd.read_csv(os.path.join('data_sets','tmdb_5000_movies.csv'))
            credits=pd.read_csv(os.path.join('data_sets','tmdb_5000_credits.csv'))

 
            logging.info('Combining the movies and credits data and storing as raw.csv ')
            raw_data = movies.merge(credits,on='title')
            logging.info(f'Raw Dataframe Head : \n{raw_data.head(5)}')


            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            raw_data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
         

            logging.info('Data Ingestion sucessfully completed')

            return(
                self.ingestion_config.raw_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)




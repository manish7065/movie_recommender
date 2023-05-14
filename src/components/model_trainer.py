# Basic Import
import numpy as np
import pandas as pd

from src.utils import save_object,load_object
from src.exception import CustomException
from src.logger import logging


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from dataclasses import dataclass
import sys
import os
import nltk
import pandas as pd
from nltk.stem.porter import PorterStemmer

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
     
        # self.data_transformation_config = DataTransformationConfig()

    def initate_model_training(self,transformed_data_path):
        try:
            logging.info(f"{'<<'*10} Model training starting {'>>'*10}")

            logging.info('loading the transformed data')

            print(f"{'-'*10}transformed data path : {transformed_data_path}")
            
            new_df = load_object(transformed_data_path)
            print("this is----------------------")
            # print(f"{'*'*10}{new_df}")

            logging.info("Stemming the transformed data tag column. ")
            logging.info(f"new_df tags : {new_df['tags'][0]} ")

            try:
                ps = PorterStemmer()
                def stm(text):
                    p=[]
                    for i in text.split():
                        p.append(ps.stem(i))
                    return " ".join(p)

                # Assuming new_df is a Pandas DataFrame with a 'tags' column
                new_df['tags'] = new_df['tags'].apply(lambda x: stm(x) if isinstance(x, str) else x)

            except Exception as e:
                # Handle any errors that occur
                print("An error occurred:", e)

            logging.info(f"Creating vectors")
            # Create a CountVectorizer object
            cv = CountVectorizer()

            vectors = cv.fit_transform(new_df['tags']).toarray()

            similarity = cosine_similarity(vectors)


            logging("Saving the model.")
            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=similarity
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)
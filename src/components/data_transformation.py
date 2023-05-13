
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
import ast
import pickle


from src.utils import save_object

@dataclass
class DataTransformationConfig:
    movie_list_obj_file_path=os.path.join('artifacts','movie_list.pkl')
    transformed_data_file_path = os.path.join('artifacts','transformed.csv')

class DataTransformation:
    def __init__(self):

        self.data_transformation_config=DataTransformationConfig()


    def get_data_transformation_object(self):
        try:
            def convert(obj):
                L=[]
                for i in ast.literal_eval(obj):
                    L.append(i['name'])
            return L
        
            def convert2(obj):
                L = []
                counter =0
                for i in ast.literal_eval(obj):
                    if counter != 3:
                        counter+=1
                        L.append(i['name'])
                    else:
                        break        
            return L 


        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)            
        
    def initaite_data_transformation(self,raw_data_path):
        try:
            logging.info(f"{'<<'*10} Initiating Data Transformation. {'>>'*10}")


            # Reading train and test data
            raw_df = pd.read_csv(raw_data_path)


            raw_df.dropna(inplace=True) # Removing null rows

            def convert(obj):
                L=[]
                for i in ast.literal_eval(obj):
                    L.append(i['name'])
                return L
        
        
            raw_df['keywords'] = raw_df['keywords'].apply(convert)

            logging.info(f"splitting and removing spaces")

            def convert2(obj):
                L = []
                counter =0
                for i in ast.literal_eval(obj):
                    if counter != 3:
                        counter+=1
                        L.append(i['name'])
                    else:
                        break        
                return L 
            
            raw_df['cast'] = raw_df['cast'].apply(convert2)

            logging.info(f"fetching the director name from crew column ")

            # Fetching the drector name
            def fetch_director(obj):
                L=[]
                for i in ast.literal_eval(obj):
                    if i['job']=='Director':
                        L.append(i['name'])
                        break
                return L
            
            raw_df['crew']=raw_df['crew'].apply(fetch_director)
            
            logging.info(f"splitting and removing spaces")

            raw_df['overview']=raw_df['overview'].apply(lambda x:x.split())
            raw_df['genres']=raw_df['genres'].apply(lambda x:[i.replace(" ","")for i in x])
            raw_df['keywords']=raw_df['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
            raw_df['cast']=raw_df['cast'].apply(lambda x:[i.replace(" ","")for i in x])
            raw_df['crew']=raw_df['crew'].apply(lambda x:[i.replace(" ","")for i in x])

            #making a Column named tags by combining all columns
            raw_df['tags'] = raw_df['overview'] + raw_df['genres'] + raw_df['keywords'] + raw_df['cast'] + raw_df['crew']

            logging.info(f"Creating new_df")
            #creating new df
            new_df = raw_df[['movie_id','title','tags']]

            logging.info(f'New transformed Dataframe Head : \n{new_df.head().to_string()}')


            logging.info("saving new transformed Data as transformed.csv")
            
            transformed_df_path = self.data_transformation_config.transformed_data_file_path
            os.makedirs(os.path.dirname(transformed_df_path),exist_ok=True)
            new_df.to_csv(transformed_df_path,index=False,header=True)

            # Creating the pickle file for data new_df, will be use to create the list of movie title in app

            save_object(
                file_path=self.data_transformation_config.movie_list_obj_file_path,
                obj=new_df
            )
            logging.info('movie list pickle file saved')

            return (
                self.data_transformation_config.movie_list_obj_file_path,
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise CustomException(e,sys)
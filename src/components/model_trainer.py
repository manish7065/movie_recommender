# Basic Import
import numpy as np
import pandas as pd

from src.components.data_transformation import DataTransformationConfig
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,load_object
from src.utils import evaluate_model

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from dataclasses import dataclass
import sys
import os
import nltk
from nltk.stem.porter import PorterStemmer

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')



class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
     
        self.data_transformation_config = DataTransformationConfig()

    def initate_model_training(self,train_array,test_array):
        try:
            logging.info(f"{'<<'*10} Model training starting {'>>'*10}")

            logging.info('loading the transformed data')

            transformed_data_file_path = os.path.join(self.data_transformation_config.transformed_data_file_path)
            new_df = load_object(transformed_data_file_path)

            logging.info("Stemming the transformed data tag column. ")
            ps = PorterStemmer()

            def stm(text):
                p=[]
                for i in text.split():
                    p.append(ps.stem(i))
                    
                return " ".join(p)
            
            new_df['tags']=new_df['tags'].apply(stm)

            logging.info(f"Creating vectors")

            vectors = cv.fit_transform(new_df['tags']).toarray()

            similarity = cosine_similarity(vectors)

            logging.info(f"Creating recommendation mmodel")


            def recommend(movie):
                movie_index = new_df[new_df['title'] == movie].index[0]
                distances = similarity[movie_index]
                movie_list=sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1:6]    
            #     movie_list = sorted(list(enumerate(distances)),reverse=True,key= lambda x:x[1])[1,6]
                
                for i in movie_list:
            #         print(i[0])
                    print(new_df.iloc[i[0]].title)



            vectors = cv.fit_transform(new_df['tags']).toarray()

            # Create a CountVectorizer object
            cv = CountVectorizer()

            # Fit the CountVectorizer object with text data
            text_data = ['This is the first document.', 'This is the second document.', 'And this is the third one.']
            cv.fit(text_data)

            # Get the feature names
            feature_names = cv.get_feature_names_out()

            # Print the feature names
            # print(feature_names)

            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge':Ridge(),
            'Elasticnet':ElasticNet()
        }
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')

            save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise CustomException(e,sys)
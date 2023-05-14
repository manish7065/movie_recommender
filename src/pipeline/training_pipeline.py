
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    raw_data_path = obj.initiate_data_ingestion()
    # print(f"{'**'*10} {raw_data_path}")
    data_transformation = DataTransformation()
    data_transformation.initaite_data_transformation(raw_data_path)
    model_trainer=ModelTrainer()
    raw_data = pd.read_csv(raw_data_path)
    # print(f"Printing Raw Data:- {raw_data}")
    model_trainer.initate_model_training(raw_data_path)





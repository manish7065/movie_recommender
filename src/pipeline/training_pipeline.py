
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer


if __name__=='__main__':
    obj=DataIngestion()
    raw_data_path = obj.initiate_data_ingestion()
    # print(f"{'**'*10} {raw_data_path}")
    data_transformation = DataTransformation()
    data_transformation.initaite_data_transformation(raw_data_path)
    data_transformation_config = DataTransformationConfig()
    transformed_data_path = data_transformation_config.transformed_data_file_path
    print(f"Printing Ytansformed Data Path:- {transformed_data_path}")

    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(transformed_data_path)





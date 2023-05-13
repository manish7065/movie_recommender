from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

d=DataIngestion()

raw_data_path = d.initiate_data_ingestion()

print(raw_data_path)

dt = DataTransformation()
print(dt.initaite_data_transformation(raw_data_path))
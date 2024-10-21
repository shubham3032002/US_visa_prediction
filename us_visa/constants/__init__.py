import os
from datetime import date

DATABASE_NAME="US_VISA"

COLLECTION_NAME="VISA_DATA"

MONGODB_URL_KEY="MONGODB_URL"

PIPELINE_NAME:str="usvisa"
ARTIFACT_DIR:str ="artifact"
FILE_NAME:str="usvisa.csv"
MODEL_FILE_NAME="model.pkl"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"

'''data ingestion related constat'''
DATA_INGESTION_COLLECTION_NAME: str = "VISA_DATA"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2
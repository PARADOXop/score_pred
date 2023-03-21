import os
import sys

from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class data_ingestion_config():
    train_data_path: str= os.path.join('artifact', 'train.csv')
    test_data_path: str= os.path.join('artifact', 'test.csv')
    raw_data_path: str= os.path.join('artifact', 'data.csv')

class data_ingestion():
    def __init__(self):
        self.ingestion_config = data_ingestion_config()

    def initiate_data_ingestion(self):  # sourcery skip: use-contextlib-suppress
        logging.info('data ingestion has been initiated')
        try:
            df = pd.read_csv('notebooks\data\stud.csv')
            logging.info('read the data from the file')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('train test split')
            train_data, test_data = train_test_split(df, test_size=0.2, random_state=32)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True) 
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('ingestion of the data is completed')
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = data_ingestion()
    obj.initiate_data_ingestion()
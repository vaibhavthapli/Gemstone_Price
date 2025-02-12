# Database----> data----->train test split
# mysql--->local---->train test split

import  os
import sys
from src.gemstone.exception import CustomException
from src.gemstone.logger import logging
import pandas as pd
from src.gemstone.utils.utils import read_sql_data
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

'''

'''
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        try:
            ##reading code
            df = read_sql_data()
            #read data from local
            #df = pd.read_csv(os.path.join('notebook/data','raw.csv'))

            logging.info("Reading completed from mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info(f"Raw data is saved at {self.ingestion_config.raw_data_path}")
            #train test
            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.1,random_state=42)


            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)


            logging.info(f"Train and test data is saved at {self.ingestion_config.train_data_path} and {self.ingestion_config.test_data_path}")
            logging.info("Data ingestion completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
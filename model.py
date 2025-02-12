from src.gemstone.logger import logging
from src.gemstone.exception import CustomException
import sys
from src.gemstone.components.data_ingestion import DataIngestion


if __name__ == '__main__':
    logging.info("Data Ingestion Started")
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except CustomException as e:
        logging.info("Data Ingestion Error")
        raise CustomException(e,sys)
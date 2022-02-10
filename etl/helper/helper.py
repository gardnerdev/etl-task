import pandas as pd 
import os
import psycopg2
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError, NoSuchTableError, NoSuchColumnError


def csvReader(filename):
    """
    Read content of csv file to pandas dataframe.

    Args:
        filename (str): name of the file
    """
    with open(filename) as file:
        reader = pd.read_csv(file, sep =' ',header=0)
    return reader



def cleanData(table, pattern='www.tidio.com/?'):
    """
    Get rid of suffix pattern for processing purposes.
    Args:
        table (pandas.core.frame.DataFrame): dataset for preprocessing   
    Returns:
        dataframe
    """
    dataset = table.assign(url=table["url"].str.replace(pattern,'', regex=False))
    dataset = dataset["url"].str.split("&", expand=False)
    return dataset.to_frame()
    
    
def splitList(row):
    """ 
    Split elements of the list (row) using separator
    Args:
        row (list): list of lists

    Returns:
        list: splitted list by '=' separator 
    """
    splitted = [[x.split("=") for x in group] for group in row]
    return splitted


def listToDict(row):
    """
    Filter list for getting rid of missing values,
    change nested list elements to dictionaries

    Args:
        row (list): list of lists

    Returns:
        [type]: [description]
    """
    filtered_rows = filter(lambda c: len(c) > 1, row)
    el_dict = {el[0]:el[1] for el in filtered_rows }
    return el_dict


def transform(row):
    """[summary]

    Args:
        row (list): [description]

    Returns:
        [type]: [description]
    """
    empty_list=[]
    empty_list = [listToDict(x) for x in splitList(row)]
    return empty_list



def load_data(data,tablename,dbname,user,host,password,port):
    """
    Load data from dataframe to db

    Args:
        data (dataframe): Dataframe to load
        tablename (str): Name of the table
        dbname (str): Db name
        user (str): User name
        host (str): Db host
        password (str): Db password
        port (str): Port number

    Returns:
        [bool]: Returns True if operation of loading data is successfull.
    """
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    try:
        engine.connect()
        logging.info("Connection to database established successfully..")
        logging.info("Loading data..")
        data.to_sql(tablename, engine, if_exists='append',index=False)
        logging.info("Data has been sucessfully loaded to database...")
        return True
    except NoSuchTableError as err:
        logging.error(f"{err.__cause__}")
        return False
    except NoSuchColumnError as err:
        logging.error(f"{err.__cause__}")
        return False
    except SQLAlchemyError as err:
        logging.error(f"{err.__cause__}")
        return False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
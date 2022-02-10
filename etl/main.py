#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import logging
import os
from helper.helper import csvReader,cleanData,load_data,transform
import configparser
import sys

os.environ['dir'] = os.path.dirname(os.path.realpath(__file__))
config = configparser.ConfigParser()
config.read('./conf/config.ini')
config=config['DEFAULT']
datapath = config['data_path']
tablename = config['tablename']
dbname = config['dbname']
user = config['user']
host = config['host']
password = config['password']
port = config['port']

logging.basicConfig(level=logging.INFO)



URL_parts = ["a_bucket","a_g_adgroupid","a_type", "a_source","a_v","a_g_campaignid","a_g_keyword","a_g_adgroupid","a_g_creative",
            "utm_campaign", "utm_content","utm_medium","utm_source","utm_term"]
sort_URL_parts = sorted(URL_parts)

mapping = {"a_bucket":"ad_bucket","a_type": "ad_type","a_source":"ad_source", "a_v":"schema_version","a_g_campaignid":"ad_campaign_id",
        "a_g_keyword":"ad_keyword","a_g_adgroupid":"ad_group_id","a_g_creative":"ad_creative"}



if  __name__ == "__main__":
    logging.info("Reading dataset...")
    raw_data = csvReader(datapath)
    logging.info("Cleaning data...")
    dataset = cleanData(raw_data)
    logging.info("Running ETL...")    
    result = dataset.apply(lambda row: transform(row))
    data = pd.json_normalize(result['url'])
    data = data.rename(columns=mapping)
    load_data(data,tablename,dbname,user,host,password,port)
    sys.exit(1)
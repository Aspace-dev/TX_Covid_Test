from cred import my_user, my_pass, my_host, my_port, my_database
# from scraper_1 import county_case_df

import sqlalchemy
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
import warnings
import os

# Connecting to clearDB(MySQL) through Heroku
engine = create_engine(f"mysql+pymysql://{my_user}:{my_pass}@{my_host}:{my_port}")
# try:
#     engine.execute(f"CREATE DATABASE {my_database}")
# except ProgrammingError:
#     warnings.warn(
#         f"Could not create database {my_database}. Database {my_database} may already exist."
#     )
#     pass
engine.execute(f"USE {my_database}")


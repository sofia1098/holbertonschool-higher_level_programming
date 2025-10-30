"""SQL Injection"""
import sys
import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


if __name__ == __main__:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv.[3]

"""
Database Testing for the MYSQL Database held on the AFS

PYTHON <-----> MYSQL

AUTHOR: KARAN SINGH
"""

from Input import databaseCredentials as sqlcred
from Input import queryData as query

import mysql.connector
import MySQLdb as db
import sshtunnel
import paramiko
import pandas as pd
import json
import requests
import time

def my_sql_database_search_product_id(QUERY,SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                         SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                        LOCAL_HOST):
    """
    Method: Connect directly with mySQL Database and send queries automatically. Retrieve results depending
    on chosen Search Criteria
    
    Diagram:
    
            ----------------------------------------------------------------------

                                        |
            -------------+              |    +----------+               +---------
                LOCAL    |              |    |  REMOTE  |               | PRIVATE
                CLIENT   | <== SSH ========> |  SERVER  | <== local ==> | SERVER
            -------------+              |    +----------+               +---------
                                        |

            ----------------------------------------------------------------------
    Inputs: 
            QUERY
            SEARCH_CRITERIA
            SSH_USERNAME
            SSH_PASSWORD
            REMOTE_BIND_ADDRESS
            SQL_USER
            SQL_PASSWORD
            SQL_DATABASE
            ITEM_TABLE_NAME,
            CART_TABLE_NAME,
            LOCAL_HOST
    
    Output: Query Results
    
    """
    
    tunnel = sshtunnel.SSHTunnelForwarder(
        ('afsconnect1.njit.edu'),   # your ssh address needs to be a tuple 
            ssh_username=SSH_USERNAME,   
            ssh_password=SSH_PASSWORD,
            remote_bind_address=REMOTE_BIND_ADDRESS # address you want to connect to
        )

    tunnel.start()
    print("activate")       
    conn = db.connect(host=LOCAL_HOST,  # your machines address 
            port=tunnel.local_bind_port,   # this figures out that port 22 goes to your port 
            user=SQL_USER,                 # sql's username
            passwd=SQL_PASSWORD,            # sql's password
            db=SQL_DATABASE)                   # sql's database 
    print("made connection")
    
    itemTableName = ITEM_TABLE_NAME
    cartTableName = CART_TABLE_NAME
    
    if SEARCH_CRITERIA == 1:
        # Search Criteria = "fetchCartItems"
        qString ="SELECT "+cartTableName+".productID, "+cartTableName+".usItemId, "+cartTableName+".quantity, "+itemTableName+".price, "+itemTableName+".imageUrl, "+itemTableName+".title "+"FROM "+itemTableName+" INNER JOIN "+cartTableName+" ON "+itemTableName+".productId = "+cartTableName+".productID"+" WHERE "+cartTableName+".userEmail = '"+QUERY+"';"
        try:
            r =  pd.read_sql_query(qString, conn)
#             print(r)
        except:
            print("error")
        return r
    if SEARCH_CRITERIA == 2:
        # Search Criteria = Search items that contain the designated title
        qString = "select * from 684Items where title like '%"+QUERY+"%';"
        try:
            r =  pd.read_sql_query(qString, conn)
            print("completedresults")
#             print('')
#             print(r)
        except:
            print("error")
        return r
    if SEARCH_CRITERIA == 3:
        # Search Criteria = Multiple Item Search
        qString = "SELECT productId, usItemId, title, imageUrl, price FROM "+itemTableName+" WHERE title LIKE \'%"+QUERY+"%\' ORDER BY hotness DESC LIMIT 500"
        try:
            r =  pd.read_sql_query(qString, conn)
#             print(r)
        except:
            print("error")
        return r
    
    else:
        qString = "select * from 684Items where title like '%"+QUERY+"%';"
        cursor = conn.cursor()
        cursor.execute(qString)
        records = cursor.fetchall()

        print("Total number of rows in python_developers is - ", cursor.rowcount)
#         print(records)

        r =  pd.read_sql_query(qString, conn)
#         print("pandas data frame")
        conn.close();      # close sql connection
        tunnel.close();    # close the tunnel connection
        print("the terminal has closed")
    
    return "The Test Has Passed"



import mysql.connector
import MySQLdb as db
import sshtunnel
import paramiko
import pandas as pd
import json
import requests
import time
from Input import integrationEndpoints

def json_response_parser(responseJson):

    datapoints = responseJson['rows']
    title = datapoints[0]['title']
     
    return title

# Integation testing with nodeServer
# Test Cases with the Search Bar Query 
def node_server_expect_response_from_search_bar(query, API_ENDPOINT):
    query = query 
    API_ENDPOINT = API_ENDPOINT   # the endpoint
    
    a_string = json.dumps({'query': query ,'searchType':'multipleItemSearch'} )
    r = requests.post( url = API_ENDPOINT, data = a_string, headers={'Accept' : 'application/json','Content-Type': 'application/json'} )
    dataDump = r.text
    datajson = r.json()
    return datajson



def server_response(API_ENDPOINT):
    
    r = requests.get( url = API_ENDPOINT, params=None)
    
    return r

def node_server_rows_response(r):

    dataDump = r.text
    
    return dataDump
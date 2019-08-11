from warrant import Cognito
import boto3
import time
import requests
import json
import random
import string
import pandas as pd
import numpy as np
import ray
from Input import input

letters = string.ascii_lowercase[:12]
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]


def register_new_user(userPoolId, appClientId, userPoolRegion, username, password):
    """
    Test userpool in AWS database for existing accounts.
    
    Inputs: 
        - awsService = 'cognito-idp'
        - regionName = "us-east-2"
    outputs:
        - Response from AWS
    """
    u = Cognito(userPoolId, appClientId, userPoolRegion)
    u.add_base_attributes()
    data = u.register(username, password)
    return data

def authenticate_new_user(userPoolId,appClientId, username, password, region ):
    
    u = Cognito(userPoolId, appClientId, username = username,user_pool_region=region)

    authenticateUser = u.admin_authenticate(password)
    
    return authenticateUser


def confirm_user_sign_up(awsService, region, userPoolId, Username):
    
    client = boto3.client(awsService, region)
    
    response = client.admin_confirm_sign_up(
    UserPoolId=userPoolId,
    Username=Username
);
    return response


def delete_user_from_aws(awsService, region, userPoolId, Username  ):
    
    client = boto3.client(awsService,region)
    
    response = client.admin_delete_user(
    UserPoolId=userPoolId,
    Username=Username
    )
    
    return response


def get_list_of_all_users(awsService, region, userPoolId):
    client = boto3.client(awsService,region)
    response = client.list_users(
    UserPoolId=userPoolId
    )
    return response

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))


def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

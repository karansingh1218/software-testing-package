{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "from warrant import Cognito\n",
    "import boto3\n",
    "import time\n",
    "import requests\n",
    "import json\n",
    "import random\n",
    "import string\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import ray\n",
    "\n",
    "USER_POOL_ID= \"us-east-2_JPUacg84r\"\n",
    "APP_CLIENT_ID = \"qn8njsu4ka9u6ssvbd2n47lmu\"\n",
    "IDENTITY_POOL_ID = \"us-east-2:cea56946-c081-4154-a035-056e8423522f\"\n",
    "REGION =  \"us-east-2\"\n",
    "AWS_SERVICE = 'cognito-idp'\n",
    "ADMIN_USERNAME = 'admin@example.com'\n",
    "TEMPORARY_PASSWORD = 'Passw0rd!'\n",
    "domains = [ \"hotmail.com\", \"gmail.com\", \"aol.com\", \"mail.com\" , \"mail.kz\", \"yahoo.com\"]\n",
    "letters = string.ascii_lowercase[:12]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def register_new_user(userPoolId, appClientId, userPoolRegion, username, password):\n",
    "    \"\"\"\n",
    "    Test userpool in AWS database for existing accounts.\n",
    "    \n",
    "    Inputs: \n",
    "        - awsService = 'cognito-idp'\n",
    "        - regionName = \"us-east-2\"\n",
    "    outputs:\n",
    "        - Response from AWS\n",
    "    \"\"\"\n",
    "    u = Cognito(userPoolId, appClientId, userPoolRegion)\n",
    "    u.add_base_attributes()\n",
    "    data = u.register(username, password)\n",
    "    return data\n",
    "             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def authenticate_new_user(userPoolId,appClientId, username, password, region ):\n",
    "    \n",
    "    u = Cognito(userPoolId, appClientId, username = 'themaaxds123@gmail.com',user_pool_region=region)\n",
    "\n",
    "    authenticateUser = u.admin_authenticate(password)\n",
    "    \n",
    "    return authenticateUser"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def confirm_user_sign_up(awsService, region, userPoolId, Username):\n",
    "    \n",
    "    client = boto3.client(awsService, region)\n",
    "    \n",
    "    response = client.admin_confirm_sign_up(\n",
    "    UserPoolId=userPoolId,\n",
    "    Username=Username\n",
    ");\n",
    "    return response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def delete_user_from_aws(awsService, region, userPoolId, Username  ):\n",
    "    \n",
    "    client = boto3.client(awsService,region)\n",
    "    \n",
    "    response = client.admin_delete_user(\n",
    "    UserPoolId=userPoolId,\n",
    "    Username=Username\n",
    "    )\n",
    "    \n",
    "    return response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_list_of_all_users(awsService, region, userPoolId):\n",
    "    client = boto3.client(awsService,region)\n",
    "    response = client.list_users(\n",
    "    UserPoolId=userPoolId\n",
    "    )\n",
    "    return response"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['hfijkfacde@mail.kz', 'gdedkeebbg@aol.com', 'ldkbgbdlfg@mail.kz', 'ecjifllcei@hotmail.com', 'ffghefjlef@aol.com', 'bkhjijfdkc@mail.kz', 'jbdggkbadi@aol.com', 'bibkkkbdgd@gmail.com', 'kccllagcdd@hotmail.com', 'hcjiefchjk@yahoo.com', 'lfgkjjbgce@mail.kz', 'giidlccfjh@hotmail.com', 'ccfgahcgaj@hotmail.com', 'alhejhgbac@gmail.com', 'bjgdldkdji@aol.com', 'dielfgacal@aol.com', 'fejlfffika@mail.kz', 'fghggblejk@gmail.com', 'cehchedcgh@yahoo.com', 'djbcdhcclk@aol.com']\n"
     ]
    }
   ],
   "source": [
    "def get_random_domain(domains):\n",
    "    return random.choice(domains)\n",
    "\n",
    "def get_random_name(letters, length):\n",
    "    return ''.join(random.choice(letters) for i in range(length))\n",
    "\n",
    "def generate_random_emails(nb, length):\n",
    "    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]\n",
    "\n",
    "randomCreatedEmail = generate_random_emails(20,10)\n",
    "print(randomCreatedEmail)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# @ray.remote\n",
    "def test_sequential_user_login_test(userLoginList, password, userPoolId, \n",
    "                                    appClientId, userPoolRegion):\n",
    "    for email in userLoginList:\n",
    "        try:\n",
    "            register_new_user(userPoolId, appClientId, userPoolRegion, email, password)\n",
    "            time.sleep(5)\n",
    "        except AssertionError:\n",
    "            print(\"The test case failed\")\n",
    "    return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_sequential_random_email_deletion(awsService, region, userPoolId, userLoginList):\n",
    "    \n",
    "    for email in userLoginList:\n",
    "        try:\n",
    "            delete_user_from_aws(awsService, region, userPoolId, email )\n",
    "            time.sleep(2)\n",
    "        except AssertionError:\n",
    "            print(\"The test case failed\")\n",
    "    return True      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# # Execute f in parallel.\n",
    "# # This is dangerous to use for AWS API\n",
    "# # AWS BLOCKS ME \n",
    "# @ray.remote\n",
    "# def f():\n",
    "#     time.sleep(1)\n",
    "#     return 1\n",
    "# ray.shutdown()\n",
    "\n",
    "# ray.init()\n",
    "# results = ray.get([test_sequential_user_login_test.remote(randomCreatedEmail, TEMPORARY_PASSWORD,\n",
    "#                                                             USER_POOL_ID, \n",
    "#                                                               APP_CLIENT_ID, REGION) for i in range(2)])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "testemail = 'hfijkfacde@mail.kz'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "test = register_new_user(USER_POOL_ID, APP_CLIENT_ID, REGION, testemail, TEMPORARY_PASSWORD)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'UserConfirmed': False, 'CodeDeliveryDetails': {'Destination': 'h***@m***.kz', 'DeliveryMedium': 'EMAIL', 'AttributeName': 'email'}, 'UserSub': 'c61c290a-e6cd-4646-807c-65e453627dd2'}\n"
     ]
    }
   ],
   "source": [
    "print(test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "testFakeEmails = test_sequential_user_login_test(randomCreatedEmail, TEMPORARY_PASSWORD,\n",
    "                                                USER_POOL_ID, APP_CLIENT_ID, REGION)\n",
    "\n",
    "deleteTheRandomCreateEmails = test_sequential_random_email_deletion(AWS_SERVICE,\n",
    "                                                                   REGION,\n",
    "                                                                   USER_POOL_ID,\n",
    "                                                                   randomCreatedEmail)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(randomCreatedEmail)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

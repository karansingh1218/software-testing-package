from Input import integrationEndpoints

from TestingLibrary import Integration

import random
import string

from naughty_string_validator import *

def naughty_string_generator():
    return get_random_naughty_string()
    
def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    
    return ''.join(random.choice(letters) for i in range(stringLength))

def naughty_string_server_test(arraySize, API_ENDPOINT):
    
    naughty_string_list = []
    server_response_list = []
    
    for element in range(0, arraySize):
        
        a = naughty_string_generator()
        print(a)
        naughty_string_list.append(a)
    print("start")
    for query in naughty_string_list:
        responseFromServer = Integration.node_server_expect_response_from_search_bar(query, API_ENDPOINT)
        print(responseFromServer)
        server_response_list.append(responseFromServer)
     
    print("done")
            
    return { 'Naughty String List ': naughty_string_list,
             'Server Response List': server_response_list }
    
    
    

def random_english_words_server_query_response( arraySize, API_ENDPOINT, stringLength):
    
    noresult = {'rows': [], 'original': {'query': 'knofp', 'searchType': 'multipleItemSearch'}}
    badQuery = noresult['rows']
    
    random_string_list = []
    
    for element in range(0, arraySize):
        a = randomString(stringLength)
        random_string_list.append(a)

    passedList = []
    failedList = [] 
    failedResponseArray = []
    passedResponseArray = []
    ResponseArray = []
    
    numberOfPassedTest = 0
    failedNumberOfTest = 0
    
    for query in random_string_list:
        
        responseFromServer = Integration.node_server_expect_response_from_search_bar(query, API_ENDPOINT)
        
        if responseFromServer['rows'] == badQuery:
            print("QUERY: {}           RESPONSE: {} ".format(query, responseFromServer))
            failedList.append(query)
            failedNumberOfTest = failedNumberOfTest + 1
            
        if responseFromServer['rows'] != badQuery:
            parsedJsonResponse = Integration.json_response_parser(responseFromServer)
            print(parsedJsonResponse)
            passedList.append(query)
            numberOfPassedTest = numberOfPassedTest + 1
            
    return { 'Number of Passed Test': numberOfPassedTest,
             'Number of Failed Test': failedNumberOfTest,
             'Passed Queries': passedList,
             'Empty Queries': failedList}
    

def compare_node_server_query_response(queryArrayList, responseQueryList, API_ENDPOINT):
    
    passedList = []
    failedList = []
    
    for query, response in zip(queryArrayList, responseQueryList):
        
        responseFromServer = Integration.node_server_expect_response_from_search_bar(query, API_ENDPOINT)
        parsedJsonResponse = Integration.json_response_parser(responseFromServer)
        
        if query != parsedJsonResponse:
#             print("query:{} and response:{} test do not match".format(query,response))
            print("FAILED TEST")
            failedList.append(query)
        
        if query == parsedJsonResponse:
#             print("query:{} and response:{} test match".format(query,response))
            print("PASSED TEST")
            passedList.append(query)
            
    return { 'Passed Query': passedList,
             'Failed Query': failedList}

def node_server_query_response_live(queryArrayList, API_ENDPOINT):
    
    passedList = []
    failedList = [] 
    failedResponseArray = []
    passedResponseArray = []
    ResponseArray = []
    
    numberOfPassedTest = 0
    failedNumberOfTest = 0
    
    for query in queryArrayList:
        
        responseFromServer = Integration.node_server_expect_response_from_search_bar(query, API_ENDPOINT)
        parsedJsonResponse = Integration.json_response_parser(responseFromServer)
        ResponseArray.append(parsedJsonResponse)
        
        if query != parsedJsonResponse:
#             print("query:{} test do not match".format(query))
            print("FAILED TEST")
            failedList.append(query)
            failedResponseArray.append(parsedJsonResponse)
            failedNumberOfTest = failedNumberOfTest + 1
        
        if query == parsedJsonResponse:
#             print("query:{} test match".format(query))
            print("PASSED TEST")
            passedList.append(query)
            passedResponseArray.append(parsedJsonResponse)
            numberOfPassedTest = numberOfPassedTest + 1 
            
    return { 'Sent Query List:': queryArrayList,
             'Recieved Response:': ResponseArray, 
             'Number of Passed Query': passedList,
             'Passed Resonses Array ': passedResponseArray,
             'Number of Failed Query': failedList,
             'Failed Response Array': failedResponseArray,
             'Number of Passed Tests': numberOfPassedTest,
             'Number of Failed Test': failedNumberOfTest
              }


def server_response_test(API_ENDPOINT):
    
    response200 = Integration.server_response(API_ENDPOINT)
    
    expectedResponseString = '<Response [200]>'
    
    if str(response200) != expectedResponseString:
        
        print("Test has failed!")
        
    else:
        print("Test has Passed")
        return 
    
#one-call-per-thread
def server_sequential_stress_response_test(numberOfRuns, API_ENDPOINT):
    
    numberOfPassedTest = 0
    failedNumberOfTest = 0
    
    for i in range(0, numberOfRuns):
        
        loopRun = server_response_test(API_ENDPOINT)
        
        if loopRun == "Test has Passed":
            numberOfPassedTest= numberOfPassedTest + 1
        
        if loopRun != "Test has Passed":
            failedNumberOfTest= failedNumberOfTest + 1
    
    return numberOfPassedTest, failedNumberOfTest


# Mimic User going on website and then using the search bar by multiple get requests
# one-call-per-thread
def sequential_server_response_requests_test(numberofRuns, websiteServer, nodeServer):
    
    numberofPassedTests = 0
    numberofFailedTests = 0
    
    for i in range(0, numberofRuns):
        
        # Get Request to React Server
        websiteServerResponse = server_response_test(websiteServer)
        # Get request to Node Server
        nodeServerResponse = server_response_test(nodeServer)
        
        if str(websiteServerResponse) and str(nodeServerResponse) == "Test has Passed":
            numberofPassedTests = numberofPassedTests + 1 
            print("multiple server response has passed")
            
        if websiteServerResponse and nodeServerResponse != "Test has Passed": 
            numberofFailedTests = numberofFailedTests + 1
            print("multiple server response has failed")
    print("Passed Tests are [{}] & Failed Tests are [{}]".format(numberofPassedTests,numberofFailedTests))
    
    return numberofPassedTests, numberofFailedTests


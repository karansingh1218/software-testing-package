from TestingLibrary import Database
from Input import databaseCredentials as sqlcred
from Input import queryData as query


def my_sql_database_item_fetch_cart_items_test(query_items_list,SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                         SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                        LOCAL_HOST):
    SEARCH_CRITERIA = 1
    query_items_list = query_items_list
    
    while True:
    
        for item in query_items_list:

            test = Database.my_sql_database_search_product_id(item, SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                 SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                LOCAL_HOST)
        else:
            return "test has passed"


def my_sql_database_item_multiple_Item_search_test(query_items_list, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                         SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                        LOCAL_HOST):
    SEARCH_CRITERIA = 3
    query_items_list = query_items_list
    
    while True:
    
        for item in query_items_list:

            test = Database.my_sql_database_search_product_id(item, SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                 SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                LOCAL_HOST)
        else:
            return "test has passed"
        

def my_sql_database_title_item_search_test(query_items_list, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                         SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                        LOCAL_HOST):
    SEARCH_CRITERIA = 2
    query_items_list = query_items_list
    
    while True:
    
        for item in query_items_list:

            test = Database.my_sql_database_search_product_id(item, SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                 SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                LOCAL_HOST)
        else:
            return "test has passed"
        
        

        
def mysql_multiple_queries_search_test(query_items_list, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                         SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                        LOCAL_HOST):
    
    SEARCH_CRITERIA = [1,2,3,4]
    query_items_list = query_items_list
    
    for search in SEARCH_CRITERIA:
        
        for item in query_items_list:
            
                test_search_criteria_2 = Database.my_sql_database_search_product_id(item, search, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                     SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                    LOCAL_HOST)
                print("Finished Test Two")
                Database.time.sleep(5)
                test_search_criteria_3 = Database.my_sql_database_search_product_id(item, search, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                 SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                LOCAL_HOST)
                print("Finished Test Three")
                Database.time.sleep(5)
                test_search_criteria_1 = Database.my_sql_database_search_product_id(item, search, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                 SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                LOCAL_HOST)
                print("Finished Test One")
                Database.time.sleep(5)
                test_search_criteria_4 = Database.my_sql_database_search_product_id(item, search, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                 SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                LOCAL_HOST)
                print("Finished Test Four")
                Database.time.sleep(5)
    return "Test Has Passed"
        

def my_sql_expected_response_from_query_search_test(querySearchList,expecteQueryResponseArray, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                         SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                        LOCAL_HOST):
    
    querySearchList = querySearchList
    expecteQueryResponseArray = expecteQueryResponseArray
    
    queryResponseDataFrame1 = Database.pd.DataFrame(expecteQueryResponseArray[0])
    queryResponseDataFrame2 = Database.pd.DataFrame(expecteQueryResponseArray[1])
    queryResponseDataFrame3 = Database.pd.DataFrame(expecteQueryResponseArray[2])
    queryResponseDataFrame5 = Database.pd.DataFrame(expecteQueryResponseArray[4])
    
    queryReponseDescription1 = queryResponseDataFrame1.loc[0 , 'description']
    queryReponseDescription2 = queryResponseDataFrame2.loc[0 , 'description']
    queryReponseDescription3 = queryResponseDataFrame3.loc[0 , 'description']
    queryReponseDescription5 = queryResponseDataFrame5.loc[0 , 'description']
    
    test1 = Database.my_sql_database_search_product_id(querySearchList[0], query.SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                     SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                    LOCAL_HOST)
    if test1.loc[0 , 'description'] !=  queryReponseDescription1:
        return "Test Had Failed "
    
    test2 = Database.my_sql_database_search_product_id(querySearchList[1], query.SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                     SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                    LOCAL_HOST)
    if test2.loc[0 , 'description'] !=  queryReponseDescription2:
        return "Test Had Failed "
    
    test3 = Database.my_sql_database_search_product_id(querySearchList[2], query.SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                     SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                    LOCAL_HOST)
    
    if test2.loc[0 , 'description'] !=  queryReponseDescription3:
        return "Test Had Failed "
    
    test4 = Database.my_sql_database_search_product_id(querySearchList[4], query.SEARCH_CRITERIA, SSH_USERNAME, SSH_PASSWORD, REMOTE_BIND_ADDRESS, SQL_USER, 
                                     SQL_PASSWORD, SQL_DATABASE, ITEM_TABLE_NAME,CART_TABLE_NAME,
                                    LOCAL_HOST)
    
    if test4.loc[0 , 'description'] !=  queryReponseDescription5:
        return "Test Had Failed "
    

    return "All Test Have Passed"


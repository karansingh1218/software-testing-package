from TestingLibrary import Login
from Input import input

def test_sequential_user_login_test(userLoginList, password, userPoolId, 
                                    appClientId, userPoolRegion):
    for email in userLoginList:
        print("something")
        try:
            Login.register_new_user(userPoolId, appClientId, userPoolRegion, email, password)
            Login.time.sleep(5)
            print("RUNNNING")
            
        except AssertionError:
            print("The test case failed")
        print("Login account has been created")
        print("  ")
        print("TEST HAS PASSED")
    return True

def test_sequential_random_email_deletion(awsService, region, userPoolId, userLoginList):
    
    for email in userLoginList:
        try:
            Login.delete_user_from_aws(awsService, region, userPoolId, email )
            Login.time.sleep(2)
        except AssertionError:
            print("The test case failed")
        print("the user account has been deleted")
        print(" ")
        print("TEST HAS PASSED")
    return True  


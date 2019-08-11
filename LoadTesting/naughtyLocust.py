from locust import HttpLocust, TaskSet, task
import json
from naughty_string_validator import *
 
class UserBehavior(TaskSet):

    @task(1)    
    def create_post(self):
        
        def naughty_string_generator():
            return get_random_naughty_string()
        
        API_ENDPOINT = 'http://afsconnect1.njit.edu:5681'
        query = naughty_string_generator() 
        print(query)
        headers = headers={'Accept' : 'application/json','Content-Type': 'application/json'}
        aString = json.dumps({'query': query ,'searchType':'multipleItemSearch'} )
        self.client.post( url = API_ENDPOINT, 
                         data = aString, 
                         headers={'Accept' : 'application/json','Content-Type': 'application/json'} )

class WebsiteUser(HttpLocust):
    task_set = UserBehavior


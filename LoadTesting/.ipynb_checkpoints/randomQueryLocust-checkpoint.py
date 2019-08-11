from locust import HttpLocust, TaskSet, task
import json
import string
import random
 
class UserBehavior(TaskSet):
    
    

    @task(1)    
    def create_post(self):
        
        def randomString(stringLength=5):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(stringLength))
        
        API_ENDPOINT = 'http://afsconnect1.njit.edu:5681'
        
        query = randomString(3)
        print(query)
        headers = headers={'Accept' : 'application/json','Content-Type': 'application/json'}
        aString = json.dumps({'query': query ,'searchType':'multipleItemSearch'} )
        self.client.post( url = API_ENDPOINT, 
                         data = aString, 
                         headers={'Accept' : 'application/json','Content-Type': 'application/json'} )

class WebsiteUser(HttpLocust):
    task_set = UserBehavior


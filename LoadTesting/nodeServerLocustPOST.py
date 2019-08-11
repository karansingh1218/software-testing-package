from locust import HttpLocust, TaskSet, task
import json
 
class UserBehavior(TaskSet):

    @task(1)    
    def create_post(self):
    
        API_ENDPOINT = 'http://afsconnect1.njit.edu:5681'
        query = "batman" 
        headers = headers={'Accept' : 'application/json','Content-Type': 'application/json'}
        aString = json.dumps({'query': query ,'searchType':'multipleItemSearch'} )
        self.client.post( url = API_ENDPOINT, 
                         data = aString, 
                         headers={'Accept' : 'application/json','Content-Type': 'application/json'} )
        
class WebsiteUser(HttpLocust):
    task_set = UserBehavior

    
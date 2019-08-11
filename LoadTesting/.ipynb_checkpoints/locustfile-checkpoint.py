from locust import HttpLocust, TaskSet, task
import json
 
class UserBehavior(TaskSet):

    @task(2)
    def get_response_from_node_server(self):
        API_ENDPOINT = 'http://afsconnect1.njit.edu:5681'
        self.client.get( url = API_ENDPOINT, params=None)

    @task(3)
    def get_response_from_react_server(self):
        ReactEndPoint = "http://afsconnect1.njit.edu:5181/?{%22serverPort%22:%225681%22,%22dashboardPort%22:5581}"
        self.client.get(url = ReactEndPoint, params=None)

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


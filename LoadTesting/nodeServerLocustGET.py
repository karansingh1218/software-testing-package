from locust import HttpLocust, TaskSet, task
import json
 
class UserBehavior(TaskSet):

    @task(1)
    def get_response_from_node_server(self):
        API_ENDPOINT = 'http://afsconnect1.njit.edu:5681'
        self.client.get( url = API_ENDPOINT, params=None)
        
class WebsiteUser(HttpLocust):
    task_set = UserBehavior


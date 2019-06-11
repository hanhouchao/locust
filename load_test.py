from locust import HttpLocust, TaskSet, task
auth = ("alauda", "Alauda2018!@#")
# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def demo_index(self):
        with self.client.get("/v2/kubernetes/clusters/ace/applications/alauda-system/", auth=auth, catch_response=True) as response:
            print(response.status_code)
            # print(response.text)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

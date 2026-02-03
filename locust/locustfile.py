from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 2) #seconds

    @task
    def hit_heavy(self):
        self.client.get("/heavy")

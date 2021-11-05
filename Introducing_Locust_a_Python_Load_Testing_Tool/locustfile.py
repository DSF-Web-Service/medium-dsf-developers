from locust import HttpUser, task, between, tag
from locust import events

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

class MyApp(HttpUser):
    wait_time = between(3, 5)

    @tag("view_data")
    @task
    def view_data(self):
        self.client.get("/")

    @tag("view_data", "view_detail_data")
    @task(3)
    def view_data_detail(self):
        self.client.get("/{id}".format(id=1))

    @tag("create_data")
    @task(2)
    def create_data(self):
        self.client.post("/", json={"firstname": "Magnus", "lastname": "Calsen"})

    @tag("update_data")
    @task(3)
    def put_data(self):
        with self.client.put("/{id}".format(id=1), json={"firstname": "Magnus", "lastname": "Calsen"}) as response:
            try:
                if response.json().get("firstname") != "Magnus":
                     response.failure("Did not get expected value in firstname")
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure("Response did not contain expected key 'firstname'")

    @tag('delete_data')
    @task(2)
    def delete_data(self):
        self.client.delete("/{id}".format(id=1))
    
import faker
from locust import TaskSet


class BaseLoadTest(TaskSet):
    fake = faker.Faker()

    def on_start(self):
        resp = self.client.post(
            "/auth/", name="get auth token", json={"username": self.fake.email()}
        )
        resp.raise_for_status()
        token = resp.json()["access_token"]
        self.client.headers = {"token": token}

    def get_many_credit_cards(self):
        return [
            "4539578763621486",
            "4111111111111111",
            "5186001700009726",
            "5186001700008785",
            "5186001700008876",
            "5186001700009908",
            "5186001700001434",
        ]

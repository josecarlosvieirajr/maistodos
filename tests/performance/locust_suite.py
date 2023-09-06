from locust import HttpUser, LoadTestShape

from tests.performance.auth import AuthLoadTest
from tests.performance.credit_card import CreditCardLoadTest
from tests.performance.health import HealthLoadTest


class SuiteTest(HttpUser):
    tasks = [
        CreditCardLoadTest,
        AuthLoadTest,
        HealthLoadTest,
    ]


class TestShape(LoadTestShape):
    stages = [
        {"duration": 60, "users": 1000, "spawn_rate": 20},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

from locust import task

from tests.performance.utils import BaseLoadTest


class HealthLoadTest(BaseLoadTest):
    @task
    def test_health(self):
        self.client.get("/health/", name="Health")

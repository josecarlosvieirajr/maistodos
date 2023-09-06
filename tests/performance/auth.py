from locust import task

from tests.performance.utils import BaseLoadTest


class AuthLoadTest(BaseLoadTest):
    @task
    def test_create_auth_user(self):
        self.client.post(
            "/auth/", name="Create auth user", json={"username": self.fake.name()}
        )

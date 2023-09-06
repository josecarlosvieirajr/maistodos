from locust import task

from tests.performance.utils import BaseLoadTest


class CreditCardLoadTest(BaseLoadTest):
    ids = None

    @task(5)
    def test_list_user(self):
        base = self.client.get(
            "/credit-card/?skip=0&limit=100", name="List all credit card"
        )
        self.ids = [item["id"] for item in base.json()] or None

    @task(4)
    def test_create_credit_card_using_faker(self):
        if not self.ids:
            for credit_card_number in self.get_many_credit_cards():
                self.client.post(
                    "/credit-card/",
                    name="Create credit card",
                    json={
                        "number": credit_card_number,
                        "holder": self.fake.name(),
                        "exp_date": self.fake.credit_card_expire(date_format="%m/%Y"),
                        "cvv": 123,
                    },
                )

    @task(3)
    def test_get_credit_card_by_id(self):
        if self.ids:
            self.client.get(
                "/credit-card/" + str(self.fake.random_element(self.ids)),
                name="Get credit card by id",
            )

    @task(2)
    def test_update_credit_card_by_id(self):
        if self.ids:
            self.client.put(
                "/credit-card/" + str(self.fake.random_element(self.ids)),
                name="Update credit card by id",
                json={
                    "holder": self.fake.name(),
                },
            )

    @task(1)
    def test_delete_credit_card_by_id(self):
        if self.ids:
            self.client.delete(
                "/credit-card/" + str(self.fake.random_element(self.ids)),
                name="Delete credit card by id",
            )

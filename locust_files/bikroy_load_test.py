from locust import HttpUser, task, between
from locust import HttpUser, task
# from locust.user.wait_time import constant
# from locust_plugins.csvreader import CSVReader

# data = CSVReader("product.csv")


class BikroyTest(HttpUser):
    # wait_time = between(1, 5)

    # host = 'https://bikroy.com'

    @task
    def go_to_bikroy(self):
        self.client.get('/en')

    @task
    def login(self):
        payload = {
            "username": "mahabub.qups@gmail.com",
            "password": "Shozib_079"
        }
        payload = {
            "session": {
                "identifier": "mahabub.qups@gmail.com",
                "password": "Shozib_079"
            }
        }
        self.client.post("/data/sessions", json=payload)


    @task(2)
    def search(self):
        # product = next(data)
        product = ['laptop', 'bike', 'keyboard']
        for i in range(0, 3):
            print(i)
            print(product[i])
            self.client.get(f"/en/ads?query={product[i]}")

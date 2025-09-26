import requests
import json


class TestOrderAPI:
    BASE_URL = "https://simple-books-api.glitch.me/orders"
    ACCESS_TOKEN = "97983d231e1a5bf0313fc9586773899c761e3bf86e102dda874ee646cf6a5f72"

    def test_submit_delete_order(self):
        # submit order
        payload = {
            "bookId": 1,
            "customerName": "John"
        }

        headers = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        res = requests.post(self.BASE_URL, headers=headers, data=json.dumps(payload))

        assert res.status_code == 201, "wrong status code"
        order_id = res.json()["orderId"]
        print("Order Submitted with orderid = ", order_id)

        # Delete Order
        del_res = requests.delete(f"{self.BASE_URL}/{order_id}", headers=headers)
        assert del_res.status_code == 204, "Order not deleted"
        print("Order Deleted")

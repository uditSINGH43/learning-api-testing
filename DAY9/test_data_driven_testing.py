import pytest
import requests
import json
from test_data_providers import read_json_data, read_csv_data

BASE_URL = "https://simple-books-api.glitch.me/orders"
AUTH_TOKEN = 'Bearer 97983d231e1a5bf0313fc9586773899c761e3bf86e102dda874ee646cf6a5f72'


def submit_delete_order(book_id, customer_name):
    # submit order
    payload = {
        "bookId": int(book_id),
        "customerName": customer_name
    }

    headers = {
        "Authorization": AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    res = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))

    assert res.status_code == 201, "wrong status code"
    order_id = res.json()["orderId"]
    print("Order Submitted with orderid = ", order_id)

    # Delete Order
    del_res = requests.delete(f"{BASE_URL}/{order_id}", headers=headers)
    assert del_res.status_code == 204, "Order not deleted"
    print("Order Deleted")


@pytest.mark.parametrize('order_data', read_json_data("DAY9/testData/orders_json_data.json"))
def test_with_json_data(order_data):
    order_data = order_data[0]
    submit_delete_order(order_data["BookID"], order_data["CustomerName"])


@pytest.mark.parametrize('book_id,customer_name', read_csv_data("DAY9/testData/orders_csv_data.csv"))
def test_with_csv_data(book_id, customer_name):
    submit_delete_order(book_id, customer_name)

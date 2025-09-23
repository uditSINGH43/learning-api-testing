import json
import pytest


@pytest.fixture(autouse=True)
def load_json_fixture(request):
    with open("DAY6/complex.json", "r") as f:
        request.cls.json_response = json.load(f)


class TestParseComplexJSONResonse:
    def test_user_Detail_validation(self):
        # verify status
        assert self.json_response["status"] == "success", "Wrong Status code"

        # Validate user details
        user_details = self.json_response["data"]["userDetails"]
        user_details['id'] = 12345
        assert user_details["id"] == 12345, "Wrong User ID"
        assert user_details["name"] == "John Doe", "Wrong name"
        assert user_details["email"] == "john.doe@example.com", "Wrong email"

        # validate home phone number
        phone = user_details["phoneNumbers"][0]
        assert phone["type"] == "home", "Wrong Type"
        assert phone["number"] == "123-456-7890", "Wrong Number"

        # validate geo coordinates
        geo = user_details["address"]["geo"]
        assert geo["latitude"] == 39.7817, "Wrong Latitude"
        assert geo["longitude"] == -89.6501, "Wrong Longitude"

        # validate preferences
        preferences = user_details["preferences"]
        assert preferences["notifications"] is True, "Expected notification to be True"
        assert preferences["theme"] == "dark", "Wrong Theme"

    def test_recent_Order_validation(self):
        recent_orders = self.json_response["data"]["recentOrders"]

        # verify total number of orders
        assert len(recent_orders) == 2, "Expected 2 Orders"

        # validate 1st order details
        first_order = recent_orders[0]
        assert first_order["orderId"] == 101, "Wrong Order ID"
        assert first_order["totalAmount"] == 1226.49, "Total amount should be 1226.49"

        items = recent_orders[0]["items"]
        items[1]["name"] == "Mouse", "items name mismatched"

        # validate second order details
        second_order = recent_orders[1]
        assert len(second_order["items"]) == 1, "Expected 1 Item"
        second_order_items = second_order["items"][0]

        assert second_order_items["name"] == "Smartphone", "item name mismatched"
        assert second_order_items["price"] == 799.99, "Price mismatched"

    def test_Preference_and_metadata_validation(self):
        # validate preferences -> Languages
        preferences = self.json_response["data"]["userDetails"]["preferences"]
        languages = preferences["languages"]
        assert len(languages) == 3, "Expected 3 Language"
        assert languages[0] == "English"
        assert languages[1] == "Spanish"
        assert languages[2] == "French"

        # Validate metadata
        metadata = self.json_response["meta"]
        assert metadata["requestId"] == "abc123xyz"
        assert metadata["responseTimeMs"] == 250, "Resposne Time mismatched"

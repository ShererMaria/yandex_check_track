import requests
import configuration
import data


def create_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=data.ORDER_DATA)
    if response.status_code == 201:
        return response.json().get("track")
    else:
        raise Exception(f"Failed to create order. Status code: {response.status_code}")


def response():
    return None

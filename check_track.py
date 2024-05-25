# Мария Шерер, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import pytest
import configuration
import sender_stand_request
import requests


def test_get_order_by_track():
    track_number = sender_stand_request.create_order()
    assert track_number is not None, "Track number not found in the response"

    # Выполнение запроса на получение заказа по треку
    response = requests.get(f"{configuration.URL_SERVICE + configuration.FIND_ORDER}?t={track_number}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


if __name__ == "__main__":
    pytest.main()
    print(f"Failed to create order. Status code: {sender_stand_request.response.status_code}")

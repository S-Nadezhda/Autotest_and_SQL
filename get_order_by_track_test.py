# Надежда Шинкевич, 37-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# Функция для позитивной проверки
def test_create_order_save_track_number_get_order_via_track_success_response():
    response_orders = sender_stand_request.post_create_orders(data.orders_body)
    track_number = response_orders.json()["track"]
    response_track = sender_stand_request.get_receiving_an_order_via_tracking(track_number)

    # Проверяется, что код ответа равен 200
    assert response_track.status_code == 200

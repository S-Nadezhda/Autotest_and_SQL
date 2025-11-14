import configuration

import requests

import data

def post_create_orders(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=orders_body,
                         headers=data.headers)

response_orders = post_create_orders(data.orders_body)

track_number = response_orders.json()["track"]

def get_receiving_an_order_via_tracking(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVING_AN_ORDER_VIA_TRACKING_PATH,
                         params={"t": track_number},
                         headers=data.headers)

response_track = get_receiving_an_order_via_tracking(track_number)

print("Статус:", response_track.status_code)
import requests
import configuration

def post_create_courier(body):
    #Отправляет запрос на создание курьера.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH,
                         json=body)

def post_create_order(body):
    #Отправляет запрос на создание заказа.
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

def get_order_by_track(track_number):
    #Отправляет запрос на получение заказа по треку."
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track_number})
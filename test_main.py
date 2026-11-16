# Сердюков Максим Викторович, 49-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


def positive_assert(response_get_order, expected_track):
    
    # Проверяем, что код ответа равен 200
    assert response_get_order.status_code == 200, "Ошибка получения заказа"
    
    # Проверяем, что в ответе вернулся именно наш заказ
    actual_track = response_get_order.json()["order"]["track"]
    assert actual_track == expected_track, "Трек в ответе не совпадает с запрошенным"


def test_create_and_get_order_by_track():
    
    #Создание курьера

    sender_stand_request.post_create_courier(data.courier_body)

    #Запрос на создание заказа
    response_post_order = sender_stand_request.post_create_order(data.order_body)
    
    #Сохранить номер трека заказа
    track_number = response_post_order.json()["track"]

    #Запрос на получение заказа по треку
    response_get_order = sender_stand_request.get_order_by_track(track_number)

    #Проверяем результат
    positive_assert(response_get_order, track_number)
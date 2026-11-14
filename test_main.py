# Сердюков Максим Викторович, 49-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def positive_assert():
    # Шаг 0: Создаем курьера
    # Допускаем 201 (создан) или 409 (уже существует), чтобы тест не падал при повторном запуске
    response_courier = sender_stand_request.post_create_courier(data.courier_body)
    assert response_courier.status_code in [201, 409]

    # Шаг 1: Выполнить запрос на создание заказа
    response_post_order = sender_stand_request.post_create_order(data.order_body)
    # Проверяем, что код ответа равен 201
    assert response_post_order.status_code == 201

    # Шаг 2: Сохранить номер трека
    track_number = response_post_order.json().get("track")
    assert track_number is not None

    # Шаг 3: Выполнить запрос на получение заказа по треку
    response_get_order = sender_stand_request.get_order_by_track(track_number)
    # Проверяем, что код ответа равен 200
    assert response_get_order.status_code == 200


# Основной тест
def test_create_and_get_order_by_track():
    positive_assert()
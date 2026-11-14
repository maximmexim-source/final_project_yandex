# Тело запроса для создания курьера
courier_body = {
    "login": "courier_test_api",
    "password": "1234",
    "firstName": "Тест"
}

# Тело запроса для создания заказа
order_body = {
    "firstName": "Иван",
    "lastName": "Тестов",
    "address": "Москва, ул. Тверская, д. 1",
    "metroStation": "Тверская",
    "phone": "+79990001122",
    "rentTime": 5,
    "deliveryDate": "2026-11-15",
    "comment": "Тестовый заказ",
    "color": ["BLACK"]
}
"""Свежие данные для заказа без зависимости от фиксированной даты."""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


def make_order_body(metro_station="1", comment="Проверка заказа"):
    tomorrow = datetime.now(ZoneInfo("Europe/Moscow")).date() + timedelta(days=1)
    return {
        # Синтетические данные: они не относятся к пользователю или реальному клиенту.
        "firstName": "Ян",
        "lastName": "Тестов",
        "address": "Тестовый адрес 1",
        "metroStation": str(metro_station),
        "phone": "00000000000",
        "rentTime": 1,
        "deliveryDate": tomorrow.isoformat(),
        "comment": comment,
        "color": ["BLACK"],
    }

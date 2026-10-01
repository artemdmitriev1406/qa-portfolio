"""Создать заказ и получить именно этот заказ по его трек-номеру."""
import pytest
import data
import sender_stand_request


@pytest.fixture
def created_order():
    body = data.make_order_body()
    response = sender_stand_request.create_order(body)
    assert response.status_code == 201, response.text
    track = response.json()["track"]
    assert isinstance(track, int) and not isinstance(track, bool), response.text
    try:
        yield track, body
    finally:
        # Отменяется только заказ, созданный этой фикстурой.
        cleanup = sender_stand_request.cancel_order(track)
        assert cleanup.status_code == 200, cleanup.text
        assert cleanup.json().get("ok") is True, cleanup.text


def test_get_created_order_by_track_returns_200(created_order):
    track, expected = created_order
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200, response.text
    order = response.json()["order"]
    assert order["track"] == track
    for field in ("firstName", "lastName", "address", "phone", "rentTime", "color", "comment"):
        assert order[field] == expected[field], f"Поле {field}: {order[field]!r}"
    assert str(order["metroStation"]) == expected["metroStation"]
    assert order["deliveryDate"][:10] == expected["deliveryDate"]

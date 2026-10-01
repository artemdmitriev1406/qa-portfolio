"""Создать отдельные тестовые данные для мобильных проверок.

Скрипт запускается вручную, pytest его не выполняет.
Созданные данные сохраняются, чтобы ими можно было пользоваться в приложении.
"""
import json
import secrets
import string
from pathlib import Path

import requests
import configuration
import data


def api(method, path, expected_status, **kwargs):
    if not configuration.BASE_URL:
        raise ValueError("Укажи адрес своего стенда в переменной SCOOTER_BASE_URL")
    response = requests.request(
        method,
        configuration.BASE_URL + path,
        timeout=configuration.TIMEOUT,
        **kwargs,
    )
    if response.status_code != expected_status:
        raise RuntimeError(f"{method} {path}: {response.status_code}; {response.text}")
    return response.json()


def save(result):
    Path("mobile_environment.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main():
    result = {"base_url": configuration.BASE_URL, "couriers": [], "orders": []}
    stations = api("GET", "/api/v1/stations/search", 200)
    if len(stations) < 9:
        raise RuntimeError("Нужно минимум 9 доступных станций для ретеста В4")
    result["stations"] = stations[:9]
    save(result)
    for first_name in ("Ян", "Ли"):
        login = "qa" + "".join(secrets.choice(string.ascii_lowercase) for _ in range(6))
        credentials = {"login": login, "password": str(1000 + secrets.randbelow(9000))}
        api("POST", "/api/v1/courier", 201, json={**credentials, "firstName": first_name})
        courier_id = api("POST", "/api/v1/courier/login", 200, json=credentials)["id"]
        result["couriers"].append({**credentials, "firstName": first_name, "id": courier_id})
        save(result)
    for index, station in enumerate(result["stations"], start=1):
        body = data.make_order_body(station["number"], f"Мобильный тест {index}")
        track = api("POST", "/api/v1/orders", 201, json=body)["track"]
        entry = {"track": track, "station": station["name"], "metroStation": station["number"], "state": "created"}
        result["orders"].append(entry)
        save(result)
        entry["id"] = api("GET", "/api/v1/orders/track", 200, params={"t": track})["order"]["id"]
        save(result)
    # Заказ первого курьера нужен для проверки разделения вкладки «Мои».
    first_order = result["orders"][0]
    courier_id = result["couriers"][0]["id"]
    api("PUT", f"/api/v1/orders/accept/{first_order['id']}", 200, params={"courierId": courier_id})
    first_order.update(state="accepted", courierId=courier_id)
    save(result)
    # Ещё один свободный заказ сохраняет 9 разных станций на вкладке «Все».
    station = result["stations"][0]
    track = api("POST", "/api/v1/orders", 201, json=data.make_order_body(station["number"], "Мобильный тест 10"))["track"]
    extra = {"track": track, "station": station["name"], "metroStation": station["number"], "state": "created"}
    result["orders"].append(extra)
    save(result)
    extra["id"] = api("GET", "/api/v1/orders/track", 200, params={"t": track})["order"]["id"]
    result["preparation_complete"] = True
    save(result)
    print("Подготовлено: 2 курьера, 10 заказов; 1 принят курьером, 9 свободны на 9 станциях.")
    print("Данные подключения и входа: mobile_environment.json")


if __name__ == "__main__":
    main()

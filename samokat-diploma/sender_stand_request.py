"""HTTP-запросы. В тесте остаются только сценарий и проверки."""
import requests
import configuration


def _base_url():
    if not configuration.BASE_URL:
        raise ValueError("Укажи адрес своего стенда в переменной SCOOTER_BASE_URL")
    return configuration.BASE_URL


def create_order(body):
    return requests.post(
        _base_url() + configuration.CREATE_ORDER_PATH,
        json=body,
        timeout=configuration.TIMEOUT,
    )


def get_order(track):
    return requests.get(
        _base_url() + configuration.GET_ORDER_PATH,
        params={"t": track},
        timeout=configuration.TIMEOUT,
    )


def cancel_order(track):
    # В исходных регрессионных кейсах отмена передаёт track в query.
    return requests.put(
        _base_url() + configuration.CANCEL_ORDER_PATH,
        params={"track": track},
        timeout=configuration.TIMEOUT,
    )

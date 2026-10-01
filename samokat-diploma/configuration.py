"""Адрес стенда и пути к API."""
import os

BASE_URL = os.getenv("SCOOTER_BASE_URL", "").rstrip("/")
CREATE_ORDER_PATH = "/api/v1/orders"
GET_ORDER_PATH = "/api/v1/orders/track"
CANCEL_ORDER_PATH = "/api/v1/orders/cancel"
TIMEOUT = 20

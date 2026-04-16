"""
webhook_dispatcher.py — Delivers webhook payloads to customer endpoints.
"""

import time


MAX_RETRIES = 4


def deliver_webhook(url, payload):
    """
    Attempt to deliver a webhook payload to the given URL.
    Retries on failure up to MAX_RETRIES times.

    Retries with exponential backoff: 10s, 30s, 90s, 270s.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        success = _send_request(url, payload)

        if success:
            return {"status": "delivered", "attempts": attempt}

        if attempt < MAX_RETRIES:
            retry_interval = 10 * (3 ** (attempt - 1))
            time.sleep(retry_interval)

    return {"status": "failed", "attempts": MAX_RETRIES}


def _send_request(url, payload):
    """
    Simulate sending an HTTP POST request.
    In production, this would use requests.post().
    Returns True on success, False on failure.
    """
    # Simulate a ~30% failure rate for testing
    import random
    return random.random() > 0.3

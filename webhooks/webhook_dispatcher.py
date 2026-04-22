"""
webhook_dispatcher.py — Delivers webhook payloads to customer endpoints.
"""

import time


MAX_RETRIES = 4
BASE_RETRY_DELAY = 10
RETRY_BACKOFF_FACTOR = 3


def deliver_webhook(url, payload):
    """
    Attempt to deliver a webhook payload to the given URL.
    Retries on failure up to MAX_RETRIES times, waiting between
    attempts using exponential backoff:
    BASE_RETRY_DELAY * (RETRY_BACKOFF_FACTOR ** (attempt - 1)).
    With the defaults this yields 10s, 30s, 90s, 270s; because the
    final attempt is not followed by a sleep, only the first three
    delays (10s, 30s, 90s) are actually used.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        success = _send_request(url, payload)

        if success:
            return {"status": "delivered", "attempts": attempt}

        if attempt < MAX_RETRIES:
            retry_interval = BASE_RETRY_DELAY * (RETRY_BACKOFF_FACTOR ** (attempt - 1))
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

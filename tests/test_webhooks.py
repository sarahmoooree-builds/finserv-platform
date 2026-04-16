"""Tests for the webhook dispatcher."""

from unittest.mock import patch

from webhooks.webhook_dispatcher import deliver_webhook


def test_webhook_delivery_returns_status():
    result = deliver_webhook("https://example.com/hook", {"event": "test"})
    assert result["status"] in ("delivered", "failed")
    assert "attempts" in result


def test_webhook_retry_uses_exponential_backoff():
    """Verify retry intervals follow exponential backoff: 10s, 30s, 90s."""
    sleep_calls = []

    with patch("webhooks.webhook_dispatcher._send_request", return_value=False), \
         patch("webhooks.webhook_dispatcher.time.sleep", side_effect=lambda s: sleep_calls.append(s)):
        result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert result["status"] == "failed"
    assert result["attempts"] == 4
    # Retries happen after attempts 1, 2, 3 (not after the final attempt 4)
    assert sleep_calls == [10, 30, 90]


def test_webhook_no_sleep_on_first_attempt_success():
    """Verify no retry delay when the first attempt succeeds."""
    sleep_calls = []

    with patch("webhooks.webhook_dispatcher._send_request", return_value=True), \
         patch("webhooks.webhook_dispatcher.time.sleep", side_effect=lambda s: sleep_calls.append(s)):
        result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert result["status"] == "delivered"
    assert result["attempts"] == 1
    assert sleep_calls == []

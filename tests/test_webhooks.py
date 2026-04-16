"""Tests for the webhook dispatcher."""

from unittest.mock import patch

from webhooks.webhook_dispatcher import deliver_webhook


def test_webhook_delivery_returns_status():
    result = deliver_webhook("https://example.com/hook", {"event": "test"})
    assert result["status"] in ("delivered", "failed")
    assert "attempts" in result


def test_webhook_retry_uses_exponential_backoff():
    """Verify retry intervals follow exponential backoff: 10s, 30s, 90s."""
    sleep_intervals = []

    with patch("webhooks.webhook_dispatcher._send_request", return_value=False), \
         patch("webhooks.webhook_dispatcher.time.sleep", side_effect=lambda s: sleep_intervals.append(s)):
        result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert result["status"] == "failed"
    assert result["attempts"] == 4
    assert sleep_intervals == [10, 30, 90]


def test_webhook_no_sleep_on_first_attempt_success():
    """Verify no sleep is called when the first attempt succeeds."""
    with patch("webhooks.webhook_dispatcher._send_request", return_value=True), \
         patch("webhooks.webhook_dispatcher.time.sleep") as mock_sleep:
        result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert result["status"] == "delivered"
    assert result["attempts"] == 1
    mock_sleep.assert_not_called()


def test_webhook_retry_succeeds_on_third_attempt():
    """Verify correct backoff intervals when delivery succeeds on retry."""
    sleep_intervals = []
    call_count = 0

    def mock_send(url, payload):
        nonlocal call_count
        call_count += 1
        return call_count == 3  # Succeed on third attempt

    with patch("webhooks.webhook_dispatcher._send_request", side_effect=mock_send), \
         patch("webhooks.webhook_dispatcher.time.sleep", side_effect=lambda s: sleep_intervals.append(s)):
        result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert result["status"] == "delivered"
    assert result["attempts"] == 3
    assert sleep_intervals == [10, 30]

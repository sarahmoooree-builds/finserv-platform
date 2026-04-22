"""Tests for the webhook dispatcher."""

from webhooks import webhook_dispatcher
from webhooks.webhook_dispatcher import MAX_RETRIES, deliver_webhook


def test_webhook_delivery_returns_status():
    result = deliver_webhook("https://example.com/hook", {"event": "test"})
    assert result["status"] in ("delivered", "failed")
    assert "attempts" in result


def test_webhook_retry_uses_exponential_backoff_on_failure(monkeypatch):
    sleeps = []
    monkeypatch.setattr(webhook_dispatcher, "_send_request", lambda url, payload: False)
    monkeypatch.setattr(webhook_dispatcher.time, "sleep", lambda seconds: sleeps.append(seconds))

    result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert sleeps == [10, 30, 90]
    assert result["status"] == "failed"
    assert result["attempts"] == MAX_RETRIES


def test_webhook_delivery_on_first_attempt_does_not_sleep(monkeypatch):
    sleeps = []
    monkeypatch.setattr(webhook_dispatcher, "_send_request", lambda url, payload: True)
    monkeypatch.setattr(webhook_dispatcher.time, "sleep", lambda seconds: sleeps.append(seconds))

    result = deliver_webhook("https://example.com/hook", {"event": "test"})

    assert sleeps == []
    assert result == {"status": "delivered", "attempts": 1}

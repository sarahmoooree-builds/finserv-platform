"""Tests for the webhook dispatcher."""

from webhooks.webhook_dispatcher import deliver_webhook


def test_webhook_delivery_returns_status():
    result = deliver_webhook("https://example.com/hook", {"event": "test"})
    assert result["status"] in ("delivered", "failed")
    assert "attempts" in result

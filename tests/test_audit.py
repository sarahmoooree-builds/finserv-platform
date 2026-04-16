"""Tests for the audit log."""

from audit.audit_log import get_audit_page


def test_first_page():
    result = get_audit_page(page=1)
    assert len(result["entries"]) == 25
    assert result["total"] == 200


def test_offset_field_exists():
    """This test currently FAILS because offset is missing from the response."""
    result = get_audit_page(page=2)
    assert "offset" in result
    assert result["offset"] == 25

"""Tests for the login service."""

import pytest
from auth.login_service import validate_email, authenticate_user


def test_valid_email():
    assert validate_email("alice@finserv.com") is True


def test_email_with_dots():
    assert validate_email("alice.jones@finserv.com") is True


def test_email_with_plus_sign():
    """This test currently FAILS due to the regex bug."""
    assert validate_email("jane+work@example.com") is True


def test_invalid_email():
    with pytest.raises(ValueError):
        validate_email("not-an-email")

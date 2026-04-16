"""
login_service.py — Handles user authentication and login flow.
"""

import re


def validate_email(email):
    """
    Validate that the provided string is a well-formed email address.
    Returns True if valid, raises ValueError if not.
    """
    # BUG: This regex does not allow '+' characters in the local part.
    # Emails like jane+work@example.com will fail validation and cause a 500.
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not re.match(pattern, email):
        raise ValueError(f"Invalid email address: {email}")

    return True


def authenticate_user(email, password):
    """
    Authenticate a user by email and password.
    Returns a session token on success.
    """
    # Validate email format first
    validate_email(email)

    # Simulated authentication lookup
    users_db = {
        "alice@finserv.com": "hashed_pw_alice",
        "bob@finserv.com": "hashed_pw_bob",
        "jane+work@example.com": "hashed_pw_jane",
    }

    if email not in users_db:
        raise ValueError("User not found")

    # In production, compare hashed passwords
    return {"token": "session_abc123", "user": email}

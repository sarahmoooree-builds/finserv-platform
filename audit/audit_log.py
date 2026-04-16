"""
audit_log.py — Provides paginated access to the audit log.
"""


# Simulated audit log entries
AUDIT_ENTRIES = [
    {"id": i, "action": f"Action {i}", "user": f"user_{i % 5}", "timestamp": f"2025-03-{10 + (i % 20):02d}"}
    for i in range(1, 201)
]


def get_audit_page(page=1, page_size=25):
    """
    Return a page of audit log entries.

    Args:
        page: The page number (1-indexed).
        page_size: Number of entries per page.

    Returns:
        dict with 'entries', 'total', 'page', 'page_size', and 'offset'.
    """
    total = len(AUDIT_ENTRIES)
    start = (page - 1) * page_size
    end = start + page_size
    entries = AUDIT_ENTRIES[start:end]

    return {
        "entries": entries,
        "total": total,
        "page": page,
        "page_size": page_size,
        "offset": start,
    }

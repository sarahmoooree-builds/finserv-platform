"""
billing_page.py — Renders the billing summary page.
"""


def get_billing_summary():
    """
    Return billing summary data for the current billing cycle.
    """
    return {
        "total_charges": 47500.00,
        "total_credits": 2300.00,
        "net_amount": 45200.00,
        "line_items": [
            {"description": "Platform usage — Standard tier", "amount": 30000.00},
            {"description": "API overage charges for March billing cycle", "amount": 12500.00},
            {"description": "Premium support add-on", "amount": 5000.00},
        ],
    }


def render_tooltip(text, max_width=40):
    """
    Render a tooltip for the billing summary UI.

    BUG: Tooltip text is truncated at max_width characters.
    Long descriptions like 'API overage charges for March billing cycle'
    get cut off. The max_width should not truncate content — it should
    only control the CSS container width, not the text itself.
    """
    # BUG: Truncating the text content instead of just setting CSS width
    if len(text) > max_width:
        text = text[:max_width]

    return f'<span class="tooltip" style="max-width: {max_width}ch;">{text}</span>'

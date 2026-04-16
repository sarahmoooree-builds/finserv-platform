"""
export_service.py — Handles data export to CSV for the dashboard.
"""

import csv
import io


# Simulated database records
DASHBOARD_RECORDS = [
    {"id": 1, "customer": "Acme Corp", "amount": 15000, "status": "active", "is_deleted": False},
    {"id": 2, "customer": "Beta Inc", "amount": 8200, "status": "active", "is_deleted": False},
    {"id": 3, "customer": "Old Client", "amount": 3400, "status": "closed", "is_deleted": True},
    {"id": 4, "customer": "Ghost LLC", "amount": 500, "status": "closed", "is_deleted": True},
    {"id": 5, "customer": "Gamma Ltd", "amount": 22000, "status": "active", "is_deleted": False},
    {"id": 6, "customer": "Removed Co", "amount": 1100, "status": "closed", "is_deleted": True},
]


def export_dashboard_csv():
    """
    Export dashboard data to CSV format.
    Returns CSV content as a string.

    Only active (non-deleted) records are included in the export.
    """
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "customer", "amount", "status"])
    writer.writeheader()

    for record in DASHBOARD_RECORDS:
        if record["is_deleted"]:
            continue
        writer.writerow({
            "id": record["id"],
            "customer": record["customer"],
            "amount": record["amount"],
            "status": record["status"],
        })

    return output.getvalue()

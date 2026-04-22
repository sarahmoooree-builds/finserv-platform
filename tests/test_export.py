"""Tests for the export service."""

import csv
import io

from export.export_service import DASHBOARD_RECORDS, export_dashboard_csv


def test_export_excludes_deleted_records():
    csv_output = export_dashboard_csv()
    assert "Old Client" not in csv_output
    assert "Ghost LLC" not in csv_output
    assert "Removed Co" not in csv_output

    reader = csv.DictReader(io.StringIO(csv_output))
    data_rows = list(reader)
    expected_count = sum(1 for r in DASHBOARD_RECORDS if not r["is_deleted"])
    assert len(data_rows) == expected_count


def test_export_includes_active_records():
    csv_output = export_dashboard_csv()
    assert "Acme Corp" in csv_output
    assert "Gamma Ltd" in csv_output

"""Tests for the export service."""

from export.export_service import export_dashboard_csv


def test_export_excludes_deleted_records():
    csv_output = export_dashboard_csv()
    assert "Old Client" not in csv_output
    assert "Ghost LLC" not in csv_output
    assert "Removed Co" not in csv_output


def test_export_includes_active_records():
    csv_output = export_dashboard_csv()
    assert "Acme Corp" in csv_output
    assert "Gamma Ltd" in csv_output
    assert "Beta Inc" in csv_output


def test_export_row_count_excludes_deleted():
    """Verify the CSV contains only non-deleted records (plus the header)."""
    csv_output = export_dashboard_csv()
    lines = [line for line in csv_output.strip().splitlines() if line]
    # 1 header + 3 active records = 4 lines
    assert len(lines) == 4

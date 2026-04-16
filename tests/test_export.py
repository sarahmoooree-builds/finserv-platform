"""Tests for the export service."""

from export.export_service import export_dashboard_csv


def test_export_excludes_deleted_records():
    """This test currently FAILS because deleted records are included."""
    csv_output = export_dashboard_csv()
    assert "Old Client" not in csv_output
    assert "Ghost LLC" not in csv_output
    assert "Removed Co" not in csv_output


def test_export_includes_active_records():
    csv_output = export_dashboard_csv()
    assert "Acme Corp" in csv_output
    assert "Gamma Ltd" in csv_output

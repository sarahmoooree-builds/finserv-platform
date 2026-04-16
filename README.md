# FinServ Platform (Test Monorepo)

A simulated enterprise monorepo for testing Backlog Autopilot's Devin integration.

This repo contains intentional bugs that match the sample issues in Backlog Autopilot. Use it as a safe target for Devin to practice autonomous issue resolution.

## Structure

```
finserv-platform/
├── auth/               # Login and authentication
├── export/             # Dashboard CSV export
├── billing/            # Billing summary and tooltips
├── audit/              # Audit log with pagination
├── webhooks/           # Webhook delivery system
├── tests/              # Test suite (some tests intentionally fail)
└── README.md
```

## Known Bugs

| Issue | File | Bug |
|---|---|---|
| #1042 | `auth/login_service.py` | Email regex rejects `+` characters |
| #1078 | `export/export_service.py` | CSV export includes soft-deleted records |
| #1112 | `billing/billing_page.py` | Tooltip truncates text content instead of just setting CSS width |
| #1156 | `audit/audit_log.py` | Pagination response missing `offset` field |
| #1203 | `webhooks/webhook_dispatcher.py` | Retry uses hardcoded 10s interval instead of exponential backoff |

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

3 tests will fail — those correspond to the open bugs.

from datetime import datetime, timedelta, timezone


def generate_utc_dt() -> datetime:
    """Generate datetime with French timezone"""
    return datetime.now(timezone(timedelta(hours=2), name="CET"))

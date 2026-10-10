# TASK:
# 1. For EACH of the three functions say whether it is correct or not, and why.
#    Careful: not necessarily all of them are wrong.
# 2. Predict what the last lines print (or which exception is raised and where).
#    Note: in Europe/Rome, on 2026-10-25 clocks go back from 03:00 to 02:00.

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ROME = ZoneInfo("Europe/Rome")


def is_expired(created_at: datetime, ttl_hours: int) -> bool:
    return datetime.now() > created_at + timedelta(hours=ttl_hours)


def next_reminder(last: datetime) -> datetime:
    """Same local (wall clock) time, one day later. `last` is aware, in ROME."""
    return last + timedelta(days=1)


def day_bounds(day: str) -> tuple[datetime, datetime]:
    """Start and end (exclusive) of a calendar day in Rome."""
    start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=ROME)
    end = start + timedelta(hours=24)
    return start, end


start, end = day_bounds("2026-10-25")
print(end)
print(end - start)
print(end.astimezone(timezone.utc) - start.astimezone(timezone.utc))

created = datetime(2026, 10, 1, 9, 0, tzinfo=ROME)
print(is_expired(created, 2))

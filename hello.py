from datetime import datetime, UTC


def greet() -> str:
    return "Hello, World!"


def greet_name(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        return greet()
    return f"Hello, {cleaned}!"


def current_time_utc() -> str:
    return f"{greet()} It is {datetime.now(UTC).strftime('%H:%M UTC')}"

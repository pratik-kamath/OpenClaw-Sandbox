def greet() -> str:
    return "Hello, World!"


def greet_name(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        return greet()
    return f"Hello, {cleaned}!"

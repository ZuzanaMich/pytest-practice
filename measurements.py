def is_within_range(value: float, min_val: float, max_val: float) -> bool:
    """Return True if value is between min_val and max_val (inclusive)."""
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val")
    return min_val <= value <= max_val


def calculate_average(readings: list[float]) -> float:
    """Return the arithmetic mean of non-empty sensor readings."""
    if not readings:
        raise ValueError("Readings list cannot be empty")
    return sum(readings) / len(readings)

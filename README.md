# Pytest Practice – Sensor Measurement Unit Tests

Practice repository for learning the fundamentals of unit testing in Python using **pytest**.

## Overview

The project tests utility functions in `measurements.py` that validate and process numeric sensor readings:
- **`is_within_range(value, min_val, max_val)`** – checks whether a reading falls within an inclusive range `[min_val, max_val]` and raises a `ValueError` if `min_val > max_val`.
- **`calculate_average(readings)`** – computes the arithmetic mean of a list of sensor readings and raises a `ValueError` if the list is empty.

## What the Tests Cover (`test_measurements.py`)

- **Positive & negative test cases** – values inside and outside the allowed range, average of a standard list of numbers.
- **Boundary value analysis (BVA)** – values exactly on the lower/upper bounds (`0.0`, `100.0`), values just outside the bounds (`-0.1`, `100.1`), and a single-element list (`[42.5]`).
- **Exception handling (`pytest.raises`)** – verifying that `ValueError` is raised for invalid range bounds (`min_val > max_val`) and empty reading lists (`[]`).
- **Floating-point precision (`pytest.approx`)** – handling binary floating-point rounding when averaging decimals (`[0.1, 0.2]`).

## Running the Tests Locally

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows (PowerShell):
   .\.venv\Scripts\Activate.ps1
   ```

2. Install `pytest`:
   ```bash
   pip install pytest
   ```

3. Run the test suite:
   ```bash
   pytest -v
   ```

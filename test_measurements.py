import pytest
from measurements import calculate_average, is_within_range


def test_value_within_range():
    assert is_within_range(25.0, 0.0, 100.0) is True


def test_value_outside_range():
    assert is_within_range(150.0, 0.0, 100.0) is False


def test_value_on_boundaries():
    assert is_within_range(0.0, 0.0, 100.0) is True
    assert is_within_range(100.0, 0.0, 100.0) is True


def test_value_just_outside_boundaries():
    assert is_within_range(-0.1, 0.0, 100.0) is False
    assert is_within_range(100.1, 0.0, 100.0) is False


def test_invalid_range_raises_error():
    with pytest.raises(ValueError):
        is_within_range(5.0, 100.0, 0.0)


def test_calculate_average_normal_list():
    assert calculate_average([10.0, 20.0, 30.0]) == 20.0


def test_calculate_average_single_value():
    assert calculate_average([42.5]) == 42.5


def test_calculate_average_empty_list_raises_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_calculate_average_decimals():
    assert calculate_average([0.1, 0.2]) == pytest.approx(0.15)

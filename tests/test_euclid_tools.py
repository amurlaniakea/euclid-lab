import numpy as np
import pytest

from src.euclid_tools import image_summary


def test_image_summary_basic():
    result = image_summary(np.array([[1, 2], [3, 4]], dtype=float))
    assert result["n_pixels"] == 4
    assert result["minimum"] == 1
    assert result["maximum"] == 4
    assert result["mean"] == 2.5


def test_image_summary_ignores_nan():
    result = image_summary(np.array([[1.0, np.nan], [3.0, 5.0]]))
    assert result["n_pixels"] == 3
    assert result["median"] == 3


def test_image_summary_requires_2d():
    with pytest.raises(ValueError):
        image_summary(np.array([1, 2, 3]))


def test_image_summary_requires_finite_values():
    with pytest.raises(ValueError):
        image_summary(np.full((2, 2), np.nan))

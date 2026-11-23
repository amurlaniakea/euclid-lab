import numpy as np
import pytest

from src.euclid_tools import display_limits, image_summary, stretch_image


def test_image_summary_basic():
    result = image_summary(np.array([[1, 2], [3, 4]], dtype=float))
    assert result["n_pixels"] == 4
    assert result["n_invalid"] == 0
    assert result["minimum"] == 1
    assert result["maximum"] == 4
    assert result["mean"] == 2.5
    assert result["median"] == 2.5


def test_image_summary_ignores_nan_and_infinity():
    result = image_summary(np.array([[1.0, np.nan], [3.0, np.inf]]))
    assert result["n_pixels"] == 2
    assert result["n_invalid"] == 2
    assert result["median"] == 2


def test_image_summary_requires_2d():
    with pytest.raises(ValueError):
        image_summary(np.array([1, 2, 3]))


def test_image_summary_requires_finite_values():
    with pytest.raises(ValueError):
        image_summary(np.full((2, 2), np.nan))


def test_display_limits_uses_percentiles():
    data = np.arange(100, dtype=float).reshape(10, 10)
    low, high = display_limits(data, 10, 90)
    assert low == pytest.approx(9.9)
    assert high == pytest.approx(89.1)


def test_display_limits_validates_percentiles():
    with pytest.raises(ValueError):
        display_limits(np.ones((2, 2)), 99, 1)


@pytest.mark.parametrize("stretch", ["linear", "log", "asinh"])
def test_stretch_image_normalizes_finite_pixels(stretch):
    data = np.array([[0.0, 1.0], [2.0, np.nan]])
    result = stretch_image(data, stretch=stretch, vmin=0, vmax=2)
    assert result[0, 0] == pytest.approx(0)
    assert result[1, 0] == pytest.approx(1)
    assert np.isnan(result[1, 1])


def test_stretch_image_rejects_unknown_mode():
    with pytest.raises(ValueError):
        stretch_image(np.ones((2, 2)), stretch="sqrt")


def test_stretch_image_requires_positive_asinh_parameter():
    with pytest.raises(ValueError):
        stretch_image(np.arange(4).reshape(2, 2), stretch="asinh", asinh_a=0)



def test_load_fits_image_round_trip(tmp_path):
    fits = pytest.importorskip("astropy.io.fits")
    from src.euclid_tools import load_fits_image

    source = np.array([[1.0, 2.0], [np.nan, 4.0]], dtype=np.float32)
    path = tmp_path / "sample.fits"
    fits.PrimaryHDU(data=source).writeto(path)
    data, header = load_fits_image(path)
    assert data.shape == (2, 2)
    assert data[0, 1] == pytest.approx(2.0)
    assert header["NAXIS"] == 2


def test_load_fits_image_rejects_out_of_range_hdu(tmp_path):
    fits = pytest.importorskip("astropy.io.fits")
    from src.euclid_tools import load_fits_image

    path = tmp_path / "sample.fits"
    fits.PrimaryHDU(data=np.ones((2, 2))).writeto(path)
    with pytest.raises(IndexError):
        load_fits_image(path, hdu=4)

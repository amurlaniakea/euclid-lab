import numpy as np
import pytest

from src.euclid_tools import (
    display_limits, image_summary, stretch_image, detect_sources, aperture_photometry,
    read_fits_catalogues,
)


def test_image_summary_basic():
    result = image_summary(np.array([[1, 2], [3, 4]], dtype=float))
    assert result["n_pixels"] == 4 and result["mean"] == 2.5


def test_image_summary_ignores_nonfinite():
    result = image_summary(np.array([[1.0, np.nan], [3.0, np.inf]]))
    assert result["n_pixels"] == 2 and result["n_invalid"] == 2


def test_image_summary_requires_finite_2d():
    with pytest.raises(ValueError): image_summary(np.array([1, 2, 3]))
    with pytest.raises(ValueError): image_summary(np.full((2, 2), np.nan))


def test_display_limits_and_validation():
    low, high = display_limits(np.arange(100).reshape(10, 10), 10, 90)
    assert low == pytest.approx(9.9) and high == pytest.approx(89.1)
    with pytest.raises(ValueError): display_limits(np.ones((2, 2)), 99, 1)


@pytest.mark.parametrize("stretch", ["linear", "log", "asinh"])
def test_stretch_image(stretch):
    result = stretch_image(np.array([[0., 1.], [2., np.nan]]),
                           stretch=stretch, vmin=0, vmax=2)
    assert result[0, 0] == pytest.approx(0)
    assert result[1, 0] == pytest.approx(1)
    assert np.isnan(result[1, 1])


def test_stretch_image_invalid_mode():
    with pytest.raises(ValueError): stretch_image(np.ones((2, 2)), stretch="sqrt")
    with pytest.raises(ValueError):
        stretch_image(np.arange(4).reshape(2, 2), stretch="asinh", asinh_a=0)


def test_load_fits_image_round_trip_and_bad_hdu(tmp_path):
    fits = pytest.importorskip("astropy.io.fits")
    from src.euclid_tools import load_fits_image
    path = tmp_path / "sample.fits"
    fits.PrimaryHDU(data=np.array([[1., 2.], [np.nan, 4.]], dtype=np.float32)).writeto(path)
    data, header = load_fits_image(path)
    assert data.shape == (2, 2) and data[0, 1] == pytest.approx(2)
    assert header["NAXIS"] == 2
    with pytest.raises(IndexError): load_fits_image(path, hdu=4)


def test_detect_sources_finds_synthetic_peak():
    pytest.importorskip("scipy")
    rng = np.random.default_rng(7)
    data = rng.normal(100, 1, (40, 40))
    data[18:22, 18:22] += 20
    found = detect_sources(data, threshold_sigma=5, min_pixels=3)
    assert len(found) == 1
    assert found[0]["xcentroid"] == pytest.approx(19.5, abs=0.2)
    assert found[0]["ycentroid"] == pytest.approx(19.5, abs=0.2)


def test_aperture_photometry_background_subtracted():
    data = np.full((31, 31), 10.0)
    yy, xx = np.indices(data.shape)
    data[(xx - 15)**2 + (yy - 15)**2 <= 4**2] += 5
    result = aperture_photometry(data, 15, 15, radius=4)
    assert result["local_background"] == pytest.approx(10)
    assert result["net_flux"] == pytest.approx(result["aperture_pixels"] * 5)
    with pytest.raises(ValueError): aperture_photometry(data, 15, 15, radius=0)


def test_read_fits_catalogue(tmp_path):
    fits = pytest.importorskip("astropy.io.fits")
    from astropy.table import Table
    path = tmp_path / "catalogue.fits"
    table = Table({"ra": [12.5, 13.5], "dec": [-1., 2.], "flux": [100., 200.]})
    fits.HDUList([fits.PrimaryHDU(), fits.BinTableHDU(table, name="SOURCES")]).writeto(path)
    catalogues = read_fits_catalogues(path)
    assert len(catalogues) == 1
    assert catalogues[0]["name"] == "SOURCES"
    assert catalogues[0]["rows"][0]["ra"] == pytest.approx(12.5)

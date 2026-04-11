from __future__ import annotations

import numpy as np
import pytest

from units import Angle, AngleUnit, Length, LengthUnit, Time, TimeUnit


def test_time_second_and_convert() -> None:
    t = Time(value=np.array([2.0]), unit=TimeUnit.MIN)
    assert np.allclose(t.second, np.array([120.0]))
    t.convert_unit(TimeUnit.S)
    assert t.unit == TimeUnit.S
    assert np.allclose(t.value, np.array([120.0]))


def test_time_arithmetic() -> None:
    a = Time(value=np.array([1.0]), unit=TimeUnit.HR)
    b = Time(value=np.array([1800.0]), unit=TimeUnit.S)
    s = a + b
    assert s.unit == TimeUnit.S
    assert np.allclose(s.value, np.array([5400.0]))
    d = a - b
    assert np.allclose(d.value, np.array([1800.0]))
    assert np.allclose((a * 2).second, np.array([7200.0]))
    assert np.allclose((2 * a).second, np.array([7200.0]))
    ratio = a / b
    assert np.allclose(ratio, np.array([2.0]))
    half = a / 2.0
    assert half.unit == TimeUnit.HR
    assert np.allclose(half.value, np.array([0.5]))


def test_time_equality() -> None:
    assert Time(value=np.array([1000.0]), unit=TimeUnit.MS) == Time(
        value=np.array([1.0]), unit=TimeUnit.S
    )


def test_length_meter_and_convert() -> None:
    L = Length(value=np.array([2.0]), unit=LengthUnit.KM)
    assert np.allclose(L.meter, np.array([2000.0]))
    L.convert_unit(LengthUnit.M)
    assert L.unit == LengthUnit.M
    assert np.allclose(L.value, np.array([2000.0]))


def test_length_arithmetic() -> None:
    a = Length(value=np.array([1.0]), unit=LengthUnit.M)
    b = Length(value=np.array([100.0]), unit=LengthUnit.CM)
    s = a + b
    assert s.unit == LengthUnit.M
    assert np.allclose(s.value, np.array([2.0]))
    ratio = a / b
    assert np.allclose(ratio, np.array([1.0]))


def test_angle_degree_radian() -> None:
    deg = Angle(value=np.array([180.0]), unit=AngleUnit.DEGREE)
    assert np.allclose(deg.radian, np.array([np.pi]))
    rad = Angle(value=np.array([np.pi]), unit=AngleUnit.RADIAN)
    assert np.allclose(rad.degree, np.array([180.0]))


def test_angle_requires_1d() -> None:
    with pytest.raises(ValueError, match="1D"):
        Angle(value=np.array([[1.0]]), unit=AngleUnit.DEGREE)

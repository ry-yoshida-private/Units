from __future__ import annotations

import numpy as np
from dataclasses import dataclass

from .unit import TimeUnit


@dataclass
class Time:
    """
    Container class for durations.

    Parameters
    ----------
    value: np.ndarray
        The value of the duration.
    unit: TimeUnit
        The unit of the duration.
    """
    value: np.ndarray
    unit: TimeUnit

    @property
    def second(self) -> np.ndarray:
        """
        Return the duration in seconds.

        Returns
        -------
        np.ndarray:
            The duration in seconds.
        """
        return self.value * self.unit.to_second

    @property
    def ms(self) -> np.ndarray:
        """
        Return the duration in milliseconds.

        Returns
        -------
        np.ndarray:
            The duration in milliseconds.
        """
        return self.second / TimeUnit.MS.to_second

    @property
    def minute(self) -> np.ndarray:
        """
        Return the duration in minutes.

        Returns
        -------
        np.ndarray:
            The duration in minutes.
        """
        return self.second / TimeUnit.MIN.to_second

    @property
    def hour(self) -> np.ndarray:
        """
        Return the duration in hours.

        Returns
        -------
        np.ndarray:
            The duration in hours.
        """
        return self.second / TimeUnit.HR.to_second

    @property
    def day(self) -> np.ndarray:
        """
        Return the duration in days.

        Returns
        -------
        np.ndarray:
            The duration in days.
        """
        return self.second / TimeUnit.DAY.to_second

    def convert_unit(
        self,
        converted_unit: TimeUnit = TimeUnit.S,
    ) -> None:
        """
        Convert the duration unit.

        Parameters
        ----------
        converted_unit: TimeUnit
            The unit to convert the duration to.
        """
        if self.unit == converted_unit:
            return

        sec_value = self.second
        self.value = sec_value / converted_unit.to_second
        self.unit = converted_unit

    def __add__(self, other: Time) -> Time:
        """
        Add two durations.

        Returns
        -------
        Time:
            The sum of the two durations in seconds.
        """
        return Time(
            value=self.second + other.second,
            unit=TimeUnit.S,
        )

    def __sub__(self, other: Time) -> Time:
        """
        Subtract two durations.

        Returns
        -------
        Time:
            The difference of the two durations in seconds.
        """
        return Time(
            value=self.second - other.second,
            unit=TimeUnit.S,
        )

    def __mul__(self, scalar: float | np.ndarray) -> Time:
        """
        Multiply duration by a scalar.

        Parameters
        ----------
        scalar: float | np.ndarray
            The scalar to multiply by.

        Returns
        -------
        Time:
            The multiplied duration in the same unit.
        """
        return Time(
            value=self.value * scalar,
            unit=self.unit,
        )

    def __rmul__(self, scalar: float | np.ndarray) -> Time:
        """
        Multiply duration by a scalar (right multiplication).

        Parameters
        ----------
        scalar: float | np.ndarray
            The scalar to multiply by.

        Returns
        -------
        Time:
            The multiplied duration in the same unit.
        """
        return self.__mul__(scalar)

    def __truediv__(self, other: Time | float | np.ndarray) -> Time | np.ndarray:
        """
        Divide duration by another duration or a scalar.

        Parameters
        ----------
        other: Time | float | np.ndarray
            The duration or scalar to divide by.

        Returns
        -------
        Time | np.ndarray:
            If dividing by Time, returns a np.ndarray (ratio).
            If dividing by float or np.ndarray, returns a Time.
        """
        if isinstance(other, Time):
            return self.second / other.second
        return Time(
            value=self.value / other,
            unit=self.unit,
        )

    def __eq__(self, other: object) -> bool:
        """Compare if this duration is equal to another."""
        if not isinstance(other, Time):
            return False
        return np.allclose(self.second, other.second, atol=1e-9)

    def __str__(self) -> str:
        """String representation of the duration."""
        return f"{self.value} {self.unit.value}"

    def __repr__(self) -> str:
        """String representation of the duration."""
        return f"Time(value={self.value}, unit={self.unit})"

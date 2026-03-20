from __future__ import annotations
import numpy as np
from dataclasses import dataclass

from .unit import LengthUnit

@dataclass
class Length:
    """
    Container class for lengths.

    Parameters
    ----------
    value: np.ndarray
        The value of the length.
    unit: LengthUnit
        The unit of the length.
    """
    value: np.ndarray
    unit: LengthUnit
    
    @property
    def meter(self) -> np.ndarray:
        """
        Return the length in meters.

        Returns
        -------
        np.ndarray:
            The length in meters.
        """
        return self.value * self.unit.to_meter

    @property
    def km(self) -> np.ndarray:
        """
        Return the length in kilometers.

        Returns
        -------
        np.ndarray:
            The length in kilometers.
        """
        return self.meter / LengthUnit.KM.to_meter

    @property
    def cm(self) -> np.ndarray:
        """
        Return the length in centimeters.

        Returns
        -------
        np.ndarray:
            The length in centimeters.
        """
        return self.meter / LengthUnit.CM.to_meter

    @property
    def mm(self) -> np.ndarray:
        """
        Return the length in millimeters.

        Returns
        -------
        np.ndarray:
            The length in millimeters.
        """
        return self.meter / LengthUnit.MM.to_meter

    @property
    def inch(self) -> np.ndarray:
        """
        Return the length in inches.

        Returns
        -------
        np.ndarray:
            The length in inches.
        """
        return self.meter / LengthUnit.INCH.to_meter

    def convert_unit(
        self, 
        converted_unit: LengthUnit = LengthUnit.M
        ) -> None:
        """
        Convert the length unit.

        Parameters
        ----------
        converted_unit: LengthUnit
            The unit to convert the length to.
        """
        if self.unit == converted_unit:
            return

        # Convert to meters first, then to target unit
        meter_value = self.meter
        self.value = meter_value / converted_unit.to_meter
        self.unit = converted_unit

    def __add__(
        self, 
        other: Length
        ) -> Length:
        """
        Add two lengths.

        Returns
        -------
        Length:
            The sum of the two lengths in meters.
        """
        return Length(
            value=self.meter + other.meter,
            unit=LengthUnit.M
            )

    def __sub__(
        self, 
        other: Length
        ) -> Length:
        """
        Subtract two lengths.

        Returns
        -------
        Length:
            The difference of the two lengths in meters.
        """
        return Length(
            value=self.meter - other.meter,
            unit=LengthUnit.M
        )

    def __mul__(
        self, 
        scalar: float | np.ndarray
        ) -> Length:
        """
        Multiply length by a scalar.

        Parameters
        ----------
        scalar: float | np.ndarray
            The scalar to multiply by.

        Returns
        -------
        Length:
            The multiplied length in the same unit.
        """
        return Length(
            value=self.value * scalar,
            unit=self.unit
        )

    def __rmul__(self, scalar: float | np.ndarray) -> Length:
        """
        Multiply length by a scalar (right multiplication).

        Parameters
        ----------
        scalar: float | np.ndarray
            The scalar to multiply by.

        Returns
        -------
        Length:
            The multiplied length in the same unit.
        """
        return self.__mul__(scalar)

    def __truediv__(self, other: Length | float | np.ndarray) -> Length | np.ndarray:
        """
        Divide length by another length or a scalar.

        Parameters
        ----------
        other: Length | float | np.ndarray
            The length or scalar to divide by.

        Returns
        -------
        Length | np.ndarray:
            If dividing by Length, returns a np.ndarray (ratio).
            If dividing by float or np.ndarray, returns a Length.
        """
        if isinstance(other, Length):
            return self.meter / other.meter
        return Length(
            value=self.value / other,
            unit=self.unit
        )


    def __eq__(self, other: object) -> bool:
        """Compare if this length is equal to another."""
        if not isinstance(other, Length):
            return False
        return np.allclose(self.meter, other.meter, atol=1e-9)  # Small tolerance for float comparison

    def __str__(self) -> str:
        """String representation of the length."""
        return f"{self.value} {self.unit.value}"

    def __repr__(self) -> str:
        """String representation of the length."""
        return f"Length(value={self.value}, unit={self.unit})"

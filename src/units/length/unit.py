from enum import Enum

class LengthUnit(Enum):
    """
    Enum defining the length unit.

    Attributes
    ----------
    KM: LengthUnit
        The length unit is kilometer.
    M: LengthUnit
        The length unit is meter.
    CM: LengthUnit
        The length unit is centimeter.
    MM: LengthUnit
        The length unit is millimeter.
    INCH: LengthUnit
        The length unit is inch.
    """
    KM = "km"
    M = "m"
    CM = "cm"
    MM = "mm"
    INCH = "inch"

    @property
    def to_meter(self) -> float:
        match self:
            case LengthUnit.KM:
                return 1000
            case LengthUnit.M:
                return 1
            case LengthUnit.CM:
                return 0.01
            case LengthUnit.MM:
                return 0.001
            case LengthUnit.INCH: # 1 inch = 25.4 mm = 0.0254 m
                return 0.0254
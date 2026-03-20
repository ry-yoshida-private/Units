from enum import Enum

class AngleUnit(Enum):
    """
    Enum defining the angle unit.

    Attributes
    ----------
    DEGREE: AngleUnit
        The angle unit is degree.
    RADIAN: AngleUnit
        The angle unit is radian.
    """
    DEGREE = "degree"
    RADIAN = "radian"

    @property
    def as_upper(self) -> str:
        return str(self.value).upper()

    @property
    def as_lower(self) -> str:
        return str(self.value).lower()

    @property
    def is_degree(self) -> bool:
        return self is AngleUnit.DEGREE

    @property
    def is_radian(self) -> bool:
        return self is AngleUnit.RADIAN
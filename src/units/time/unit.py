from enum import Enum


class TimeUnit(Enum):
    """
    Enum defining the time unit.

    Attributes
    ----------
    MS: TimeUnit
        The time unit is millisecond.
    S: TimeUnit
        The time unit is second.
    MIN: TimeUnit
        The time unit is minute.
    HR: TimeUnit
        The time unit is hour.
    DAY: TimeUnit
        The time unit is day.
    """
    MS = "ms"
    S = "s"
    MIN = "min"
    HR = "h"
    DAY = "day"

    @property
    def to_second(self) -> float:
        match self:
            case TimeUnit.MS:
                return 1e-3
            case TimeUnit.S:
                return 1.0
            case TimeUnit.MIN:
                return 60.0
            case TimeUnit.HR:
                return 3600.0
            case TimeUnit.DAY:
                return 86400.0

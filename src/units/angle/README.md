# angle

## Overview

This module provides utilities for working with angles, including unit conversion between degrees and radians, and trigonometric function calculations.

## Components

| Component | Description |
|-----------|-------------|
| [angle.py](./angle.py) | Container class for angles with unit conversion and trigonometric operations (sin, cos, tan). |
| [unit.py](./unit.py) | Enum defining angle units (degree, radian) with utility properties. |

## Usage

```python
import numpy as np

from units import Angle, AngleUnit

theta = Angle(value=np.array([30.0, 45.0, 60.0]), unit=AngleUnit.DEGREE)
print(theta.radian)
print(theta.sin)

theta.convert_unit(AngleUnit.RADIAN)
print(theta.value)
```
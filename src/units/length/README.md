# length

## Overview

This module provides utilities for working with length values and units, including unit conversion and length calculations.

## Components

| Component | Description |
|-----------|-------------|
| [unit.py](./unit.py) | Enum defining length units (km, m, cm, mm) with conversion to meters. |
| [length.py](./length.py) | Container class for length values with unit conversion capabilities. |

## Usage

```python
import numpy as np

from units import Length, LengthUnit

road = Length(value=np.array([2.5]), unit=LengthUnit.KM)
print(road.meter)  # [2500.]

segment = Length(value=np.array([300.0]), unit=LengthUnit.M)
total = road + segment
print(total.km)  # [2.8]
```

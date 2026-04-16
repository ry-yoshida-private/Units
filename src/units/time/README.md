# time

## Overview

This module provides utilities for working with time durations and units, including conversion between milliseconds, seconds, minutes, hours, and days, and arithmetic on `Time` values backed by NumPy arrays.

## Components

| Component | Description |
|-----------|-------------|
| [unit.py](./unit.py) | Enum defining time units (`ms`, `s`, `min`, `h`, `day`) with conversion factors to seconds. |
| [time.py](./time.py) | Container class for durations with unit conversion, accessors in each supported unit, and basic arithmetic. |

## Usage

```python
import numpy as np

from units import Time, TimeUnit

warmup = Time(value=np.array([15.0]), unit=TimeUnit.MIN)
run = Time(value=np.array([45.0]), unit=TimeUnit.MIN)
total = warmup + run

print(total.second)  # [3600.]
print(total.hour)    # [1.]
```

# time

## Overview

This module provides utilities for working with time durations and units, including conversion between milliseconds, seconds, minutes, hours, and days, and arithmetic on `Time` values backed by NumPy arrays.

## Components

| Component | Description |
|-----------|-------------|
| [unit.py](./unit.py) | Enum defining time units (`ms`, `s`, `min`, `h`, `day`) with conversion factors to seconds. |
| [time.py](./time.py) | Container class for durations with unit conversion, accessors in each supported unit, and basic arithmetic. |

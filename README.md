![Python build & test](https://github.com/software-students-spring2024/3-python-package-exercise-lazyllm3/actions/workflows/event-logger.yml/badge.svg)
# Unit Conversion Toolkit
Conversion of units is the conversion of the unit of measurement in which a quantity is expressed, typically through a multiplicative conversion factor that changes the unit without changing the quantity. This is also often loosely taken to include replacement of a quantity with a corresponding quantity that describes the same physical property. [Source: Wiki](https://en.wikipedia.org/wiki/Conversion_of_units).<br />Our project is designed to swiftly and accurately convert between a wide array of measurement units across categories like length, weight, volume, temperature, time, and area, streamlining both professional tasks and everyday calculations.<br />

## Installation

1. Download package:
```
pip install -i https://test.pypi.org/simple/ unit-conversion-toolkit==0.1.1
```
2. Activate the virtual environment: 
```
pipenv shell
```
3. Create a Python program file that imports the package and uses it, e.g. 
```python
from unit_conversion_toolkit import converters
```
4. and then call the functions, for example:
```python
print(converters.convert_length(5, 'kilometer', 'mile'))
```

## Functions
1. Convert Length Measurements
```python
convert_length(value, from_unit, to_unit)
```

This function converts a length measurement from one unit to another. It supports conversions between meters, kilometers, and miles. The function first converts the input value to meters using predefined conversion rates, and then converts from meters to the target unit, returning the converted value.

Example:
```python
from converters import convert_length

length_in_kilometers = convert_length(1, "mile", "kilometer")
print(length_in_kilometers)  # Output: 1.60934
```

2. Convert Weight Measurements
```python
convert_weight(value, from_unit, to_unit)
```

The convert_weight function is designed to convert weight measurements between different units, including kilograms, grams, and pounds. It converts the input weight to kilograms as an intermediary step, using specified conversion factors, and then converts this intermediate value to the target weight unit.

Example:
```python
from converters import convert_weight

weight_in_kilograms = convert_weight(1, "pound", "kilogram")
print(weight_in_kilograms)  # Output: 0.453592
```

3. Convert Volume Measurements
```python
convert_volume(value, from_unit, to_unit)
```

This function facilitates the conversion of volume measurements across various units such as liters, milliliters, and gallons. It operates by first converting the provided volume to liters using established conversion factors, followed by a conversion from liters to the desired volume unit.

Example:
```python
from converters import convert_volume

volume_in_liters = convert_volume(1, "gallon", "liter")
print(volume_in_liters)  # Output: 3.78541
```
4. Convert Temperature Scales
```python
convert_temperature(value, from_scale, to_scale)
```

convert_temperature is a versatile function that allows for the conversion of temperature values between Celsius, Fahrenheit, and Kelvin scales. Depending on the input and target scales, it applies the appropriate formula for conversion and rounds the result to two decimal places.

Example:
```python
from converters import convert_temperature

temperature_in_fahrenheit = convert_temperature(0, "celsius", "fahrenheit")
print(temperature_in_fahrenheit)  # Output: 32.0
```

5. Convert Time Measurements
```python
convert_time(value, from_unit, to_unit)
```

The function convert_time converts time measurements between minutes, hours, and days. It standardizes the input time value to minutes, leveraging predefined conversion rates, and subsequently converts these minutes to the target time unit, facilitating an array of time-related calculations.

Example:
```python
from converters import convert_time

time_in_hours = convert_time(1440, "minute", "hour")
print(time_in_hours)  # Output: 24.0
```

6. Convert Area Measurements
```python
convert_area(value, from_unit, to_unit)
```

Designed for the conversion of area measurements, this function supports units such as square meters, square yards, and square feet. It converts the input area to square meters using a set of conversion factors and then inverts this process to obtain the final value in the desired area unit.

Example:
```python
from converters import convert_area

area_in_square_meters = convert_area(1, "square_foot", "square_meter")
print(area_in_square_meters)  # Output: 0.092903
```
## How To Contribute
1. Clone the repositary

```bash
git clone https://github.com/software-students-spring2024/3-python-package-exercise-lazyllm3/
```
2. Set up the environment
```
pipenv shell
```
3. Install build
```
pipenv install build
```
4. Modify the code
5. To build the package, run the following command:
```
pipenv run python -m build
```
6. Install pytest
```
pipenv install pytest
```
7. To test the package, run the following command:
```
pipenv run pytest
```


## Link to Example Python Program

[Example_Program](https://github.com/software-students-spring2024/3-python-package-exercise-lazyllm3/blob/Angel/__main__.py) 

## Link to package's page on the PyPI website
https://test.pypi.org/project/unit-conversion-toolkit/0.1.1/

## Contributors
1. [Angel Wu](https://github.com/angelWu2002)	
2. [Weilin Cheng](https://github.com/M1stery232)
3. [Ruichen Wang](https://github.com/rcwang937)	
4. [Haoyang Li](https://github.com/LeoLi727)	

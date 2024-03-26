# Unit Conversion Toolkit
Conversion of units is the conversion of the unit of measurement in which a quantity is expressed, typically through a multiplicative conversion factor that changes the unit without changing the quantity. This is also often loosely taken to include replacement of a quantity with a corresponding quantity that describes the same physical property. [Source: Wiki](https://en.wikipedia.org/wiki/Conversion_of_units).<br />Our project is designed to swiftly and accurately convert between a wide array of measurement units across categories like length, weight, volume, temperature, time, and area, streamlining both professional tasks and everyday calculations.<br />

## Installation

1. Create a `pipenv`-managed virtual environment and install the latest version of the package installed: 
```
pipenv install -i https://pypi.org/simple/ asciiarttools
```
2. Activate the virtual environment: 
```
pipenv shell
```
3. Create a Python program file that imports the package and uses it, e.g. 
```python
from asciiarttools import asciiarttools
```
and then call the functions, for example:
```python
asciiarttools.convertImageToAsciiImage('cat1.jpg', 'output.png')
```

## Functions
1. Convert Length Measurements
```python
convert_length(value, from_unit, to_unit)
```

This function converts a length measurement from one unit to another. It supports conversions between meters, kilometers, and miles. The function first converts the input value to meters using predefined conversion rates, and then converts from meters to the target unit, returning the converted value.

2. Convert Weight Measurements
```python
convert_weight(value, from_unit, to_unit)
```

The convert_weight function is designed to convert weight measurements between different units, including kilograms, grams, and pounds. It converts the input weight to kilograms as an intermediary step, using specified conversion factors, and then converts this intermediate value to the target weight unit.

3. Convert Volume Measurements
```python
convert_volume(value, from_unit, to_unit)
```

This function facilitates the conversion of volume measurements across various units such as liters, milliliters, and gallons. It operates by first converting the provided volume to liters using established conversion factors, followed by a conversion from liters to the desired volume unit.

4. Convert Temperature Scales
```python
convert_temperature(value, from_scale, to_scale)
```

convert_temperature is a versatile function that allows for the conversion of temperature values between Celsius, Fahrenheit, and Kelvin scales. Depending on the input and target scales, it applies the appropriate formula for conversion and rounds the result to two decimal places.

5. Convert Time Measurements
```python
convert_time(value, from_unit, to_unit)
```

The function convert_time converts time measurements between minutes, hours, and days. It standardizes the input time value to minutes, leveraging predefined conversion rates, and subsequently converts these minutes to the target time unit, facilitating an array of time-related calculations.

6. Convert Area Measurements
```python
convert_area(value, from_unit, to_unit)
```

Designed for the conversion of area measurements, this function supports units such as square meters, square yards, and square feet. It converts the input area to square meters using a set of conversion factors and then inverts this process to obtain the final value in the desired area unit.
## How To Contribute
1. Clone the repositary

```bash
git clone https://github.com/software-students-spring2024/3-python-package-exercise-lazyllm3/
```


## Link to Example Python Program

[Example_Program](https://github.com/software-students-spring2024/3-python-package-exercise-lazyllm3/blob/Angel/__main__.py) 

## Link to package's page on the PyPI website
https://test.pypi.org/project/unit-conversion-toolkit/0.1.1/

## Contributors
1. [Angel Wu (Net Id: cw3561)](https://github.com/angelWu2002)	
2. [Weilin Cheng (Net Id: wc2182)](https://github.com/M1stery232)
3. [Ruichen Wang (Net Id: rw2671)](https://github.com/rcwang937)	
4. [Haoyang Li (Net Id: hl3951)](https://github.com/LeoLi727)	

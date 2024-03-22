# tests/test_converters.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Test Case for Length
from unit_conversion_toolkit.converters import convert_length

def test_convert_length_meters_to_kilometers():
    assert convert_length(1000, 'meter', 'kilometer') == 1

def test_convert_length_miles_to_kilometers():
    assert round(convert_length(1, 'mile', 'kilometer'), 3) == 1.609

def test_convert_length_kilometers_to_miles():
    assert round(convert_length(1, 'kilometer', 'mile'), 3) == 0.621

# Test Case for Weight
from unit_conversion_toolkit.converters import convert_weight

def test_convert_weight_kilograms_to_grams():
    assert convert_weight(1, 'kilogram', 'gram') == 1000

def test_convert_weight_grams_to_kilograms():
    assert convert_weight(1000, 'gram', 'kilogram') == 1

def test_convert_weight_kilograms_to_pounds():
    assert round(convert_weight(1, 'kilogram', 'pound'), 5) == round(2.20462, 5)

# Test Case for Volume
from unit_conversion_toolkit.converters import convert_volume

def test_convert_volume_liters_to_milliliters():
    assert convert_volume(1, 'liter', 'milliliter') == 1000

def test_convert_volume_gallons_to_liters():
    assert round(convert_volume(1, 'gallon', 'liter'), 5) == round(3.78541, 5)

def test_convert_volume_milliliters_to_liters():
    assert convert_volume(1000, 'milliliter', 'liter') == 1

# Test Case for Tempreture
from unit_conversion_toolkit.converters import convert_temperature

def test_convert_temperature_celsius_to_fahrenheit():
    assert convert_temperature(0, 'celsius', 'fahrenheit') == 32

def test_convert_temperature_fahrenheit_to_celsius():
    assert convert_temperature(32, 'fahrenheit', 'celsius') == 0

def test_convert_temperature_celsius_to_kelvin():
    assert convert_temperature(0, 'celsius', 'kelvin') == 273.15

def test_convert_temperature_kelvin_to_celsius():
    assert convert_temperature(273.15, 'kelvin', 'celsius') == 0

def test_convert_temperature_fahrenheit_to_kelvin():
    assert round(convert_temperature(32, 'fahrenheit', 'kelvin'), 2) == 273.15

def test_convert_temperature_kelvin_to_fahrenheit():
    assert convert_temperature(273.15, 'kelvin', 'fahrenheit') == 32

# Test Case for Time
from unit_conversion_toolkit.converters import convert_time

def test_convert_time_minutes_to_hours():
    assert convert_time(60, 'minute', 'hour') == 1

def test_convert_time_hours_to_days():
    assert convert_time(24, 'hour', 'day') == 1

def test_convert_time_minutes_to_days():
    assert convert_time(1440, 'minute', 'day') == 1

# Test Case for Area
from unit_conversion_toolkit.converters import convert_area

def test_convert_area_square_meters_to_square_yards():
    assert round(convert_area(1, 'square_meter', 'square_yard'), 5) == round(1 / 0.836127, 5)

def test_convert_area_square_yards_to_square_meters():
    assert round(convert_area(1, 'square_yard', 'square_meter'), 5) == round(0.836127, 5)

def test_convert_area_square_meters_to_square_foot():
    assert round(convert_area(1, 'square_meter', 'square_foot'), 5) == round(1 / 0.092903, 5)

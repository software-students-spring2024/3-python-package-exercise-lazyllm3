# unit_conversion_toolkit/converters.py

# function 1
def convert_length(value, from_unit, to_unit):
    # Define the conversion rates to meters
    to_meter = {"meter": 1, "kilometer": 1000, "mile": 1609.34}
    
    # Convert the value to meters first
    value_in_meters = value * to_meter[from_unit]
    
    # Now convert from meters to the target unit
    return value_in_meters / to_meter[to_unit]

# function 2
def convert_weight(value, from_unit, to_unit):
    # Conversion factors to kilograms
    to_kilogram = {"kilogram": 1, "gram": 0.001, "pound": 0.453592}
    value_in_kilograms = value * to_kilogram[from_unit]
    # Conversion factor needs to be inverted to convert from kilograms to the target unit
    return value_in_kilograms / to_kilogram[to_unit]

# function 3
def convert_volume(value, from_unit, to_unit):
    # Conversion factors to liters
    to_liter = {"liter": 1, "milliliter": 0.001, "gallon": 3.78541}
    value_in_liters = value * to_liter[from_unit]
    # Conversion factor needs to be inverted to convert from liters to the target unit
    return value_in_liters / to_liter[to_unit]

# function 4
def convert_temperature(value, from_scale, to_scale):
    if from_scale == "celsius":
        if to_scale == "fahrenheit":
            return round(value * 9 / 5 + 32, 2)
        elif to_scale == "kelvin":
            return round(value + 273.15, 2)
    elif from_scale == "fahrenheit":
        if to_scale == "celsius":
            return round((value - 32) * 5 / 9, 2)
        elif to_scale == "kelvin":
            return round((value + 459.67) * 5 / 9, 2)
    elif from_scale == "kelvin":
        if to_scale == "celsius":
            return round(value - 273.15, 2)
        elif to_scale == "fahrenheit":
            return round(value * 9 / 5 - 459.67, 2)


# unit_conversion_toolkit/converters.py

def convert_length(value, from_unit, to_unit):
    # Define the conversion rates to meters
    to_meter = {"meter": 1, "kilometer": 1000, "mile": 1609.34}
    
    # Convert the value to meters first
    value_in_meters = value * to_meter[from_unit]
    
    # Now convert from meters to the target unit
    return value_in_meters / to_meter[to_unit]

# def convert_weight(value, from_unit, to_unit):
#     weight_units = {"kilogram": 1, "gram": 1000, "pound": 2.20462}
#     return value * weight_units[from_unit] / weight_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion factors to kilograms
    to_kilogram = {"kilogram": 1, "gram": 0.001, "pound": 0.453592}
    value_in_kilograms = value * to_kilogram[from_unit]
    # Conversion factor needs to be inverted to convert from kilograms to the target unit
    return value_in_kilograms / to_kilogram[to_unit]

# def convert_volume(value, from_unit, to_unit):
#     volume_units = {"liter": 1, "milliliter": 1000, "gallon": 0.264172}
#     return value * volume_units[from_unit] / volume_units[to_unit]

def convert_volume(value, from_unit, to_unit):
    # Conversion factors to liters
    to_liter = {"liter": 1, "milliliter": 0.001, "gallon": 3.78541}
    value_in_liters = value * to_liter[from_unit]
    # Conversion factor needs to be inverted to convert from liters to the target unit
    return value_in_liters / to_liter[to_unit]

# def convert_temperature(value, from_scale, to_scale):
#     if from_scale == "celsius":
#         return value * 9 / 5 + 32 if to_scale == "fahrenheit" else value + 273.15
#     elif from_scale == "fahrenheit":
#         return (value - 32) * 5 / 9 if to_scale == "celsius" else (value + 459.67) * 5 / 9
#     elif from_scale == "kelvin":
#         return value - 273.15 if to_scale == "celsius" else value * 9 / 5 - 459.67

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


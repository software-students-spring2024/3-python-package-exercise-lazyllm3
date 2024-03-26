from unit_conversion_toolkit import converters as uct

def main():
    # Convert 5 kilometers to miles
    km_to_miles = uct.convert_length(5, 'kilometer', 'mile')
    print(f"5 kilometers is equal to {km_to_miles} miles")

    # Convert 2000 grams to pounds
    grams_to_pounds = uct.convert_weight(2000, 'gram', 'pound')
    print(f"2000 grams is equal to {grams_to_pounds} pounds")

    # Convert 1 gallon to liters
    gallon_to_liters = uct.convert_volume(1, 'gallon', 'liter')
    print(f"1 gallon is equal to {gallon_to_liters} liters")

    # Convert 100 degrees Celsius to Fahrenheit
    celsius_to_fahrenheit = uct.convert_temperature(100, 'celsius', 'fahrenheit')
    print(f"100 degrees Celsius is equal to {celsius_to_fahrenheit} degrees Fahrenheit")

    # Convert 2 hours to minutes
    hours_to_minutes = uct.convert_time(2, 'hour', 'minute')
    print(f"2 hours is equal to {hours_to_minutes} minutes")

    # Convert 500 square feet to square meters
    square_feet_to_square_meters = uct.convert_area(500, 'square_foot', 'square_meter')
    print(f"500 square feet is equal to {square_feet_to_square_meters} square meters")

if __name__ == "__main__":
    main()

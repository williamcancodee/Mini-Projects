def convert_units(value, from_unit, to_unit, category):
    """
    Converts a value from one unit to another within a specified category.

    Args:
        value (float or int): The value to convert.
        from_unit (str): The unit to convert from.
        to_unit (str): The unit to convert to.
        category (str): The category of units ('length', 'weight', 'temperature').

    Returns:
        float: The converted value or an error message.
    """

    # Validate input types
    if not isinstance(value, (int, float)):
        return "Value must be a number."
    if not all(isinstance(u, str) for u in [from_unit, to_unit, category]):
        return "Units and category must be strings."

    category = category.lower()
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if category == 'length':
        # Conversion factors to meters
        length_factors = {
            'meter': 1,
            'kilometer': 1000,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'yard': 0.9144,
            'mile': 1609.344
        }
        if from_unit not in length_factors or to_unit not in length_factors:
            return "Invalid length units."
        # Convert to meters then to target unit
        value_in_meters = value * length_factors[from_unit]
        converted_value = value_in_meters / length_factors[to_unit]
        return round(converted_value, 4)

    elif category == 'weight':
        # Conversion factors to grams
        weight_factors = {
            'gram': 1,
            'kilogram': 1000,
            'milligram': 0.001,
            'pound': 453.592,
            'ounce': 28.3495,
            'ton': 1000000
        }
        if from_unit not in weight_factors or to_unit not in weight_factors:
            return "Invalid weight units."
        # Convert to grams then to target unit
        value_in_grams = value * weight_factors[from_unit]
        converted_value = value_in_grams / weight_factors[to_unit]
        return round(converted_value, 4)

    elif category == 'temperature':
        if from_unit not in ['celsius', 'fahrenheit', 'kelvin'] or to_unit not in ['celsius', 'fahrenheit', 'kelvin']:
            return "Invalid temperature units."
        if from_unit == to_unit:
            return value
        # Convert to Celsius first
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        # Convert from Celsius to target
        if to_unit == 'fahrenheit':
            converted_value = celsius * 9/5 + 32
        elif to_unit == 'kelvin':
            converted_value = celsius + 273.15
        else:
            converted_value = celsius
        return round(converted_value, 2)

    else:
        return "Invalid category. Choose 'length', 'weight', or 'temperature'."

# Test the function
if __name__ == "__main__":
    print("Length: 5 meters to feet:", convert_units(5, 'meter', 'foot', 'length'))
    print("Weight: 10 pounds to kilograms:", convert_units(10, 'pound', 'kilogram', 'weight'))
    print("Temperature: 25 Celsius to Fahrenheit:", convert_units(25, 'celsius', 'fahrenheit', 'temperature'))
    print("Error - invalid category:", convert_units(1, 'meter', 'foot', 'volume'))
    print("Error - invalid unit:", convert_units(1, 'invalid', 'foot', 'length'))

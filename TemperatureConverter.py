'temp converter'
input_str = input("Enter the tempreture: ")
tempreture = int(input_str)
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
if unit.upper() == "C":
    converted = (tempreture * 9/5) + 32
    print(f"{tempreture}°C is equal to {converted}°F")
elif unit.upper() == "F":
    converted = (tempreture - 32) * 5/9
    print(f"{tempreture}°F is equal to {converted}°C")
else:
    print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# End of TemperatureConverter.py
# Temperature Converter
# This program converts temperatures between Celsius and Fahrenheit.
 
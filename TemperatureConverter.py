'temp converter'
# input_str = input("Enter the tempreture: ")
# tempreture = int(input_str)
# unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")


# if unit.upper() == "C":
#     converted = (tempreture * 9/5) + 32
#     print(f"{tempreture}°C is equal to {converted}°F")
# elif unit.upper() == "F":
#     converted = (tempreture - 32) * 5/9
#     print(f"{tempreture}°F is equal to {converted}°C")
# else:
#     print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")



def convert_temperature():
    while True:
        input_str = input("Enter the temperature (or 'q' to quit): ").strip()
        if input_str.lower() == 'q':
            print("Exiting.")
            break

        try:
            temperature = float(input_str)
        except ValueError:
            print("Invalid temperature. Please enter a number or 'q' to quit.")
            continue

        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        if unit == "C":
            converted = (temperature * 9/5) + 32
            print(f"{temperature}°C is equal to {converted}°F")
        elif unit == "F":
            converted = (temperature - 32) * 5/9
            print(f"{temperature}°F is equal to {converted}°C")
        else:
            print("Error: Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    convert_temperature()

 
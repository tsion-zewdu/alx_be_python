FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temp_input = input("Enter the temperature to convert: ")
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp_input.replace('.', '', 1).isdigit() or (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
    temperature = float(temp_input)
    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
else:
    print("Invalid temperature. Please enter a numeric value.")


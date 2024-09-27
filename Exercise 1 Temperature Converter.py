# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main Program of Temperature Converter
def main():
    while True:
        # Ask the user to input a temperature
        temperature = float(input("Enter a temperature: "))

        # Ask the user to select the conversion type
        print("Select the conversion type:")
        print("1. From Celsius to Fahrenheit")
        print("2. From Fahrenheit to Celsius")
        conversion_type = int(input("Enter 1 or 2: "))

        # Perform the appropriate conversion and print the result
        if conversion_type == 1:
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result}°F")
        elif conversion_type == 2:
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result}°C")
        else:
            print("Invalid conversion type. Please try again.")

        # Ask the user if they want to perform another conversion
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            break

# Entry point of the program
if __name__ == "__main__":
    main()
KELVIN_OFFSET = 273.15

celsius = float(input("Suhu Celsius: "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print(f"Fahrenheit = {fahrenheit:.2f}")
print(f"Kelvin     = {kelvin:.2f}")

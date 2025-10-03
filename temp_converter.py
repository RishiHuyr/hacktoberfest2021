def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15
def k_to_c(k): return k - 273.15

if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose option: ")

    val = float(input("Enter value: "))
    if choice == "1":
        print(f"{val} °C = {c_to_f(val):.2f} °F")
    elif choice == "2":
        print(f"{val} °F = {f_to_c(val):.2f} °C")
    elif choice == "3":
        print(f"{val} °C = {c_to_k(val):.2f} K")
    elif choice == "4":
        print(f"{val} K = {k_to_c(val):.2f} °C")
    else:
        print("Invalid option")

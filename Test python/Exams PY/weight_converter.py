weight = input("Enter your weight: ")
unit = input("Enter the unut ot weight (L)lbs or (K)kg: ")
unit = unit.upper()

if unit == 'L':
    weight_lbs = 0.0
    weight_lbs = weight / 2.2
    print(f"{weight_lbs}lbs")
elif unit == 'K':
    weight_kg = 0.0
    weight_kg = weight / 0.45
    print(f"{weight_kg}kg")
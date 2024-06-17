distance = int(input("Distance: "))
fuel = float(input("Litres of fuel: "))
price_per_litre = float(input("Price per litre: "))

total_fuel = (fuel * distance) / 100
total_price = total_fuel * price_per_litre

print(round(total_price,2))
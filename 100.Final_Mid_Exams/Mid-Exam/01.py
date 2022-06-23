budget = float(input())
price_floor = float(input())

price_egg = price_floor * 0.75
price_milk = price_floor * 1.25 / 4

price_czonac = price_floor + price_milk + price_egg

cozonac = 0
eggs_count = 0

while budget > price_czonac:
    cozonac += 1
    eggs_count += 3

    if cozonac % 3 == 0:
        eggs_count -= cozonac - 2

    budget -= price_czonac

print(f"You made {cozonac} cozonacs! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")

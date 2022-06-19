import re

line = input()

furnitures = []
total_price = 0

pattern = r"^>>(?P<product>[a-zA-Z]+)<<(?P<price>[\d]+\.?[\d]+)!(?P<quantity>[\d]+)$"

while not line == "Purchase":
    furniture = re.match(pattern, line)
    if furniture:
        name = furniture["product"]
        price = float(furniture["price"])
        quantity = float(furniture["quantity"])

        furnitures.append(name)
        total_price += price * quantity

    line = input()

print("Bought furniture:")
[print(x) for x in furnitures]
print(f"Total money spend: {total_price:.2f}")

budget = float(input())
flour_price = float(input())

cakes_quantity = 0
colored_eggs = 0
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
cakes_price = flour_price + eggs_price + milk_price

while budget > cakes_price:
    cakes_quantity += 1
    budget -= cakes_price
    colored_eggs += 3
    if cakes_quantity % 3 == 0:
        colored_eggs -= cakes_quantity - 2

print(f'You made {cakes_quantity} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

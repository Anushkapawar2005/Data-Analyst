
# **kwargs - accept multiple keyword arguments

def shopping_cart(**products):
  total = 0
  print("Items purchased: ")
  for item, price in products.items():
    print(f"{item}: rs{price}")
    total += price
  print(f"Total: rs{total}")

shopping_cart(apple=15, orange=12,mango=10)
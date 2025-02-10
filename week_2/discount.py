print("Culculate discount Price")
# 1. full price
# 2. discount %
# 3. discount price = full price - discount price
# 4. discount prict = full price * % discount / 100

full_price = float(input("Enter Full price $: "))  # input get value fron user

# print(type(full_price))

discount = float(input("Enter Discount %: "))

discount_price = full_price * discount / 100

discounted_price = full_price- discount_price

print("Discounted Price: $", discounted_price)
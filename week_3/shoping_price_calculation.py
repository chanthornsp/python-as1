# We have shoping 3 items with different prices.
# Calculate the total price of the items. using in-place operations.
print('Shoping Price Calculation')

item_1 = float(input('Enter the price of item 1: $'))
item_2 = float(input('Enter the price of item 2: $'))
item_3 = float(input('Enter the price of item 3: $'))

# int default price
price = 0

price += item_1 # = price + price + item_1
price += item_2
price += item_3

print("Total price: $", price)




# Calculate net price based on 15% discount

price = int(input("Enter price :"))
discount = price * 15 // 100
net_price = price - discount

print(f"Base Price  : {price:6}")
print(f'- Discount  : {discount:6}')
print(f'Net price   : {net_price:6}')

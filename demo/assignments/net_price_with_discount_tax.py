# Calculate Net price based on 18% Tax and 15 % discount
price = float(input("Enter a price:"))
discount = price * 15 / 100
discounted_price = price - discount
tax = discounted_price * 18 / 100
net_price = discounted_price + tax

print(f"Base price    : {price:8.2f}")
print(f"- Discount    : {discount:8.2f}")
print(f"After Discount: {discounted_price:8.2f}")
print(f"+ Tax         : {tax:8.2f}")
print(f"Net price     : {net_price:8.2f}")

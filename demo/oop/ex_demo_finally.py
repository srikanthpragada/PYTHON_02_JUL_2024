
try:
    num = int(input("Enter number :"))
    print(100 // num)
except ValueError:
    print("Sorry! Invalid number!")
finally:
    print("Finally!")

print("The End")



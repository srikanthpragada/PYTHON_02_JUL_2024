# Calculate Net salary with HRA DA and tax
salary = float(input("Enter the basic salary: "))

if salary < 50000:
    hra = salary * 20 / 100
    da = salary * 10 / 100
else:
    hra = salary * 25 / 100
    da = salary * 12 / 100

gross = salary + hra + da

if gross > 100000:
    tax = gross * 10 / 100
else:
    tax = 0.0

netsalary = gross - tax

print(f"Basic Salary   : {salary:8.0f}")
print(f"+ HRA          : {hra:8.0f}")
print(f"+ DA           : {da:8.0f}")
print(f"Gross Salary   : {gross:8.0f}")
print(f" - Tax         : {tax:8.0f}")
print(f"Net Salary     : {netsalary:8.0f}")

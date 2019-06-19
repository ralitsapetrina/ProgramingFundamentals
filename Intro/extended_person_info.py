name = input()
age = int(input())
town = input()
salary = float(input())

print(f'Name: {name}\nAge: {age}\nTown: {town}\nSalary: ${salary:.2f}')

if age < 18:
    age_range = "teen"
elif age < 70:
    age_range = "adult"
else:
    age_range = "elder"

if salary < 500:
    salary_range = "low"
elif salary < 2000:
    salary_range = "medium"
else:
    salary_range = "high"


print(f'Age range: {age_range}\nSalary range: {salary_range}')
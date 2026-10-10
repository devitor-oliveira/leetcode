empNumber = int(input())
workedHours = int(input())
salaryHour = float(input())

salaryMonth: float = salaryHour * workedHours

print(f"NUMBER = {empNumber}")
print(f"SALARY = U$ {salaryMonth:.2f}")
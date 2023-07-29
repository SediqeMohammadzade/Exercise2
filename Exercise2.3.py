name = input("Enter your name:")
family = input("Enter your family:")
grade1 = float(input("Enter your grade1:"))
grade2 = float(input("Enter your grade2:"))
grade3 = float(input("Enter your grade3:"))

avg = (grade1 + grade2 + grade3) / 3

if avg >= 17:
    result ="Great"

if 12<= avg >= 17:
   result ="Normal"

if avg <= 12:
   result ="Fail"

print(result)
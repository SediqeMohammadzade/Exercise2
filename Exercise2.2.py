a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

D = a + b
if D >= c:
    result = "These three sides can form a triangle"
else:
    result = "These three sides can not form a triangle"

E = a + c
if E >= b:
    result = "These three sides can form a triangle"
else:
    result = "These three sides can not form a triangle"
F = b + c
if F >= a:
    result = "These three sides can form a triangle"
else:
    result = "These three sides can not form a triangle"

print(result)
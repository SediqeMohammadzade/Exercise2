import math
op = input("Enter op(+,-,*,/,sin,cos,tan,cot,factorial,radical)")
a = int(input(Enter a:))
b = int(input(Enter b:))
c = int(input(Enter c:))
if op == "+":
    result = a + b
if op == "-":
    result = a - b
if op == "*":
    result = a * b
if op == "/":
    if b == 0:
        print("Error")
    else:
        result = a / b
if op == "sin":
    result = (math.sin(c))
if op == "cos":
    result = (math.cos(c))
if op == "tan":
    result = (math.tan(c))
if op == "cot":
    if math.tan(c)==0:
        print("Error")
    else:
        result = (1/math.tan(c))
if op == "factorial":
    if c >= 0:
        result = (math.factorial(c))
if op == "radical":
    if = c >= 0:
        result = (math.sqrt(c))
    else:
        print("Error")
print(result)
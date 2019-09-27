
a = int(input("input0: "))
b = int(input("input1: "))
c = str(input("input2: "))

if c == "add":
    sum = a + b
 
    print("OUTPUT:", sum)

elif c == "subtract":
    sum = a - b
 
    print("OUTPUT:", sum)

elif c == "multiply":
    sum = a * b
 
    print("OUTPUT:", sum)

elif c == "divide":
    sum = a / b
 
    print("OUTPUT:", sum)

else:
    print("operator doesn't exist")
from collections import Counter

A = list(input("Enter List :"))

list_freq= (Counter(A))


print("Input :", A)


for key, value in list_freq.items():
   print(key, " = ", value)
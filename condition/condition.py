# Conditional example
x = 10
if x == 0:
  print("zero")
elif x % 2 == 0:
  print("even")
else:
  print("odd")

print("odd") if x % 2 else print("even")

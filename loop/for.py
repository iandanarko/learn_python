weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 1. loop in
for day in weeks:
  print(day)

# 2. loop with index:
for i, day in enumerate(weeks):
  print([i, day])

# 3. loop range from 0..end:
for i in range(len(weeks)):
  print(weeks[i])

# 4, loop range from end to 0:
for i in range(len(weeks)-1, -1, -1):
  print(weeks[i])

# 5. loop dict
dict = {1: "one", 2: "two"}
for k, v in dict.items():
  print([k, v])

# 6. loop multi array
arr1 = ["1.0", "1.1"]
arr2 = ["2.0", "2.1"]
for val1, val2 in zip(arr1, arr2):
  print([val1, val2])
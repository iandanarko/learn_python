# lambda is just like a normal function
def make_incrementor(n):
  return lambda x: x + n

f = make_incrementor(42)

print(f(0))

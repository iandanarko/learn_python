# List as defautl parameter
def f(a, L=[]):
  L.append(a)
  return L

print(f(1)) # [1]
print(f(2)) # [1, 2]
print(f(3)) # [1, 2, 3]

def f(a, L=None):
  if L is None:
    L = []
  L.append(a)
  return L

print(f(1)) # [1]
print(f(2)) # [2]
print(f(3)) # [3]

# keywords argument
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
  print("--This parrot wouldn't", action, end=' ')
  print("if you put", voltage, "volts through it.")
  print("--Lovely plumage, the", type)
  print("-- It's", state, "!")

# valid
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOODOOM')
parrot(action='VODOOM', voltage=1000000)
parrot('a million', 'berefit of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

# Varidic argument
def cheeseshop(kind, *arguments, **keywords):
  print("-- Do you have any ", kind, "?")
  print("-- I'm sorry, we're all out of", kind)
  for arg in arguments:
    print(arg)
  print("-" * 40)
  for kw in keywords:
    print(kw, ":", keywords[kw])

cheeseshop("Limburger", # kind
"It's very runny sir.", # *arguments
"It's really very, VERY runny, sir.", # *arguments
shopkeeper="Michael Palin", # **keywords
client="John Cleese", # **keywords
sketch="Cheese Shop Sketch" # **keywords
)


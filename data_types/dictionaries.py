# Dictionaries
tel = {
  "jack": 4098,
  "sape": 4139
}

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127

print(tel)

#list tel
print(list(tel))

#sort
print(sorted(tel))

print('irv' in tel)

for k, v in tel.items():
  print(k, v)

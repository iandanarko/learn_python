# Create Function
def myFunction(param: str) -> str:
  return "Called from function with param ${0}".format((param))

print(myFunction("Hello World"))

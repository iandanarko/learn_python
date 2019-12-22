def scope_test():
  def do_local():
    # spam scope only on do_local()
    spam = "local spam" # asssign to middle do_local() spam
  def do_nonlocal():
    # If a name is declared global, then all references and assignments go directly to the middle scope containing the
    # module’s global names. To rebind variables found outside of the innermost scope, the nonlocal statement
    # can be used
    nonlocal spam
    spam = "nonlocal spam" # asssign to middle scope_test() spam
  def do_global():
    global spam
    spam = "global spam" # asssign to global spam
  spam = "test spam"
  do_local()
  print("After local assignment:", spam) # test spam
  do_nonlocal() 
  print("After nonlocal assignment:", spam) # non local spam
  do_global()
  print("After global assignment:", spam) # non local spam

scope_test()
print("In global scope:", spam)

# The global statement can be used to indicate that particular variables live in the global scope and should
# be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and
# should be rebound there.

# global and nonlocal only used for assigning value to global variable
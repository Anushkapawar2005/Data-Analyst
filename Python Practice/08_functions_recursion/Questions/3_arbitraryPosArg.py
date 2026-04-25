
# *args - accept multiple positional arguments

def greeting(*names):
  for name in names:
    print(f"Hello, {name}!")
greeting("Anu","Radha","Shyam")
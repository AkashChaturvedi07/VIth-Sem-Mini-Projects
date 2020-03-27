for line in open('prog.py'):
  if line.startswith('import'):
    modulenames=line.split()
    print(modulenames[1])
    with open(modulenames[1]) as f:
      with open('out.py', "a") as f1:
        for line2 in f:
          f1.write(line2)
        f1.write("\n")
        f1.write("\n")


for line in open('prog.py'):
  if not line.startswith('import'):
    with open('out.py', "a") as f1:
      f1.write(line)



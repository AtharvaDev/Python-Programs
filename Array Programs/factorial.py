def fact(n):
  fact = 1
  if n == 0:
    return 0
  else:
    while n>0:
      fact *= n 
      n -= 1

  return fact

print(fact(int(input("factorial of a number: "))))
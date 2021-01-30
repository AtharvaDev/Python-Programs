def simple(p,t,r):
  total =  p * (pow((1 + r / 100), t)) 
  total = total-p

  return total

p = int(input("principle amount: "))
t = int(input("time: "))
r = float(input("rate of int: "))

print(simple(p,t,r))
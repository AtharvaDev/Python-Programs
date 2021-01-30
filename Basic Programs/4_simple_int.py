def simple(p,t,r):
  total = p*t*r
  total = total/100
  return total

p = int(input("principle amount: "))
t = int(input("principle amount: "))
r = int(input("principle amount: "))

print(simple(p,t,r))
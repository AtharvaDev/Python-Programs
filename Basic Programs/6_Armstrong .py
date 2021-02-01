n= int(input("Enter a number: "))
arr = list(map(int ,str(n)))
final = 0

for i in arr:
  temp = i * i * i
  final += temp
  # print (temp)

if (n==final):
  print( str(n) + ' is Armstrong number')
else:
  print( str(n) + ' is not Armstrong number')
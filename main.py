start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for i in range(start, end+1):
    for x in range(2, i):
      if(i%x ==0):
        break
    else:  
      print(i)

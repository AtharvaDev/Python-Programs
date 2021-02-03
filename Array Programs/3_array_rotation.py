
# Python Program for array rotation


# //////////////////////////////////////////////
arr = []
n = int(input("Enter number of elements : ")) 
print("Now enter 5 element: ")
for i in range(0, n): 
    ele = int(input()) 
    arr.append(ele)
d = int(input("Enter no. of rotations: \n"))
print("\n Original array is: ")
print(arr)
print("\n Array after rotations: ")

temp = []
for i in range(d):
  if i <= d:
    temp.append(arr[i])

arr = arr[d:n]
for j in range(len(temp)):
  arr.append(temp[j])

print(arr)

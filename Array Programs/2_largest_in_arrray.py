# Python Program to find largest element in an array


def largest(arr):
  large = 0
  n = len(arr)
  for i in range (n):
    if arr[i]> large:
      large = arr[i]

  return large
# arr = [10, 324, 45, 90, 9808] 
arr = []
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    arr.append(ele)

print(largest(arr))
def Binary(ele,low,high,arr):
  if high>=low:
    mid=(high+low)//2
  if arr[mid]==ele:
    return mid
  elif arr[mid]>ele:
    return Binary(ele,low,mid-1,arr)
  else:
    return Binary(ele,mid+1,high,arr)

arr = list(map(int, input("Enter numbers separated by space: ").split()))
high = len(arr) - 1
ele = int(input("Element to find: "))
pos = Binary(ele,0,high,arr)
print(f"{ele} found at {pos+1}")

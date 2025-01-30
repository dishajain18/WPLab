arr=(input("Enter list of names separated by space: ")).split()
arr.sort(key=lambda x: x.lower()) #to make sure it doesnt differentiate b/w capital and small
print("Sorted:",end=" ")
print(" ".join(arr))

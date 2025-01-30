arr = list(map(int, input("Enter numbers separated by space: ").split()))
smallest = arr[0]

for val in arr:
    if val < smallest:
        smallest = val

print(f"{smallest} is smallest")

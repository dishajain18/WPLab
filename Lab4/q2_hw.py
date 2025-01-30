def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True
        if not swapped:
            break  # Optimization: Stop if no swaps were made in a pass

# Example usage
arr = list(map(int, input("Enter numbers separated by space: ").split()))
bubble_sort(arr)
print("Sorted array:", arr

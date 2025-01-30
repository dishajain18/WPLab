class PairSum:
  def __init__(self, numbers, target):
    self.numbers = numbers
    self.target = target
  
  def find_pair(self):
    seen = {} # Dictionary to store the number and its index
    for i, num in enumerate(self.numbers):
      complement = self.target - num
      if complement in seen:
        # If complement is found, return the indices
        return seen[complement]+1, i+1
      seen[num] = i
    return None # If no pair is found


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Target sum: "))

pair_finder = PairSum(numbers, target)
result = pair_finder.find_pair()

if result:
print(f"Indices of the pair: {result[0]}, {result[1]}")
else:
print("No pair found")

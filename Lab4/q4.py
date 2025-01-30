class Subsets:
  def __init__(self, nums):
    self.nums = nums
  def generate_subsets(self):
    result = [[]]
  for num in self.nums:
    result+=[item + [num] for item in result]
  return result


nums = list(map(int, input("Enter numbers separated by space: ").split()))
subsets_generator = Subsets(nums)
subsets = subsets_generator.generate_subsets()

# Print all unique subsets
print(subsets)

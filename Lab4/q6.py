class Power:
  def __init__(self, x, n):
    self.x = x
    self.n = n
  def my_pow(self):
    return self._power(self.x, self.n)
  def _power(self, x, n):
    if n == 0:
      return 1 # Base case: x^0 = 1
    elif n < 0:
      return 1 / self._power(x, -n) # Handle negative powers
    elif n % 2 == 0:
      half = self._power(x, n // 2)
      return half * half # If n is even, use (x^(n/2))^2
    else:
      return x * self._power(x, n - 1) # If n is odd, use x * x^(n-1)

x = int(input("x: "))
n = int(input("n: "))
power_calculator = Power(x, n)
result = power_calculator.my_pow()
print(f"{x}^{n} = {result}")

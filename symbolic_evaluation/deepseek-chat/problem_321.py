import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is π/2
# Compute numerator (π) and denominator (2)
numerator = mp.pi
denominator = 2

# Perform division: π/2
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
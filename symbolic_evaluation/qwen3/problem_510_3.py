import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate denominator components
sqrt3 = mp.sqrt(3)          # Compute square root of 3
denominator = 3 * sqrt3     # 3 multiplied by sqrt(3)

# Calculate numerator components
numerator = 7 * mp.pi       # 7 times pi

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
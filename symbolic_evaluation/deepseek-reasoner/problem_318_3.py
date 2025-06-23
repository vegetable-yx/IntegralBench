import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 2/π using exact mathematical constants
numerator = 2
denominator = mp.pi
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
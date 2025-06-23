import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 1/e using mpmath constant
result = 1/mp.e

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
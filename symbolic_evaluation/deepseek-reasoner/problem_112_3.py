import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3 using mpmath
sqrt3 = mp.sqrt(3)

# Compute 4 divided by sqrt(3)
result = mp.mpf(4) / sqrt3

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
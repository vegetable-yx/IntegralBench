import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Directly assign the constant π from mpmath
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
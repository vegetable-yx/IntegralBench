import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Assign the constant π from mpmath
result = mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
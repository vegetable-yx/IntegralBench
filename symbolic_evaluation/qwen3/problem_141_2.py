import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sinh(1)
sinh_val = mp.sinh(1)

# Square the result to get sinh^2(1)
result = sinh_val ** 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
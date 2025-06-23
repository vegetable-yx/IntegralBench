import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Assign the exact integer value as a floating-point number
result = mp.mpf(1005)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
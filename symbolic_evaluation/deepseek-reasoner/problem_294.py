import mpmath as mp
mp.dps = 15  # Set internal precision

# Assign the exact integer value as a mpmath floating-point number
result = mp.mpf(2)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
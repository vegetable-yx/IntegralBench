import mpmath as mp
mp.dps = 15

# Assign the exact integer value to a mpmath floating-point number
result = mp.mpf(99)

# Print the result with 10 decimal places of precision
print(mp.nstr(result, n=10))
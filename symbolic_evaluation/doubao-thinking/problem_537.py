import mpmath as mp
mp.dps = 15

# Assign the exact integer value using mpmath's floating-point type
result = mp.mpf(3)

# Print the result with 10 decimal place precision
print(mp.nstr(result, n=10))
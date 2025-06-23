import mpmath as mp
mp.dps = 15

# Assign the exact integer value using mpmath floating-point type
result = mp.mpf(4)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
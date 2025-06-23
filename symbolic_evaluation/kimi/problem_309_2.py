import mpmath as mp
mp.dps = 15

# Assign the mathematical constant π directly from mpmath
result = mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
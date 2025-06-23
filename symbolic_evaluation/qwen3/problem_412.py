import mpmath as mp
mp.dps = 15

# Assign Euler's number directly from mpmath constants
result = mp.e

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
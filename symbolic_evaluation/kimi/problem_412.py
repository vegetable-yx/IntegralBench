import mpmath as mp
mp.dps = 15

# Assign Euler's number constant
result = mp.e

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
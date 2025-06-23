import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical result is exactly 0
result = mp.mpf(0)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
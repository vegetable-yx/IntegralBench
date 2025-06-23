import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical result is exactly zero
result = mp.mpf(0)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
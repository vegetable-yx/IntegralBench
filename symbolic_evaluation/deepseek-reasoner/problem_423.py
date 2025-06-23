import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical solution is a simple integer value
result = mp.mpf(99)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
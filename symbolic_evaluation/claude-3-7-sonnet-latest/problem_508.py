import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical result is a constant: 4
result = mp.mpf(4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
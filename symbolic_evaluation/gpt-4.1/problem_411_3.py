import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression simplifies to the constant 1
result = mp.mpf(1)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
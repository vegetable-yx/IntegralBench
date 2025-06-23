import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# The analytical expression simplifies to a constant integer 8
result = mp.mpf(8)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical solution is a constant integer 18
result = mp.mpf(18)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
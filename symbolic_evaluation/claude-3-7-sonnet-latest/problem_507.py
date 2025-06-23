import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# The analytical result is a constant integer value
result = mp.mpf(18)

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))
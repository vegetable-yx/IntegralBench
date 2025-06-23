import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is the constant integer 18
result = mp.mpf(18)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))
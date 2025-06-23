import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 1/2
# Compute the fraction directly
result = mp.mpf(1) / mp.mpf(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
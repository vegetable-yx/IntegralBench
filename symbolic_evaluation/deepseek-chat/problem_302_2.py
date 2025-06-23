import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute arcsin(0.25)
arcsin_val = mp.asin(0.25)

# Square the result
result = arcsin_val ** 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
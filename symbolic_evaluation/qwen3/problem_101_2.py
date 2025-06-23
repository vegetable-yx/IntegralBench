import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the value 1/4 as an mpf
x = mp.mpf(1)/4

# Calculate arcsin(1/4)
arcsin_val = mp.asin(x)

# Square the arcsine value
result = arcsin_val ** 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
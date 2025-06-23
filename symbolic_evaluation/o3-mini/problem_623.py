import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the arcsine of 1/3
asin_val = mp.asin(1 / mp.mpf(3))

# Multiply the result by pi
result = mp.pi * asin_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))
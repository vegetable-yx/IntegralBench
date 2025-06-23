import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for arcsine: 1/4
arg = mp.mpf(1) / 4

# Compute arcsin(1/4)
asin_val = mp.asin(arg)

# Cube the arcsine value
asin_cubed = asin_val ** 3

# Multiply by 1/3 to get final result
result = asin_cubed / 3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))
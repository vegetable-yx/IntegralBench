import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the arcsine of 1/3 using mp.asin
asin_val = mp.asin(1/mp.mpf(3))

# Multiply by pi to get the final result
result = mp.pi * asin_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
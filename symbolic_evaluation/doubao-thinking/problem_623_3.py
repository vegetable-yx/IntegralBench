import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute arcsin(1/3)
asin_val = mp.asin(1/3)

# Multiply by pi
result = mp.pi * asin_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
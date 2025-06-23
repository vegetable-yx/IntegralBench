import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the arcsine of 1/3
x = mp.mpf('1/3')  # Represent 1/3 exactly
asin_val = mp.asin(x)  # Compute arcsin(1/3)

# Multiply the result by pi
result = mp.pi * asin_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Compute the arcsine of 1/3 using mpmath's asin function
arcsine_value = mp.asin(mp.mpf(1)/3)

# Multiply the result by pi
result = mp.pi * arcsine_value

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))
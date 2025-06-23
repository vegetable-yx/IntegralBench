import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the fraction 80/23
fraction_value = mp.mpf(80) / mp.mpf(23)

# Compute the natural logarithm of the fraction
result = mp.log(fraction_value)

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))
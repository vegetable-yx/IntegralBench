import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the fraction (1 + sqrt(2)) / 2
fraction = (1 + sqrt2) / 2

# Compute the natural logarithm of the fraction
log_value = mp.log(fraction)

# Multiply by pi to get the final result
result = mp.pi * log_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
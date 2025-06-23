import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the numerator: 3 + 2*sqrt(2)
numerator = 3 + 2 * sqrt2

# Form the fraction: (3 + 2*sqrt(2)) / 3
fraction = numerator / 3

# Compute the natural logarithm of the fraction
log_val = mp.log(fraction)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
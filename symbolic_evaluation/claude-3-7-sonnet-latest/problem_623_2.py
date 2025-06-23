import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the square root of 8
sqrt8 = mp.sqrt(8)

# Compute numerator: 3 + sqrt(8)
numerator = 3 + sqrt8

# Form the fraction: (3 + sqrt(8)) / 6
fraction = numerator / 6

# Take the natural logarithm of the fraction
log_val = mp.log(fraction)

# Multiply by pi to get the final result
result = mp.pi * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
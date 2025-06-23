import mpmath as mp

# Set decimal places for internal precision to 15
mp.dps = 15

# Calculate the numerator: 1 + sqrt(2)
numerator = 1 + mp.sqrt(2)

# Calculate the fraction: (1 + sqrt(2)) / 2
fraction = numerator / 2

# Compute the natural logarithm of the fraction
log_value = mp.log(fraction)

# Multiply by pi to get the final result
result = mp.pi * log_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
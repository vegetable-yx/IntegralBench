import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the numerator: 1 + square root of 2
numerator = 1 + mp.sqrt(2)

# Compute the denominator
denominator = 2

# Form the fraction: (1 + sqrt(2)) / 2
fraction = numerator / denominator

# Compute the natural logarithm of the fraction
log_value = mp.log(fraction)

# Multiply by pi to get the final result
result = mp.pi * log_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
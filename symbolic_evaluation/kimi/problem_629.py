import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator
numerator = mp.mpf(253)

# Calculate the denominator
denominator = mp.mpf(3)

# Compute the fraction 253/3
fraction = numerator / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
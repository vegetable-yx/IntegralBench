import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define numerator and denominator
numerator = 1
denominator = 5

# Compute the result of the fraction 1/5
result = mp.mpf(numerator) / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = 253
denominator = 3

# Compute the fraction 253/3 using mpmath
fraction = mp.mpf(numerator) / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
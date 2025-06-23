import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator and denominator
numerator = 2
denominator = mp.pi

# Compute the fraction 2/π
fraction = mp.fdiv(numerator, denominator)

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
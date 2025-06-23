import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute numerator (2 + sqrt(3))
numerator = 2 + sqrt3

# Compute denominator (sqrt(3))
denominator = sqrt3

# Calculate the fraction (2 + sqrt(3))/sqrt(3)
fraction = numerator / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π
pi_val = mp.pi

# Compute π squared
pi_sq = pi_val ** 2

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate numerator: 3 * π² * ln(2)
numerator = 3 * pi_sq * ln2

# Denominator is 32
denominator = 32

# Compute the fraction: numerator / denominator
fraction = numerator / denominator

# Apply negative sign
result = -fraction

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp
mp.dps = 15

# Calculate numerator: 1
numerator = 1

# Calculate denominator: 2
denominator = 2

# Compute the fraction: 1/2
fraction = numerator / denominator

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Multiply the fraction by the natural logarithm
result = fraction * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π² and ln2
product = pi_squared * ln2

# Divide by 72 to get final result
result = product / 72

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
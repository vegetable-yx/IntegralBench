import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 4
pi_sq_over_4 = pi_squared / 4

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply the two components
result = pi_sq_over_4 * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
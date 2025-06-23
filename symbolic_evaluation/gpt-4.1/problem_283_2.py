import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide pi squared by 8
pi_sq_over_8 = pi_squared / 8

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Multiply the two parts to get the result
result = pi_sq_over_8 * ln_3

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))
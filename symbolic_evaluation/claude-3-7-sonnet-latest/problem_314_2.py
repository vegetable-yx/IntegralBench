import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi**2

# Divide by 6
pi_squared_over_6 = pi_squared / 6

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply to get the final result
result = pi_squared_over_6 * ln3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
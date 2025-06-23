import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Multiply the components to get final result
result = pi_squared * ln_2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
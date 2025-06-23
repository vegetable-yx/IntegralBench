import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply π and ln(3)
numerator = pi_value * ln3

# Divide by 8 to get final result
result = numerator / 8

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
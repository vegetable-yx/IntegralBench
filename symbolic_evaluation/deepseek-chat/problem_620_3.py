import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute π using mpmath constant
pi_value = mp.pi

# Compute natural logarithm of 2
ln2_value = mp.log(2)

# Multiply π and ln(2)
numerator = pi_value * ln2_value

# Divide the result by 8
result = numerator / 8

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))
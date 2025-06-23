import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2_value = mp.log(2)

# Multiply π and ln(2) to get final result
result = pi_value * ln2_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
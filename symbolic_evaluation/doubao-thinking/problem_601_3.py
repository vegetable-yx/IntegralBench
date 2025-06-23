import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath constant
pi_value = mp.pi

# Calculate natural logarithm of 2
ln2_value = mp.log(2)

# Multiply π by ln(2)
result = pi_value * ln2_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply π and ln(2) to get the final result
result = pi_val * ln2_val

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
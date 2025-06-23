import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply π and ln(2)
numerator = pi_val * ln2_val

# Divide by 2 to get the final result
result = numerator / 2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))
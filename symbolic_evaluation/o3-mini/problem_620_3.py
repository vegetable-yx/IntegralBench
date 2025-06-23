import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply π and ln(2)
product = pi_val * ln2_val

# Divide by 8 to get the final result
result = product / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
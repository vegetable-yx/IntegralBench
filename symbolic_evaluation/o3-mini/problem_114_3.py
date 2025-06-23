import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
product = pi_val * ln2_val

# Compute the final result: -(product)/2
result = -product / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
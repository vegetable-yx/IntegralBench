import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute π using mpmath's constant
pi_val = mp.pi

# Compute natural logarithm of 2
ln2_val = mp.log(2)

# Multiply π and ln(2)
product = pi_val * ln2_val

# Calculate final result: -(π * ln2)/4
result = -product / 4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
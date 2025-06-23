import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 1.5
ln_val = mp.log(1.5)

# Multiply by pi
pi_ln = mp.pi * ln_val

# Divide by 4 to get the final result
result = pi_ln / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
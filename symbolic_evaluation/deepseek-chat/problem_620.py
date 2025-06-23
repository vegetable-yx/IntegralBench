import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply π by ln(2)
pi_times_ln2 = pi_val * ln2_val

# Divide by 8 to get final result
result = pi_times_ln2 / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate ln(2)
ln2 = mp.log(2)

# Multiply by pi
pi_times_ln2 = mp.pi * ln2

# Divide by 4
divided_by_four = pi_times_ln2 / 4

# Apply the negative sign
result = -divided_by_four

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
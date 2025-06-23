import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi: pi * ln(2)
pi_times_ln2 = mp.pi * ln2

# Multiply by 2: 2 * pi * ln(2)
result = 2 * pi_times_ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
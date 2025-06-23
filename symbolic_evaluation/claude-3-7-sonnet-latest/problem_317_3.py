import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi
pi_times_ln2 = mp.pi * ln2

# Multiply by 2 to get the final result
result = 2 * pi_times_ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
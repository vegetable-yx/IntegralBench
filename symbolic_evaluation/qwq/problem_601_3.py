import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Multiply by pi to get the final result
pi_times_ln2 = mp.pi * ln_2

# Print the result with exactly 10 decimal places
print(mp.nstr(pi_times_ln2, n=10))
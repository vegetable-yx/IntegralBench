import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by the logarithm result using exact mathematical constant pi
pi_times_ln2 = mp.pi * ln2

# Print the final result with 10 decimal places precision
print(mp.nstr(pi_times_ln2, n=10))
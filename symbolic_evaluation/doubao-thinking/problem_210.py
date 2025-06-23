import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Compute π^3 divided by 8
pi_cubed_over_8 = (pi ** 3) / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute π multiplied by ln(2)
pi_times_ln2 = pi * ln2

# Sum both components for final result
result = pi_cubed_over_8 + pi_times_ln2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
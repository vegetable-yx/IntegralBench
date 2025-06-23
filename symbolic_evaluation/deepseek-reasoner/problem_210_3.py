import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π^3 term
pi = mp.pi
pi_cubed = mp.power(pi, 3)

# Divide π^3 by 8
pi_cubed_over_8 = pi_cubed / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply π with ln2
pi_ln2 = pi * ln2

# Combine terms for final result
result = pi_cubed_over_8 - pi_ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
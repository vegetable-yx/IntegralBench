import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Compute (1 - ln2)
one_minus_ln2 = 1 - ln_2

# Multiply components together
result = 2 * sqrt_pi * one_minus_ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
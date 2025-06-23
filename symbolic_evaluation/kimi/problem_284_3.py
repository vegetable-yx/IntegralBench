import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply the components to get final result
result = pi_over_2 * ln2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate (1/2) * ln2
half_ln2 = 0.5 * ln2

# Compute the final result: 1 - pi/4 - (1/2)*ln(2)
result = 1 - pi_over_4 - half_ln2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
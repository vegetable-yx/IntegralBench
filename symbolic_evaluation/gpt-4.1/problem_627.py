import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate (1/2) * ln(2)
half_ln2 = 0.5 * mp.log(2)

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Combine the terms: (1/2)ln(2) + 1 - pi/4
result = half_ln2 + 1 - pi_over_4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
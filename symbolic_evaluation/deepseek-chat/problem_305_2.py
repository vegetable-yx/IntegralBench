import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate pi/8
pi_over_8 = mp.pi / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate ln(2)/4
ln2_over_4 = ln2 / 4

# Combine the results: pi/8 - ln(2)/4
result = pi_over_8 - ln2_over_4

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))
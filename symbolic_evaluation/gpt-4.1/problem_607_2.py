import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Multiply to get the result: (pi/4) * ln(2)
result = pi_over_4 * ln_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
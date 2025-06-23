import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute ln^2(2)
ln2_squared = ln2 ** 2

# Compute pi cubed
pi_cubed = pi_val ** 3

# First term: pi^3 / 48
term1 = pi_cubed / 48

# Second term: (pi / 4) * ln^2(2)
term2 = (pi_val / 4) * ln2_squared

# Final result: term1 - term2
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
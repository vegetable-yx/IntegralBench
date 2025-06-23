import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Compute natural logarithm of 2
ln2_val = mp.log(2)

# First term: 8 * pi * ln(2)
term1 = 8 * pi_val * ln2_val

# Compute pi cubed
pi_cubed = pi_val**3

# Second term: pi^3 / 3
term2 = pi_cubed / 3

# Final result: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
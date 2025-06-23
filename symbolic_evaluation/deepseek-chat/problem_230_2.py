import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π
pi_val = mp.pi

# Compute natural logarithm of 2
ln2_val = mp.log(2)

# Calculate π^3
pi_cubed = pi_val**3

# First term: π^3 / 192
term1 = pi_cubed / 192

# Calculate (ln(2))^2
ln2_squared = ln2_val**2

# Second term: (π / 16) * (ln(2))^2
term2 = (pi_val / 16) * ln2_squared

# Final result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
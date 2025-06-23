import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Calculate ln(2) (natural logarithm of 2)
ln2_val = mp.log(2)

# Compute π^3
pi_cubed = pi_val ** 3

# First term: π^3 / 12
term1 = pi_cubed / 12

# Compute (ln(2))^2
ln2_squared = ln2_val ** 2

# Second term: π * (ln(2))^2 / 2
term2 = (pi_val * ln2_squared) / 2

# Final result: term1 - term2
result = term1 - term2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Calculate ln(2)
ln2_val = mp.log(2)

# Compute ln(2) squared
ln2_sq = ln2_val ** 2

# Calculate first term: π^3 / 24
term1 = (pi_val ** 3) / 24

# Calculate second term: (π / 2) * (ln(2))^2
term2 = (pi_val / 2) * ln2_sq

# Sum both terms to get the result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
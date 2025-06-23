import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Compute π²/4
pi_sq_over_4 = mp.pi**2 / 4

# Compute -2π ln(2)
term2 = -2 * mp.pi * ln2

# Compute 4 (ln(2))²
term3 = 4 * (ln2)**2

# Sum all terms
result = pi_sq_over_4 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
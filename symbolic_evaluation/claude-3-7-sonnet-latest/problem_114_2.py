import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi)
pi_val = mp.pi

# Compute ln(2)
ln2_val = mp.log(2)

# Calculate first term: (π/2) * ln(2)
term1 = (pi_val / 2) * ln2_val

# Calculate second term: π/4
term2 = pi_val / 4

# Subtract the second term from the first
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
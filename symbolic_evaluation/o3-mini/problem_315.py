import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ln(2) to high precision
ln2 = mp.log(2)

# Calculate the cube of ln(2)
ln2_cubed = ln2 ** 3

# First term: (1/6) * (ln(2))^3
term1 = (1/6) * ln2_cubed

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Second term: (7/8) * zeta(3)
term2 = (7/8) * zeta3

# Combine terms: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
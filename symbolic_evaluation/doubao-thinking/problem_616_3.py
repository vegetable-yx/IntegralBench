import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^2 term
pi_squared = mp.pi ** 2
term1 = pi_squared / 48

# Calculate (ln 2)^2 term
ln2 = mp.log(2)
ln2_squared = ln2 ** 2
term2 = ln2_squared / 2

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
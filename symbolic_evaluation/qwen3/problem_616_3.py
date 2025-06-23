import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate (ln 2)^2 component
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Compute first term: (ln^2 2)/4
term1 = ln2_squared / 4

# Calculate π^2 component
pi_squared = mp.pi ** 2

# Compute second term: π²/48
term2 = pi_squared / 48

# Sum both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
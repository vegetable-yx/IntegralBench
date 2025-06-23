import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π³ term divided by 16
pi_cubed = mp.pi ** 3
pi_term = pi_cubed / 16

# Calculate (ln 2) squared term
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Calculate π*(ln2)^2 divided by 2
pi_ln2_term = (mp.pi * ln2_squared) / 2

# Combine both terms for final result
result = pi_term + pi_ln2_term

print(mp.nstr(result, n=10))
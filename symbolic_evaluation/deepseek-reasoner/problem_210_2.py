import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate π²/16 term
pi_sq_over_16 = mp.pi**2 / 16

# Calculate (π * ln(2))/4 term
pi_ln2_over_4 = (mp.pi * mp.log(2)) / 4

# Get Catalan's constant
catalan = mp.catalan

# Combine all terms
result = pi_sq_over_16 + pi_ln2_over_4 - catalan

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
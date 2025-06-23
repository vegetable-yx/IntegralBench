import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute π² * ln(2)
pi_sq_ln2 = pi_sq * ln2

# Divide by 8 and apply negative sign
result = -pi_sq_ln2 / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))
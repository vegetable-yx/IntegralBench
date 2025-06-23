import mpmath as mp
mp.dps = 15

from mpmath import mp
mp.dps = 15

# Compute Beta(1/4, 1/2)
B = mp.beta(mp.mpf('1/4'), mp.mpf('1/2'))

# Compute ln(2) and pi/2 terms
ln2 = mp.log(2)
pi_half = mp.pi / 2

# Calculate the first part of the expression
beta_term = B * (ln2 + pi_half)

# Note: I_2 is undefined in the given expression. Assuming I_2 = 0 for calculation
# This assumption may not reflect the correct mathematical result
I2 = mp.mpf(0)

# Combine terms and compute final result
result = 2 * (beta_term + I2)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))
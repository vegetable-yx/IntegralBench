import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate intermediate values step by step
# Compute the value of the natural logarithm of 2
ln2 = mp.log(2)

# Compute the value of the Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute the constant term involving pi
pi_term = 3 * mp.pi**2 * ln2 / 16

# Compute the constant term involving zeta(3)
zeta3_term = 7 * zeta3 / 8

# Combine the terms to get the final result
result = pi_term + zeta3_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
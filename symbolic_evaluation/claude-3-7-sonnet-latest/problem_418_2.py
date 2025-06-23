import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# Compute the Riemann zeta function value at 2: ζ(2) = π²/6
zeta_2 = pi_squared / 6

# Subtract 1 to get the final result
result = zeta_2 - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
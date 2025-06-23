import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the value of π
pi_val = mp.pi

# Compute ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Calculate the result: (π * ζ(3)) / 2
result = (pi_val * zeta_3) / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
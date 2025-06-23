import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate results
mp.dps = 15

# Compute ζ(3) using the Riemann zeta function
zeta_3 = mp.zeta(3)

# Multiply by the fraction 7/8
result = (7 / 8) * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
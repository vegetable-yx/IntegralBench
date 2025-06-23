import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ζ(3) - Apéry's constant using Riemann zeta function
zeta3 = mp.zeta(3)

# Calculate the fraction 7/8 with high precision
fraction = mp.mpf(7) / mp.mpf(8)

# Multiply to get final result: (7/8)*ζ(3)
result = fraction * zeta3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
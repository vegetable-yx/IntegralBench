import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^3 term divided by 48
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 48

# Calculate ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Calculate π*ζ(3) term divided by 8
term2 = (mp.pi * zeta_3) / 8

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
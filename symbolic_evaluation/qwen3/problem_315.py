import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Compute the final result by negating ζ(3)
result = -zeta_3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
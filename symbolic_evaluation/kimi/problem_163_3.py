import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision

# Compute the Riemann zeta function at s=2
result = mp.zeta(2)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))
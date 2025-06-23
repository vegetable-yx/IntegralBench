import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Riemann zeta function at s=3
result = mp.zeta(3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate complete elliptic integrals of first and second kind at k=1/2
K_value = mp.ellipk(1/2)
E_value = mp.ellipe(1/2)

# Compute the final result using the analytical expression
result = (3/2) * K_value - 2 * E_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
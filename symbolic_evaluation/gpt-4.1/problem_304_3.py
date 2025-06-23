import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the complete elliptic integral of the second kind E(1/2)
E_val = mp.ellipe(0.5)

# Compute the complete elliptic integral of the first kind K(1/2)
K_val = mp.ellipk(0.5)

# Calculate intermediate expression: 4 * E(1/2) - K(1/2)
temp = 4 * E_val - K_val

# Final result: (4 * E(1/2) - K(1/2)) / 6
result = temp / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
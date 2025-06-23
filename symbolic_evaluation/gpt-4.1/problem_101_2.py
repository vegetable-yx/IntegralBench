import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate E(0.25) - complete elliptic integral of the second kind
E_val = mp.ellipe(0.25)

# Calculate K(0.25) - complete elliptic integral of the first kind
K_val = mp.ellipk(0.25)

# Compute the expression: 2 * E(0.25) - (15/8) * K(0.25)
result = 2 * E_val - (15/8) * K_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
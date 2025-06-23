import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate K(0.25) - complete elliptic integral of the first kind
k_val = mp.ellipk(0.25)

# Calculate E(0.25) - complete elliptic integral of the second kind
e_val = mp.ellipe(0.25)

# Compute term1: -15.75 * K(0.25)
term1 = -15.75 * k_val

# Compute term2: 16 * E(0.25)
term2 = 16 * e_val

# Sum the terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the first kind K(1/2)
k_half = mp.ellipk(0.5)

# Compute the complete elliptic integral of the second kind E(1/2)
e_half = mp.ellipe(0.5)

# Calculate the expression: 8 * [E(1/2) - (3/4) * K(1/2)]
result = 8 * (e_half - (3/4) * k_half)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the argument for the elliptic integral
phi = mp.asin(1/4)

# Compute the incomplete elliptic integral of the second kind E(φ, m=4)
elliptic_e = mp.ellipe(phi, 4)

# Multiply by 1/2 to get the final result
result = 0.5 * elliptic_e

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
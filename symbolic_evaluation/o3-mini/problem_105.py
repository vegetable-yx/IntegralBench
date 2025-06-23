import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the elliptic integral: phi = pi/6
phi = mp.pi / 6

# Compute the incomplete elliptic integral of the second kind: E(phi, m) with m=2
elliptic_value = mp.ellipe(phi, 2)

# Multiply the result by 2
result = 2 * elliptic_value

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))
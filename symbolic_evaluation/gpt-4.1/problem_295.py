import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the modulus k = 1/sqrt(2)
k = 1 / mp.sqrt(2)

# Compute complete elliptic integral of the first kind, K(k)
K_val = mp.ellipk(k)

# Compute complete elliptic integral of the second kind, E(k)
E_val = mp.ellipe(k)

# Square both elliptic integral values
K_sq = K_val**2
E_sq = E_val**2

# Compute the expression: 2 * [E(k)^2 - K(k)^2]
result = 2 * (E_sq - K_sq)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
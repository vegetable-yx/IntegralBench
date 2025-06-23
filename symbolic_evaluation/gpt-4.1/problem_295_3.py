import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the modulus k = 1/sqrt(2)
k = mp.mpf(1) / mp.sqrt(2)

# Compute the complete elliptic integral of the second kind E(k)
E_val = mp.ellipe(k)

# Compute the complete elliptic integral of the first kind K(k)
K_val = mp.ellipk(k)

# Square the elliptic integral values
E_sq = E_val ** 2
K_sq = K_val ** 2

# Combine the terms: 2*(E(k))^2 - (K(k))^2
result = 2 * E_sq - K_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
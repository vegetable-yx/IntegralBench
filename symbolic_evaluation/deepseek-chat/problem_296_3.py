import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the argument for the elliptic functions
k_val = 1 / mp.sqrt(2)

# Compute complete elliptic integral of the first kind K(k)
K = mp.ellipk(k_val)

# Compute complete elliptic integral of the second kind E(k)
E = mp.ellipe(k_val)

# Square each elliptic integral value
K_sq = K**2
E_sq = E**2

# Sum the squared terms
sum_sq = E_sq + K_sq

# Multiply by the constant factor 4/15
result = (4 / 15) * sum_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
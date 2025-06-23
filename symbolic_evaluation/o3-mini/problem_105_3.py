import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the argument for the elliptic integrals
k_value = mp.mpf(1)/4

# Compute the complete elliptic integral of the second kind E(k)
E_value = mp.ellipe(k_value)

# Compute the complete elliptic integral of the first kind K(k)
K_value = mp.ellipk(k_value)

# Calculate the first term: 4 * E(1/4)
term1 = 4 * E_value

# Calculate the second term: 3 * K(1/4)
term2 = 3 * K_value

# Combine the terms: 4E(1/4) - 3K(1/4)
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
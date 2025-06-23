import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define the parameter m = k^2, where k = 1/4
m = mp.mpf(1)/16

# Compute complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m)

# Compute complete elliptic integral of the second kind E(m)
E_val = mp.ellipe(m)

# Calculate the expression: 2*E(1/4) - (15/8)*K(1/4)
term1 = 2 * E_val
term2 = (mp.mpf(15)/8) * K_val
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
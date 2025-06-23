import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter m = (1/4)^2 = 1/16 for elliptic integrals
m = mp.mpf(1)/16

# Compute complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m)

# Compute complete elliptic integral of the second kind E(m)
E_val = mp.ellipe(m)

# Calculate the integral result using the derived expression:
# result = 4 * E(m) - (15/4) * K(m)
result = 4 * E_val - (15/4) * K_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
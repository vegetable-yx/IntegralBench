import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the angle: arcsin(1/4)
phi = mp.asin(mp.mpf(1)/4)

# The modulus k is 4, so compute parameter m = k^2 = 16
m = 4**2

# Evaluate incomplete elliptic integral of the second kind E(phi, m)
E_val = mp.ellipe(phi, m)

# Multiply by 1/2 to get final result
result = E_val / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
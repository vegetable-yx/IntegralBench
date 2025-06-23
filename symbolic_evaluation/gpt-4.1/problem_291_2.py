import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modulus k = 1/2
k = mp.mpf('0.5')

# Convert modulus to parameter m = k^2 for elliptic integral
m = k**2

# Compute complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m)

# Compute the constant factor pi/2
pi_over_2 = mp.pi / 2

# Multiply to get final result
result = pi_over_2 * K_val

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))
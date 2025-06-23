import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modulus k = 1/sqrt(2)
k = 1 / mp.sqrt(2)

# Compute the parameter m = k^2 for the elliptic integral
m = k**2

# Evaluate the complete elliptic integral of the second kind E(m)
E_val = mp.ellipe(m)

# Multiply by 2 to get the final result
result = 2 * E_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
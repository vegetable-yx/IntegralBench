import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter m = k^2 where k = 1/2
m = mp.mpf('0.25')

# Compute the complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m)

# Compute the complete elliptic integral of the second kind E(m)
E_val = mp.ellipe(m)

# Calculate the difference: K(m) - E(m)
diff = K_val - E_val

# Multiply the difference by 2 to get the final result
result = 2 * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
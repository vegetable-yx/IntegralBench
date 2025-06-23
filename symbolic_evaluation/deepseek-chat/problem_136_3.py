import mpmath as mp

# Set the internal decimal precision to 15
mp.dps = 15

# Compute the complete elliptic integral of the second kind with parameter m = -1
E_value = mp.ellipe(-1)

# Multiply by sqrt(2)
result = mp.sqrt(2) * E_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
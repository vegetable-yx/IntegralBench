import mpmath as mp

# Set the precision to 15 decimal places
mp.dps = 15

# Calculate k = 1 / sqrt(2)
k_value = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind at k
K_value = mp.ellipk(k_value)

# Square the result
K_squared = K_value**2

# Multiply by 4
result = 4 * K_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
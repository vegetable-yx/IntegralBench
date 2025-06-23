import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the elliptic integral: 1/sqrt(2)
k_value = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind K(k)
K_value = mp.ellipk(k_value)

# Multiply by 2*pi to get the final result
result = 2 * mp.pi * K_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
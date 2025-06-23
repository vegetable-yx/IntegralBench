import mpmath as mp

# Set internal decimal places for calculations
mp.dps = 15

# Compute the argument for the elliptic integral
k_value = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind
K_value = mp.ellipk(k_value)

# Multiply by 4 to get the final result
result = 4 * K_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))
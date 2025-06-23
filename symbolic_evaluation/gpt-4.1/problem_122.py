import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate the argument for the elliptic integral
k_value = mp.sqrt(15) / 4

# Compute the complete elliptic integral of the first kind K(k)
K_val = mp.ellipk(k_value)

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * K_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
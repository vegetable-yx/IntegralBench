import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the elliptic function: k = sqrt(3)/2
k_value = mp.sqrt(3) / 2

# Compute the complete elliptic integral of the first kind: K(k)
ellipk_value = mp.ellipk(k_value)

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * ellipk_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
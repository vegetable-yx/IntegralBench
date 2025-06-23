import mpmath as mp
mp.dps = 15

# Calculate the complete elliptic integral of the second kind at m=-1
E_value = mp.ellipe(-1)

# Calculate the square root of 2
sqrt_two = mp.sqrt(2)

# Combine components for final result
result = 2 * sqrt_two * E_value

print(mp.nstr(result, n=10))
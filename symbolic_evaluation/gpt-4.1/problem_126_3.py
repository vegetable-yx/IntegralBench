import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k=0.5
# K(k) = ellipk(k) in mpmath
k_value = 0.5
K = mp.ellipk(k_value)

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * K

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
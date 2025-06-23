import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k = 1/2
k_value = mp.mpf(1)/2
K_half = mp.ellipk(k_value)

# Multiply the elliptic integral by 2
two_K_half = 2 * K_half

# Subtract pi from the result
result = two_K_half - mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
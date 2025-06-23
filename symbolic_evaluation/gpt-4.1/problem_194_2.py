import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k=1/2
k_val = mp.mpf(1)/2  # Argument for elliptic integral
K_half = mp.ellipk(k_val)  # K(1/2)

# Multiply by 2
two_K = 2 * K_half

# Subtract π
result = two_K - mp.pi

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
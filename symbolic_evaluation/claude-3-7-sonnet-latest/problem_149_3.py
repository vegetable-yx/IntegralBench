import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k = 1/2
k_val = mp.mpf(1)/mp.mpf(2)
K_val = mp.ellipk(k_val)

# Square the result and multiply by 4
result = 4 * (K_val ** 2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k = 1/2
k_val = mp.mpf('0.5')
K_val = mp.ellipk(k_val)

# Square the result
K_squared = K_val ** 2

# Multiply by 2
result = 2 * K_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
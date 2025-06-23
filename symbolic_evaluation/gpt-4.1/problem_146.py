import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modulus squared (m) for the elliptic integral: m = (1/sqrt(2))^2 = 0.5
m = mp.mpf('0.5')

# Compute the complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m)

# Square the elliptic integral value
K_sq = K_val ** 2

# Multiply by 2*sqrt(2) to get the final result
result = 2 * mp.sqrt(2) * K_sq

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
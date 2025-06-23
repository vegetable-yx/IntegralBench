import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the elliptic integral: 1/sqrt(2)
arg = 1 / mp.sqrt(2)

# Compute the complete elliptic integral of the first kind K(k) at k = 1/sqrt(2)
K_val = mp.ellipk(arg)

# Square the result of the elliptic integral
K_sq = K_val ** 2

# Multiply by pi/2
result = (mp.pi / 2) * K_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
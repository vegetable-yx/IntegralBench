import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the complete elliptic integral of the first kind at k=0.5
k_value = 0.5
K = mp.ellipk(k_value)  # K(k) = complete elliptic integral of the first kind

# Compute the expression: (π/8) * K(0.5)
pi = mp.pi
result = (pi / 8) * K

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
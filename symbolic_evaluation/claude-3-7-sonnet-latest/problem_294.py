import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modulus squared m = k^2 for k=0.5
m_val = 0.5**2  # m_val = 0.25

# Calculate the complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m_val)

# Square the elliptic integral value
K_sq = K_val**2

# Multiply by 4/3 to get the final result
result = (4/3) * K_sq

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
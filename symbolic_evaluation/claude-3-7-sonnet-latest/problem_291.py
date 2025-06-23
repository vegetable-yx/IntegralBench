import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the modulus squared m = k^2 where k = sqrt(3)/2
m_val = (mp.sqrt(3)/2)**2  # m = (sqrt(3)/2)^2 = 3/4

# Compute complete elliptic integral of the first kind K(m)
K_val = mp.ellipk(m_val)

# Multiply by pi to get the final result
result = mp.pi * K_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
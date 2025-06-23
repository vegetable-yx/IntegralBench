import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate complete elliptic integrals
E_half = mp.ellipe(0.5)  # E(1/2) - complete elliptic integral of the second kind
K_half = mp.ellipk(0.5)   # K(1/2) - complete elliptic integral of the first kind

# Compute each term of the expression separately
term1 = (11.0/2.0) * E_half  # (11/2)E(1/2)
term2 = (3.0/2.0) * K_half   # (3/2)K(1/2)

# Combine terms and subtract pi
result = term1 - term2 - mp.pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
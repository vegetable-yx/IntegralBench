import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute the complete elliptic integral parameter
m = mp.mpf(1)/2

# Calculate complete elliptic integrals of first and second kind
K = mp.ellipk(m)  # First kind
E = mp.ellipe(m)  # Second kind

# Compute D-function value using relationship D(m) = (K(m) - E(m))/m
D_value = (K - E) / m

# Calculate final result using π/2 - 2*D(1/2)
result = mp.pi/2 - 2 * D_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
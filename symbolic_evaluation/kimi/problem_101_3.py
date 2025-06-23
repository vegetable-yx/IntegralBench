import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Define the parameter k squared (k^2 = (0.25)^2 = 0.0625)
k_squared = mp.mpf('0.0625')

# Compute complete elliptic integrals of first and second kinds
K = mp.ellipk(k_squared)
E = mp.ellipe(k_squared)

# Calculate components of the final result using derived formula
term1 = 16 * E
term2 = 15 * K
combined = term1 - term2

# Multiply by constant factor 0.125 to get final result
result = mp.fmul(combined, mp.mpf('0.125'))

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))
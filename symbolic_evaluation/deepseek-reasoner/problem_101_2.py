import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Compute complete elliptic integrals of first and second kind
E_val = mp.ellipe(0.25)  # E(1/4)
K_val = mp.ellipk(0.25)  # K(1/4)

# Calculate the bracketed expression components
term1 = E_val
term2 = (15/16) * K_val

# Combine terms and multiply by 2
combined_term = term1 - term2
result = 2 * combined_term

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))
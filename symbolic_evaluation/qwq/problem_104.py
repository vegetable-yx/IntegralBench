import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute complete elliptic integrals of first and second kind
K_val = mp.ellipk(mp.mpf('0.25'))  # K(1/4)
E_val = mp.ellipe(mp.mpf('0.25'))  # E(1/4)

# Calculate the difference between K and E values
diff_KE = K_val - E_val

# Multiply by 1/4 coefficient
term = diff_KE * mp.mpf('0.25')

# Compute π/8 component
pi_term = mp.pi / 8

# Combine components for final result
result = pi_term - term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
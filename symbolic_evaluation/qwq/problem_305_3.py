import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate the modulus parameter
k = 1 / mp.sqrt(5)

# Compute complete elliptic integrals of first and second kinds
F_val = mp.ellipk(k)   # K(k) = F(π/2, k)
E_val = mp.ellipe(k)   # E(k) = E(π/2, k)

# Calculate the difference between the elliptic integrals
diff = F_val - E_val

# Compute the constant factor sqrt(5)/2
sqrt5_over_2 = mp.sqrt(5) / 2

# Calculate final result
result = sqrt5_over_2 * diff

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))
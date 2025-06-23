import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute π using mpmath's constant
pi_val = mp.pi

# Calculate the modified Bessel function of first kind I_1(6)
bessel_i1 = mp.besseli(1, 6)

# Compute the final result (π/3) * I_1(6)
result = (pi_val * bessel_i1) / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))
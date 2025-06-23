import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate J_1(2) using Bessel function of the first kind
bessel_term = mp.besselj(1, 2)

# Compute 1 minus the Bessel function value
one_minus_bessel = 1 - bessel_term

# Multiply by 1/4 to get the final result
result = one_minus_bessel * mp.mpf(1)/4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))
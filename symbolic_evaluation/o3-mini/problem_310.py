import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute exponential integrals
ei_neg1 = mp.ei(-1)  # Exponential integral Ei(-1)
ei_pos1 = mp.ei(1)   # Exponential integral Ei(1)

# Compute imaginary error function
erfi_1 = mp.erfi(1)  # Imaginary error function erfi(1)

# Compute constants
e = mp.e
sqrt_pi = mp.sqrt(mp.pi)

# Calculate individual terms
term1 = e * ei_neg1         # e * Ei(-1)
term2 = (1/e) * ei_pos1     # e^{-1} * Ei(1)
term3 = sqrt_pi * erfi_1    # sqrt(pi) * erfi(1)

# Combine terms and multiply by 1/2
combined = term1 - term2 + term3
result = 0.5 * combined

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate common components
sqrt3 = mp.sqrt(3)  # Square root of 3
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi

# Compute error function terms
erf_term = 5 * mp.exp(3) * mp.erf(sqrt3)  # 5e^3 * erf(sqrt(3))
erfi_term = 7 * mp.exp(-3) * mp.erfi(sqrt3)  # 7e^-3 * erfi(sqrt(3))

# Combine terms and multiply by sqrt(pi)/8
total = erf_term + erfi_term
result = (sqrt_pi / 8) * total

# Print result with 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the value of 'a' (example value, can be adjusted)
a_val = 1.0
a = mp.mpf(a_val)

# Compute common expressions
z = a**2 / 4  # Argument for hypergeometric functions
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi

# Calculate gamma function values
gamma_5_4 = mp.gamma(mp.mpf('1.25'))  # Γ(5/4)
gamma_3_4 = mp.gamma(mp.mpf('0.75'))  # Γ(3/4)
gamma_7_4 = mp.gamma(mp.mpf('1.75'))  # Γ(7/4)

# Compute the first term: [√π * a * Γ(5/4) / (4 * Γ(3/4))] * ₁F₂(1/2; 1, 5/4; z)
coeff1 = (sqrt_pi * a * gamma_5_4) / (4 * gamma_3_4)
hyper1 = mp.hyp1f2(mp.mpf('0.5'), 1, mp.mpf('1.25'), z)  # ₁F₂(1/2; 1, 5/4; z)
term1 = coeff1 * hyper1

# Compute the second term: [√π * a² * Γ(3/4) / (8 * Γ(7/4))] * ₁F₂(1; 3/2, 7/4; z)
coeff2 = (sqrt_pi * a**2 * gamma_3_4) / (8 * gamma_7_4)
hyper2 = mp.hyp1f2(1, mp.mpf('1.5'), mp.mpf('1.75'), z)  # ₁F₂(1; 3/2, 7/4; z)
term2 = coeff2 * hyper2

# Combine terms for final result
result = term1 - term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (user can modify these values)
a = 1.0
b = 1.0

# Calculate constant factor: 8 * sqrt(pi) / 3
const_factor = 8 * mp.sqrt(mp.pi) / 3

# Calculate a^{1/4}
a_quart = a ** 0.25

# Calculate 1 / sqrt(b)
b_sqrt_inv = 1 / mp.sqrt(b)

# Combine variable-dependent terms: (a^{1/4}) / sqrt(b)
ab_term = a_quart * b_sqrt_inv

# Calculate argument for cosh: (a*b)/2
cosh_arg = (a * b) / 2.0

# Compute hyperbolic cosine term
cosh_term = mp.cosh(cosh_arg)

# Combine all components: [8*sqrt(pi)/3] * [a^{1/4}/sqrt(b)] * cosh(ab/2)
result = const_factor * ab_term * cosh_term

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))
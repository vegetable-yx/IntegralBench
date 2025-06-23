import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define t1 = ln(1 + sqrt(2))
t1 = mp.log(1 + mp.sqrt(2))

# Precompute exponential terms for efficiency
exp_t1 = mp.exp(t1)
exp_3t1 = mp.exp(3 * t1)
exp_neg_t1 = mp.exp(-t1)
exp_neg_3t1 = mp.exp(-3 * t1)

# Precompute hyperbolic functions
sinh_t1 = mp.sinh(t1)
cosh_t1 = mp.cosh(t1)
sinh_3t1 = mp.sinh(3 * t1)

# Compute the constant term A = π/16
A = mp.pi / 16

# Compute the expression inside the brackets for term B
term1 = (mp.mpf(1)/12) * exp_3t1 * (t1 - mp.mpf(1)/3)
term2 = -(mp.mpf(1)/4) * (t1 + 1) * exp_neg_t1
term3 = -(mp.mpf(1)/4) * exp_t1 * (t1 - 1)
term4 = -(mp.mpf(1)/12) * exp_neg_3t1 * (t1 + mp.mpf(1)/3)
term5 = t1 * cosh_t1
term6 = -sinh_t1
term7 = mp.mpf(1)/18

inside_brackets = term1 + term2 + term3 + term4 + term5 + term6 + term7
B = (mp.mpf(1)/4) * inside_brackets

# Compute additional hyperbolic terms
C = -(mp.mpf(1)/16) * sinh_3t1
D = -(mp.mpf(1)/16) * sinh_t1

# Compute the polynomial-hyperbolic term
E_inside = (t1**2 * sinh_t1) - (2 * t1 * cosh_t1) + (2 * sinh_t1)
E = -(mp.mpf(1)/4) * E_inside

# Sum all components
result = A + B + C + D + E

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))
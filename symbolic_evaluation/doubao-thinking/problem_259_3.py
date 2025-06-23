import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the point of evaluation
x = mp.mpf(1.0)

# Compute Bessel functions at x=1
J0_1 = mp.besselj(0, x)
J1_1 = mp.besselj(1, x)

# Compute Struve functions at x=1
H0_1 = mp.struveh(0, x)
H1_1 = mp.struveh(1, x)

# Calculate the definite integral of J0(t) from 0 to 1 using known analytical form:
# ∫_0^1 J0(t) dt = (π/2) * [J0(1)*H1(1) - J1(1)*H0(1)]
integral_val = (mp.pi / 2) * (J0_1 * H1_1 - J1_1 * H0_1)

# Compute the inner expression: (integral - J0(1))
inner_expr = integral_val - J0_1

# Multiply by π to get the final result
result = mp.pi * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
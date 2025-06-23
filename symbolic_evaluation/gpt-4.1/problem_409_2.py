import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Evaluate the antiderivative at the upper limit (x=1)
x1 = 1
# First term: -0.5 * ln(x^2 + 1)
term1_1 = -0.5 * mp.log(x1**2 + 1)
# Second term: 0.5 * ln((x-1)^2 + 1)
term2_1 = 0.5 * mp.log((x1 - 1)**2 + 1)
# Third term: arctan(x-1)
term3_1 = mp.atan(x1 - 1)
F1 = term1_1 + term2_1 + term3_1

# Evaluate the antiderivative at the lower limit (x=0)
x0 = 0
# First term: -0.5 * ln(x^2 + 1)
term1_0 = -0.5 * mp.log(x0**2 + 1)
# Second term: 0.5 * ln((x-1)^2 + 1)
term2_0 = 0.5 * mp.log((x0 - 1)**2 + 1)
# Third term: arctan(x-1)
term3_0 = mp.atan(x0 - 1)
F0 = term1_0 + term2_0 + term3_0

# Compute the definite integral from 0 to 1
integral_val = F1 - F0

# Compute the expression: π/4 - integral
pi = mp.pi
quarter_pi = pi / 4
result = quarter_pi - integral_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))
import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the inverse hyperbolic sine of 7
u = mp.asinh(7)

# Calculate the exponents
exp1 = (4/3) * u
exp2 = (2/3) * u

# Compute the exponential terms
term1 = mp.exp(exp1)   # e^(4/3 * asinh(7))
term2 = mp.exp(-exp1)  # e^(-4/3 * asinh(7))
term3 = mp.exp(exp2)   # e^(2/3 * asinh(7))
term4 = mp.exp(-exp2)  # e^(-2/3 * asinh(7))

# Combine terms as per the expression: (term1 + term2 - 2*term3 - 2*term4 + 2)
inner_expr = term1 + term2 - 2*term3 - 2*term4 + 2

# Multiply by 3/8
result = (3/8) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
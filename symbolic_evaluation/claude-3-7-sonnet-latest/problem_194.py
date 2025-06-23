import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared divided by 24
pi_sq_over_24 = mp.pi**2 / 24

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute (pi/2) * ln(2)
pi_half_ln2 = (mp.pi / 2) * ln2

# Retrieve Catalan's constant
catalan = mp.catalan

# Calculate the expression inside the parentheses: (pi/2)*ln(2) - Catalan
inner_expr = pi_half_ln2 - catalan

# Multiply the inner expression by 1/4
quarter_inner = inner_expr / 4

# Combine both terms: pi^2/24 + (1/4)*( (pi/2)ln2 - Catalan )
result = pi_sq_over_24 + quarter_inner

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))
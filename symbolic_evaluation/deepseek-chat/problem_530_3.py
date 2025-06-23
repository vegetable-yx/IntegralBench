import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate pi/2
pi_over_2 = mp.pi / 2

# Calculate the constant 2
constant_2 = mp.mpf(2)

# Compute 3 + 2*sqrt(2)
inner_sqrt = mp.sqrt(2)  # sqrt(2)
inner_expr = 3 + 2 * inner_sqrt  # 3 + 2*sqrt(2)

# Compute natural logarithm of (3 + 2*sqrt(2))
log_term = mp.log(inner_expr)

# Divide the logarithm by sqrt(2) to get the third term
third_term = log_term / inner_sqrt

# Combine all terms: pi/2 - 2 + [ln(3 + 2*sqrt(2))/sqrt(2)]
result = pi_over_2 - constant_2 + third_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))